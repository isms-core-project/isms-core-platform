<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Repository_Structure-2E8B57?style=for-the-badge" alt="ISMS CORE Repository Structure"/>
</p>

<h1 align="center">📂 Repository Structure</h1>

<p align="center"><a href="STRUCTURE.md">English</a> · <a href="STRUCTURE.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<p align="center">
  <em>本储存库中所有文件夹、文件与成品类型的完整地图。</em>
</p>

---

## 成品类型 — 每个控制套件里有什么

在阅读文件夹树之前，先了解每一种成品类型是什么：

| 成品 | 格式 | 是什么 | 谁来用 |
|----------|--------|------------|-------------|
| **POL** | Markdown | 治理政策 — 描述该控制措施要求什么、由谁负责、适用哪些标准。填上组织名称／CISO／生效日期后即可签署发布。 | ISMS 经理 → 董事会／员工 |
| **IMP-UG** | Markdown | 实施用户指南 — ISMS 经理如何实施与操作该控制措施。角色、流程步骤、KPI、评审周期。 | ISMS 经理 |
| **IMP-TG** | Markdown | 实施技术指南 — 给工程师的逐步操作。指令、配置、厂商注意事项、强化检查表。 | 安全工程师 |
| **SCR** | Python 3.11+ | 评估生成器 — `python3 generate_*.py` 产出结构化的 Excel 合规工作簿。唯一相依套件：`openpyxl`。 | ISMS 经理 → 审计人员 |
| **WKBK** | Excel (.xlsx) | 产出的合规工作簿 — 逐控制措施的评估项目、证据状态、评分与审计人员备注。由 SCR 生成器产出。 | 审计人员／控制措施负责人 |
| **REF** | Markdown | 取自 ISO 标准条文、对应本控制措施的参考摘录。与相邻附录 A 控制措施的交叉参照。 | ISMS 经理／审计人员 |
| **CTX** | Markdown | 将本控制套件连结至相邻与相依套件的脉络文件 — 用于控制措施堆叠与依赖项对应。 | ISMS 经理 |
| **FORM** | Markdown | 可直接使用的模板：证据表单、会议议程、批准记录、风险接受表单。 | ISMS 经理／控制措施负责人 |

**运营产品：** 仅有 POL + SCR + WKBK（不含 IMP-UG/TG — 设计上刻意从简）

**隐私／云端／AI：** POL + IMP-UG + IMP-TG + SCR + WKBK

---

## 顶层储存库

```
factory_isms/
│
├── README.md                  # 项目总览与快速开始
├── PARADIGM.md                # 产品总览与范式转移指南
├── PLATFORM.md                # 平台架构、功能与完整部署指南（含安装指南）
├── STRUCTURE.md               # 本文件
├── COMPLIANCE.md              # 29 个合规评估模块 — 涵盖范围备注
├── CONTRIBUTING.md            # QA 流程与标准
├── PHILOSOPHY.md              # 反货物崇拜方法论
├── CODE_OF_CONDUCT.md         # 社群标准
├── SECURITY.md                # 漏洞通报政策
├── LICENSE                    # AGPL-3.0 — 规范下方内容包（双重授权，见 README §License）
│
├── isms-core-framework/       # 🏗️ ISO 27001:2022 — 完整工程产品
├── isms-core-operational/     # ⚡ ISO 27001:2022 — 轻量中小企业版
├── isms-core-privacy/         # 🔒 ISO 27701:2025 — 隐私扩充套件
├── isms-core-cloud/           # ☁️ ISO 27018:2025 云端扩充套件 + ISO 27017:2026 云端安全
├── isms-core-ai/              # 🤖 ISO 42001:2023 — AI 扩充套件
├── isms-core-platform/        # 🖥️ 平台部署套件 — 自有 LICENSE（Apache 2.0）
├── USER_MANUAL/               # 📖 完整用户手册（21 章）— 由应用程序内 /docs/user-manual.md 提供
├── COMPLIANCE.md              # 📋 评估模块涵盖范围
└── screenshots/               # 平台 UI 萤幕截图
```

---

## 🏗️ isms-core-framework/ — ISO 27001:2022 完整工程

53 个控制套件涵盖全部 93 项附录 A 控制措施。每个套件都包含完整成品组合（POL、IMP-UG、IMP-TG、SCR、WKBK、REF、CTX、FORM）。

```
isms-core-framework/
│
├── README.md                              # 产品总览
├── CONTROLS.md                            # 53 个控制套件索引 — 从这里开始
├── COVERAGE.md                            # 93 项附录 A 控制措施 → 53 个套件的对应
├── STATUS.md                              # 实施指标
├── STACKING.md                            # 控制措施分组与堆叠方法论
├── CHANGELOG.md                           # 版本历史
│
├── 00-foundation-policies/                # 法规框架基线
│   ├── isms-pol-00-regulatory-framework/
│   │   └── POL/                           # ISMS-POL-00 (EN + FR + DE + IT)
│   └── isms-pol-01-isms-scope/
│       └── POL/                           # ISMS-POL-01 (EN + FR + DE + IT)
│
├── A.5-organisational-controls/           # 21 个控制套件
│   └── isms-a.5.X-X-control-name/
│       ├── POL/                           # 治理政策（EN + fr/ + de/ + it/）
│       ├── IMP/
│       │   ├── IMP-UG/                    # 用户指南 — ISMS 经理
│       │   └── IMP-TG/                    # 技术指南 — 工程师
│       ├── SCR/                           # Python 评估生成器
│       ├── WKBK/                          # 产出的 Excel 工作簿
│       ├── REF/                           # ISO 标准参考摘录
│       ├── CTX/                           # 控制措施脉络 + 依赖项对应
│       └── FORM/                          # 模板与表单
│
├── A.6-people-controls/                   # 4 个控制套件（结构相同）
├── A.7-physical-controls/                 # 6 个控制套件（结构相同）
└── A.8-technological-controls/            # 22 个控制套件（结构相同）
```

**关键文件：**
- `CONTROLS.md` — 全部 53 个套件的索引清单，含控制措施名称与附录 A 参照
- `COVERAGE.md` — 将 93 项 ISO 27001:2022 附录 A 控制措施对应到 53 个套件（部分套件涵盖多项控制措施）
- `STACKING.md` — 解释成熟组织如何堆叠套件

---

## ⚡ isms-core-operational/ — ISO 27001:2022 中小企业版

53 个控制群组，成品组合较精简（POL + SCR + WKBK）。没有实施指南 — 运营政策设计上即完整且自足。

```
isms-core-operational/
│
├── README.md
├── CONTROLS.md                            # 53 个控制群组索引
├── STATUS.md
├── CHANGELOG.md
│
├── 00-checklist-engine/                   # 共用的检查表生成器引擎
│
├── A.5-organisational-controls/           # 21 个控制群组
│   └── isms-a.5.X-X-control-name/
│       ├── POL/                           # OP-POL（EN + fr/ + de/ + it/）
│       ├── SCR/                           # Python 合规检查表生成器
│       └── WKBK/                          # 产出的 Excel 检查表
│
├── A.6-people-controls/                   # 4 个控制群组
├── A.7-physical-controls/                 # 6 个控制群组
└── A.8-technological-controls/            # 22 个控制群组
```

---

## 🔒 isms-core-privacy/ — ISO 27701:2025 隐私扩充套件

21 个控制群组，分属三种范围：控管者（a.1.x）、处理者（a.2.x）与共用（a.3.x）。

```
isms-core-privacy/
│
├── README.md
├── 00-checklist-engine/                   # 共用的隐私检查表引擎
│
├── 00-priv-foundation-policies/           # 基础政策
│   ├── priv-pol-00-privacy-regulatory-framework/
│   │   └── POL/                           # PRIV-POL-00 (EN + fr/ + de/ + it/)
│   └── priv-pol-01-privacy-governance/
│       └── POL/                           # PRIV-POL-01 (EN + fr/ + de/ + it/)
│
├── privacy-controller/                    # 8 个控管者控制群组（a.1.x）
│   └── priv-a.1.X.X-X-control-name/
│       ├── POL/                           # PRIV-POL（EN + fr/ + de/ + it/）
│       ├── IMP/
│       │   ├── IMP-UG/
│       │   └── IMP-TG/
│       ├── SCR/
│       └── WKBK/
│
├── privacy-processor/                     # 5 个处理者控制群组（a.2.x）
│   └── priv-a.2.X.X-X-control-name/      # 与控管者结构相同
│
└── privacy-shared/                        # 8 个共用控制群组（a.3.x）
    └── priv-a.3.X.X-X-control-name/      # 与控管者结构相同
```

---

## ☁️ isms-core-cloud/ — ISO 27018:2025 云端扩充套件 + ISO 27017:2026 云端安全

16 个控制群组，分属两项独立标准：12 个涵盖云服务提供商的
PII 保护要求（ISO 27018:2025），以及 4 个独立的云端安全扩充控制措施
（ISO 27017:2026），外加一份指南附录，针对既有 38 项已在云端情境适用的
附录 A 控制措施。

```
isms-core-cloud/
│
├── README.md
├── iso27018-pii-cloud/
│   └── cld-a.X-control-name/              # 12 个附录 A 控制群组
│       ├── POL/                           # CLD-POL（EN + fr/ + de/ + it/）
│       ├── IMP/
│       │   ├── IMP-UG/
│       │   └── IMP-TG/
│       ├── SCR/
│       └── WKBK/
└── iso27017-sec-cloud/
    ├── cld-sec-a.X-control-name/           # 4 个独立扩充控制措施
    │   ├── POL/                            # CLD-SEC-POL（EN + fr/ + de/ + it/）
    │   ├── IMP/
    │   │   ├── IMP-UG/
    │   │   └── IMP-TG/
    │   └── SCR/
    └── cld-sec-guidance-addendum/
        └── REF/                            # 其余 38 项附录 A 控制措施的既有控制措施指南
```

---

## 🤖 isms-core-ai/ — ISO 42001:2023 AI 扩充套件

12 个 AI 控制群组（2 个基础 + 10 个附录 A），涵盖 AI 治理、影响评估、负责任使用与第三方 AI 关系。

```
isms-core-ai/
│
├── README.md
├── 00-checklist-engine/                   # 共用的 AI 检查表引擎
│
├── 00-ai-foundation-policies/             # 基础政策
│   ├── ai-pol-00-ai-regulatory-applicability/
│   │   └── POL/                           # AI-POL-00 (EN + fr/ + de/ + it/)
│   └── ai-pol-01-aims-governance-and-decision-making/
│       └── POL/                           # AI-POL-01 (EN + fr/ + de/ + it/)
│
└── ai-a.X.X-X-control-name/              # 10 个附录 A 控制群组
    ├── POL/                               # AI-POL（EN + fr/ + de/ + it/）
    ├── IMP/
    │   ├── IMP-UG/                        # 用户指南 — ISMS 经理
    │   └── IMP-TG/                        # 技术指南 — 工程师
    └── SCR/                               # Python 合规检查表生成器
```

---

## 🖥️ isms-core-platform/ — 平台部署套件

Docker Compose 部署套件。**仅提供映像档** — 本目录不附任何应用程序原始码，只包含*执行*整套堆叠所需的内容。`docker-compose.yml` 会从 GHCR、Docker Hub 与私有注册表拉取预建映像档（`isms-core-backend`、`-frontend`、`-nginx`、`-opensearch`、`-connectors`、`-feeds`、`-threat-intel`、`-smtp-bridge`，另加一次性的设置／数据映像档）。完整应用程序原始码（backend、frontend、connectors、feeds、threat-intel、smtp-bridge、nginx、opensearch、datasets）位于私有的 `factory_isms_project` 工作储存库，并在建置时打包进上述映像档 — 它不属于这个公开储存库。

```
isms-core-platform/
│
├── .env.example                           # 环境变数模板 → 复制为 .env
├── backup.env.example                     # 备份服务环境模板
├── docker-compose.yml                     # 多服务正式堆叠（以 profile 为基础，用 image: 而非 build:）
├── bootstrap.sh                           # 首次启动导入脚本（幂等，可安全重复执行）
├── CHANGELOG.md                           # 平台版本变更记录
├── LICENSE                                # Apache 2.0 — 仅适用于本目录（见 README §License）
├── .gitignore
│
├── garage/                                # Garage S3 对象储存（选用 profile）— 上游映像档，仅设置
│   └── garage.toml                        # Garage 配置，系结挂载至 dxflrs/garage
│
├── schemas/
│   └── init_db.sql                        # PostgreSQL 初始结构定义，系结挂载至 postgres:18-alpine
│
└── certs/                                 # TLS 凭证挂载点（已列入 gitignore — 仅执行期）
    ├── cert.pem                           # 自定义凭证（选用 — 不存在时自动产生）
    └── key.pem                            # 私钥（选用）
```

**由 `docker-compose.yml` 启动的服务：**

| 容器 | 角色 |
|-----------|------|
| `isms-core-nginx` | TLS 终止 + 反向代理 |
| `isms-core-backend` | FastAPI REST API |
| `isms-core-frontend` | Angular 22 + Material 3 WebUI |
| `isms-core-postgres` | PostgreSQL 18 — 主要数据存放区 |
| `isms-core-redis` | Redis 8 — 工作阶段缓存 + Celery 消息代理 |
| `isms-core-opensearch` | OpenSearch 3.x — 全文检索 + 威胁情报 |
| `isms-core-worker` | Celery worker — 背景导入与同步工作 |
| `isms-core-beat` | Celery Beat — 每晚证据封存（02:00 UTC）、每日 KPI 快照（06:00 UTC） |
| `isms-core-feeds` | 威胁情报计划器 — MITRE ATT&CK、ATLAS、CISA KEV、EPSS、NVD CVE/CPE、ENISA EUVD |
| `isms-core-connectors` | 自动化证据执行器 — 44 个连接器，持续执行 |
| `isms-core-dashboards-setup` | 一次性 OpenSearch Dashboards 布建 — 启动时导入 19 个自动化仪表板 |

选用 profile（视需要加入部署命令）：
- `--profile opensearch-single` — 标准部署**必要**（启动 OpenSearch）
- `--profile threat-intel` — OSINT IOC 馈送（CIRCL MISP、Botvrij、AbuseIPDB、URLhaus、ThreatFox、SSLBL、AlienVault OTX、Feodo Tracker、RFD、Stopforumspam、MalwareBazaar、Malpedia）；需在 `.env` 中设置 `THREAT_INTEL_ENABLED=true`
- `--profile opensearch-cluster` — 3 节点 OpenSearch 丛集（企业版）
- `--profile dashboards` — 连接埠 5601 上的 OpenSearch Dashboards UI
- `--profile garage` — Garage S3 对象储存
- `--profile mailpit` — 本机邮件捕捉器（开发用）
- `--profile smtp-bridge` — Microsoft 365／OAuth 邮件转送

---

## 📁 翻译子目录

所有 POL 文件（涵盖全部五项产品）均提供英文与另外三种语言。英文文件直接放在 `POL/` 下。译本则放在语言子目录中：

```
POL/
├── ISMS-POL-A.5.1 - Information Security Policies.md     # 英文（正本）
├── fr/
│   └── ISMS-POL-A.5.1 - Politique de Sécurité de l'Information - FR.md
├── de/
│   └── ISMS-POL-A.5.1 - Informationssicherheitsrichtlinie - DE.md
└── it/
    └── ISMS-POL-A.5.1 - Politica di Sicurezza delle Informazioni - IT.md
```

同样的模式也适用于 OP-POL、PRIV-POL、CLD-POL 与 AI-POL 文件。

---

## 📋 Screenshots/

README.md 与 PLATFORM.md 中引用的平台 UI 萤幕截图。有 `light/` 与 `dark/` 子文件夹，命名为 `NN_isms_core_feature_name_<theme>.png`。文件只用 light。

---

<p align="center">
  <strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>
