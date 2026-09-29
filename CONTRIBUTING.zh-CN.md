<h1 align="center">🎋 为 ISMS CORE 贡献</h1>

<p align="center"><a href="CONTRIBUTING.md">English</a> · <a href="CONTRIBUTING.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/QA-Engineering_First-2E8B57?style=for-the-badge" alt="QA Engineering First"/>
</p>

<p align="center">
  <a href="#-qa-关卡"><img src="https://img.shields.io/badge/QA_Gates-Enforced-00AA00?style=flat-square" alt="QA Gates"/></a>
  <a href="#-python-脚本标准"><img src="https://img.shields.io/badge/Python-Standardized-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
  <a href="#-线上研究要求"><img src="https://img.shields.io/badge/Research-Required-FF6600?style=flat-square" alt="Research Required"/></a>
  <a href="#-工程原则"><img src="https://img.shields.io/badge/Feynman-Approved-0066CC?style=flat-square" alt="Feynman Approved"/></a>
</p>

<p align="center">
  <em>并非所有文件都需要相同程度的标准化。把严谨用在该用的地方。</em>
</p>

---

## 🎯 QA 理念

ISMS CORE 针对**可靠性**、**可维护性**与**正确性**的重点所在，施加适当程度的严谨。

> *「标准化是好的。过度标准化是货柜崇拜。把严谨用在该用的地方。」*

---

## 📋 文件类型与品质标准

<table>
<tr>
<th>类型</th>
<th>一致性</th>
<th>变更频率</th>
<th>QA 关卡</th>
<th>徽章</th>
</tr>
<tr>
<td><strong>📜 POL</strong>（政策）</td>
<td>🔴 高</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Formal_Approval-9400D3?style=flat-square" alt="Formal"/></td>
</tr>
<tr>
<td><strong>📋 IMP</strong>（实作）</td>
<td>🟡 中等</td>
<td>中</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Living_Document-32CD32?style=flat-square" alt="Living"/></td>
</tr>
<tr>
<td><strong>🐍 SCR</strong>（脚本）</td>
<td>🔴 高</td>
<td>中</td>
<td><code># QA_VERIFIED:</code></td>
<td><img src="https://img.shields.io/badge/Code_Review-3776AB?style=flat-square" alt="Code Review"/></td>
</tr>
<tr>
<td><strong>📚 REF</strong>（参考数据）</td>
<td>🟡 中等</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Technical_Accuracy-FF6600?style=flat-square" alt="Technical"/></td>
</tr>
<tr>
<td><strong>🏢 CTX</strong>（情境）</td>
<td>🟡 中等</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Accuracy_Verified-0066CC?style=flat-square" alt="Verified"/></td>
</tr>
<tr>
<td><strong>📝 FORM</strong>（表单）</td>
<td>🟡 中等</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Template_Verified-32CD32?style=flat-square" alt="Template"/></td>
</tr>
</table>

---

### 📋 IMP 文件结构（UG／TG）

每一份 IMP（实作）文件都以**成对组合**的两个档案存在——一份用户指南与一份技术规格。这样的分离让审计人员、实作人员与开发人员各自拿到量身打造的文件，而不互相污染。

```
IMP/
├── ISMS-IMP-A.8.9.1-UG - Baseline Configuration Assessment.md    ← 供实作人员
└── ISMS-IMP-A.8.9.1-TG - Baseline Configuration Assessment.md    ← 供开发人员／审计人员
```

#### UG — 用户填写指南

**适用对象：** 信息安全分析师、控制措施拥有者、评估人员、合规主管

UG 是**由人撰写**的文件，引导读者完成一份评估工作簿。它回答的问题是：*「我手上有这份 Excel 档案——该拿它怎么办？」*

| 章节 | 用途 |
|---------|---------|
| 评估总览 | 本评估涵盖的范围、为何重要、范畴界线 |
| 先决条件 | 开始前必须就绪的事项（访问权、数据、批准） |
| 工作簿结构 | 逐一工作表概述 Excel 工作簿 |
| 填写逐步指南 | 逐步骤描述如何填写每一张工作表 |
| 证据收集 | 该搜集哪些证据、存放位置、命名惯例 |
| 常见陷阱 | 8-10 个 `MISTAKE:` 范例与修正 |
| 质量检查清单 | 提交前的检核项目 |
| 评审与批准 | 由谁审查、批准流程、升级处理 |

#### TG — 技术规格

**适用对象：** Python 开发人员、Excel 工作簿开发人员、QA 工程师

TG 是由 Python 生成器脚本（`SCR/generate_*.py`）**自动产生**。它是生成器代码的人类可读版本——每一张工作表、字段、数据验证下拉列表、色彩样式与公式，都以结构化表格记录。

| 章节 | 用途 |
|---------|---------|
| 工作簿概览 | 文件编号、输出档名、工作表总数、控制项引用 |
| 配色方案 | 所有色码、样式名称与用途描述 |
| 工作表 N：*名称* | 逐工作表的规格，含字段、宽度、验证、公式 |
| 数据验证清单 | 生成器中定义的所有下拉列表值清单 |

**重新产生 TG：** 每当生成器变更，工厂脚本就会重新产生 TG 内容：

```bash
python3 generate_tg_from_scr.py --apply          # 全部 252 个 TG
python3 generate_tg_from_scr.py --control a.8.9   # 单一控制群组
```

每一份 TG 技术内容的开头都会标记其来源：

```
> 由 `generate_a89_1_baseline_configuration.py` 自动产生
> 重新产生指令：`python3 generate_tg_from_scr.py --apply`
```

#### IMP QA 准则（v4.5+）

| 要求 | 描述 |
|-------------|-------------|
| ✅ UG/TG 分离 | 每份 IMP 都以 `-UG` 与 `-TG` 档案成对存在 |
| ✅ 标准表头 | 三行格式：粗体标题、副标（UG/TG）、ISO 控制项引用 |
| ✅ 控制措施引文 | 依 ISO 27001:2022 附录 A，使用 "should"（而非 "shall"） |
| ✅ 英式拼法 | organisation、authorised、standardised |
| ✅ 标准结尾 | `**END OF SPECIFICATION**` + 分隔线 + 以破折号（—）带出的引文 |
| ✅ QA 标记 | 🎋 标记之后的 `<!-- QA_VERIFIED: YYYY-MM-DD -->` |

---

## 🚦 QA 关卡

<p align="center">
  <img src="https://img.shields.io/badge/Gate-Pass_Required-00AA00?style=for-the-badge" alt="Gate Pass Required"/>
</p>

内容**唯有在 QA 关卡通过后**才会晋升到本储存库。每种文件类型都带有一个 QA 标记，晋升前必须存在：

| 文件 | 必要的 QA 标记 |
|----------|--------------------|
| POL / IMP / REF / CTX / FORM | 档案结尾的 `<!-- QA_VERIFIED: YYYY-MM-DD -->` |
| SCR（Python 脚本） | `# QA_VERIFIED: YYYY-MM-DD` 页尾区块 |

> **维护者注意：** 晋升由私有 `factory_claude_ai` 储存库中的内部开发工具（`95-isms-core-factory/promote_control.sh`）处理。本储存库中的内容在发布到此之前，都已通过所有 QA 关卡。

---

## 🐍 Python 脚本标准

### 必要结构

```python
# =============================================================================
# 文件中继数据
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.X.X.X"
WORKBOOK_NAME = "Assessment Name"
CONTROL_ID = "A.X.X"
CONTROL_NAME = "Control Name"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# 时间戳记
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# 输出档名
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"
```

### 日志

| ❌ 不要 | ✅ 要 |
|----------|-------|
| `print("message")` | `logger.info("message")` |

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)
```

### QA 页尾

```python
# =============================================================================
# QA_VERIFIED: YYYY-MM-DD
# QA_STATUS: PASSED
# QA_TOOL: Claude Code
# CHANGES: 变更描述
# =============================================================================
```

---

## 📂 文件夹结构

每个控制项都自成一格，包含所有成品类型：

```
isms-a.X.X-control-name/
├── POL/                      # 📜 政策文件
├── IMP/                      # 📋 实作指南（UG + TG 成对）
├── SCR/                      # 🐍 脚本（生成器、正规化器、合并器）
├── WKBK/                     # 📊 产生的 Excel 工作簿
├── REF/                      # 📚 参考数据（如适用）
├── CTX/                      # 🏢 情境文件（如适用）
└── FORM/                     # 📝 表单与模板（如适用）
```

---

## 🔍 线上研究要求

<p align="center">
  <img src="https://img.shields.io/badge/⚠️_Research-MANDATORY-FF0000?style=for-the-badge" alt="Research Mandatory"/>
</p>

**所有 IMP 与 SCR 开发都必须包含线上研究**，以验证：

- ✅ 该控制措施的最新最佳实务
- ✅ 与 NIST、CIS、MITRE ATT&CK 框架的一致性
- ✅ 实作指南的技术准确性
- ✅ 最新工具能力与整合模式

**关键参照框架：**

<p align="center">
  <img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square" alt="ISO"/>
  <img src="https://img.shields.io/badge/NIST_CSF-2.0-FF6600?style=flat-square" alt="NIST"/>
  <img src="https://img.shields.io/badge/CIS_Controls-v8-00AA00?style=flat-square" alt="CIS"/>
  <img src="https://img.shields.io/badge/MITRE_ATT&CK-Enterprise-DC143C?style=flat-square" alt="MITRE"/>
</p>

---

## ⚖️ 工程原则

> *「标准化是好的。过度标准化是货柜崇拜。把严谨用在该用的地方。」*

**Feynman 会问：** *「这样的差异有存在的目的吗？」*

| 答案 | 动作 |
|--------|--------|
| ✅ 是 | 记录原因并保留 |
| ❌ 否 | 标准化 |
| ⚠️ 破坏功能 | 不要强求一致 |

---

## 🔬 验证流程

<p align="center">
  <img src="https://img.shields.io/badge/Multi--Stage-QA_Process-DC143C?style=for-the-badge" alt="Multi-Stage QA Process"/>
</p>

每一个控制套件都会经过结构化的多阶段验证流程，以确保品质与正确性。

```
  ┌──────────────────────────┐
  │ ISMS Core 项目           │
  │ （架构师／拥有者）       │
  └─────────────┬────────────┘
                │ 需求 + 领域专业知识
                ▼
  ┌──────────────────────────┐
  │ Claude Code（Sonnet）    │──── 实作
  │ 建置 + 代码审查        │     POL, IMP, SCR, REF, CTX
  └─────────────┬────────────┘
                │
                ▼
  ┌──────────────────────────┐
  │ ISMS Copilot X           │──── 审计审查
  │ （文件 + QA）            │     阶段 1：适足性，阶段 2：有效性
  └─────────────┬────────────┘
                │
                ▼
  ┌──────────────────────────┐
  │ ISMS Core 项目           │
  │ 最终批准关卡             │
  └──────────────────────────┘
```

| 贡献者 | 角色 | 重点 |
|-------------|------|-------|
| **Claude Code（Sonnet）** | 实作 + QA | 政策撰写、Python 生成器、代码审查、模式分析 |
| **ISMS Copilot X** | 文件审计 | 阶段 1 文件适足性、阶段 2 实作有效性 |
| **ISMS Core 项目** | 架构师 + 最终关卡 | 方法论、领域专业知识、IP 拥有权、批准权限 |

每一个阶段都在 ISMS Core 项目撰写的**专用指令集**下运作——这些结构化提示定义了范畴、限制、输出格式与审计准则。它们是受控的运营文件，精确规定必须检查什么、忽略什么（例如占位日期），以及如何分类发现事项。

### 发现事项分类

| 严重性 | 准则 | 动作 |
|----------|----------|--------|
| **严重** | 缺少控制措施实作、审计阻碍 | 晋升前必须解决 |
| **高** | 证据或涵盖范围有显著缺口 | 晋升前必须解决 |
| **中** | 指南不完整、轻微不一致 | 于 QA 阶段解决 |
| **低** | 风格、格式、改善机会 | 留待未来迭代追踪 |

---

## 🤖 AI 辅助开发

<table>
<tr>
<th>贡献者</th>
<th>角色</th>
</tr>
<tr>
<td><strong>ISMS Core 项目</strong></td>
<td>方法论、架构、领域专业知识、IP 拥有权</td>
</tr>
<tr>
<td><strong>Claude Code（Sonnet）</strong></td>
<td>主要实作伙伴——详见下方贡献描述</td>
</tr>
<tr>
<td><strong>ISMS Copilot X</strong></td>
<td>文件审计、适足性审查、实作有效性</td>
</tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/IP_Ownership-Gregory_Griffin-FFD700?style=flat-square" alt="IP Ownership"/>
</p>

---

## 🧠 Claude Code — 实作贡献

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Sonnet_4.6-CC785C?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code Sonnet"/>
  <img src="https://img.shields.io/badge/Dec_2025–Ongoing-Continuous-2E8B57?style=for-the-badge" alt="Ongoing"/>
</p>

Claude Code（Anthropic，Sonnet 模型系列）自 2025 年 12 月 31 日起一直是 ISMS CORE 的主要实作伙伴，合作仍在持续。在 ISMS Core 项目指导的持续结对工作阶段中——该项目撰写了所有方法论、架构决策、提示指令集与多模型协作——Claude Code 交付了完整的自动化层、撰写并精炼了所有文件，并打造了让本项目得以维护的工厂基础设施。

### 打造了什么

<table>
<tr>
<th>类别</th>
<th>成品</th>
<th>规模</th>
</tr>
<tr>
<td><strong>Python 脚本</strong></td>
<td>工作簿生成器</td>
<td><strong>285</strong> 支脚本 — 188 (FW) + 53 (OP) + 21 (PRIV) + 12 (CLD) + 10 (AI) + 1 (AI 生成器工具)</td>
</tr>
<tr>
<td><strong>IMP 文件</strong></td>
<td>每项评估的用户指南（UG）+ 技术规格（TG）</td>
<td><strong>464</strong> 个档案 — 376 FW（188 UG + 188 TG）+ 42 PRIV + 24 CLD + 20 AI + 2 AI 基础</td>
</tr>
<tr>
<td><strong>POL 文件</strong></td>
<td>以 "WITH WHAT" 验证方法论构成的政策框架</td>
<td><strong>53</strong> 份框架 POL + <strong>53</strong> 份运营 OP-POL</td>
</tr>
<tr>
<td><strong>Excel 工作簿</strong></td>
<td>含数据验证、公式、条件式格式的评估工作簿</td>
<td><strong>188</strong> (FRAMEWORK) + <strong>53</strong> (OPERATIONAL)</td>
</tr>
<tr>
<td><strong>工厂自动化</strong></td>
<td>组装、晋升、备份、同步、拆分、正规化脚本</td>
<td>10+ 项主要工具</td>
</tr>
<tr>
<td><strong>QA 基础设施</strong></td>
<td>QA 关卡、状态仪表板、验证流水线</td>
<td><strong>53/53</strong> 控制项通过</td>
</tr>
</table>

### 历程

```
2025 年 12 月 31 日：试点控制项建立 -> A.8.24
2026 年 1 月：      ISMS CORE 框架 -> 53 个控制套件完成 93 项控制措施
2026 年 2 月：      ISMS CORE 运营版 -> 53 个控制套件完成 93 项控制措施
2026 年 3 月：      ISMS CORE 隐私（ISO 27701:2025）-> 完成 21 个控制群组
2026 年 3 月：      ISMS CORE 云端（ISO 27018:2025）-> 完成 12 个控制群组
2026 年 3 月：      ISMS CORE 平台 -> 于 isms-core.com 上线
2026 年 4 月：      ISMS CORE AI（ISO 42001:2023）-> 完成 12 个控制群组
2026 年 4 月：      FR + DE + IT 翻译 -> 全部 5 个套件完成
2026 年 4 月：      威胁情报扩充 -> 第 39–49 阶段
                    各连接器 OpenSearch 索引、ENISA EUVD、Exploit-DB、
                    MITRE ATT&CK v19、AlienVault OTX（第 12 个 OSINT 来源）、
                    VirusTotal 扩充、TLP 标签、威胁曝险页面、
                    18 个 OSD 仪表板、EBIOS RM、通知系统、安全审计
2026 年 5 月：      用户手册更新 -> 第 16 章（威胁情报）全面重写
```

### 平台

**ISMS CORE 平台**（`isms-core-platform/`）已上线——一个 FastAPI 后端，搭配 PostgreSQL、OpenSearch、Docker Compose 部署、nginx TLS 与框架关联引擎。它把以档案为基础的框架转化为可运作的合规平台：由数据库驱动、可透过 WebUI 编辑，具备证据追踪、缺口管理、29 个合规评估模块、涵盖 59 个轴（4,671 个对象）的对照映射，以及 44 个自动化证据连接器，将即时证据推送至各来源的 OpenSearch 索引。

<p align="center">
  <em>怀抱著这样的信念打造：安全合规应是工程纪律，而非打勾作秀。</em>
</p>

---

<p align="center">
  <strong>Copyright © 2025-2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
  <em>竹子天线真正管用的地方。</em> 🎋
</p>
