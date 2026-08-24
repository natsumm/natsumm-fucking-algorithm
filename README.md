# Algorithm Practice Lab

一个使用 Python 3 进行长期、渐进式算法练习的项目。`docs/` 保存原始题库，`practice/` 保存自己真正写过和复盘过的题目。

## 学习路线

| 等级 | 主题 | 进入下一阶段的标准 |
| --- | --- | --- |
| 01 | Python 基础、数组、字符串 | 10 题，简单题 30 分钟内完成 |
| 02 | 模拟、排序、哈希统计 | 15 题，能独立处理多条件规则 |
| 03 | 双指针、滑动窗口、区间 | 12 题，能识别连续区间问题 |
| 04 | 栈、队列、链表、二分 | 12 题，能说明数据结构选择原因 |
| 05 | 递归、回溯、DFS、BFS | 15 题，能画出搜索状态与边界 |
| 06 | 贪心、动态规划 | 15 题，能写出状态定义或贪心依据 |
| 07 | 图、树、综合题 | 持续练习，按专题复盘 |

详细目标见 [roadmap.md](roadmap.md)。不要按日历强制升级；达到标准后再前进。

## 目录结构

```text
docs/                  原始题目资料，只读参考
practice/              按等级存放自己的解答
templates/             单题模板
notes/                 进度、错题和知识笔记
tools/new_problem.py   创建新练习的脚手架
tests/                 项目工具测试
```

## 开始第一题

```powershell
python tools/new_problem.py 1 attendance "考勤信息"
Get-Content practice/level_01_basics/attendance/sample_input.txt | python practice/level_01_basics/attendance/solution.py
python -m unittest discover -s tests -v
```

创建后，先填写题目的 `README.md`，再实现 `solution.py`。提交前更新 [notes/progress.md](notes/progress.md)，做错的原因写入 [notes/mistakes.md](notes/mistakes.md)。

## 每题练习循环

1. 读题并手算样例，不看答案。
2. 写清输入、输出、约束和朴素思路。
3. 简单题限时 30～40 分钟，超时只看提示，不直接抄代码。
4. 补充至少 3 个边界用例并运行。
5. 写复杂度、错误原因和二刷日期。
6. 次日或三日后闭卷重写；能独立完成才算掌握。

项目只使用 Python 标准库，无需安装第三方依赖。建议使用 Python 3.10 或更高版本。
