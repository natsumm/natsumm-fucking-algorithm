# 移动零

- 来源：LeetCode 283
- 难度：简单
- 核心标签：数组、双指针
- 首次练习日期：2026-08-26
- 首次耗时：未记录

## 题目描述

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

必须在不复制数组的情况下原地对数组进行操作。

## 示例

示例 1：

```text
输入：nums = [0, 1, 0, 3, 12]
输出：[1, 3, 12, 0, 0]
```

示例 2：

```text
输入：nums = [0]
输出：[0]
```

## 提示

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

进阶：尽量减少完成操作的次数。

## 我的答案 1：借用额外的数据结构

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return nums

        no_zero_dict = {}
        for i, n in enumerate(nums):
            if n != 0:
                no_zero_dict[i] = n

        no_zero_list = list(no_zero_dict.values())
        for i in range(len(nums)):
            if not no_zero_list:
                nums[i] = 0
                continue
            nums[i] = no_zero_list.pop(0)

        return nums
```

这版能够得到正确结果，但使用了字典和列表，不符合原地操作的空间要求。此外，列表的 `pop(0)` 每次都需要移动后续元素，最坏时间复杂度为 `O(n^2)`，空间复杂度为 `O(n)`。

## 我的答案 2：原地覆盖

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[left] = nums[i]
            left += 1

        for i in range(left, len(nums)):
            nums[i] = 0

        return nums
```

`left` 表示下一个非零元素应写入的位置。第一次遍历把所有非零元素按原顺序覆盖到数组前部，第二次遍历把剩余位置填成 `0`。

- 时间复杂度：`O(n)`
- 额外空间复杂度：`O(1)`

## GPT 参考答案

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # left：下一个非零元素应该放置的位置
        left = 0

        # right：遍历整个数组，寻找非零元素
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        # [0, left) 已经是按原顺序排列的非零元素
        for i in range(left, len(nums)):
            nums[i] = 0
```

参考答案与我的答案 2 思路相同，区别主要在变量命名和注释。

## 复盘

- 完成情况：第二版独立完成并符合题意
- 第一版问题：使用额外数据结构，且 `pop(0)` 导致最坏 `O(n^2)` 时间复杂度
- 学到的模式：使用慢指针记录下一个有效元素的写入位置，可以原地稳定地筛选数组元素
- 二刷日期与结果：待复习
