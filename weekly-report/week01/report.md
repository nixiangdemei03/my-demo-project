# Week 1 Report — nixiangdemei03

## 1. 本周做了什么（事实清单）

- 在 `D:\claude-code-demo\RBT\` 初始化了 RBT 项目（留学生地图服务平台），`git init` + `gh repo create` 创建私有仓库并推送到 GitHub
- 搭建项目目录结构：`frontend/`、`backend/`、`docs/`、`makedown/`、`模板/`、`weekly-report/`
- 编写 `CLAUDE.md`（minimal 版 → 项目定位版），`AGENTS.md`（→ See CLAUDE.md），`docs/shared-context.md`（Codex & Claude 通用），`README.md` v0
- 重写 `makedown/CLAUDE.md` 为 V0 版本（含项目目标、7 步开发工作流、文件修改边界限制）
- 跑通 hello-world：FastAPI `/api/hello` → `{"msg":"hello"}` + React 前端展示 + Vite proxy 代理联调
- 写了 `Makefile`（`make dev` / `make test` / `make deploy`）和 `.gitignore`
- 完成 4 次规范化 commit（feat: / docs: / chore:）并推送到 `github.com/nixiangdemei03/my-demo-project`
- 前端依赖用 npm 安装，后端用 pip 安装 FastAPI + uvicorn，端到端验证通过（curl localhost:5173/api/hello → `{"msg":"hello"}`）

## 2. 本周学到了什么（知识 + 反思）

- 学到 CLAUDE.md 的写法：抽象描述（"做一个好用的工具"）vs 具体场景（"悉尼留学生找美食+发搬家需求"）——后者 Claude 给的代码明显更贴合。这个在模板的反例里也看到了，自己写一遍体感更强。
- 学到 `git rm --cached` 可以移除已跟踪文件但保留本地副本，用来清理被误提交的 `.claude/settings.local.json`。之前只会 `git rm`，不知道 `--cached` 的用法。
- 最 aha 的瞬间：Vite 的 proxy 配置让前端 `/api/*` 请求自动转发到后端 8000 端口，不用写 CORS 也不用配 nginx，一行配置解决。
- 还没完全搞懂的：Cloudflare Workers 和 Pages 的部署流程只是写了占位 Makefile 命令，实际没跑过。

## 3. AI 协作记录

- 最爽的一次：让 Claude 写 "minimal CLAUDE.md"，然后我描述项目（留学生地图 + 服务市场），它直接生成了包含 Core features、Map 技术栈选型（Leaflet / Mapbox）的完整配置。我用这个内容直接覆盖了根目录的 CLAUDE.md。
- 最坑的一次：第一次 push 时 SSH `Host key verification failed`，Claude 直接帮我跑了 `ssh-keyscan github.com >> ~/.ssh/known_hosts`，一次解决。不算坑，算是帮我救了回来。
- 个人套路：先用 Claude 生成文件骨架 → 我检查确认 → Claude 执行验证（启动服务 + curl 测试）→ 一起 commit。每个步骤让 AI 做了之后我都要亲眼看到输出才往下走。

## 4. 决策记录

- 选了 FastAPI 而不是 Flask：因为 FastAPI 自带 OpenAPI 文档，后续前端对接更方便，而且异步支持更好。
- 选了 Vite 而不是 CRA：Vite 冷启动快，proxy 配置简单，CRA 已经停止维护。
- 地图暂定 Leaflet（免费）而不是 Google Maps（收费+API key 门槛对留学生太高）。
- `.claude/` 加入 `.gitignore`：这是 Claude Code 自动生成的权限文件，每台机器不同，不该进仓库。

## 5. 下周打算

1. 搭建用户系统：注册/登录 API + 前端页面（至少把表单画出来）
2. 跑通 Leaflet 地图组件，在悉尼 CBD 区域标注 3-5 个测试地点
3. 引入数据库（PostgreSQL），把 hello-world 的硬编码改成从数据库读

## 6. 资源沉淀

- [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart) — 官方快速入门，照着走了一遍安装和第一个 prompt
- [Your first day in Claude Code](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code) — 15 分钟 walkthrough，讲清楚了 /init、/plan、/review 几个核心命令
- [Conventional Commits](https://www.conventionalcommits.org/) — 规范 commit message 的参考，这周所有 commit 都按这个格式写了

## 7. 求助 / 卡点

- Cloudflare Workers + Pages 的实际部署流程还没跑过。Makefile 里的 `make deploy` 是占位命令。下周如果要做部署，需要搞清楚 wrangler 的配置。
