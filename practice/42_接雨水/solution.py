"""接雨水（LeetCode 42）

- 来源：LeetCode 42
- 难度：困难
- 核心标签：数组、动态规划、双指针、单调栈
- 完成状态：已解答
- 首次练习日期：2026-08-27
- 首次耗时：未记录
- 运行本题目测试：python3.12 practice/42_接雨水/solution.py

题目描述：
给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子在下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：该高度图一共可以接 6 个单位的雨水。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

解题思路（GPT 的回答，整理后）：
使用两个数组预处理每个位置左侧和右侧的最高柱子：

- `left_max[i]`：区间 `[0, i]` 中的最高柱子。
- `right_max[i]`：区间 `[i, n - 1]` 中的最高柱子。
- 位置 `i` 的水面高度由较矮的一侧决定，因此该位置的积水量是
  `min(left_max[i], right_max[i]) - height[i]`。

完整的可运行实现见本文件 `trap()`。

困难需学习：
1. 积水量为什么取两侧最高柱子的较小值？
   水会从较矮的一侧溢出，所以水面最多只能到达 `min(左侧最高柱, 右侧最高柱)`。
2. 为什么可以逐列计算后相加？
   每根柱子的宽度都是 `1`，每一列的水量就是“水面高度减柱子高度”，总水量等于所有列的水量之和。
3. 为什么公式不会得到负数？
   `left_max[i]` 和 `right_max[i]` 的统计范围都包含当前位置 `i`，因此两者都不小于 `height[i]`。
4. 前缀最大值与后缀最大值模式。
   当某个位置的答案同时依赖左侧整体信息和右侧整体信息时，可以分别从左到右、从右到左预处理。
5. 边界为什么不用计算？
   最左和最右位置缺少一侧围挡，无法存水；少于三根柱子时一定无法形成凹槽。

复杂度：
- 时间复杂度：`O(n)`，三次线性遍历。
- 额外空间复杂度：`O(n)`，使用两个长度为 `n` 的辅助数组。

测试设计：
- 官方样例：`[0,1,0,2,1,0,1,3,2,1,2,1]` → `6`
- 官方样例：`[4,2,0,3,2,5]` → `9`
- 柱子不足三根：`[1,2]` → `0`
- 没有凹槽：`[1,2,3,4]` → `0`
- 简单凹槽：`[3,0,3]` → `3`

复盘：
- 当前掌握：能够使用前缀最大值和后缀最大值求解。
- 待学习：空间复杂度为 `O(1)` 的双指针解法，以及单调栈按层计算积水的解法。
- 二刷日期与结果：待复习。
"""

from __future__ import annotations

import json


def trap(height: list[int]) -> int:
    """使用前缀、后缀最大值计算总积水量。"""
    if len(height) < 3:
        return 0

    n = len(height)

    # 困难需学习：left_max[i] 包含 height[i] 本身，表示区间 [0, i]
    # 内的最高柱子。当前位置要存水，必须知道左边最高能挡到哪里。
    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # 困难需学习：同理，right_max[i] 表示区间 [i, n - 1]
    # 内的最高柱子，因此需要从右向左递推。
    right_max = [0] * n
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water_total = 0
    for i in range(1, n - 1):
        # 困难需学习：水面由左右两侧较矮的最高柱子决定，因为水会
        # 从较矮的一侧溢出。再减去当前柱高，就是宽度为 1 的这一列水量。
        # 两个最大值都包含当前位置，所以该差值一定不会小于 0。
        water_level = min(left_max[i], right_max[i])
        water_total += water_level - height[i]

    return water_total


def solve(data: str) -> str:
    """解析 JSON 高度数组，返回能够接住的雨水总量。"""
    height: list[int] = json.loads(data)
    return str(trap(height))


def main() -> None:
    data1 = "[0,1,0,2,1,0,1,3,2,1,2,1]"
    expected1 = "6"
    print(f"预期：{expected1}，实际：{solve(data1)}")

    data2 = "[4,2,0,3,2,5]"
    expected2 = "9"
    print(f"预期：{expected2}，实际：{solve(data2)}")

    data3 = "[1,2]"
    expected3 = "0"
    print(f"预期：{expected3}，实际：{solve(data3)}")

    data4 = "[1,2,3,4]"
    expected4 = "0"
    print(f"预期：{expected4}，实际：{solve(data4)}")

    data5 = "[3,0,3]"
    expected5 = "3"
    print(f"预期：{expected5}，实际：{solve(data5)}")


if __name__ == "__main__":
    main()
