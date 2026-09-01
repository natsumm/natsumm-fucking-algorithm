"""和为 K 的子数组（LeetCode 560）测试用例。

Solution 尚未实现：模块级 xfail 标记让未实现状态显示为 xfailed（预期失败）。
实现解法并自测通过后，请删除下方 pytestmark 行再提交。
"""

from __future__ import annotations

import importlib

import pytest

Solution = importlib.import_module("practice.560_和为K的子数组.solution").Solution

# pytestmark = pytest.mark.xfail(
#     raises=NotImplementedError, reason="Solution 尚未实现"
# )


def test_example_1() -> None:
    """官方示例 1：nums = [1,1,1]，k = 2。"""
    solution = Solution()
    assert solution.subarraySum([1, 1, 1], 2) == 2


def test_example_2() -> None:
    """官方示例 2：nums = [1,2,3]，k = 3。"""
    solution = Solution()
    assert solution.subarraySum([1, 2, 3], 3) == 2


def test_single_element_match() -> None:
    """边界用例：单个元素等于 k。"""
    solution = Solution()
    assert solution.subarraySum([1], 1) == 1


def test_single_element_no_match() -> None:
    """边界用例：单个元素不等于 k。"""
    solution = Solution()
    assert solution.subarraySum([1], 0) == 0


def test_negative_numbers() -> None:
    """边界用例：含负数与零。"""
    solution = Solution()
    assert solution.subarraySum([1, -1, 0], 0) == 3
