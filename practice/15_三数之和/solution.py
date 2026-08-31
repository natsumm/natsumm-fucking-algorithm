"""三数之和：直接运行本文件即可查看测试结果。"""

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
