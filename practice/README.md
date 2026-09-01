# Practice

每道题使用独立目录，目录名格式为 `<题目编号>_<中文题名>`，例如 `560_和为K的子数组`；无编号的题目（如华为 OD 机试题）直接使用题名，例如 `考勤信息`。

每道题的题目标识、完整题面、练习记录和运行测试的命令统一写在 `solution.py` 开头的模块 docstring 中，不单独创建题目 README。由 Coding Agent 初始化的新题目使用 `solution.py`（LeetCode 模板，题面在模块 docstring）和 `test_solution.py`（pytest 用例）两个文件。

运行 `python3.12 tools/new_problem.py --help` 查看创建方式。
