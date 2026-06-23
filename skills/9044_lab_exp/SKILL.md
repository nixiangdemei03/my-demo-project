---
name: 9044_lab_exp
description: Lab 知识点分析与刷题生成 — 从课程网页抓取 Tutorial 题目 + SSH 获取 CSE 已有实验代码，分析知识点/易错点/易考察点，生成 10 道练习题目。
trigger: when the user wants to analyze a lab file, generate practice questions from code, or mentions "分析lab" / "刷题" / "9044" / "生成练习题"
---

# /9044_lab_exp

## 这个 skill 做什么

按 UNSW 校历周数自动匹配，从 `https://cgi.cse.unsw.edu.au/~cs2041/26T2/tut/XX/questions` 抓取 Tutorial 题目，SSH 到 CSE 服务器 `zid@cse.unsw.edu.au` 获取已有实验代码作为补充素材。分析题目和代码中的知识点、易错点、易考察点，生成知识点总结和 10 道练习题（简单 3 + 中等 4 + 难题 3），输出到 `~/Desktop/9044/`。

## 输入

- 可选：周数（如 week04），默认按 UNSW 校历自动计算当前教学周
- 题目来源：`https://cgi.cse.unsw.edu.au/~cs2041/26T2/tut/XX/questions`
- 参考答案（可选）：`https://cgi.cse.unsw.edu.au/~cs2041/26T2/tut/XX/answers`
- SSH：`zid@cse.unsw.edu.au` 获取 CSE 上已有的 lab 代码作为分析素材（优先密钥免密登录）
- CSE 绝对路径：`***`（用户 HOME 目录）

## 输出格式

### 知识点总结 → `~/Desktop/9044/lab/<原文件名>_analysis.md`

```markdown
# Lab Analysis — <文件名>
> 分析日期：<日期> | 来源文件：<文件路径>

## 知识点清单
| # | 知识点 | 行号 | 说明 |
|---|--------|:----:|------|
| 1 | 指针运算 | L12-18 | 通过指针遍历数组 |

## 易错点
### 错误 1: 数组越界
- 位置: L25
- 错误写法: `for(i=0; i<=n; i++)`
- 正确写法: `for(i=0; i<n; i++)`
- 解释: 数组长度为 n 时，最大索引为 n-1

## 易考察点
| # | 考察形式 | 考察内容 | 难度 |
|---|----------|----------|:--:|
| 1 | 改错题 | L20 的边界条件 | 中 |

## 快速自测
- [ ] 我能解释每个知识点的原理吗？
- [ ] 我能指出每处易错点的问题吗？
- [ ] 我能独立写出易考察点的答案吗？
```

### 练习题 → `~/Desktop/9044/刷题/`

三级目录结构，共 10 题（简3 / 中4 / 难3），**每个难度独立编号从 01 起，跨周连续递增**：

```
刷题/
├── README.md              ← 含「编号分配」表，追踪每个难度已用编号和下次起始
├── 简单/
│   ├── 01/  (problem.sh + solution.sh + README.md)
│   ├── 02/  (problem.sh + solution.sh + README.md)
│   └── 03/  (problem.sh + solution.sh + README.md)
├── 中等/
│   ├── 01/  (problem.sh + solution.sh + README.md)
│   ├── 02/  (problem.sh + solution.sh + README.md)
│   ├── 03/  (problem.sh + solution.sh + README.md)
│   └── 04/  (problem.sh + solution.sh + README.md)
└── 困难/
    ├── 01/  (problem.sh + solution.sh + README.md)
    ├── 02/  (problem.sh + solution.sh + README.md)
    └── 03/  (problem.sh + solution.sh + README.md)
```

**编号规则**：每个难度独立计数，各自从 01 开始。下次生成时读取 `README.md` 中各难度「下次起始」列，接续编号。生成后更新 README 的编号分配表。

每道题包含以下文件：
- `problem.sh` — 带 `TODO` 的代码模板（用户需补全）
- `solution.sh` — 完整参考解答
- `README.md` — 题目描述、约束条件、期望输出
- `test.sh` — （可选）自动化测试脚本，`sh test.sh solution` 验证解答；含 3-15 个测试用例覆盖边界条件

## 执行流程

### Step 0: 检查本地已有输出

1. 确定周数后，检查本地输出是否已存在：
   - `~/Desktop/9044/lab/labXX_analysis.md`
   - `~/Desktop/9044/刷题/README.md` 中是否已登记本周 lab 的题目
2. **如果已有本周输出** → 读 README 编号分配表确认完整性，询问用户是否需要重新生成
   - 用户确认重新生成 → 继续 Step 1
   - 用户认为完整 → 结束
3. **如果不存在** → 继续 Step 1

### Step 1: 确定周数并获取用户确认

1. 如果用户未指定周数，按 UNSW 校历计算当前教学周
2. **必须询问用户确认** — 向用户输出：
   ```
   📅 根据 UNSW 校历推算，当前为 Week XX。是否正确？
   ```
3. **等待用户确认后才能继续**：
   - 用户回复"是"/"对的"/"正确" → 继续 Step 2
   - 用户回复其他周数（如"week03"）→ 以用户指定为准
   - 用户不确认 → 不执行后续步骤

### Step 2: 获取题目

1. 抓取题目：`https://cgi.cse.unsw.edu.au/~cs2041/26T2/tut/XX/questions`（按用户确认的周数）
2. 可选：抓取参考答案 `https://cgi.cse.unsw.edu.au/~cs2041/26T2/tut/XX/answers`
3. 用 WebFetch 读取全部内容
4. 如网页不可达 → 提示用户确认周数
5. 可选：SSH 到 `zid@cse.unsw.edu.au` 获取 CSE 上已有的 lab 代码作为补充分析素材

### Step 3: 获取 CSE 补充代码（可选）

1. SSH → CSE 服务器 `~/labXX/` 下的 `.c`/`.sh`/`.py` 文件（命名规范：`lab04` 无下划线）
2. **优先**：密钥免密登录 `ssh -o BatchMode=yes zid@cse.unsw.edu.au`
3. **Fallback**：如密钥未配置，用 `SSHPASS` 环境变量 + `sshpass -e` 传输
4. 只读不写，不修改 CSE 上任何文件

### Step 4: 分析文件

从知识点（核心概念+行号+说明）、易错点（位置+错误写法+正确写法+解释）、易考察点（考察形式+内容+难度）三个维度分析。

### Step 5: 生成知识点总结

输出 `labXX_analysis.md` 到 `~/Desktop/9044/lab/`，格式见「知识点总结」模板。

### Step 6: 生成练习题

1. 读取 `~/Desktop/9044/刷题/README.md` 中各难度的「下次起始」编号
2. 按难度生成文件夹（如 `简单/04/`、`中等/05/`、`困难/04/`）
3. 每题包含 `problem.sh` + `solution.sh` + `README.md`
4. 对可自动化验证的题目，额外生成 `test.sh`（测试用例 3-15 个，覆盖边界条件）
5. 更新 `刷题/README.md` 的编号分配表（已用编号 + 下次起始）
6. 题目与已分析知识点的对应关系写入 README 题目列表

### Step 7: 清理

删除临时文件（`temp_lab_file` 等），报告全部产出路径。

## 必须遵守

- SSH 优先使用密钥免密登录（`ssh -o BatchMode=yes`），仅在密钥不可用时 fallback 到 `SSHPASS` + `sshpass -e`
- 密码方式 fallback 时不出现于命令行参数；使用后立即 `unset SSHPASS`
- 每次连接成功后立即关闭会话，不修改学生账户上的任何文件
- 不保留远程文件的本地缓存（`temp_lab_file` 完成后删除）
- 生成的题目保存到 `~/Desktop/` 而非项目仓库
- 权限失败时提示用户检查 SSH 凭据，不反复尝试
- 每题必须对应一个已分析出的知识点；简单题检验记忆、中等题需要代码分析、难题综合 2+ 知识点

## 依赖

| 工具 | 用途 | 安装 |
|------|------|------|
| WebFetch | 抓取课程网页题目 | Claude Code 内置 |
| `ssh` / `scp` | CSE 连接与文件传输（密钥免密） | 系统自带 |
| `sshpass` | 密码方式 SSH（fallback） | `apt install sshpass` / `brew install sshpass` |

> 如 `sshpass` 未安装，自动降级为交互式提问（让用户在终端手动 scp）。

## 反模式

- 使用平板 `_practice.md` 单文件存所有题目 → 三级目录结构（刷题/难度/编号/），每题独立文件夹
- 编号全局跨难度共用（如简单01-03、中等04-07）→ 每个难度独立从 01 起编号
- 只生成 README.md 无代码文件 → 每题必须有 `problem.sh` + `solution.sh`
- 可测试的题目不提供 `test.sh` → 凡是输入→输出可验证的题目都应带测试
- 跑题生成与 lab 文件无关的通用题目
- 把 lab 文件或分析结果提交到项目仓库
- 分析空洞（"这段代码用了循环"）→ 必须标注行号+具体说明
