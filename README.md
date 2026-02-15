# AI无限进化系统

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![AI Assistants](https://img.shields.io/badge/AI%20Assistants-15+-green.svg)

**让AI能够持续学习和进化的智能技能系统**

**支持15+主流AI助手，一键快速部署！**

[功能特性](#功能特性) • [快速开始](#快速开始) • [支持的AI助手](#支持的ai助手) • [使用指南](#使用指南) • [系统架构](#系统架构)

</div>

---

## 📖 项目简介

AI无限进化系统是一个创新的技能管理系统，支持**15+主流AI助手**，能够让AI助手在每次对话中持续学习和进化。系统通过自动分析对话内容，提取语言模式和思考规则，实现真正的"无限进化"。

### 核心价值

- 🧠 **持续学习**：每次对话后自动更新技能，无需手动干预
- 🎯 **精准理解**：学习用户的语言习惯和表达方式，提供更精准的响应
- 🔄 **自动进化**：通过积累对话经验，持续优化AI的思考方式和响应质量
- 🎨 **灵活扩展**：通过钩子机制轻松扩展新功能
- 📊 **透明管理**：所有更新都有详细记录，可追溯系统进化轨迹
- 🚀 **多平台支持**：支持15+主流AI助手，一键快速部署

## ✨ 功能特性

### 1. 三层技能架构

系统采用三层技能架构，确保规则的有序管理和应用：

```
优先级（从高到低）：
1. san/SKILL.md      ← 最高优先级，用户输入语言规则和AI思考规则
2. father/SKILL.md   ← 主技能管理器，协调更新机制
3. order/SKILL.md    ← 其他技能，通过钩子触发
```

### 2. 自动更新机制

**核心特性**：每次对话结束后，系统会自动：

- ✅ 分析对话内容，提取语言模式和思考规则
- ✅ 更新san/SKILL.md（必须更新，即使没有新内容）
- ✅ 可选更新order/SKILL.md（仅在需要时）
- ✅ 记录详细的更新日志

### 3. 钩子系统

通过简单的钩子格式触发特定功能：

```bash
/钩子名 [参数]
```

**示例**：
```bash
/计算 1+1
/搜索 关键词
/总结 文档内容
```

### 4. 多AI助手支持

- ✅ 支持15+主流AI助手
- ✅ 一键快速初始化
- ✅ 自动适配不同AI助手的规则文件格式

## 🚀 快速开始

### 前置要求

- 任意支持的AI助手（见下方列表）
- Python 3.7+（用于更新脚本，可选）

### 方式一：使用Python脚本（推荐）

#### 1. 克隆仓库

```bash
git clone https://github.com/lpg-001/ai-infinite-evolution.git
cd ai-infinite-evolution
```

#### 2. 快速初始化

**初始化单个AI助手：**

```bash
# 初始化Cursor
python init.py --ai cursor

# 初始化Claude Code
python init.py --ai claude

# 初始化Windsurf
python init.py --ai windsurf

# 初始化GitHub Copilot
python init.py --ai copilot
```

**初始化所有AI助手：**

```bash
python init.py --ai all
```

**查看所有支持的AI助手：**

```bash
python init.py --list
```

**指定项目路径：**

```bash
python init.py --ai cursor --path /path/to/your/project
```

#### 3. 在AI助手中打开项目

初始化完成后，在对应的AI助手中打开项目，系统会自动加载规则文件。

### 方式二：使用Shell脚本（Linux/macOS）

```bash
# 初始化Cursor
./init.sh --ai cursor

# 初始化所有AI助手
./init.sh --ai all

# 查看所有选项
./init.sh --list
```

### 方式三：手动安装

1. **克隆仓库**

```bash
git clone https://github.com/lpg-001/ai-infinite-evolution.git
cd ai-infinite-evolution
```

2. **复制规则文件**

根据你使用的AI助手，从`templates/`目录复制对应的规则文件到项目根目录：

```bash
# 例如：使用Cursor
cp templates/.cursorrules .cursorrules

# 例如：使用Claude Code
cp templates/.clauderules .clauderules
```

3. **在AI助手中打开项目**

在对应的AI助手中打开项目，系统会自动加载规则文件。

## 🤖 支持的AI助手

系统支持以下15+主流AI助手：

| AI助手 | 规则文件 | 初始化命令 |
|--------|---------|-----------|
| **Claude Code** | `.clauderules` | `python init.py --ai claude` |
| **Cursor** | `.cursorrules` | `python init.py --ai cursor` |
| **Windsurf** | `.windsurfrules` | `python init.py --ai windsurf` |
| **Antigravity** | `.antigravityrules` | `python init.py --ai antigravity` |
| **GitHub Copilot** | `.copilotrules` | `python init.py --ai copilot` |
| **Kiro** | `.kirorules` | `python init.py --ai kiro` |
| **Codex CLI** | `.codexrules` | `python init.py --ai codex` |
| **Qoder** | `.qoderrules` | `python init.py --ai qoder` |
| **Roo Code** | `.roocoderules` | `python init.py --ai roocode` |
| **Gemini CLI** | `.geminirules` | `python init.py --ai gemini` |
| **Trae** | `.traerules` | `python init.py --ai trae` |
| **OpenCode** | `.opencoderules` | `python init.py --ai opencode` |
| **Continue** | `.continuerules` | `python init.py --ai continue` |
| **CodeBuddy** | `.codebuddyrules` | `python init.py --ai codebuddy` |
| **Droid (Factory)** | `.droidrules` | `python init.py --ai droid` |




## 📚 使用指南

### 基本使用

#### 正常对话

只需与AI正常对话即可，系统会自动：

1. **对话前**：加载san/SKILL.md和father/SKILL.md
2. **对话中**：根据加载的技能进行响应
3. **对话后**：
   - 分析对话内容
   - 更新san/SKILL.md（必须）
   - 可选更新order/SKILL.md
   - 说明更新内容

#### 使用钩子触发功能

如果需要触发特定功能，使用钩子格式：

```bash
/钩子名 [参数]
```

系统会自动检测钩子，并在order/SKILL.md中查找对应的技能。

### 技能文件说明

#### san/SKILL.md

**作用**：用户输入语言规则和AI思考规则

**内容**：
- 用户输入语言规则（语言模式、表达习惯、常用术语等）
- AI思考规则（思考流程、问题分析方法、响应风格等）

**更新规则**：
- ✅ 每次对话后必须更新
- ✅ 必须明确说明更新内容
- ✅ 即使没有新内容，也要进行优化性更新

#### father/SKILL.md

**作用**：主技能管理器

**功能**：
- 管理技能优先级
- 协调各技能模块的更新
- 在对话结束时自动更新san/SKILL.md

**更新方式**：系统自动管理，无需手动修改

#### order/SKILL.md

**作用**：其他技能规则

**内容**：
- 特定功能实现
- 工具使用方法
- 工作流程
- 特殊处理规则

**更新规则**：
- ⚠️ 只有当对话涉及相关技能时才更新
- ✅ 新增技能时必须添加对应的钩子定义

### 更新机制详解

#### 更新触发时机

**每次对话结束时自动触发**

#### 更新流程

1. **对话内容分析**
   - 识别用户输入的语言模式
   - 识别AI的思考方式
   - 识别需要新增或修改的规则

2. **更新判断**
   - **san技能**：必须更新（默认触发）
   - **order技能**：仅在需要时更新

3. **执行更新**
   - 更新对应的SKILL.md文件
   - 记录更新日志
   - 说明更新内容

#### 更新内容格式

```markdown
**最后更新时间**: 2025-01-XX HH:MM:SS（系统自动更新）
**更新内容**: 
- [新增/优化] 用户输入语言规则：[具体内容]
- [新增/优化] AI思考规则：[具体内容]
```

## 🏗️ 系统架构

### 目录结构

```
.
├── father/
│   └── SKILL.md              # 主技能管理器
├── san/
│   └── SKILL.md              # 用户输入语言规则和AI思考规则
├── order/
│   └── SKILL.md              # 其他技能规则（带钩子机制）
├── templates/                 # AI助手规则文件模板
│   ├── .cursorrules          # Cursor规则模板
│   ├── .clauderules          # Claude Code规则模板
│   ├── .windsurfrules         # Windsurf规则模板
│   └── ...                   # 其他AI助手规则模板
├── init.py                   # Python初始化脚本
├── init.sh                   # Shell初始化脚本
├── create_templates.py        # 模板生成脚本
├── README.md                 # 项目说明文档（本文件）
└── @.cursor/
    └── skills/
        ├── README.md          # 使用指南
        ├── 快速开始.md        # 快速开始指南
        ├── 系统总览.md        # 系统总览
        ├── 更新机制说明.md    # 更新机制详细说明
        ├── 实施计划.md        # 实施计划
        └── update_skill.py    # 自动更新脚本
```

### 工作流程

```
┌─────────────────────────────────────────────────────────┐
│                    AI无限进化系统                          │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ san/SKILL.md │    │father/SKILL  │    │order/SKILL.md│
│  (最高优先级) │    │    .md       │    │  (钩子触发)  │
└──────────────┘    └──────────────┘    └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
                ┌──────────────────────┐
                │   update_skill.py     │
                │   自动更新脚本        │
                └──────────────────────┘
```

### 核心组件

1. **San Skill**：用户输入语言规则和AI思考规则
2. **Father Skill**：主技能管理器，协调更新机制
3. **Order Skill**：其他技能规则，通过钩子触发
4. **更新脚本**：自动分析对话并更新技能文件
5. **初始化脚本**：快速为不同AI助手部署系统

## 🔧 高级用法

### 自定义钩子

在order/SKILL.md中添加新的钩子和技能：

```markdown
## 钩子列表

### /自定义钩子名

**功能说明**：描述钩子的功能

**使用方法**：
```
/自定义钩子名 [参数]
```

**实现细节**：
- 具体实现说明
- 参数说明
- 返回值说明
```

### 手动更新技能

虽然系统会自动更新，但你也可以手动编辑技能文件：

1. 编辑san/SKILL.md添加新的语言规则或思考规则
2. 编辑order/SKILL.md添加新的钩子和技能
3. 保持更新日志的格式规范

### 使用更新脚本

可以使用Python脚本手动触发更新：

```python
from @.cursor.skills.update_skill import SkillUpdater

updater = SkillUpdater()
result = updater.process_conversation_end(
    user_input="用户输入内容",
    ai_response="AI响应内容"
)
```

## 📖 最佳实践

1. **让系统自然进化**：正常对话即可，系统会自动学习和优化
2. **使用钩子扩展功能**：需要新功能时，在order/SKILL.md中添加钩子
3. **关注更新说明**：每次对话后查看更新内容，了解系统进化情况
4. **保持技能专注**：
   - san专注于语言和思考规则
   - order专注于功能实现
5. **定期查看日志**：了解系统的进化轨迹和优化方向
6. **选择合适的AI助手**：根据你的需求选择最适合的AI助手

## ❓ 常见问题

### Q: 如何查看系统进化情况？

A: 查看san/SKILL.md和order/SKILL.md的"最后更新时间"和"更新内容"部分。

### Q: 如何添加新功能？

A: 在order/SKILL.md中添加新的钩子和对应的技能说明。

### Q: 系统会自动删除旧规则吗？

A: 不会，系统会持续积累规则，实现真正的"无限进化"。

### Q: 如何重置系统？

A: 删除san/SKILL.md和order/SKILL.md中的内容，系统会重新开始学习。

### Q: 更新会影响性能吗？

A: 不会，更新机制经过优化，对对话响应速度没有影响。

### Q: 可以在其他AI助手中使用吗？

A: 可以！系统支持15+主流AI助手，使用`python init.py --list`查看所有选项。

### Q: 如何切换AI助手？

A: 只需在项目根目录放置对应AI助手的规则文件即可。例如，从Cursor切换到Claude Code，只需将`.cursorrules`替换为`.clauderules`。

## 🤝 贡献指南

欢迎贡献代码、提出建议或报告问题！

### 贡献方式

1. **Fork** 本仓库
2. **创建** 特性分支 (`git checkout -b feature/AmazingFeature`)
3. **提交** 更改 (`git commit -m 'Add some AmazingFeature'`)
4. **推送** 到分支 (`git push origin feature/AmazingFeature`)
5. **开启** Pull Request

### 贡献指南

- 遵循现有的代码风格
- 添加必要的注释和文档
- 确保更新机制正常工作
- 更新相关的文档

## 📝 更新日志

### v1.0.0 (2025-01-27)

- ✨ 初始版本发布
- ✅ 三层技能架构
- ✅ 自动更新机制
- ✅ 钩子系统
- ✅ 优先级管理
- ✅ 多AI助手支持（15+）
- ✅ 快速初始化脚本（Python + Shell）
- ✅ 模板文件自动生成

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！

## 📧 联系方式

- **GitHub**: [lpg-001/ai-infinite-evolution](https://github.com/lpg-001/ai-infinite-evolution)
- **Issues**: [GitHub Issues](https://github.com/lpg-001/ai-infinite-evolution/issues)
- **Discussions**: [GitHub Discussions](https://github.com/lpg-001/ai-infinite-evolution/discussions)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个Star！⭐**

Made with ❤️ by AI无限进化系统团队

</div>
