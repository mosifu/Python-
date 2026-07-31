# Python 学习笔记（Java 背景 + 黑马课程）

> 基于 B 站「黑马程序员 Python+AI 零基础入门到大神」课程（BV1sHU9BmEne，185集）的 AI 辅助学习仓库。

> 📌 **分支说明**：`main` 分支存放 **AI 学习工具链配置**（Skill + 智能体）；完整的笔记、示例代码和每日复盘在 [`learn`](https://github.com/mosifu/Python-/tree/learn) 分支。

---

## 🎯 解决什么问题

有 Java 基础的开发者学 Python 时，常遇到两个痛点：

1. **知识迁移慢**：Python 与 Java 有大量相似概念，但语法差异（缩进、`elif`、`and/or`、`self`、无 `new` 等）容易写错，缺乏系统对比。
2. **学完就忘**：看视频不动手、记笔记无结构、没有复盘机制，知识留不下来。

本仓库用 **Java 对比学习法 + AI 辅助笔记/复盘** 解决上述问题：
- 每个知识点都附 **Java 相似点 / 不同点** 对照表，避免把 Java 习惯错误套用到 Python
- 学习过程由 Claude Code 的 Skill 和两个智能体辅助，自动生成结构化笔记和每日复盘

---

## ✨ 主要功能

### main 分支（本分支）：AI 学习工具链

| 工具 | 文件 | 作用 |
|------|------|------|
| **学习 Skill** | `.cursor/skills/learn-python-beginner/SKILL.md` | 定义学习路径（阶段0-7）、Java 对照表、笔记模板、「生成笔记」命令规则 |
| **学习分析师** | `.claude/agents/learning-analyst.md` | 分析每日笔记+代码，生成 9 段复盘报告和练习题 |
| **练习批改员** | `.claude/agents/practice-reviewer.md` | 批改练习答案，逐题反馈对错和修正建议 |

### learn 分支：完整学习内容

| 内容 | 路径 | 说明 |
|------|------|------|
| 结构化笔记 | `notes/阶段2-核心语法/` | 7 份 `.md`（2.1~2.7），含 Java 对比表和坑点 |
| 可运行示例 | `notes/*/examples/` | 29 个 `.py` 示例，只用标准库 |
| 每日复盘 | `daily_summaries/YYYY-MM-DD/` | 8 天复盘（summary 报告 + practice 练习） |

---

## 📦 项目结构

```
python_work/
├── main 分支（本分支）                     # AI 工具链配置
│   ├── .cursor/skills/learn-python-beginner/
│   │   └── SKILL.md                      # 学习路径 + 笔记生成规则
│   └── .claude/agents/
│       ├── learning-analyst.md           # 每日复盘分析师
│       └── practice-reviewer.md          # 练习批改助教
│
└── learn 分支                              # 完整学习内容
    ├── notes/阶段2-核心语法/
    │   ├── 2.1-数据存储与运算.md          # 第09-21集 ✅
    │   ├── 2.2-流程控制.md                # 第22-35集 ✅
    │   ├── 2.3-数据容器.md                # 第36-55集 ✅
    │   ├── 2.4-函数.md                    # 第57-70集 ✅
    │   ├── 2.5-类型注解与模块.md          # 第71-76集 ✅
    │   ├── 2.6-面向对象基础.md            # 第77-85集 ✅
    │   ├── 2.7-异常处理.md                # 第86-87集 ✅
    │   └── */examples/*.py                # 29个可运行示例
    └── daily_summaries/
        └── 2026-MM-DD/                    # 每日复盘
            ├── summary_YYYY-MM-DD.md
            └── practice_YYYY-MM-DD.py
```

---

## 📈 学习进度

| 阶段 | 集数 | 主题 | 状态 |
|------|:--:|------|:--:|
| 2.1 | 09-21 | 数据存储与运算（字面量/变量/类型/字符串/输入输出/运算符） | ✅ |
| 2.2 | 22-35 | 流程控制（if/match/while/for/嵌套循环） | ✅ |
| 2.3 | 36-55 | 数据容器（list/str/tuple/set/dict） | ✅ |
| 2.4 | 57-70 | 函数（参数/作用域/*args/**kwargs/lambda/递归） | ✅ |
| 2.5 | 71-76 | 类型注解与模块（注解/import/包） | ✅ |
| 2.6 | 77-85 | 面向对象基础（class/魔法方法/类属性） | ✅ |
| 2.7 | 86-87 | 异常处理（try/except/finally） | ✅ |
| 3 | 88-119 | AI 应用实战（大模型/提示词/Streamlit） | 🔜 |

> 阶段 2 核心语法已全部完成，具备与 Java SE 基础对等的能力。

---

## 🛠️ 安装方法

### 前置条件

- [Python 3.10+](https://www.python.org/downloads/)（match 语法、`|` 联合类型需要 3.10+）
- [Claude Code CLI](https://code.claude.com/)（用于 Skill 和智能体）
- [Git](https://git-scm.com/)

### 步骤

```bash
# 1. 克隆仓库
git clone https://github.com/mosifu/Python-.git
cd Python-

# 2. 获取完整学习内容（main 只有工具链，learn 有笔记和示例）
git checkout learn

# 3. 验证 Python 环境
python --version   # 需要 3.10+

# 4. 运行任意示例验证环境（无需安装依赖，示例只用标准库）
python "notes/阶段2-核心语法/2.1-数据存储与运算/examples/01_数字字面量.py"
```

> 本仓库的示例代码**只使用 Python 标准库**，无需 `pip install` 任何第三方包。

### 启用 AI 辅助工具链

Skill 和 Agent 已内置在仓库中，Claude Code 启动时会自动加载：

```bash
# Skill 位置：.cursor/skills/learn-python-beginner/SKILL.md
# Agent 位置：.claude/agents/learning-analyst.md
#            .claude/agents/practice-reviewer.md
```

---

## 📖 使用方法

### 日常学习流程

```
看视频  ->  遇到不懂的提问  ->  生成笔记  ->  每日复盘  ->  推送 GitHub
```

#### 1. 看视频学习
按学习路径观看 B 站课程，跟着敲代码练习。

#### 2. 提问并生成笔记
学完一个知识点后，把练习代码发给 Claude，说 **「生成笔记」**：

```
# 你只需说：
生成笔记

# Claude 会：
# 1. 读取你的练习代码
# 2. 对照 SKILL 中的学习路径定位章节
# 3. 生成 .md 笔记（含 Java 对比表）+ .py 示例代码
# 4. 优秀案例直接收录进笔记
```

#### 3. 每日复盘
一天学习结束后，说 **「帮我复盘今天的学习」**：

```
# learning-analyst 智能体会：
# 1. 扫描今日笔记和示例代码
# 2. 评估知识覆盖、代码质量、掌握度
# 3. 生成 summary_YYYY-MM-DD.md（9段报告）
# 4. 生成 practice_YYYY-MM-DD.py（练习题+自测题）
```

#### 4. 批改练习
做完 `practice_*.py` 里的练习后，说 **「批改练习」**：

```
# practice-reviewer 智能体会：
# 1. 解析每道题的"我的回答"
# 2. 逐题标记 ✅/❌/⚠️
# 3. 给出错误分析和标准答案
# 4. 输出总体正确率和复习建议
```

#### 5. 推送到 GitHub
```bash
git add -A
git commit -m "今日学习：阶段X.X 主题（第XX-XX集）"
git push origin learn
```

---

## 📝 输入输出示例

### 示例1：生成笔记

**输入**（学习者发送练习代码 + 命令）：

```
今天我学习了 list 列表，这是我的代码 [附 .py 文件]... 请帮我生成笔记
```

**输出**（Claude 生成）：

```
notes/阶段2-核心语法/2.3-数据容器/
├── 2.3-数据容器.md          ← 含 Java 对比表 + 坑点编号
└── examples/
    ├── 01_list列表.py       ← 可运行示例
    └── 02_str字符串操作.py
```

笔记片段示例：

```markdown
### 1. 什么是 list
- **是什么**：列表就像火车，每节车厢可装不同类型的东西
- **Java 对比**：≈ ArrayList，但 Python 列表可存不同类型

| | Python list | Java ArrayList |
|------|-------------|---------------|
| 定义 | `[1, 2, 3]` | `new ArrayList<>(List.of(1,2,3))` |
| 混合类型 | ✅ 可以 | ❌ 必须同类型 |
```

### 示例2：每日复盘

**输入**：

```
帮我复盘今天的学习
```

**输出**：

```
daily_summaries/2026-07-25/
├── summary_2026-07-25.md   ← 9段报告
└── practice_2026-07-25.py  ← 8道练习题
```

复盘报告片段：

```markdown
| 项目 | 结果 |
|------|------|
| 综合评级 | A 级（4.7/5.0） |
| 知识覆盖 | 函数9大知识点全覆盖 |
| 掌握度 | 85-90% |
| 核心坑点 | sum覆盖内置函数、global放函数中间 |
```

### 示例3：运行示例代码

**输入**：

```bash
python "notes/阶段2-核心语法/2.4-函数/examples/02_函数进阶.py"
```

**输出**：

```
=== 9. 电商订单计算器 ===
  商品总额: 10388
  减优惠券: 10 -> 10378
  减积分(4000分=40元) -> 10338
  加运费: 9.9
  订单总金额: 10347.9
```

---

## 🤖 AI 工具链说明

### learning-analyst（学习分析师）

| 项目 | 说明 |
|------|------|
| 触发词 | 「帮我复盘」「今日学习总结」 |
| 输入 | `notes/` 下的笔记和示例代码 |
| 输出 | `daily_summaries/YYYY-MM-DD/` 双文件 |
| 限制 | 只读 `notes/`，只写 `daily_summaries/` |

### practice-reviewer（练习批改员）

| 项目 | 说明 |
|------|------|
| 触发词 | 「批改练习」「检查练习」 |
| 输入 | `practice_*.py` 中的 `# 我的回答：` |
| 输出 | 逐题批改反馈（✅/❌/⚠️ + 修正建议） |
| 规则 | 编程题提取非注释代码，自测题提取注释回答 |

### learn-python-beginner Skill

定义了完整的学习路径（阶段0-7）、Java 对照表、笔记模板、示例代码规范（禁用超前语法）。

---

## 📊 项目数据

| 指标 | 数量 | 所在分支 |
|------|:--:|:--:|
| 学习笔记 | 7 份（2.1~2.7） | learn |
| 可运行示例 | 29 个 `.py` 文件 | learn |
| 每日复盘 | 8 天 | learn |
| AI 智能体 | 2 个 | main + learn |
| 学习 Skill | 1 个 | main + learn |
| 完成集数 | 第 09-87 集（阶段2全部完成） | learn |

---

## 📚 课程来源

- **课程**：黑马程序员 Python+AI 零基础入门到大神
- **B站**：https://www.bilibili.com/video/BV1sHU9BmEne/
- **总集数**：185 集（约 50 小时）

---

## 📄 License

本仓库为个人学习笔记，仅供学习交流使用。课程内容版权归黑马程序员所有。
