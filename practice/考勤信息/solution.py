"""考勤信息：直接运行本文件即可查看测试结果。"""

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
