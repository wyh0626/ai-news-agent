"""Reviewer Agent 测试"""

from src.agents.reviewer import _auto_review


def test_auto_review_passes():
    good_md = """# AI 日报 - 2025-02-13

> 共 10 条新闻

## LLM
- [News 1](https://example.com/1)
- [News 2](https://example.com/2)
- [News 3](https://example.com/3)

## 开源
- [News 4](https://example.com/4)
- [News 5](https://example.com/5)

---
*自动生成*
"""
    result = _auto_review(good_md)
    assert result["passed"] is True
    assert result["score"] == 100


def test_auto_review_too_short():
    result = _auto_review("short")
    assert result["passed"] is False
    assert "过短" in str(result["issues"])


def test_auto_review_no_title():
    content = "no title here\n" * 20
    result = _auto_review(content)
    assert result["passed"] is False


def test_auto_review_no_links():
    content = "# Title\n" + "content line\n" * 20
    result = _auto_review(content)
    assert result["passed"] is False
    assert "链接" in str(result["issues"])
