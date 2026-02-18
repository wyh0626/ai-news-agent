"""AI 过滤工具测试 - 覆盖降级关键词方案和解析逻辑"""

import pytest

from src.tools.ai_filter import _fallback_filter, _parse_indices


class TestFallbackFilter:
    """LLM 不可用时的降级关键词过滤"""

    def test_ai_titles_matched(self):
        titles = [
            "New GPT-5 released by OpenAI",
            "Tax reform bill passes",
            "LLM benchmark results comparison",
            "Cooking recipes for beginners",
            "Deep learning for protein folding",
        ]
        result = _fallback_filter(titles)
        assert 0 in result  # GPT
        assert 1 not in result  # Tax
        assert 2 in result  # LLM
        assert 3 not in result  # Cooking
        assert 4 in result  # Deep learning

    def test_empty_list(self):
        assert _fallback_filter([]) == []

    def test_all_ai(self):
        titles = ["AI model", "Machine learning paper", "Neural network design"]
        result = _fallback_filter(titles)
        assert len(result) == 3

    def test_no_ai(self):
        titles = ["Weather forecast", "Sports news", "Stock market update"]
        result = _fallback_filter(titles)
        assert len(result) == 0


class TestParseIndices:
    """解析 LLM 返回的序号数组"""

    def test_valid_json_array(self):
        assert _parse_indices("[0, 2, 5, 7]", 10) == [0, 2, 5, 7]

    def test_empty_array(self):
        assert _parse_indices("[]", 10) == []

    def test_with_code_block(self):
        assert _parse_indices("```json\n[1, 3]\n```", 10) == [1, 3]

    def test_out_of_range_filtered(self):
        result = _parse_indices("[0, 2, 99]", 10)
        assert 0 in result
        assert 2 in result
        assert 99 not in result

    def test_fallback_to_regex(self):
        result = _parse_indices("AI related: 0, 3, 5", 10)
        assert 0 in result
        assert 3 in result
        assert 5 in result
