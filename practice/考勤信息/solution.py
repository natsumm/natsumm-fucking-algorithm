"""考勤信息（华为 OD 机试）

- 来源：华为 OD 机试题库
- 难度：简单
- 核心标签：字符串、遍历、计数、滑动窗口
- 首次练习日期：2026-08-25
- 原题文件：docs/algorithm-1/(100分) - 考勤信息（Java & Python& JS & C++ & C ）.html
- 运行本题目测试：python3.12 practice/考勤信息/solution.py

题意摘要：
每位员工有一行考勤记录，每条记录是以下四种状态之一：
- `absent`：缺勤
- `late`：迟到
- `leaveearly`：早退
- `present`：正常上班

同时满足以下条件才能获得出勤奖：
1. 全部记录中，缺勤不超过一次；
2. 不能连续出现迟到或早退（`late` 和 `leaveearly` 的任意相邻组合都不允许）；
3. 任意连续 7 次考勤中，`absent`、`late`、`leaveearly` 合计不超过 3 次。

输入与输出：
- 输入：第一行是员工数量 `n`；随后 `n` 行，每行是一位员工用空格分隔的考勤记录。
- 输出：依次输出每位员工的判断结果，使用空格分隔；满足条件输出 `true`，否则输出 `false`。
- 约束：记录条数至少为 1；输入字符串长度小于 10000；不存在非法状态。

解题思路：
请在编码前回答：
1. 如何统计整段记录中的缺勤次数？
2. 如何判断两个相邻状态是否都属于迟到或早退？
3. 如何检查所有长度为 7 的连续区间？记录不足 7 条时应怎样处理？

先写出自己的朴素方案，再考虑是否需要优化。

复杂度：
- 时间：待填写
- 空间：待填写

测试设计：
- 只有一条 `present`
- 恰好一次 `absent`
- 出现两次不相邻的 `absent`
- `late leaveearly` 连续出现
- 恰好 7 条记录，其中异常状态分别为 3 次和 4 次
- 超过 7 条记录，违规窗口不在开头

复盘：
- 首次耗时：
- 错误原因：
- 学到的模式：
- 二刷日期与结果：
"""

from __future__ import annotations


def solve(data: str) -> str:
    """解析输入并返回答案；请从这里开始实现。"""
    str_arr = data.split("\n")
    # 错误 1：无条件删除最后一项，假设输入一定以换行结尾。
    # 若输入为 "1\npresent"，这里会误删唯一一条考勤记录。
    str_arr = str_arr[:-1]
    num = int(str_arr[0])
    str_arr = str_arr[1:]
    if len(str_arr) != num:
        return "false"
    # 错误 2：题目要求为每位员工分别产生 true/false。
    # 当前循环中任一员工违规就直接返回，最终也只会返回一个结果。
    for s in str_arr:
        text = s.split()
        unnormal_dict = {"absent": 0, "late": 0, "leaveearly": 0}
        late_or_leaveearly_idx = -1
        for i, t in enumerate(text):
            if t == "absent":
                unnormal_dict["absent"] = unnormal_dict['absent'] + 1
            if t == "late":
                if late_or_leaveearly_idx != -1 and i - late_or_leaveearly_idx == 1:
                    return "false"
                late_or_leaveearly_idx = i
                unnormal_dict["late"] = unnormal_dict['late'] + 1
            if t == "leaveearly":
                if late_or_leaveearly_idx != -1 and i - late_or_leaveearly_idx == 1:
                    return "false"
                late_or_leaveearly_idx = i
                unnormal_dict["leaveearly"] = unnormal_dict['leaveearly'] + 1
        if unnormal_dict["absent"] > 1:
            return "false"
        # 错误 3：这里统计的是整段记录的异常总数，而题目要求检查
        # “任意连续 7 次考勤”。记录超过 7 条时两者并不等价。
        if len(text) >= 7 and sum(unnormal_dict.values()) > 3:
            return "false"
    return "true"


def can_receive_award_by_gpt(records: list[str]) -> bool:
    """判断一位员工能否获得出勤奖（GPT 编写）。

    答案要点：
    1. 使用计数器检查 absent 是否超过一次；
    2. 记录前一项是否为 late/leaveearly，检查相邻违规；
    3. 使用长度为 7 的滑动窗口统计异常状态；
    4. 任一条件不满足时立即返回 False。
    """
    absent_count = 0
    previous_was_late_or_leaveearly = False
    abnormal_in_window = 0

    for index, record in enumerate(records):
        if record == "absent":
            absent_count += 1
            if absent_count > 1:
                return False

        is_late_or_leaveearly = record in {"late", "leaveearly"}
        if previous_was_late_or_leaveearly and is_late_or_leaveearly:
            return False
        previous_was_late_or_leaveearly = is_late_or_leaveearly

        if record != "present":
            abnormal_in_window += 1

        if index >= 7 and records[index - 7] != "present":
            abnormal_in_window -= 1

        if index >= 6 and abnormal_in_window > 3:
            return False

    return True


def solve_by_gpt(data: str) -> str:
    """完整参考答案（GPT 编写）。

    答案要点：
    1. 使用 strip().splitlines() 兼容末尾有无换行；
    2. 每位员工必须独立判断，分别生成 true 或 false；
    3. 最后使用空格连接所有员工的结果；
    4. 单人判断交给 can_receive_award_by_gpt，职责更清晰。
    """
    lines = data.strip().splitlines()
    if not lines:
        return ""

    employee_count = int(lines[0])
    attendance_lines = lines[1:]
    if len(attendance_lines) != employee_count:
        raise ValueError("员工数量与考勤记录行数不一致")

    results = []
    for line in attendance_lines:
        records = line.split()
        result = "true" if can_receive_award_by_gpt(records) else "false"
        results.append(result)

    return " ".join(results)


def main() -> None:
    data1 = "1\npresent"
    print("预期：true，实际：", solve(data1))

    data2 = "1\nabsent absent"
    print("预期：false，实际：", solve(data2))


if __name__ == "__main__":
    main()
