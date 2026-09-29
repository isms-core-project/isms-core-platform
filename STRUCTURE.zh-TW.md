<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Repository_Structure-2E8B57?style=for-the-badge" alt="ISMS CORE Repository Structure"/>
</p>

<h1 align="center">📂 Repository Structure</h1>

<p align="center"><a href="STRUCTURE.md">English</a> · <strong>繁體中文</strong> · <a href="STRUCTURE.zh-CN.md">简体中文</a></p>

<p align="center">
  <em>本儲存庫中所有資料夾、文件與成品類型的完整地圖。</em>
</p>

---

## 成品類型 — 每個控制套件裡有什麼

在閱讀資料夾樹之前，先了解每一種成品類型是什麼：

| 成品 | 格式 | 是什麼 | 誰來用 |
|----------|--------|------------|-------------|
| **POL** | Markdown | 治理政策 — 說明該控制措施要求什麼、由誰負責、適用哪些標準。填上組織名稱／CISO／生效日期後即可簽署發布。 | ISMS 經理 → 董事會／員工 |
| **IMP-UG** | Markdown | 實施使用者指南 — ISMS 經理如何實施與操作該控制措施。角色、流程步驟、KPI、審查週期。 | ISMS 經理 |
| **IMP-TG** | Markdown | 實施技術指南 — 給工程師的逐步操作。指令、組態、廠商注意事項、強化檢核表。 | 安全工程師 |
| **SCR** | Python 3.11+ | 評鑑產生器 — `python3 generate_*.py` 產出結構化的 Excel 合規工作簿。唯一相依套件：`openpyxl`。 | ISMS 經理 → 稽核人員 |
| **WKBK** | Excel (.xlsx) | 產出的合規工作簿 — 逐控制措施的評鑑項目、證據狀態、評分與稽核人員備註。由 SCR 產生器產出。 | 稽核人員／控制措施負責人 |
| **REF** | Markdown | 取自 ISO 標準條文、對應本控制措施的參考摘錄。與相鄰附錄 A 控制措施的交叉參照。 | ISMS 經理／稽核人員 |
| **CTX** | Markdown | 將本控制套件連結至相鄰與相依套件的脈絡文件 — 用於控制措施堆疊與相依性對應。 | ISMS 經理 |
| **FORM** | Markdown | 可直接使用的範本：證據表單、會議議程、核准紀錄、風險接受表單。 | ISMS 經理／控制措施負責人 |

**營運產品：** 僅有 POL + SCR + WKBK（不含 IMP-UG/TG — 設計上刻意從簡）

**隱私／雲端／AI：** POL + IMP-UG + IMP-TG + SCR + WKBK

---

## 頂層儲存庫

```
factory_isms/
│
├── README.md                  # 專案總覽與快速開始
├── PARADIGM.md                # 產品總覽與範式轉移指南
├── PLATFORM.md                # 平台架構、功能與完整部署指南（含安裝指引）
├── STRUCTURE.md               # 本文件
├── COMPLIANCE.md              # 29 個合規評鑑模組 — 涵蓋範圍備註
├── CONTRIBUTING.md            # QA 流程與標準
├── PHILOSOPHY.md              # 反貨物崇拜方法論
├── CODE_OF_CONDUCT.md         # 社群標準
├── SECURITY.md                # 弱點通報政策
├── LICENSE                    # AGPL-3.0 — 規範下方內容包（雙重授權，見 README §License）
│
├── isms-core-framework/       # 🏗️ ISO 27001:2022 — 完整工程產品
├── isms-core-operational/     # ⚡ ISO 27001:2022 — 輕量中小企業版
├── isms-core-privacy/         # 🔒 ISO 27701:2025 — 隱私擴充套件
├── isms-core-cloud/           # ☁️ ISO 27018:2025 雲端擴充套件 + ISO 27017:2026 雲端安全
├── isms-core-ai/              # 🤖 ISO 42001:2023 — AI 擴充套件
├── isms-core-platform/        # 🖥️ 平台部署套件 — 自有 LICENSE（Apache 2.0）
├── USER_MANUAL/               # 📖 完整使用者手冊（21 章）— 由應用程式內 /docs/user-manual.md 提供
├── COMPLIANCE.md              # 📋 評鑑模組涵蓋範圍
└── screenshots/               # 平台 UI 螢幕截圖
```

---

## 🏗️ isms-core-framework/ — ISO 27001:2022 完整工程

53 個控制套件涵蓋全部 93 項附錄 A 控制措施。每個套件都包含完整成品組合（POL、IMP-UG、IMP-TG、SCR、WKBK、REF、CTX、FORM）。

```
isms-core-framework/
│
├── README.md                              # 產品總覽
├── CONTROLS.md                            # 53 個控制套件索引 — 從這裡開始
├── COVERAGE.md                            # 93 項附錄 A 控制措施 → 53 個套件的對應
├── STATUS.md                              # 實施指標
├── STACKING.md                            # 控制措施分組與堆疊方法論
├── CHANGELOG.md                           # 版本歷程
│
├── 00-foundation-policies/                # 法規架構基線
│   ├── isms-pol-00-regulatory-framework/
│   │   └── POL/                           # ISMS-POL-00 (EN + FR + DE + IT)
│   └── isms-pol-01-isms-scope/
│       └── POL/                           # ISMS-POL-01 (EN + FR + DE + IT)
│
├── A.5-organisational-controls/           # 21 個控制套件
│   └── isms-a.5.X-X-control-name/
│       ├── POL/                           # 治理政策（EN + fr/ + de/ + it/）
│       ├── IMP/
│       │   ├── IMP-UG/                    # 使用者指南 — ISMS 經理
│       │   └── IMP-TG/                    # 技術指南 — 工程師
│       ├── SCR/                           # Python 評鑑產生器
│       ├── WKBK/                          # 產出的 Excel 工作簿
│       ├── REF/                           # ISO 標準參考摘錄
│       ├── CTX/                           # 控制措施脈絡 + 相依性對應
│       └── FORM/                          # 範本與表單
│
├── A.6-people-controls/                   # 4 個控制套件（結構相同）
├── A.7-physical-controls/                 # 6 個控制套件（結構相同）
└── A.8-technological-controls/            # 22 個控制套件（結構相同）
```

**關鍵文件：**
- `CONTROLS.md` — 全部 53 個套件的索引清單，含控制措施名稱與附錄 A 參照
- `COVERAGE.md` — 將 93 項 ISO 27001:2022 附錄 A 控制措施對應到 53 個套件（部分套件涵蓋多項控制措施）
- `STACKING.md` — 解釋成熟組織如何堆疊套件

---

## ⚡ isms-core-operational/ — ISO 27001:2022 中小企業版

53 個控制群組，成品組合較精簡（POL + SCR + WKBK）。沒有實施指南 — 營運政策設計上即完整且自足。

```
isms-core-operational/
│
├── README.md
├── CONTROLS.md                            # 53 個控制群組索引
├── STATUS.md
├── CHANGELOG.md
│
├── 00-checklist-engine/                   # 共用的檢核表產生器引擎
│
├── A.5-organisational-controls/           # 21 個控制群組
│   └── isms-a.5.X-X-control-name/
│       ├── POL/                           # OP-POL（EN + fr/ + de/ + it/）
│       ├── SCR/                           # Python 合規檢核表產生器
│       └── WKBK/                          # 產出的 Excel 檢核表
│
├── A.6-people-controls/                   # 4 個控制群組
├── A.7-physical-controls/                 # 6 個控制群組
└── A.8-technological-controls/            # 22 個控制群組
```

---

## 🔒 isms-core-privacy/ — ISO 27701:2025 隱私擴充套件

21 個控制群組，分屬三種範圍：控管者（a.1.x）、處理者（a.2.x）與共用（a.3.x）。

```
isms-core-privacy/
│
├── README.md
├── 00-checklist-engine/                   # 共用的隱私檢核表引擎
│
├── 00-priv-foundation-policies/           # 基礎政策
│   ├── priv-pol-00-privacy-regulatory-framework/
│   │   └── POL/                           # PRIV-POL-00 (EN + fr/ + de/ + it/)
│   └── priv-pol-01-privacy-governance/
│       └── POL/                           # PRIV-POL-01 (EN + fr/ + de/ + it/)
│
├── privacy-controller/                    # 8 個控管者控制群組（a.1.x）
│   └── priv-a.1.X.X-X-control-name/
│       ├── POL/                           # PRIV-POL（EN + fr/ + de/ + it/）
│       ├── IMP/
│       │   ├── IMP-UG/
│       │   └── IMP-TG/
│       ├── SCR/
│       └── WKBK/
│
├── privacy-processor/                     # 5 個處理者控制群組（a.2.x）
│   └── priv-a.2.X.X-X-control-name/      # 與控管者結構相同
│
└── privacy-shared/                        # 8 個共用控制群組（a.3.x）
    └── priv-a.3.X.X-X-control-name/      # 與控管者結構相同
```

---

## ☁️ isms-core-cloud/ — ISO 27018:2025 雲端擴充套件 + ISO 27017:2026 雲端安全

16 個控制群組，分屬兩項獨立標準：12 個涵蓋雲端服務供應商的
PII 保護要求（ISO 27018:2025），以及 4 個獨立的雲端安全擴充控制措施
（ISO 27017:2026），外加一份指引附錄，針對既有 38 項已在雲端情境適用的
附錄 A 控制措施。

```
isms-core-cloud/
│
├── README.md
├── iso27018-pii-cloud/
│   └── cld-a.X-control-name/              # 12 個附錄 A 控制群組
│       ├── POL/                           # CLD-POL（EN + fr/ + de/ + it/）
│       ├── IMP/
│       │   ├── IMP-UG/
│       │   └── IMP-TG/
│       ├── SCR/
│       └── WKBK/
└── iso27017-sec-cloud/
    ├── cld-sec-a.X-control-name/           # 4 個獨立擴充控制措施
    │   ├── POL/                            # CLD-SEC-POL（EN + fr/ + de/ + it/）
    │   ├── IMP/
    │   │   ├── IMP-UG/
    │   │   └── IMP-TG/
    │   └── SCR/
    └── cld-sec-guidance-addendum/
        └── REF/                            # 其餘 38 項附錄 A 控制措施的既有控制措施指引
```

---

## 🤖 isms-core-ai/ — ISO 42001:2023 AI 擴充套件

12 個 AI 控制群組（2 個基礎 + 10 個附錄 A），涵蓋 AI 治理、衝擊評鑑、負責任使用與第三方 AI 關係。

```
isms-core-ai/
│
├── README.md
├── 00-checklist-engine/                   # 共用的 AI 檢核表引擎
│
├── 00-ai-foundation-policies/             # 基礎政策
│   ├── ai-pol-00-ai-regulatory-applicability/
│   │   └── POL/                           # AI-POL-00 (EN + fr/ + de/ + it/)
│   └── ai-pol-01-aims-governance-and-decision-making/
│       └── POL/                           # AI-POL-01 (EN + fr/ + de/ + it/)
│
└── ai-a.X.X-X-control-name/              # 10 個附錄 A 控制群組
    ├── POL/                               # AI-POL（EN + fr/ + de/ + it/）
    ├── IMP/
    │   ├── IMP-UG/                        # 使用者指南 — ISMS 經理
    │   └── IMP-TG/                        # 技術指南 — 工程師
    └── SCR/                               # Python 合規檢核表產生器
```

---

## 🖥️ isms-core-platform/ — 平台部署套件

Docker Compose 部署套件。**僅提供映像檔** — 本目錄不附任何應用程式原始碼，只包含*執行*整套堆疊所需的內容。`docker-compose.yml` 會從 GHCR、Docker Hub 與私有註冊表拉取預建映像檔（`isms-core-backend`、`-frontend`、`-nginx`、`-opensearch`、`-connectors`、`-feeds`、`-threat-intel`、`-smtp-bridge`，另加一次性的設定／資料映像檔）。完整應用程式原始碼（backend、frontend、connectors、feeds、threat-intel、smtp-bridge、nginx、opensearch、datasets）位於私有的 `factory_isms_project` 工作儲存庫，並在建置時打包進上述映像檔 — 它不屬於這個公開儲存庫。

```
isms-core-platform/
│
├── .env.example                           # 環境變數範本 → 複製為 .env
├── backup.env.example                     # 備份服務環境範本
├── docker-compose.yml                     # 多服務正式堆疊（以 profile 為基礎，用 image: 而非 build:）
├── bootstrap.sh                           # 首次啟動匯入腳本（冪等，可安全重複執行）
├── CHANGELOG.md                           # 平台版本變更紀錄
├── LICENSE                                # Apache 2.0 — 僅適用於本目錄（見 README §License）
├── .gitignore
│
├── garage/                                # Garage S3 物件儲存（選用 profile）— 上游映像檔，僅設定
│   └── garage.toml                        # Garage 組態，繫結掛載至 dxflrs/garage
│
├── schemas/
│   └── init_db.sql                        # PostgreSQL 初始結構定義，繫結掛載至 postgres:18-alpine
│
└── certs/                                 # TLS 憑證掛載點（已列入 gitignore — 僅執行期）
    ├── cert.pem                           # 自訂憑證（選用 — 不存在時自動產生）
    └── key.pem                            # 私密金鑰（選用）
```

**由 `docker-compose.yml` 啟動的服務：**

| 容器 | 角色 |
|-----------|------|
| `isms-core-nginx` | TLS 終止 + 反向代理 |
| `isms-core-backend` | FastAPI REST API |
| `isms-core-frontend` | Angular 22 + Material 3 WebUI |
| `isms-core-postgres` | PostgreSQL 18 — 主要資料存放區 |
| `isms-core-redis` | Redis 8 — 工作階段快取 + Celery 訊息代理 |
| `isms-core-opensearch` | OpenSearch 3.x — 全文檢索 + 威脅情報 |
| `isms-core-worker` | Celery worker — 背景匯入與同步工作 |
| `isms-core-beat` | Celery Beat — 每晚證據封存（02:00 UTC）、每日 KPI 快照（06:00 UTC） |
| `isms-core-feeds` | 威脅情報排程器 — MITRE ATT&CK、ATLAS、CISA KEV、EPSS、NVD CVE/CPE、ENISA EUVD |
| `isms-core-connectors` | 自動化證據執行器 — 44 個連接器，持續執行 |
| `isms-core-dashboards-setup` | 一次性 OpenSearch Dashboards 佈建 — 啟動時匯入 19 個自動化儀表板 |

選用 profile（視需要加入部署命令）：
- `--profile opensearch-single` — 標準部署**必要**（啟動 OpenSearch）
- `--profile threat-intel` — OSINT IOC 饋送（CIRCL MISP、Botvrij、AbuseIPDB、URLhaus、ThreatFox、SSLBL、AlienVault OTX、Feodo Tracker、RFD、Stopforumspam、MalwareBazaar、Malpedia）；需在 `.env` 中設定 `THREAT_INTEL_ENABLED=true`
- `--profile opensearch-cluster` — 3 節點 OpenSearch 叢集（企業版）
- `--profile dashboards` — 連接埠 5601 上的 OpenSearch Dashboards UI
- `--profile garage` — Garage S3 物件儲存
- `--profile mailpit` — 本機郵件捕捉器（開發用）
- `--profile smtp-bridge` — Microsoft 365／OAuth 郵件轉送

---

## 📁 翻譯子目錄

所有 POL 文件（涵蓋全部五項產品）均提供英文與另外三種語言。英文文件直接放在 `POL/` 下。譯本則放在語言子目錄中：

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

同樣的模式也適用於 OP-POL、PRIV-POL、CLD-POL 與 AI-POL 文件。

---

## 📋 Screenshots/

README.md 與 PLATFORM.md 中引用的平台 UI 螢幕截圖。有 `light/` 與 `dark/` 子資料夾，命名為 `NN_isms_core_feature_name_<theme>.png`。文件只用 light。

---

<p align="center">
  <strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>
