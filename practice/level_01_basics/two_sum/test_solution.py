"""两数之和（LeetCode 1）测试用例。

Solution 尚未实现：模块级 xfail 标记让未实现状态显示为 xfailed（预期失败）。
实现解法并自测通过后，请删除下方 pytestmark 行再提交。
"""

from __future__ import annotations

import pytest

from practice.level_01_basics.two_sum.solution import Solution

pytestmark = pytest.mark.xfail(
    raises=NotImplementedError, reason="Solution 尚未实现"
)


def test_example_1() -> None:
    """官方示例 1：nums = [2,7,11,15]，target = 9。"""
    solution = Solution()
    assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2() -> None:
    """官方示例 2：nums = [3,2,4]，target = 6。"""
    solution = Solution()
    assert solution.two_sum([3, 2, 4], 6) == [1, 2]


def test_example_3() -> None:
    """官方示例 3：nums = [3,3]，target = 6。"""
    solution = Solution()
    assert solution.two_sum([3, 3], 6) == [0, 1]


def test_minimal_input() -> None:
    """边界用例：最小输入，仅两个元素。"""
    solution = Solution()
    assert solution.two_sum([1, 2], 3) == [0, 1]


def test_negative_numbers() -> None:
    """边界用例：负数与零。"""
    solution = Solution()
    assert solution.two_sum([-3, 4, 3, 90], 0) == [0, 2]
