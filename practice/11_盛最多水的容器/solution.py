"""盛最多水的容器（LeetCode 11）

- 来源：LeetCode 11
- 难度：中等
- 核心标签：数组、双指针、贪心
- 首次练习日期：2026-08-27
- 首次耗时：未记录
- 运行本题目测试：python3.12 practice/11_盛最多水的容器/solution.py

题目描述：
给定一个长度为 `n` 的整数数组 `height`。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])`。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

示例 1：
输入：height = [1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
输入：height = [1,1]
输出：1

提示：
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

解题思路（我的答案）：
使用左右指针分别指向数组两端。每次计算当前两条线围成的面积，然后移动较短的那一侧：因为容器的盛水量由较短的边决定，移动较长的边不可能使面积变大（宽度必然减小，高度不会增加），只有移动较短的边才可能遇到更高的边从而获得更大的面积。

复杂度：
- 时间复杂度：`O(n)`，每个元素最多被访问一次。
- 额外空间复杂度：`O(1)`，只使用常数个变量。

测试设计：
- 样例：`[1,8,6,2,5,4,8,3,7]` → `49`
- 最小输入：`[1,1]` → `1`
- 单调递增：`[1,2,3,4,5]` → 首尾决定的最大面积
- 单调递减：`[5,4,3,2,1]` → 首尾决定的最大面积
- 包含零：`[0,2]` → `0`

复盘：
- 完成情况：独立完成双指针最优解
- 学到的模式：双指针向中间收敛时，优先移动限制条件更严格的一侧（较短边），从而保证不会错过更优解
- 二刷日期与结果：待复习
"""

from __future__ import annotations

import json


def max_area(height: list[int]) -> int:
    """计算两条垂线能构成的最大容器面积。"""
    if not height or len(height) < 2:
        return 0

    max_result = 0
    left = 0
    right = len(height) - 1

    # 左右指针还没有相遇时持续计算
    while left < right:
        area = min(height[left], height[right]) * (right - left)

        if area > max_result:
            max_result = area

        # 移动较短的一侧，才有机会得到更大的面积
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_result


def solve(data: str) -> str:
    """解析 JSON 数组，返回最大容器面积。"""
    height: list[int] = json.loads(data)
    return str(max_area(height))


def main() -> None:
    data1 = "[1,8,6,2,5,4,8,3,7]"
    expected1 = "49"
    print(f"预期：{expected1}，实际：{solve(data1)}")

    data2 = "[1,1]"
    expected2 = "1"
    print(f"预期：{expected2}，实际：{solve(data2)}")

    data3 = "[1,2,3,4,5]"
    expected3 = "6"
    print(f"预期：{expected3}，实际：{solve(data3)}")

    data4 = "[5,4,3,2,1]"
    expected4 = "6"
    print(f"预期：{expected4}，实际：{solve(data4)}")

    data5 = "[0,2]"
    expected5 = "0"
    print(f"预期：{expected5}，实际：{solve(data5)}")


if __name__ == "__main__":
    main()
