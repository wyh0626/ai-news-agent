"""Publish 08:00 Beijing digests, preserving GitHub Trending as a separate section."""

import argparse
import fcntl
import json
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.intake.digest import atomic_write, build_digest, day_window, publication_day  # noqa: E402
from src.intake.github_projects import daily_projects  # noqa: E402
from src.intake.store import Store  # noqa: E402


def git(repo, *args, check=True):
    result = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, timeout=180)
    if check and result.returncode:
        # Git stderr can contain credential-bearing URLs. Never echo it to public logs.
        raise RuntimeError(f"git {args[0]} failed; inspect the publishing checkout")
    return result


def generated_path(path):
    p = Path(path)
    if p.is_absolute() or ".." in p.parts:
        return False
    return (path.startswith("site/src/content/blog/grok-daily-") and path.endswith(".md")) or (
        path.startswith("site/public/news-shots/") and path.endswith(".webp")
    )


def dirty_paths(repo):
    output = git(repo, "status", "--porcelain", "-z").stdout
    return {line[3:] for line in output.split("\0") if line}


def sync_repo(repo):
    if git(repo, "branch", "--show-current").stdout.strip() != "main":
        raise ValueError("Publishing requires a dedicated main checkout")
    if dirty_paths(repo):
        raise ValueError("Publishing checkout has unrelated or unfinished changes")
    git(repo, "fetch", "origin", "main")
    ahead = git(repo, "rev-list", "origin/main..HEAD").stdout.strip()
    if ahead:
        paths = git(repo, "diff", "--name-only", "origin/main...HEAD").stdout.splitlines()
        if not paths or not all(generated_path(p) for p in paths):
            raise ValueError("Refusing to publish unrelated local commits")
        # Only locally generated content commits can be rebased; never force-push.
        if git(repo, "rebase", "origin/main", check=False).returncode:
            git(repo, "rebase", "--abort", check=False)
            raise RuntimeError("Generated content conflicts with origin/main; manual review needed")
        git(repo, "push", "origin", "HEAD:main")
    else:
        git(repo, "merge", "--ff-only", "origin/main")


def pending_days(start, end, last=None):
    current = date.fromisoformat(start)
    if last:
        current = max(current, date.fromisoformat(last) + timedelta(days=1))
    finish = date.fromisoformat(end)
    while current <= finish:
        yield current.isoformat()
        current += timedelta(days=1)


def finish_pending(repo, directory):
    manifest = directory / "publish-pending.json"
    pending = json.loads(manifest.read_text())
    files = pending["files"]
    if not files or not all(generated_path(p) for p in files):
        raise ValueError("Invalid pending publication file list")
    if git(repo, "branch", "--show-current").stdout.strip() != "main":
        raise ValueError("Publishing requires a dedicated main checkout")
    if dirty_paths(repo) - set(files):
        raise ValueError("Unrelated changes in publishing checkout")
    stage = directory / "publish-stage" / pending["date"]
    for name in files:
        target = repo / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(stage / name, target)
    git(repo, "add", "--", *files)
    if git(repo, "diff", "--cached", "--quiet", check=False).returncode == 1:
        git(repo, "commit", "-m", f"AI Daily {pending['date']}: Grok news and GitHub projects")
    sync_repo(repo)
    state = directory / "publish-state.json"
    previous = json.loads(state.read_text()).get("last_date") if state.exists() else None
    atomic_write(
        state, json.dumps({"last_date": max(previous or pending["date"], pending["date"])})
    )
    manifest.unlink()
    return pending


def source_urls(store, day):
    start, end = day_window(day)
    with store.connect() as db:
        rows = db.execute(
            "SELECT payload FROM news JOIN telegram_outbox ON news.id=telegram_outbox.news_id "
            "WHERE news.created>=? AND news.created<?",
            (start, end),
        )
        return [s["url"] for row in rows for s in json.loads(row[0]).get("sources", [])]


def publish(args):
    directory = args.data_dir.resolve()
    directory.mkdir(parents=True, exist_ok=True)
    if args.push and not (directory / "news.sqlite3").is_file():
        raise ValueError("Missing existing intake database")
    with (directory / "publish.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        store = Store(directory / "news.sqlite3")
        end = args.date or publication_day()
        if args.push and end > publication_day():
            raise ValueError("Cannot publish a window before its 08:00 cutoff")
        if args.push:
            pending = directory / "publish-pending.json"
            if pending.exists():
                print(
                    json.dumps(
                        {"recovered": finish_pending(args.repo_dir, directory)}, ensure_ascii=False
                    )
                )
            sync_repo(args.repo_dir)
        state = directory / "publish-state.json"
        last = json.loads(state.read_text()).get("last_date") if state.exists() else None
        days = [end] if args.date else list(pending_days(args.start_date or end, end, last))
        for day in days:
            github = (
                daily_projects(directory, day, exclude_urls=source_urls(store, day))
                if args.github
                else {"items": [], "status": "disabled"}
            )
            stage = directory / "publish-stage" / day
            result = build_digest(store, directory, stage / "site", day, projects=github["items"])
            result["github_status"] = github["status"]
            if args.push and result["files"]:
                files = [
                    str(Path(p).relative_to(stage)) for p in result["files"] + result["asset_files"]
                ]
                atomic_write(
                    directory / "publish-pending.json", json.dumps({"date": day, "files": files})
                )
                finish_pending(args.repo_dir, directory)
            elif args.push:
                atomic_write(state, json.dumps({"last_date": max(last or day, day)}))
            print(
                json.dumps(
                    {**result, "pushed": bool(args.push and result["files"])}, ensure_ascii=False
                )
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="Publication date YYYY-MM-DD, ending at 08:00 Beijing")
    parser.add_argument(
        "--start-date", help="First publication date; missed closed windows are recovered"
    )
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data/grok-intake")
    parser.add_argument("--repo-dir", type=Path, default=ROOT)
    parser.add_argument(
        "--github", action="store_true", help="Include original GitHub Trending source"
    )
    parser.add_argument(
        "--push", action="store_true", help="Commit generated content and push main"
    )
    args = parser.parse_args()
    for value in [args.date, args.start_date]:
        if value:
            date.fromisoformat(value)
    publish(args)


if __name__ == "__main__":
    main()
