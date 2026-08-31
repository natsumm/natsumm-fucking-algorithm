"""移动零：直接运行本文件即可查看测试结果。"""

from __future__ import annotations

import json


def move_zeroes_with_extra_space(nums: list[int]) -> None:
    """我的答案 1：借用额外的数据结构。"""
    no_zero_dict: dict[int, int] = {}
    for index, number in enumerate(nums):
        if number != 0:
            no_zero_dict[index] = number

    no_zero_list = list(no_zero_dict.values())
    for index in range(len(nums)):
        if not no_zero_list:
            nums[index] = 0
            continue
        nums[index] = no_zero_list.pop(0)


def move_zeroes(nums: list[int]) -> None:
    """我的答案 2：原地将零移动到末尾。"""
    left = 0
    for index in range(len(nums)):
        if nums[index] == 0:
            continue
        nums[left] = nums[index]
        left += 1

    for index in range(left, len(nums)):
        nums[index] = 0


def move_zeroes_by_gpt(nums: list[int]) -> None:
    """GPT 参考答案。"""
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1

    for index in range(left, len(nums)):
        nums[index] = 0


def solve(data: str) -> str:
    """解析 JSON 数组，原地移动零并返回 JSON 格式的结果。"""
    nums: list[int] = json.loads(data)
    move_zeroes(nums)
    return json.dumps(nums, ensure_ascii=False)


def main() -> None:
    data1 = "[0, 1, 0, 3, 12]"
    expected1 = "[1, 3, 12, 0, 0]"
    print(f"预期：{expected1}，实际：{solve(data1)}")

    data2 = "[0]"
    expected2 = "[0]"
    print(f"预期：{expected2}，实际：{solve(data2)}")

    data3 = "[1, 2, 3]"
    expected3 = "[1, 2, 3]"
    print(f"预期：{expected3}，实际：{solve(data3)}")

    data4 = "[0, 0, 0]"
    expected4 = "[0, 0, 0]"
    print(f"预期：{expected4}，实际：{solve(data4)}")


if __name__ == "__main__":
    main()
