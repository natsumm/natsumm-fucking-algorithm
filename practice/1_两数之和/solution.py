"""两数之和（LeetCode 1）

- 来源：LeetCode
- 题号：1
- 英文名：Two Sum
- 难度：简单
- 核心标签：数组、哈希表
- 链接：https://leetcode.cn/problems/two-sum/
- 运行本题目测试：python3.12 -m pytest practice/1_两数之和

题目描述：
给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出和为目标值 `target` 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。你可以按任意顺序返回答案。

输入与输出：
- 输入：整数数组 `nums`、整数 `target`
- 输出：两个整数下标组成的列表
- 约束：
  - `2 <= nums.length <= 10^4`
  - `-10^9 <= nums[i] <= 10^9`
  - `-10^9 <= target <= 10^9`
  - 只会存在一个有效答案

示例 1：
- 输入：`nums = [2,7,11,15]`，`target = 9`
- 输出：`[0,1]`
- 解释：`nums[0] + nums[1] == 9`

示例 2：
- 输入：`nums = [3,2,4]`，`target = 6`
- 输出：`[1,2]`

示例 3：
- 输入：`nums = [3,3]`，`target = 6`
- 输出：`[0,1]`

官方示例与边界用例见同目录 `test_solution.py`。

LeetCode 代码模板：仅保留方法签名，不包含任何实现。
实现解法后运行上述测试命令验证，或自行补充 `main()` 直接运行本文件。
"""

from __future__ import annotations


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """返回和为 target 的两个数的下标。"""
        raise NotImplementedError("Solution 尚未实现")
