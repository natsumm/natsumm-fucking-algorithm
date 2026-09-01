"""最小覆盖子串测试用例。

实现解法后运行本题目测试命令，全部通过即可。
"""

from __future__ import annotations

import importlib

# 目录名以数字开头（如 76_最小覆盖子串），无法使用 import 语句，改用 importlib 按字符串导入
Solution = importlib.import_module("practice.76_最小覆盖子串.solution").Solution


def test_example_1() -> None:
    """官方示例 1。"""
    solution = Solution()
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"


def test_example_2() -> None:
    """官方示例 2：整个 s 即答案。"""
    solution = Solution()
    assert solution.minWindow("a", "a") == "a"


def test_example_3() -> None:
    """官方示例 3：s 无法满足 t 的重复字符需求。"""
    solution = Solution()
    assert solution.minWindow("a", "aa") == ""


def test_t_longer_than_s() -> None:
    """t 比 s 长，必然无解。"""
    solution = Solution()
    assert solution.minWindow("ab", "abc") == ""


def test_s_equals_t() -> None:
    """s 与 t 相同。"""
    solution = Solution()
    assert solution.minWindow("abc", "abc") == "abc"


def test_repeated_chars() -> None:
    """t 含重复字符，窗口需包含相同次数。"""
    solution = Solution()
    assert solution.minWindow("aab", "aa") == "aa"


def test_case_sensitive() -> None:
    """大小写视为不同字符。"""
    solution = Solution()
    assert solution.minWindow("aAbB", "AB") == "AbB"
