import argparse
import json
import subprocess
from datetime import datetime

import httpx
import pytest

from scripts import publish_grok_digest as pub
from src.intake.digest import build_digest
from src.intake.github_projects import daily_projects, parse_projects
from src.intake.store import Store


def feed(*projects):
    return (
        "<rss><channel>"
        + "".join(
            f"<item><link>https://github.com/{name}</link><description><![CDATA[<p>{desc}</p><hr>README</description>]]></description></item>"
            for name, desc in projects
        )
        + "</channel></rss>"
    ).encode()


def test_github_short_description_filter_and_link_validation():
    xml = feed(
        ("team/ai-tool", "AI coding agent"),
        ("team/db", "Fast database"),
        ("team/ai-tool", "AI duplicate"),
        ("team/foo/issues/1", "AI news"),
    )
    result = parse_projects(xml)
    assert [p["name"] for p in result] == ["team/ai-tool"]
    assert result[0]["description"] == "AI coding agent"


def test_github_three_day_dedup_grok_exclusion_and_cached_retry(tmp_path):
    calls = []

    def handler(request):
        assert "authorization" not in request.headers
        calls.append(request)
        return httpx.Response(
            200,
            content=feed(("a/one", "AI agent"), ("b/two", "LLM engine"), ("c/three", "GPT tools")),
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        old = daily_projects(
            tmp_path,
            "2026-11-09",
            client=client,
            now=datetime.fromisoformat("2026-11-09T08:00:00+08:00"),
        )
        assert len(old["items"]) == 3
        current = daily_projects(
            tmp_path,
            "2026-11-10",
            client=client,
            now=datetime.fromisoformat("2026-11-10T08:00:00+08:00"),
        )
        assert current["items"] == []
        assert daily_projects(tmp_path, "2026-11-10", client=client) == current
        assert len(calls) == 2
        later = daily_projects(
            tmp_path,
            "2026-11-13",
            client=client,
            now=datetime.fromisoformat("2026-11-13T08:00:00+08:00"),
            exclude_urls=["https://github.com/a/one"],
        )
        assert [p["name"] for p in later["items"]] == ["b/two", "c/three"]


def test_github_failure_does_not_invent_or_freeze_a_snapshot(tmp_path):
    with httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(503))) as client:
        result = daily_projects(
            tmp_path,
            "2026-11-10",
            client=client,
            now=datetime.fromisoformat("2026-11-10T08:00:00+08:00"),
        )
    assert result["status"] == "fetch_failed" and result["items"] == []
    assert not (tmp_path / "github-trending/2026-11-10.json").exists()


def test_projects_only_digest_and_missed_days(tmp_path):
    projects = [
        {"name": "test/ai", "url": "https://github.com/test/ai", "description": "AI toolkit"}
    ]
    result = build_digest(
        Store(tmp_path / "news.sqlite3"),
        tmp_path,
        tmp_path / "site",
        "2026-11-10",
        projects=projects,
    )
    assert result["count"] == 0 and result["projects"] == 1 and len(result["files"]) == 2
    assert list(pub.pending_days("2026-11-10", "2026-11-13", "2026-11-11")) == [
        "2026-11-12",
        "2026-11-13",
    ]
    assert list(pub.pending_days("2026-11-10", "2026-11-09")) == []


def test_publish_recovers_commit_after_failed_push(tmp_path, monkeypatch):
    remote, repo, data = tmp_path / "remote.git", tmp_path / "repo", tmp_path / "data"

    def run(*args):
        subprocess.run(["git", *map(str, args)], check=True, capture_output=True)

    run("init", "--bare", "--initial-branch=main", remote)
    run("clone", remote, repo)
    run("-C", repo, "config", "user.name", "Test")
    run("-C", repo, "config", "user.email", "test@example.org")
    (repo / "README").write_text("initial")
    run("-C", repo, "add", "README")
    run("-C", repo, "commit", "-m", "initial")
    run("-C", repo, "push", "origin", "main")
    name = "site/src/content/blog/grok-daily-2026-11-10-zh.md"
    stage = data / "publish-stage/2026-11-10" / name
    stage.parent.mkdir(parents=True)
    stage.write_text("test generated content")
    (data / "publish-pending.json").write_text(json.dumps({"date": "2026-11-10", "files": [name]}))
    original = pub.git

    def fail_push(repo, *args, **kwargs):
        if args[0] == "push":
            raise RuntimeError("simulated push failure")
        return original(repo, *args, **kwargs)

    monkeypatch.setattr(pub, "git", fail_push)
    with pytest.raises(RuntimeError, match="simulated"):
        pub.finish_pending(repo, data)
    assert not (data / "publish-state.json").exists()
    assert (data / "publish-pending.json").exists()
    first_head = original(repo, "rev-parse", "HEAD").stdout
    monkeypatch.setattr(pub, "git", original)
    pub.finish_pending(repo, data)
    assert original(repo, "rev-parse", "HEAD").stdout == first_head
    assert original(repo, "rev-parse", "origin/main").stdout == first_head
    assert json.loads((data / "publish-state.json").read_text())["last_date"] == "2026-11-10"
    assert not (data / "publish-pending.json").exists()


def test_publish_refuses_future_window(tmp_path, monkeypatch):
    Store(tmp_path / "news.sqlite3")
    monkeypatch.setattr(pub, "publication_day", lambda: "2026-11-09")
    args = argparse.Namespace(data_dir=tmp_path, date="2026-11-10", push=True)
    with pytest.raises(ValueError, match="before its 08:00"):
        pub.publish(args)
