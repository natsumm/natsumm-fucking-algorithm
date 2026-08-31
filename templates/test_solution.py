"""题目名称测试用例。

Solution 尚未实现：模块级 xfail 标记让未实现状态显示为 xfailed（预期失败）。
实现解法并自测通过后，请删除下方 pytestmark 行再提交。
"""

from __future__ import annotations

import importlib

import pytest

# 目录名以数字开头（如 560_和为K的子数组），无法使用 import 语句，改用 importlib 按字符串导入
Solution = importlib.import_module("practice.<题目目录名>.solution").Solution

pytestmark = pytest.mark.xfail(
    raises=NotImplementedError, reason="Solution 尚未实现"
)


def test_example_1() -> None:
    """官方示例 1：替换为题目示例的输入与期望输出。"""
    solution = Solution()
    assert solution.method_name()  # TODO: 替换为题目示例的调用与断言
