"""滑动窗口最大值（LeetCode 239）

- 来源：LeetCode
- 题号：239
- 英文名：Sliding Window Maximum
- 难度：困难
- 核心标签：队列、滑动窗口、单调队列、堆（优先队列）
- 链接：https://leetcode.cn/problems/sliding-window-maximum/
- 运行本题目测试：python3.12 -m pytest practice/239_滑动窗口最大值

题目描述：
给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值。

输入与输出：
- 输入：整数数组 `nums`、整数 `k`
- 输出：每个滑动窗口内最大值的数组

示例 1：
- 输入：`nums = [1,3,-1,-3,5,3,6,7]`，`k = 3`
- 输出：`[3,3,5,5,6,7]`
- 解释：
  滑动窗口的位置                  最大值
  ---------------                 -----
  [1  3  -1] -3  5  3  6  7        3
   1 [3  -1  -3] 5  3  6  7        3
   1  3 [-1  -3  5] 3  6  7        5
   1  3  -1 [-3  5  3] 6  7        5
   1  3  -1  -3 [5  3  6] 7        6
   1  3  -1  -3  5 [3  6  7]       7

示例 2：
- 输入：`nums = [1]`，`k = 1`
- 输出：`[1]`

提示：
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

官方示例与边界用例见同目录 `test_solution.py`。

LeetCode 代码模板：仅保留方法签名，不包含任何实现。
实现解法后运行上述测试命令验证，或自行补充 `main()` 直接运行本文件。
"""

from __future__ import annotations

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return self.violentEnumeration(nums, k)
        # TODO 复习单调队列
        queue = deque()
        result = []
        for right in range(len(nums)):
            while queue and queue[0] < right - k + 1:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)
            if right >= k - 1:
                result.append(nums[queue[0]])

        return result



    # 暴力枚举，时间复杂度不符合要求
    def violentEnumeration(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = left + k
        result = []
        while right <= len(nums):
            result.append(max(nums[left:right]))
            left += 1
            right += 1
        return result

        
