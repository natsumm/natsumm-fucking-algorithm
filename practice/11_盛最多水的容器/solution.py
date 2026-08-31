"""盛最多水的容器：直接运行本文件即可查看测试结果。"""

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
