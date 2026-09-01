"""三数之和（LeetCode 15）

- 来源：LeetCode 15
- 难度：中等
- 核心标签：数组、双指针、排序、去重
- 首次练习日期：2026-08-27
- 首次耗时：未记录
- 运行本题目测试：python3.12 practice/15_三数之和/solution.py

题目描述：
给你一个整数数组 `nums`，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k`，同时还满足 `nums[i] + nums[j] + nums[k] == 0`。

请你返回所有和为 `0` 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

提示：
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

解题思路（我的答案）：
先将数组排序，然后固定第一个数 `nums[i]`，在 `i` 右侧使用双指针寻找两数之和等于 `-nums[i]` 的组合。通过对 `i`、`left`、`right` 三个位置分别去重，保证结果中不会出现重复的三元组。

复杂度：
- 时间复杂度：`O(n^2)`，排序耗时 `O(n log n)`，外层循环 `O(n)`，内层双指针 `O(n)`。
- 额外空间复杂度：`O(1)`，不计输出结果本身的空间；排序可能使用 `O(log n)` 到 `O(n)` 的栈空间，取决于排序实现。

测试设计：
- 样例：`[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`
- 无结果：`[0,1,1]` → `[]`
- 全零：`[0,0,0]` → `[[0,0,0]]`
- 多个重复值：`[-2,0,0,2,2]` → `[[-2,0,2]]`
- 最小长度：`[1,-1,0]` → `[[-1,0,1]]`

复盘：
- 完成情况：独立完成双指针 + 三重去重方案
- 学到的模式：排序后将三数之和转化为「固定一个数 + 双指针求两数之和」，并在每层循环中跳过重复值以避免结果重复
- 二刷日期与结果：待复习
"""

from __future__ import annotations

import json


def three_sum(nums: list[int]) -> list[list[int]]:
    """返回所有和为 0 且不重复的三元组。"""
    # 先排序，方便使用双指针，同时便于跳过重复元素
    nums = sorted(nums)
    result: list[list[int]] = []

    # 固定第一个数 nums[i]，再通过双指针寻找另外两个数
    for i in range(len(nums)):
        # 数组已排序，nums[i] > 0 时，后面三个数之和一定大于 0
        if nums[i] > 0:
            break

        # 第一个数去重：相同的 nums[i] 只处理一次
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # 当前组合已经使用，左右指针同时向中间移动
                left += 1
                right -= 1

                # 跳过 left 的重复值
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # 跳过 right 的重复值
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                # 总和太小，需要增大，因此左指针右移
                left += 1

            else:
                # 总和太大，需要减小，因此右指针左移
                right -= 1

    return result


def solve(data: str) -> str:
    """解析 JSON 数组，返回 JSON 格式的三元组列表。"""
    nums: list[int] = json.loads(data)
    return json.dumps(three_sum(nums), ensure_ascii=False, separators=(",", ":"))


def main() -> None:
    data1 = "[-1,0,1,2,-1,-4]"
    expected1 = "[[-1,-1,2],[-1,0,1]]"
    print(f"预期：{expected1}，实际：{solve(data1)}")

    data2 = "[0,1,1]"
    expected2 = "[]"
    print(f"预期：{expected2}，实际：{solve(data2)}")

    data3 = "[0,0,0]"
    expected3 = "[[0,0,0]]"
    print(f"预期：{expected3}，实际：{solve(data3)}")

    data4 = "[-2,0,0,2,2]"
    expected4 = "[[-2,0,2]]"
    print(f"预期：{expected4}，实际：{solve(data4)}")

    data5 = "[1,-1,0]"
    expected5 = "[[-1,0,1]]"
    print(f"预期：{expected5}，实际：{solve(data5)}")


if __name__ == "__main__":
    main()
