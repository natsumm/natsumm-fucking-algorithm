"""和为 K 的子数组（LeetCode 560）

- 来源：LeetCode
- 题号：560
- 英文名：Subarray Sum Equals K
- 难度：中等
- 核心标签：数组、哈希表、前缀和
- 链接：https://leetcode.cn/problems/subarray-sum-equals-k/
- 运行本题目测试：python3.12 -m pytest practice/560_和为K的子数组

题目描述：
给你一个整数数组 `nums` 和一个整数 `k`，请你统计并返回该数组中和为 `k` 的子数组的个数。

子数组是数组中元素的连续非空序列。

输入与输出：
- 输入：整数数组 `nums`、整数 `k`
- 输出：和为 `k` 的连续非空子数组的个数
- 约束：
  - `1 <= nums.length <= 2 * 10^4`
  - `-1000 <= nums[i] <= 1000`
  - `-10^7 <= k <= 10^7`

示例 1：
- 输入：`nums = [1,1,1]`，`k = 2`
- 输出：`2`

示例 2：
- 输入：`nums = [1,2,3]`，`k = 3`
- 输出：`2`

官方示例与边界用例见同目录 `test_solution.py`。
"""

from __future__ import annotations

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """统计并返回和为 k 的连续非空子数组的个数。"""
        prefix_count = {0:1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            result += prefix_count.get(prefix_sum - k, 0)
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        return result
