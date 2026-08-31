"""题目名称测试用例。

Solution 尚未实现：模块级 xfail 标记让未实现状态显示为 xfailed（预期失败）。
实现解法并自测通过后，请删除下方 pytestmark 行再提交。
"""

from __future__ import annotations

import pytest

from practice.__LEVEL_DIR__.__SLUG__.solution import Solution

pytestmark = pytest.mark.xfail(
    raises=NotImplementedError, reason="Solution 尚未实现"
)


def test_example_1() -> None:
    """官方示例 1：替换为题目示例的输入与期望输出。"""
    solution = Solution()
    assert solution.method_name()  # TODO: 替换为题目示例的调用与断言
