"""字母异位词分组：直接运行本文件即可查看测试结果。"""

from __future__ import annotations

import json


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """按照字母异位关系对字符串进行分组。"""
    result: dict[str, list[str]] = {}
    for string in strs:
        key = "".join(sorted(string))
        if key not in result:
            result[key] = []
        result[key].append(string)
    return list(result.values())


def solve(data: str) -> str:
    """解析 JSON 字符串数组，并返回 JSON 格式的分组结果。"""
    strs = json.loads(data)
    return json.dumps(group_anagrams(strs), ensure_ascii=False)


def main() -> None:
    data1 = '["eat", "tea", "tan", "ate", "nat", "bat"]'
    expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    print(f"预期：{expected1}，实际：{group_anagrams(json.loads(data1))}")

    data2 = '[""]'
    expected2 = [[""]]
    print(f"预期：{expected2}，实际：{group_anagrams(json.loads(data2))}")

    data3 = '["a"]'
    expected3 = [["a"]]
    print(f"预期：{expected3}，实际：{group_anagrams(json.loads(data3))}")


if __name__ == "__main__":
    main()
