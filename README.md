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
practice/              按题目编号存放自己的解答（目录名：编号_中文题名）
templates/             单题模板
notes/                 进度、错题和知识笔记
tools/new_problem.py   创建新练习的脚手架
tests/                 项目工具测试
pytest.ini             pytest 配置，支持单题与全量测试
```

## 开始第一题

```powershell
python3.12 tools/new_problem.py 560 "和为K的子数组"
python3.12 -m pytest practice/560_和为K的子数组   # 单题测试
python3.12 -m pytest                             # 全部测试
```

直接运行每道题的 `solution.py`，`main()` 会执行代码中直接写入的少量测试 case，并显示预期与实际结果。每道题通常只保留 `README.md` 和 `solution.py`，无需额外维护样例输入、输出文件。由 Coding Agent 初始化的新题目使用三件套结构（`README.md` + `solution.py` + `test_solution.py`），通过 pytest 验证：解法未实现时测试显示 `xfailed`（预期失败），实现后删除测试文件顶部的 `pytestmark` 行即可转绿。提交前更新 [notes/progress.md](notes/progress.md)，做错的原因写入 [notes/mistakes.md](notes/mistakes.md)。

## 每题练习循环

1. 读题并手算样例，不看答案。
2. 写清输入、输出、约束和朴素思路。
3. 简单题限时 30～40 分钟，超时只看提示，不直接抄代码。
4. 补充至少 3 个边界用例并运行。
5. 写复杂度、错误原因和二刷日期。
6. 次日或三日后闭卷重写；能独立完成才算掌握。

项目只使用 Python 标准库，无需安装第三方依赖。建议使用 Python 3.10 或更高版本。
