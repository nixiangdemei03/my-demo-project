# 02 — 原型工作流

> PRD → 低保真线框图 → 对照 PRD 校准。

## 流程

```
PRD v1.0 定稿
  → 确定页面清单（按角色分包：buyer/supplier/admin）
  → 每页对应 1-N 条 PRD 用户故事
  → 写统一 CSS（灰度、无装饰、只表达布局和流程）
  → 批量生成 HTML 页面（每页含 topbar + 核心内容区 + prototype-note）
  → 输出导航首页（index.html），含故事覆盖矩阵
  → PRD 更新后 → 校准原型（逐页比对 PRD 变更 → 修改不一致处）
  → 加入中英文切换器
```

## 原型结构

```
projects/prototypes/
├── index.html              ← 导航首页 + PRD 故事覆盖表
├── shared/wireframe.css    ← 灰度线框样式
├── buyer/                  ← 7 页：搜索→下单→追踪
├── supplier/               ← 4 页：工作台→产品→订单→主页
└── admin/                  ← 2 页：统计→审核
```

## 原型校准

| 步骤 | 操作 |
|:--:|------|
| 1 | 读最新 PRD 全文 |
| 2 | 逐页对比原型，标记不一致处 |
| 3 | 输出校准报告（编号 + 页面 + 问题 + PRD 现状 + 原型现状 + 严重度） |
| 4 | 逐页修改 |
| 5 | 验证交叉链接无断裂 |

## 设计原则

- 灰度无装饰 — 不写颜色不写动画，只表达布局、字段、跳转关系
- 每页标注覆盖的 PRD 用户故事 ID
- 页面间交叉链接（buyer→supplier、supplier→buyer、admin→buyer）
- 浏览器可直接打开，无需服务器

## 关键文件

- 原型：[projects/prototypes/](../projects/prototypes/)
- CSS：[projects/prototypes/shared/wireframe.css](../projects/prototypes/shared/wireframe.css)
