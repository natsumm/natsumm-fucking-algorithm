"""滑动窗口最大值测试用例。

实现解法后运行本题目测试命令，全部通过即可。
"""

from __future__ import annotations

import importlib

# 目录名以数字开头（如 239_滑动窗口最大值），无法使用 import 语句，改用 importlib 按字符串导入
Solution = importlib.import_module("practice.239_滑动窗口最大值.solution").Solution


def test_example_1() -> None:
    """官方示例 1。"""
    solution = Solution()
    assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]


def test_example_2() -> None:
    """官方示例 2：数组只有一个元素。"""
    solution = Solution()
    assert solution.maxSlidingWindow([1], 1) == [1]


def test_window_size_one() -> None:
    """窗口大小为 1：每个元素依次成为最大值。"""
    solution = Solution()
    assert solution.maxSlidingWindow([1, -1, 0], 1) == [1, -1, 0]


def test_window_equals_length() -> None:
    """窗口大小等于数组长度：只返回全数组最大值。"""
    solution = Solution()
    assert solution.maxSlidingWindow([4, 3, 5, 2], 4) == [5]


def test_decreasing() -> None:
    """单调递减数组：最大值依次后移。"""
    solution = Solution()
    assert solution.maxSlidingWindow([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]


def test_all_equal() -> None:
    """全部相等的数组。"""
    solution = Solution()
    assert solution.maxSlidingWindow([1, 1, 1, 1], 3) == [1, 1]
