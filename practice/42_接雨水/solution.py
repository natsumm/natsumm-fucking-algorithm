"""接雨水：直接运行本文件即可查看测试结果。"""

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
