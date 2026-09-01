"""题目名称测试用例。

Solution 尚未实现：测试会因 NotImplementedError 失败。
实现解法后运行本题目测试命令，全部通过即可。
"""

from __future__ import annotations

import importlib

# 目录名以数字开头（如 560_和为K的子数组），无法使用 import 语句，改用 importlib 按字符串导入
Solution = importlib.import_module("practice.<题目目录名>.solution").Solution


def test_example_1() -> None:
    """官方示例 1：替换为题目示例的输入与期望输出。"""
    solution = Solution()
    assert solution.method_name()  # TODO: 替换为题目示例的调用与断言
