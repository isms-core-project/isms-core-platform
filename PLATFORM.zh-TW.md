<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Platform-2E8B57?style=for-the-badge" alt="ISMS CORE Platform"/>
</p>

<h1 align="center">🎋 ISMS CORE Platform</h1>

<p align="center"><a href="PLATFORM.md">English</a> · <strong>繁體中文</strong> · <a href="PLATFORM.zh-CN.md">简体中文</a></p>

<p align="center">
  <strong>生產部署指南 — API、WebUI 與連接器層</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Live_(v1.1)-00AA00?style=flat-square" alt="Live"/>
  <img src="https://img.shields.io/badge/Backend-FastAPI-0066CC?style=flat-square" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Database-PostgreSQL_18-336791?style=flat-square" alt="PostgreSQL 18"/>
  <img src="https://img.shields.io/badge/Frontend-Angular_22_+_Material_3-DD0031?style=flat-square" alt="Angular"/>
  <img src="https://img.shields.io/badge/Deployment-Docker_Compose-2496ED?style=flat-square" alt="Docker"/>
  <img src="https://img.shields.io/badge/Services-11_containers-2E8B57?style=flat-square" alt="11 Services"/>
</p>

<p align="center">
  <em>五項產品。一個平台。全數上線。</em>
</p>

---

> **⚠️ 請先讀這段 —— IKEA 說明書警告 ⚠️**
>
> 這是部署說明書。請從頭讀到尾。不要跳過步驟。不要即興發揮。
>
> 如果你今晚就要部署，請依序執行步驟 0 到 6。**上線檢核表**在本文件最後。
>
> 最常見的失敗模式，是在堆疊完全啟動前就執行 `bootstrap.sh`，或是乾脆整段跳過。兩種都會把事情搞壞。請讀步驟 4。

---

## 什麼是 ISMS CORE Platform？

ISMS CORE Platform 是**API 與 WebUI 層**，把 ISMS CORE 各項產品（框架、營運、隱私、雲端 PII、雲端安全、AI）轉化為一套即時運作的合規管理系統。政策、評鑑工作簿與實施指引是內容 —— Platform 則是引擎，負責匯入、關聯並呈現這些內容，形成涵蓋 ISO 27001:2022、ISO 27701:2025、ISO 27018:2025、ISO 27017:2026 與 ISO 42001:2023 的統一營運儀表板。

**沒有 Platform：** 你手上只有磁碟裡的政策檔案與 Excel 工作簿。漂亮的紙上作業。

**有了 Platform：** 你擁有的是一套即時運作的合規系統 —— 可搜尋、可評分、可追蹤缺口、可連結證據、可供稽核，而且（搭配連接器）由真實基礎設施持續自動餵入證據。

> Platform 是加值項。本儲存庫出貨的六項內容產品（框架、營運、隱私、雲端 PII、雲端安全、AI）沒有它也能完美運作。Platform 是給需要持續合規管理、而非定期翻檔案檢視的團隊所用的營運層。

---

## 架構

### 十項服務堆疊

```
                        ┌────────────────────────────────────────────────┐
  用戶端                │            ISMS CORE Platform                   │
  (瀏覽器)              │                                                  │
      │                 │  ┌──────────────────────────────────────────┐   │
      ▼                 │  │  isms-core-nginx（連接埠 80 + 443）      │   │
  https://{HOST_IP} ────┼─►│  TLS 終止 + 反向代理                    │   │
                        │  │  / → 前端  /api/ → 後端                  │   │
                        │  └──────────┬───────────────┬───────────────┘   │
                        │             │               │                    │
                        │             ▼               ▼                    │
                        │  ┌──────────────┐  ┌──────────────────┐        │
                        │  │ isms-core-   │  │  isms-core-      │        │
                        │  │ frontend     │  │  backend         │        │
                        │  │ Angular 22   │  │  FastAPI         │        │
                        │  │ + Material 3 │  │  + SQLAlchemy    │        │
                        │  └──────────────┘  └────┬──────┬──────┘        │
                        │                         │      │                 │
                        │             ┌───────────┘      │                 │
                        │             ▼                  ▼                 │
                        │  ┌──────────────┐  ┌──────────────────┐        │
                        │  │ isms-core-   │  │  isms-core-      │        │
                        │  │ postgres     │  │  redis           │        │
                        │  │ PostgreSQL18 │  │  Redis 8         │        │
                        │  └──────────────┘  └────┬─────────────┘        │
                        │                         │                        │
                        │             ┌───────────┘                        │
                        │             ▼                                     │
                        │  ┌──────────────┐  ┌──────────────────┐        │
                        │  │ isms-core-   │  │  isms-core-beat  │        │
                        │  │ worker       │  │  Celery Beat     │        │
                        │  │ Celery Worker│  │  （夜間工作）    │        │
                        │  └──────────────┘  └──────────────────┘        │
                        │                                                  │
                        │  ┌──────────────────────────────────────────┐   │
                        │  │  isms-core-opensearch（內部）            │   │
                        │  │  全文搜尋（政策／IMP）                   │   │
                        │  │  + nvd-cve / nvd-cpe + 證據索引          │   │
                        │  └────────────────────┬─────────────────────┘   │
                        │                       │                          │
                        │             ┌─────────┴─────────┐               │
                        │             ▼                   ▼               │
                        │  ┌──────────────────┐  ┌──────────────────┐   │
                        │  │ isms-core-feeds  │  │ isms-core-       │   │
                        │  │ 威脅情報         │  │ 連接器           │   │
                        │  │ MITRE · KEV ·    │  │ 44 個證據        │   │
                        │  │ EPSS · NVD CVE · │  │ 連接器           │   │
                        │  │ ENISA EUVD · EDB │  │                  │   │
                        │  └──────────────────┘  └──────────────────┘   │
                        └────────────────────────────────────────────────┘
```

### 服務

| 容器 | 技術 | 角色 |
|-----------|-----------|------|
| `isms-core-nginx` | nginx (Alpine) | 反向代理 —— TLS 終止，將 `/api/` 導向後端、`/` 導向前端。連接埠 80 + 443。 |
| `isms-core-backend` | FastAPI 0.109+ | REST API、身分驗證（JWT）、業務邏輯、匯入協調。僅限內部 —— 由 nginx 代理。 |
| `isms-core-frontend` | Angular 22 + Material 3 | WebUI —— 儀表板、控制措施瀏覽器、證據管理。僅限內部 —— 由 nginx 代理。 |
| `isms-core-postgres` | PostgreSQL 18 Alpine | 主要資料存放區 —— 所有合規資料。僅限內部（生產環境不對外開放連接埠）。 |
| `isms-core-redis` | Redis 8 Alpine | 工作階段快取 + Celery 任務代理。僅限內部。 |
| `isms-core-opensearch` | OpenSearch 3.x | 對政策與 IMP 內容的全文搜尋 + NVD CVE/CPE 索引。僅限內部。 |
| `isms-core-worker` | Celery 5.3 | 背景任務 —— 匯入、同步、合規重算。佇列：`isms`。 |
| `isms-core-beat` | Celery Beat | 排程工作 —— 每日 02:00 UTC 的夜間證據封存；每日 06:00 UTC 的 KPI 快照。無健康檢查（設計如此）。 |
| `isms-core-feeds` | Python 3.12 + schedule | 威脅情報排程器 —— MITRE ATT&CK、MITRE ATLAS、CISA KEV、VulnCheck KEV、FIRST EPSS、NVD CVE/CPE、ENISA EUVD、Exploit-DB（每日約 52K 筆漏洞利用）。寫入 Postgres 與 OpenSearch。環境變數：`FEEDS_CVE_ENABLED`、`FEEDS_CPE_FULL`、`FEEDS_EUVD_ENABLED`、`FEEDS_VULNCHECK_ENABLED`、`NIST_API_KEY`、`VULNCHECK_API_KEY`。 |
| `isms-core-threat-intel` | Python 3.12 + schedule | **選用**（透過 `COMPOSE_PROFILES=...,threat-intel` 啟用）OSINT IOC 情報來源容器 —— 12 個來源：CIRCL MISP、Botvrij MISP、AbuseIPDB、URLhaus、ThreatFox、SSLBL、AlienVault OTX、Red Flag Domains、Stopforumspam、MalwareBazaar、Feodo Tracker、Malpedia。VirusTotal 增補（選用）。隨選觸發伺服器位於連接埠 9002。環境變數：`THREAT_INTEL_ENABLED`、`ABUSEIPDB_API_KEY`、`OTX_API_KEY`、`MALWAREBAZAAR_API_KEY`、`VT_API_KEY`、`SHODAN_API_KEY`、`TI_MISP_IMPORT_FROM_DATE`。 |
| `isms-core-connectors` | Python 3.12 | 自動化證據執行器 —— 動態載入全部 44 個連接器，將證據推送至 `connector_evidence` 資料表。環境變數：`CONNECTORS_WORKER_SECRET`。 |
| `isms-core-backup` | offen/docker-volume-backup v2 | **選用**（透過 `COMPOSE_PROFILES=...,backup` 啟用）每日磁碟區備份 —— 將 `postgres-data`、`garage-meta`、`garage-data` 封存到主機上的 `BACKUP_ARCHIVE_PATH`。以 cron 執行（預設 03:30 UTC），會短暫停止 postgres 以確保一致性。設定檔：`backup.env`。無健康檢查（設計如此）。 |

> **生產環境存取：** 透過 nginx 使用 `https://{HOST_IP}`。請勿直接存取 `:3000` 或 `:8000` —— 這些連接埠在生產環境並未開放。

---

> **部署設定檔 — 設在 `.env`，不在命令列**
>
> `.env` 裡的 `COMPOSE_PROFILES` 決定哪些服務群組會啟用。Docker Compose 會自動讀取 —— 命令列不需要任何 `--profile` 旗標。在 `.env.example` 中挑一行 `COMPOSE_PROFILES`，取消註解，`docker compose up -d` 就能直接運作。
>
> | `COMPOSE_PROFILES` 值 | 會啟動什麼 |
> |---|---|
> | `opensearch-single` | 標準堆疊（預設） |
> | `opensearch-single,threat-intel` | + OSINT IOC 情報來源 —— 另須設定 `THREAT_INTEL_ENABLED=true` |
> | `opensearch-single,dashboards` | + 連接埠 5601 上的 OpenSearch Dashboards |
> | `opensearch-single,garage` | + Garage S3 物件儲存 |
> | `opensearch-single,mailpit` | + Mailpit 本機郵件攔截器（僅限開發） |
> | `opensearch-single,smtp-bridge` | + Microsoft 365 SMTP 中繼 |
> | `opensearch-single,backup` | + 每日自動磁碟區備份（請先設定 `backup.env`） |
> | `opensearch-single,threat-intel,dashboards,smtp-bridge,backup` | 完整標準堆疊 + OSINT IOC 情報來源 —— 另須設定 `THREAT_INTEL_ENABLED=true` |
> | `opensearch-cluster,garage,dashboards,threat-intel,smtp-bridge,backup` | 完整企業堆疊 + OSINT IOC 情報來源 —— 另須設定 `THREAT_INTEL_ENABLED=true` |
>
> **`opensearch-single` 與 `opensearch-cluster` 互斥 —— 永遠只能包含其中一個。**
>
> **證據儲存後端（`EVIDENCE_STORE`）：** 預設為 `postgres`。設為 `opensearch` 時，證據會改經 OpenSearch 傳送，檔案存放於 Garage S3 —— 需要 `garage` + `opensearch-cluster` 設定檔。

---

### 資料模型

| 實體 | 說明 |
|--------|-------------|
| **控制群組** | 100 個群組 —— 54 個 ISMS（ISO 27001）、21 個隱私（ISO 27701）、12 個雲端 PII（ISO 27018）、1 個雲端安全（ISO 27017）、12 個 AI（ISO 42001） |
| **政策** | POL、OP-POL、PRIV-POL、CLD-POL、CLD-SEC-POL、AI-POL、INS、REF、CTX、FORM —— 具型別、標記產品、追蹤狀態 |
| **實施** | IMP-UG/TG 文件，已索引至 OpenSearch 以供全文搜尋 |
| **評鑑** | Excel 工作簿內容：工作表、項目、逐項合規狀態；框架、營運、隱私、雲端 PII、雲端安全與 AI 檢核表 |
| **缺口** | 已識別的合規缺口，含嚴重性、擁有者、SLA 與矯正追蹤 |
| **證據** | 連結至控制群組與評鑑項目的證據項目 —— 手動上傳 + 連接器自動匯入 |
| **連接器證據** | 來自連接器的自動化證據 —— 含時間戳、已分類、標示來源 |
| **框架** | 39 個參考資料集：ISO 27001、NIST CSF 2.0、NIST AI RMF 1.0、MITRE ATT&CK v19、GDPR、DORA、NIS2、CIS Controls v8、BSI IT-Grundschutz Kompendium、TISAX/VDA ISA 6.0、Swiss nDSG 2023、Swiss ISG (SR 128)、EU CRA 2024、EU AI Act、CyberFundamentals BE、BaFin BAIT DE、CSSF 20-750 LU、ACN IT、UK NIS、UK Operational Resilience、NCSC CAF v4.0、ReCyF v2.5（法國 NIS2）、FINMA、COBIT 2019，以及更多 |
| **對照映射** | 跨框架關聯：4,671 個物件 / 59 條軸線 —— 包括 ISO 27001 ↔ MITRE ATT&CK v19（36）、ISO 27001 ↔ FINMA（73）、ISO 27001 ↔ OWASP ASVS 5.0（22）、NIST SP 800-53 R5 ↔ MITRE ATT&CK v19（590）、BSI IT-Grundschutz（ISO 27001 ↔ BSI：386，ISO 27701 ↔ BSI：101，ISO 27018 ↔ BSI：51）、NCSC CAF v4.0（41）、ReCyF v2.5 / FR NIS2（20）、Swiss ISG（27）、ISO 27017 ↔ CSA CCM v4.1/NIST CSF 2.0/FINMA/ISO 27001/DORA/NIS2（37），以及歐盟各國框架（CyberFundamentals BE：107，BaFin BAIT：69，CSSF LU：47，ACN IT：43，UK NIS：51，UK Op. Resilience：34） |
| **NIST CSF 2.0 設定檔** | 具名評鑑設定檔 —— 全部 106 項子類別的等級 1–4 評分、依功能計分、缺口分析、XLSX 匯入／匯出 |
| **合規評鑑** | 29 個框架 —— 完整涵蓋範圍請見 [COMPLIANCE.zh-TW.md](COMPLIANCE.zh-TW.md) |
| **專案** | 工作區層 —— 具名專案擁有精選的政策、實施、評鑑、缺口與證據子集；新增時套用文件變數替換（組織名稱、CISO、生效日期）；具作用中／停用／草稿／已封存的生命週期 |
| **系統事件日誌** | 平台每項動作的不可變軌跡（誰、做了什麼、何時、資源） |
| **威脅情報** | 情報來源執行紀錄、CISA KEV 條目、VulnCheck KEV 條目（獨立資料表 —— 涵蓋範圍比 CISA 更廣，約 67% 的條目不在 CISA KEV 中）、EPSS 分數、MITRE 技術、ENISA EUVD 條目、Exploit-DB 交互參照。NVD CVE（約 250K 份文件）與 CPE（約 50-100K 份文件）儲存於 OpenSearch 索引 `nvd-cve` / `nvd-cpe`，並在索引時以 EPSS + KEV + VulnCheck KEV + EUVD + Exploit-DB 交互增補（比對到的 CVE 會加上 `edb_id`、`edb_verified`、`edb_description`、`in_vulncheck_kev` 欄位）。支援 CVSS 4.0。OSINT IOC 情報來源（12 個來源）：CIRCL MISP + Botvrij MISP（120K+ IOC）、AbuseIPDB 黑名單、URLhaus、ThreatFox、SSLBL、AlienVault OTX（帶 TLP 標籤與信心分數的 pulses）、Feodo Tracker、Red Flag Domains、Stopforumspam、MalwareBazaar、Malpedia（惡意程式家族 + 威脅行為者）—— 全部索引至各來源專屬的 OpenSearch 索引，並在匯入時以 ATT&CK TID、家族代號、行為者代號與 TLP 標籤交互增補。VirusTotal 增補每日更新 IOC 信心分數；GreyNoise 在 IP 增補頁面提供隨選的 IP 雜訊分類（免費方案每週 50 次查詢，僅限手動查詢）。 |

---

## 平台畫面

<table>
<tr>
<td align="center"><strong>登入</strong><br/><img src="screenshots/light/01_isms_core_login_light.png" width="380" alt="登入畫面"/></td>
<td align="center"><strong>首頁 — 產品儀表板</strong><br/><img src="screenshots/light/02_isms_core_home_light.png" width="380" alt="首頁儀表板 — ISMS、隱私、雲端、AI 產品切換器，附即時指標"/></td>
</tr>
<tr>
<td align="center"><strong>合規概觀</strong><br/><img src="screenshots/light/03_isms_core_compliance_overview_light.png" width="380" alt="合規概觀 — 53 個控制群組、100% FW/OP 涵蓋、稽核準備度"/></td>
<td align="center"><strong>連接器 — 自動化證據</strong><br/><img src="screenshots/light/73_isms_core_connectors_light.png" width="380" alt="連接器儀表板 — MS Entra ID、Defender XDR、M365、Azure CSPM — 全部作用中／健康"/></td>
</tr>
<tr>
<td align="center"><strong>ISMS Compass — AI 缺口分析</strong><br/><img src="screenshots/light/19_isms_core_compass_light.png" width="380" alt="ISMS Compass — 貼上任何文件，與黃金標準比對，取得缺口分析"/></td>
<td align="center"><strong>系統狀態</strong><br/><img src="screenshots/light/77_isms_core_system_light.png" width="380" alt="系統狀態 — 所有服務健康、資料庫統計、OpenSearch 索引、Celery Worker 運作中"/></td>
</tr>
<tr>
<td align="center"><strong>NIST CSF 2.0 評鑑</strong><br/><img src="screenshots/light/25_isms_core_nist_csf20_light.png" width="380" alt="NIST CSF 2.0 — 106 項子類別評鑑、等級 1–4 評分、功能拆解、缺口分析"/></td>
<td align="center"><strong>NIS2 指令評鑑</strong><br/><img src="screenshots/light/35_isms_core_nis2_light.png" width="380" alt="NIS2 EU 2022/2555 — 第 21 條安全措施與第 23 條通報義務"/></td>
</tr>
</table>

---

## 功能

| 功能 | 說明 |
|---------|-------------|
| **控制措施瀏覽器** | 瀏覽全部 99 個控制群組（ISMS + 隱私 + 雲端 + AI），含合規分數、政策狀態、評鑑歷程 |
| **合規儀表板** | 四項產品的彙總分數與章節拆解；ISMS／隱私／雲端／AI 產品切換器 |
| **涵蓋熱圖** | 依控制群組與章節呈現的政策與評鑑涵蓋範圍 |
| **政策管理員** | 瀏覽、篩選、預覽並管理所有 POL/OP-POL/PRIV-POL/CLD-POL/AI-POL/INS/REF/CTX 文件 |
| **評鑑追蹤器** | 框架（188 個工作簿）、營運（53 份檢核表）、隱私（21）、雲端（12）、AI（10），含逐項合規狀態 |
| **缺口管理** | 完整缺口生命週期：建立、指派、追蹤、結案 —— 嚴重性、SLA 監控、BSI 200-3 自動風險計算器（可能性 × 衝擊 → 風險等級，依 ISO 章節預先映射的威脅代碼） |
| **證據追蹤器** | 具到期追蹤、驗證狀態與新鮮度警示的證據項目 |
| **連接器** | 從 44 個系統自動匯入證據 —— 來自真實基礎設施的持續合規訊號 |
| **夜間證據封存** | Celery Beat 工作每日 02:00 UTC 封存過期的連接器證據 |
| **對照檢視器** | 跨框架映射：4,671 個物件 / 59 條軸線 —— ISO 27001 ↔ NIST CSF ↔ MITRE ATT&CK v19 ↔ GDPR ↔ DORA ↔ BSI IT-Grundschutz ↔ FINMA ↔ OWASP ASVS 5.0 ↔ NCSC CAF ↔ ReCyF v2.5，以及更多 |
| **QA／存在性檢查器** | 驗證所有預期產出是否齊備（框架、營運、隱私、雲端 PII、雲端安全、AI） |
| **系統事件日誌** | 平台所有動作的完整稽核日誌 |
| **管理面板** | 使用者管理（CRUD）、系統資訊、服務健康狀態、資料庫統計、匯入觸發 |
| **全文搜尋** | 透過 OpenSearch 搜尋所有政策與 IMP 文件內容（可依產品篩選） |
| **ISMS Compass** | 對照 ISMS CORE 黃金標準的 AI 缺口分析（需要 `ANTHROPIC_API_KEY`） |
| **合規評鑑套件** | 29 個合規框架，具評鑑、計分、缺口追蹤與匯出。請見 [COMPLIANCE.zh-TW.md](COMPLIANCE.zh-TW.md)。 |
| **NIST CSF 2.0 評鑑** | 6 項功能（含 GV — 治理）下的 106 項子類別、等級 1–4 評分、雷達圖 + 長條圖、可從官方 NIST 範本匯入 XLSX、匯出 XLSX/CSV |
| **NIS2 評鑑** | EU 2022/2555 —— 第 21(2) 條的 10 項安全措施 + 第 23 條的 5 項通報義務，成熟度 0–4 |
| **DORA 評鑑** | EU 2022/2554 —— 5 大支柱（ICT 風險、事件通報、韌性測試、第三方風險、資訊分享）下的 27 條條文，成熟度 0–4 |
| **CIS Controls v8 評鑑** | 18 項控制措施下的 153 項防護措施，成熟度 0–4 |
| **BSI IT-Grundschutz 評鑑** | 10 個層級下的全部 111 個 Bausteine，成熟度 0–4。搭配橫跨三項 ISO 標準的 538 筆對照映射。 |
| **CSRM 評鑑（NCSC CH）** | 自訂的物件導向模組 —— IT Protection Objects、20 項 NIST CSF 2.0 基準要求、二元狀態、6 項控制目標 |
| **TISAX 評鑑** | VDA ISA 6.0 —— 9 個領域下的 79 項要求，成熟度 0–4 |
| **Swiss ISG 評鑑（SR 128）** | 瑞士聯邦資訊安全法 2024 —— 27 項要求、24 小時內向 BACS/OFCS 通報網路攻擊（Art. 74e），成熟度 0–4；ISO 27001 對照：40 筆映射 |
| **Swiss nDSG 評鑑** | 瑞士聯邦資料保護法 2023 —— 6 章下的 25 項條款，成熟度 0–4 |
| **EU 網路韌性法評鑑** | EU 2024/2847 —— 6 個群組下的 26 項基本要求，成熟度 0–4 |
| **EU AI Act 評鑑** | EU 2024/1689 —— 第三章高風險 AI 系統要求中的 9 條條文（Art. 8–15、Art. 27），成熟度 0–4 |
| **NIST AI RMF 1.0 評鑑** | 4 項功能（GOVERN、MAP、MEASURE、MANAGE）下的 72 項子類別，成熟度 0–4；ISO 42001 對照：32 筆映射，EU AI Act：31 筆映射 |
| **EU 雲端主權框架** | 8 項主權目標（SOV-1 至 SOV-8）、SEAL-0 至 SEAL-4 評分、加權主權分數 |
| **COBIT 2019 評鑑** | 40 項治理／管理目標，能力評分 0–4 |
| **CyberFundamentals（BE）** | 41 項對齊 NIST CSF 2.0 的實務，成熟度 0–4；ISO 27001 對照：107 筆映射 |
| **BaFin BAIT（DE）** | Rundschreiben 10/2017（2021 修訂）—— 12 個模組下的 23 項要求，成熟度 0–4；ISO 27001 對照：69 筆映射 |
| **CSSF 20-750（LU）** | ICT 風險 —— 7 個領域下的 19 項要求，成熟度 0–4；ISO 27001 對照：47 筆映射 |
| **ACN 指引（IT）** | Determinazione obblighi di base（2025 年 4 月）—— 37 項措施／87 項要求（Important）或 43 項措施／116 項要求（Essential），成熟度 0–4；ISO 27001 對照：43 筆映射 |
| **UK NIS 評鑑** | UK NIS Regulations 2018 —— 3 項目標下的 13 項要求，成熟度 0–4；ISO 27001 對照：51 筆映射 |
| **UK 營運韌性** | FCA/PRA PS21/3 + PS26/2 —— 4 項目標下的 12 項要求，成熟度 0–4；ISO 27001 對照：34 筆映射 |
| **NCSC CAF v4.0 評鑑** | 英國 NCSC 網路評鑑框架 v4.0 —— 14 項原則與 4 項目標下的 41 項貢獻結果；未達成／部分達成／已達成；ISO 27001 對照：65 筆映射 |
| **ReCyF v2.5 評鑑（法國 NIS2）** | ANSSI ReCyF v2.5 —— 4 大支柱（Gouvernance / Protection / Défense / Résilience）下的 20 項安全目標、152 項要求；法國待通過的 NIS2 轉換法；ISO 27001 對照：50 筆映射 |
| **評鑑集合** | 將多個評鑑組成具名集合，並附衍生統計（完成率 %、合規率 %、狀態彙總）。可匯出為 CSV、彩色標示的 XLSX 或 PDF（A4）。 |
| **專案工作區** | 建立具名專案 —— 擁有、編輯並追蹤從文件庫精選的政策與實施。所見即所得編輯、文件變數替換、批次操作、SCR 檢核表、完整性計分。 |
| **文件編輯器** | TipTap v3 所見即所得 + 原始碼切換；網格表格自動轉換（RST → GFM）；中繼資料註解剝除 |
| **連接器證據晉升** | 將自動化的連接器證據晉升至證據追蹤器，範圍限定於作用中的專案 |
| **可收合側邊欄** | Azure Portal 風格的純圖示側邊欄 —— 可收合為 52 px 的長條、完整工具提示、狀態保存在 localStorage |
| **RBAC** | 角色型存取：超級管理員／管理員／ISMS 經理／稽核員／控制措施擁有者／檢視者 |
| **核准流程** | 內容狀態生命週期：草稿 → 審查 → 已核准 → 已發布 |
| **風險登錄表** | 專案範圍的風險情境，含 5×5 可能性／衝擊矩陣與視覺化風險熱圖 |
| **風險熱圖** | 彩色標示的 5×5 網格 —— 一眼掌握所有風險，可深入任一格 |
| **矯正 + ITSM 推送** | 風險接受簽核 + 含 ETA、成本、工作量、進度的行動計畫；冪等地推送至 Jira／ServiceNow；工單狀態同步 |
| **KPI 儀表板** | 9 項具名指標：`compliance_score`、`policy_coverage`、`risk_score_avg`、`risk_critical_count`、`evidence_freshness`、`gap_open_count`、`gap_closure_rate`、`remediation_overdue`、`audit_readiness`；走勢圖 |
| **稽核準備度分數** | 由全部 9 項 KPI 指標衍生的複合主分數 |
| **指標組合** | `super_admin` 可在單一檢視中查看所有組織的 KPI 指標 |
| **TPRM** | 供應商登記表，含關鍵性評級；DORA ICT 服務欄位；供應商評鑑；含到期警示的合約追蹤；專屬的 DORA 登錄表檢視 |
| **BIA** | 營運衝擊分析 —— 具 RTO/RPO/MTPD 時數的資產紀錄；財務、營運、聲譽與法規衝擊分數；復原測試追蹤 |
| **EBIOS RM** | 完整的 ANSSI 五場工作坊風險方法論 —— 重大事件、風險來源、策略情境（可能性 × 嚴重度矩陣）、對應 MITRE ATT&CK 技術的攻擊路徑 |
| **自訂框架匯入** | 以 YAML 上傳自訂或特定產業的框架；透過 `iso_mappings` 自動對應至 ISO 27001；顯示涵蓋率 % |
| **國家在地化** | 政策呈現會依 8 個司法管轄區調整法規引用：CH（預設）、FR、BE、LU、DE、AT、IT、GB —— 於請求時依 `org.country` 套用 |
| **跨框架涵蓋** | 以 BFS 推論將 ISO 27001 評鑑涵蓋範圍映射至 NIS2、DORA 與 GDPR；提供映射矩陣與推論涵蓋兩個分頁 |
| **MFA** | 以 TOTP 為基礎的 2FA —— 相容於 Google Authenticator／Authy；QR 碼設定；8 組單次備用碼；輸入 6 位數後自動送出 |
| **威脅情報情報來源** | 兩個專責容器，拉取 21+ 個來源。`isms-core-feeds`（9 個）：MITRE ATT&CK v19（每週 —— 697 項技術、15 項戰術）、MITRE ATLAS（每週）、CISA KEV（每日）、VulnCheck KEV（每日 —— VulnCheck 自有、涵蓋更廣的 KEV 目錄；約 67% 的條目不在 CISA 的目錄中）、FIRST EPSS（每日 —— 10K 上限，每日同步 OpenSearch）、NVD CVE 全量+增量（每週／每日 —— 約 250K 筆 CVE，支援 CVSS 4.0）、NVD CPE Option B（每週）、ENISA EUVD（每日 —— 已遭利用 + 重大 CVE）、Exploit-DB（每日 —— 約 52K 筆漏洞利用條目，以 CVE ID 交互參照至 NVD CVE；在 CVE 瀏覽器中加入 EDB 標籤 + Metasploit 徽章）。`isms-core-threat-intel`（選用設定檔，12 個來源）：CIRCL MISP + Botvrij MISP（每 6 小時增量，120K+ IOC）、AbuseIPDB（每日）、URLhaus（每日 —— 惡意程式 URL）、ThreatFox（每 6 小時 —— 惡意程式 IOC）、SSLBL（每日 —— 惡意 SSL 憑證指紋）、AlienVault OTX（每日 —— 帶 TLP 標籤與信心分數的 pulses）、Red Flag Domains（每日）、Stopforumspam（每日）、MalwareBazaar（每 6 小時 —— 惡意程式雜湊）、Feodo Tracker（每 6 小時 —— C2 殭屍網路 IP）、Malpedia（每週 —— 惡意程式家族 + 行為者）。VirusTotal 增補（每日 —— 選用，更新 IOC 信心分數）。GreyNoise（僅隨選 IP 查詢，`isms-core-backend` —— 非排程情報來源，免費方案每週 50 次查詢）。所有 OSINT IOC 在匯入時以 ATT&CK TID、家族代號、行為者代號、TLP 標籤交互增補。 |
| **CVE / CPE 瀏覽器** | 依嚴重性、EPSS 分數、CVSS 版本（v2/v3/v4）、年份、僅 KEV、僅 VulnCheck、EUVD 標記、僅 EDB（Exploit-DB 交互參照篩選）搜尋並篩選約 250K 筆 NVD CVE 條目。詳細面板：CVSS 分數（v2/v3/v4）、CPE 適用性、CWE、NVD 參照、CISA KEV 徽章、VulnCheck KEV 徽章（獨立於 CISA 的）、EUVD 徽章、EDB/EDB✓ 標籤（當 `edb_verified` 時顯示 Metasploit 徽章）。另有獨立的 CPE 分頁。 |
| **EUVD 瀏覽器** | ENISA 歐洲弱點資料庫 —— 瀏覽已遭利用與重大弱點；可依分數篩選，並有僅已遭利用、僅重大、EU 指派（互斥）等切換；詳細面板含廠商、產品、EPSS、別名。 |
| **KEV 稽核報告（A.8.8）** | 使用 CISA KEV 情報來源的 ISO 27001:2022 A.8.8 稽核軌跡 —— 依 CVE 的矯正狀態、逐廠商彙總、供稽核人員取證用的 CSV 匯出。 |
| **威脅暴露** | 將即時 IOC 情報來源中的作用中 MITRE 技術映射至 ISO 27001 控制措施 —— 缺口會標示出來。摘要列：作用中技術 / 受影響控制措施 / 缺口數。逐技術表格含 IOC 數量、來源情報標籤，以及彩色標示的控制措施標籤（綠色 ≥ 70%、橙色 40–69%、紅色 < 40%、灰色 = 未評鑑）。需在 `COMPOSE_PROFILES` 中包含 `threat-intel`。 |
| **IOC 瀏覽器** | 依類型（IP / 網域 / URL / 雜湊）、來源與自由文字，搜尋並篩選全部 12 個來源（CIRCL MISP、Botvrij MISP、AbuseIPDB、URLhaus、ThreatFox、SSLBL、AlienVault OTX、Red Flag Domains、Stopforumspam、MalwareBazaar、Feodo Tracker、Malpedia）的 OSINT IOC。欄位：類型、值、來源、信心、TLP 標籤、最後出現時間、歸因（家族 / 行為者 / ATT&CK TID 標籤）。展開任一列可看含所有標記的完整細節。 |
| **IP 增補** | 針對單一 IP 的隨選查詢，涵蓋五個來源：AbuseIPDB（濫用分數 + 檢舉次數 + 類別）、Shodan 付費 API（開放連接埠、橫幅、CVE、主機名稱）或 InternetDB 免費備援、MaxMind GeoLite2（地理位置／ASN）、IPInfo（隱私分類）、GreyNoise（雜訊／掃描器分類 + RIOT 狀態）。AbuseIPDB／Shodan 快取 24 小時；MaxMind／IPInfo／GreyNoise 快取 30 天（用量較低或配額較嚴的來源）。 |
| **惡意程式圖鑑** | 以 Malpedia 為來源的惡意程式家族瀏覽器（別名、說明、ATT&CK TID、關聯行為者）與威脅行為者名錄（國家歸因、動機）。 |
| **健康警示橫幅** | 當過去 24 小時內任一情報來源執行、連接器同步或 OpenSearch 檢查回報錯誤時，顯示可關閉的警示橫幅。情報與供應商群組的側邊欄會有紅點標記。 |
| **CPE Option B 切換** | 威脅情報來源頁面上的管理介面開關，可在執行時啟用／停用 NVD CPE Option B。設定儲存於 `platform_settings` 資料表，會覆寫環境變數。 |
| **儀表板情報卡片** | 儀表板上的四張可點擊摘要卡：CVE 索引數量、CISA KEV 總數、MITRE ATT&CK 狀態、情報來源健康狀態。 |
| **專案範圍的風險／缺口／證據** | 風險情境、缺口與證據項目都以作用中的專案為範圍 —— 切換專案即切換脈絡 |

---

## 生產部署 —— 逐步操作

### 步驟 0 — 前置條件

**軟體：**
```bash
docker --version          # 必須為 24.0 或更高
docker compose version    # 必須為 v2.x（不是舊版 docker-compose v1）
```

若任一指令失敗，請安裝 Docker Desktop（macOS/Windows）或 Linux 版 Docker Engine。

**硬體（生產環境最低需求）：**
- 記憶體：6 GB 可用（OpenSearch 約 1.5 GB、後端約 512 MB、前端約 256 MB、Postgres 約 512 MB）
- 磁碟：20 GB 可用
- CPU：最少 2 核心，建議 4 核心

**僅限 Linux —— OpenSearch 核心參數需求：**

```bash
# 立即生效：
sudo sysctl -w vm.max_map_count=262144

# 重開機後仍保留：
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```

macOS 與 Windows 的 Docker Desktop 會自動處理 —— 無須任何操作。

---

### 目錄結構

平台預期 ISMS CORE 內容儲存庫與平台目錄**並排**放置：

```
/your/base/directory/
├── factory_isms/
│   ├── isms-core-platform/          ← docker-compose.yml 放在這裡
│   ├── isms-core-framework/         ← FRAMEWORK 內容（以唯讀方式掛載）
│   ├── isms-core-operational/       ← OPERATIONAL 內容（以唯讀方式掛載）
│   ├── isms-core-privacy/           ← PRIVACY 內容 — ISO 27701:2025（以唯讀方式掛載）
│   ├── isms-core-cloud/             ← CLOUD 內容 — ISO 27018:2025（以唯讀方式掛載）
│   └── isms-core-ai/                ← AI 內容 — ISO 42001:2023（以唯讀方式掛載）
```

`docker-compose.yml` 會將全部五個產品目錄以唯讀磁碟區掛載。平台永遠不會修改這些檔案。

---

### 步驟 1 — 將檔案複製到伺服器

```bash
# 請在你的開發機上執行：
rsync -av \
  --exclude='.env' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.git' \
  --exclude='node_modules' \
  --exclude='certs' \
  /path/to/factory_isms/isms-core-platform/ \
  user@server:/home/user/isms-core/

ssh user@server
cd /home/user/isms-core
```

---

### 步驟 2 — 建立 .env

```bash
cp .env.example .env
```

編輯 `.env` —— 最低必要設定。請用下列指令產生每個密鑰：
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

```env
# 部署模式 —— Docker Compose 會自動讀取；不需要 --profile 旗標。
# 以下預設值適用於大多數部署。所有選項請見 .env.example。
COMPOSE_PROFILES=opensearch-single
# COMPOSE_PROFILES=opensearch-single,threat-intel      # ⚠ 另須設定 THREAT_INTEL_ENABLED=true
# COMPOSE_PROFILES=opensearch-cluster,garage,dashboards,threat-intel  # 企業版

# 主機
HOST_IP=10.0.0.112                    # 必填 —— 你的伺服器 IP
FQDN=                                 # 選填 —— 使用 Let's Encrypt TLS 時設定
PLATFORM_URL=https://10.0.0.112       # 必填 —— 須與上方 HOST_IP 一致
CORS_ORIGINS=https://10.0.0.112       # 必填 —— 須與上方 HOST_IP 一致

# 密鑰 —— 用上方指令逐一產生
POSTGRES_PASSWORD=                    # 必填
REDIS_PASSWORD=                       # 必填
SECRET_KEY=                           # 必填 —— 至少 32 個字元的隨機十六進位
CONNECTORS_WORKER_SECRET=             # 必填 —— 與 SECRET_KEY 相同方式產生

# 管理員帳戶
ADMIN_EMAIL=admin@isms-core.dev
ADMIN_PASSWORD=                       # 必填 —— 無預設值；留空則平台拒絕啟動
```

> **`ADMIN_PASSWORD` 沒有預設值。** 若留空，管理員帳戶不會被建立，你也無法登入。
>
> 所有選填設定請見 `.env.example`：AI／Compass 金鑰、電子郵件、TI API 金鑰、NVD 情報來源、OpenSearch 調校與 Garage S3。

---

### 步驟 3 — 啟動堆疊

```bash
docker compose up -d
```

> `.env` 裡的 `COMPOSE_PROFILES` 會告訴 Docker Compose 要啟動哪些服務。預設值（`opensearch-single`）已在 `.env.example` 中啟用。命令列不需要任何 `--profile` 旗標。

首次執行會拉取所有映像檔（沒有本機建置步驟 —— 後端／前端等都以預先建置好的映像檔從 GHCR/Docker Hub 出貨）。視連線速度而定，這需要 **3–5 分鐘**。之後重啟約需 60 秒。

```bash
docker compose logs -f    # 觀看進度（按 Ctrl+C 停止觀看）
docker compose ps         # 檢查所有容器
```

預期輸出 —— 所有容器都顯示 `healthy` 或 `Up`：

```
NAME                        STATUS
isms-core-nginx             Up (healthy)
isms-core-backend           Up (healthy)
isms-core-frontend          Up (healthy)
isms-core-postgres          Up (healthy)
isms-core-redis             Up (healthy)
isms-core-opensearch        Up (healthy)
isms-core-worker            Up (healthy)
isms-core-connectors        Up (healthy)
isms-core-feeds             Up (healthy)
isms-core-beat              Up
```

> `isms-core-beat` 顯示 `Up` 而沒有 `(healthy)` —— 這是正常的。Celery Beat 沒有 HTTP 端點。
> 若 `backup` 設定檔已啟用，`isms-core-backup` 也會顯示為 `Up`（無健康檢查 —— 它依 cron 排程執行）。

**Alembic 遷移會自動執行。** 後端在啟動時透過 `entrypoint.sh` 套用所有待處理的遷移。不需要手動執行 `alembic upgrade head`。

---

### 步驟 4 — 載入內容

#### 選擇性載入 —— 只掛載你需要的部分

```yaml
# docker-compose.yml —— 只掛載你想要的產品
volumes:
  - ../isms-core-framework:/app/isms-framework:ro
  - ../isms-core-operational:/app/isms-operational:ro
  # - ../isms-core-privacy:/app/isms-privacy:ro       # 註解掉 = 不匯入
  # - ../isms-core-cloud:/app/isms-cloud:ro
  # - ../isms-core-ai:/app/isms-ai:ro
  - ../isms-core-external:/app/isms-external:ro       # 選填 —— 你自己的文件
```

第五個掛載點 —— `isms-core-external` —— 可放入你既有的政策文件，供 ISMS Compass 對照 ISMS CORE 黃金標準做缺口分析。

#### 選項 A —— bootstrap.sh（首次部署建議使用）

`bootstrap.sh` 是一次性腳本，會：
1. 等待堆疊進入健康狀態
2. 以管理員身分驗證
3. 植入所有 ISMS 控制群組
4. 依序匯入所有政策、實施、內容與工作簿
5. 觸發 OpenSearch 完整重建索引
6. 完成後印出匯入統計

```bash
chmod +x bootstrap.sh
bash bootstrap.sh
```

這需要 **3–5 分鐘**。請勿中斷。

> **bootstrap.sh 可安全重複執行**，任何時候都行。它不會產生重複資料。

#### 選項 B —— 管理 WebUI（逐步操作）

以管理員身分登入 → **管理 → 首次執行設定**。由上而下依序執行：

| 步驟 | 按鈕 | 作用 |
|------|--------|-------------|
| 1 | **載入參考框架** | 植入控制群組 + 載入全部 37 個參考資料集。**務必先執行。** |
| 2 | **匯入政策** | 從已掛載的磁碟區匯入所有 POL、OP-POL、PRIV-POL、CLD-POL、REF、CTX、FORM 文件。 |
| 3 | **匯入實施（IMP）** | 匯入 IMP-UG 與 IMP-TG 文件，並將它們索引至 OpenSearch。 |
| 4 | **匯入評鑑工作簿** | 從產生器腳本解析框架評鑑工作簿的結構。 |
| 5 | **匯入營運檢核表** | 解析營運合規檢核表的結構。 |
| — | **完整同步（步驟 2–5）** | 依序執行全部四個匯入器。步驟 1 必須先單獨完成。 |

#### 匯入之後 —— 你會看到什麼

| 區段 | 內容 |
|---------|-------------|
| **儀表板** | 合規概觀、稽核準備度分數、主要缺口；ISMS／隱私／雲端／AI 產品切換器 |
| **控制措施** | 99 個控制群組（54 ISMS + 21 隱私 + 12 雲端 + 12 AI），含政策／評鑑／缺口狀態 |
| **政策** | 已匯入的文件（POL + OP-POL + PRIV-POL + CLD-POL + AI-POL + 基礎 + REF/CTX/INS） |
| **評鑑** | 188 個框架 + 53 個營運 + 21 個隱私 + 12 個雲端 + 10 個 AI 工作簿結構，含逐項合規狀態 |
| **缺口** | 已識別的合規缺口 —— 建立、指派、追蹤 |
| **證據** | 上傳證據並連結至控制群組與要求 |
| **涵蓋** | 框架與營運涵蓋範圍的熱圖 |
| **QA** | 存在性檢查器 —— 驗證全部五項產品的產出完整性 |
| **合規評鑑** | 29 個框架 —— NIST CSF 2.0、NIS2、DORA、CIS v8、BSI IT-Grundschutz、BSI C5:2026、BSI C3A、TISAX、Swiss nDSG/ISG、EU AI Act、NIST AI RMF、NCSC CAF v4.0、ReCyF v2.5（FR NIS2）、PCI DSS v4.0.1，以及更多 |
| **風險登錄表** | 風險登錄表 —— 空白，可供輸入資料 |
| **KPI 指標** | KPI 儀表板 —— 空白，可供輸入資料 |
| **TPRM** | 第三方風險管理 —— 空白，可供輸入資料 |
| **BIA** | 營運衝擊分析 —— 空白，可供輸入資料 |
| **EBIOS RM** | EBIOS 風險管理器 —— 空白，可供輸入資料 |
| **矯正** | 矯正追蹤 —— 已連結至缺口，可供指派 |
| **管理** | 使用者管理、系統健康狀態、匯入控制 |

---

### 步驟 5 — 驗證

```bash
docker compose ps
curl -k https://localhost/health
```

預期回應：
```json
{"status":"ok","database":"ok","opensearch":"ok"}
```

開啟 `https://{HOST_IP}`，接受自簽憑證警告，然後登入。

---

### 步驟 6 — 變更管理員密碼

**管理 → 使用者 → 編輯管理員使用者** —— 把系統交給任何人之前，請先變更密碼。

---

### 步驟 7 — 啟用 MFA

我們強烈建議在正式上線前，為所有管理員帳戶啟用 MFA。

1. 登入 → 前往 **系統**（管理側邊欄）
2. 在 **安全性** 區段中，點選 **啟用 MFA**
3. 用 Google Authenticator、Authy 或任何 TOTP 應用程式掃描 QR 碼
4. 輸入 6 位數驗證碼以確認
5. **複製你的 8 組備用碼**並妥善保存 —— 它們只會顯示一次

之後登入時，輸入密碼後會要求你提供 6 位數 TOTP 驗證碼。若你的驗證器應用程式遺失，請在登入畫面使用備用碼。

---

## TLS 憑證選項

### 模式 1 — Let's Encrypt（對外公開時建議使用）

```bash
FQDN=yourdomain.com   # 先在 .env 設定
./nginx/scripts/setup-letsencrypt.sh yourdomain.com admin@yourdomain.com
```

### 模式 2 — 自訂憑證（企業／內部 CA）

1. 將憑證放在 `./certs/cert.pem`，金鑰放在 `./certs/key.pem`
2. `docker compose restart isms-core-nginx`

### 模式 3 — 自簽（預設，無須設定）

首次開機時自動產生。瀏覽器會顯示安全性警告 —— 對內部部署而言這是預期且無害的。

- **Chrome/Edge：** 進階 → 繼續前往 {HOST_IP}
- **Firefox：** 進階… → 接受風險並繼續
- **Safari：** 顯示詳細資料 → 前往此網站

---

## 電子郵件設定（選填）

電子郵件預設為停用（`MAIL_HOST` 留空）。若要啟用，請在 `.env` 設定 `COMPOSE_PROFILES` 與 `MAIL_HOST`，然後執行 `docker compose up -d`。

### 選項 A — Mailpit（僅限本機測試 —— 切勿用於生產環境）

在 `.env` 中：
```env
COMPOSE_PROFILES=opensearch-single,mailpit
MAIL_HOST=isms-core-mailpit
MAIL_PORT=1025
```

然後執行 `docker compose up -d`。Mailpit 網頁介面：`http://{HOST_IP}:8025`

### 選項 B — SMTP 橋接（Microsoft 365 / Exchange Online）

在 `.env` 中：
```env
COMPOSE_PROFILES=opensearch-single,smtp-bridge
MAIL_HOST=isms-core-smtp-bridge
MAIL_PORT=1025
SMTP_BRIDGE_TENANT_ID=<your-tenant-id>
SMTP_BRIDGE_CLIENT_ID=<your-app-client-id>
SMTP_BRIDGE_CLIENT_SECRET=<your-app-secret>
SMTP_BRIDGE_FROM_ADDRESS=<sender@yourdomain.com>
SMTP_BRIDGE_FROM_NAME=ISMS CORE
```

然後執行 `docker compose up -d`。

---

## 連接器 —— 自動化證據

`isms-core-connectors` 會隨主堆疊自動啟動。請在 `.env` 設定 `CONNECTORS_WORKER_SECRET`（後端與連接器執行器使用相同值）。

### 支援的連接器（44 個系統）

| 類別 | 連接器 |
|----------|-----------|
| **Microsoft** | Entra ID、Microsoft Defender、Microsoft Sentinel、Microsoft Intune、Microsoft 365、Microsoft Purview、Azure CSPM |
| **網路與防火牆** | FortiGate、FortiAnalyzer、FortiManager、Palo Alto PAN-OS、Cisco ASA、Cisco ISE、Zscaler |
| **ITSM** | ServiceNow（雙向）、Jira / Jira Service Management（雙向）、GLPI |
| **弱點與 EDR** | Qualys、Tenable.sc、Tenable.io、CrowdStrike Falcon、SentinelOne、Wazuh、OpenVAS |
| **身分與 PAM** | Windows Active Directory、LDAP、FreeIPA、Authentik、Keycloak、CyberArk、HashiCorp Vault、Devolutions Server |
| **監控與 SIEM** | PRTG Network Monitor、Graylog、Zabbix、Generic SIEM |
| **雲端安全** | AWS Security Hub、Google Cloud SCC |
| **威脅情報** | OpenCTI、OpenAEV、Threat Intel Feed |
| **DevOps** | GitHub、GitLab |

> **Jira 與 ServiceNow：** 除了證據蒐集之外，兩者都支援對外推送至 ITSM。缺口紀錄與矯正行動可從缺口管理與矯正頁面推送成工單。推送具冪等性（不會重複），工單狀態也會同步回平台。

---

## 威脅情報 —— OSINT IOC 情報來源

`isms-core-threat-intel` 容器是選用設定檔，可在標準弱點情報來源之上加入 OSINT IOC 情報。若要啟用，請在 `.env` 中設定：

```env
COMPOSE_PROFILES=opensearch-single,threat-intel
THREAT_INTEL_ENABLED=true
```

然後執行 `docker compose up -d`。`THREAT_INTEL_ENABLED=true` 旗標會啟用 **IOC 瀏覽器**、**IP 增補**、**惡意程式圖鑑** 與 **威脅暴露** 的側邊欄項目。

### 情報來源

| 情報來源 | 排程 | API 金鑰 | 匯入內容 |
|------|----------|---------|-----------------|
| **CIRCL MISP** | 每 6 小時：00:00、06:00、12:00、18:00 UTC（增量） | 無（公開） | IOC（IP、網域、URL、雜湊），含 ATT&CK TID + Malpedia galaxy 標籤 + TLP |
| **Botvrij MISP** | 每 6 小時：01:00、07:00、13:00、19:00 UTC（錯開的增量） | 無（公開） | 相同結構 —— 以 `(ioc_type, value, source)` 對 CIRCL 去重 |
| **AbuseIPDB 黑名單** | 每日 02:00 UTC | `ABUSEIPDB_API_KEY` | 前 10,000 個信心值=100 的濫用 IP → `ti_iocs` + `ti-abuseipdb-blacklist` OpenSearch 索引 |
| **URLhaus** | 每日 03:00 UTC | 無 | 惡意程式下載 URL + 酬載雜湊（abuse.ch） |
| **ThreatFox** | 每 6 小時：03:00、09:00、15:00、21:00 UTC | `THREATFOX_API_KEY`（選填） | 惡意程式 IOC（IP、網域、URL、雜湊），含信心分數與惡意程式家族標籤 |
| **SSL 黑名單（SSLBL）** | 每日 04:00 UTC | 無 | 惡意程式 C2 基礎設施所用 SSL 憑證的 SHA1 指紋 |
| **AlienVault OTX** | 每日 04:30 UTC | `OTX_API_KEY` | Open Threat Exchange pulses —— 含 TLP 標籤、ATT&CK TID、由 pulse 訂閱者數量衍生的信心分數的 IOC |
| **Feodo Tracker** | 每 6 小時：04:30、10:30、16:30、22:30 UTC | 無 | Emotet、QakBot、TrickBot、Dridex 殭屍網路的 C2 IP（信心 85）；`ti-feodotracker` |
| **Red Flag Domains** | 每日 05:00 UTC | 無 | 新註冊的可疑網域 |
| **Stopforumspam** | 每日 05:30 UTC | 無 | 垃圾訊息發送者的 IP、電子郵件與使用者名稱資料庫（約 140K 個 IP） |
| **VirusTotal 增補** | 每日 07:00 UTC | `VT_API_KEY`（選填） | 以 VT 偵測比率增補既有 IOC —— 僅更新 `confidence`；不會新增 IOC。上限 450 次請求／日（免費方案安全值）。 |
| **MalwareBazaar** | 每 6 小時：02:00、08:00、14:00、20:00 UTC | `MALWAREBAZAAR_API_KEY` | 惡意程式樣本檔案雜湊（MD5/SHA1/SHA256），含惡意程式家族分類 |
| **Malpedia** | 每週，週日 03:00 UTC | 無 | 來自 MISP galaxy 的惡意程式家族（3,600+）與威脅行為者（900+）—— 無須 API 金鑰 |

**隨選增補**（無排程 —— 從 IP 增補頁面觸發，全部快取於 `ti_enrichment_cache`）：
- **AbuseIPDB 查詢** —— 單一 IP 的濫用分數、檢舉次數、類別；快取 24 小時
- **Shodan** —— 開放連接埠、橫幅、CVE、主機名稱；付費 API（`SHODAN_API_KEY`）或免費 InternetDB 備援；快取 24 小時
- **MaxMind GeoLite2** —— 國家／城市／ASN 地理位置；`MAXMIND_ACCOUNT_ID` + `MAXMIND_LICENSE_KEY`；快取 30 天
- **IPInfo** —— 隱私分類（VPN/Proxy/Tor/Relay/Hosting/Clean）；`IPINFO_API_KEY`；快取 30 天
- **GreyNoise** —— 網際網路雜訊／掃描器分類 + RIOT（已知合法服務）狀態；`GREYNOISE_API_KEY`；快取 30 天（免費方案每週 50 次查詢，因此快取較積極）

### 首次執行行為

首次啟動時（或 `TI_RUN_ON_START=true` 時），每個情報來源會立即執行，而非等待其排程時段。之後的執行對 MISP 僅取增量（只抓取新的 manifest UUID）。

控制首次執行的 MISP 歷史深度：
```env
TI_MISP_IMPORT_FROM_DATE=2024-01-01   # 預設 —— 兩年區間
# TI_MISP_IMPORT_FROM_DATE=2000-01-01  # 完整歷史（首次執行較慢）
```

### OpenSearch 索引

| 索引 | 情報來源 |
|-------|------|
| `ti-misp-circl` | CIRCL MISP |
| `ti-misp-botvrij` | Botvrij MISP |
| `ti-abuseipdb-blacklist` | AbuseIPDB 黑名單 |
| `ti-urlhaus` | URLhaus |
| `ti-threatfox` | ThreatFox |
| `ti-sslbl` | SSL 黑名單（SSLBL） |
| `ti-red-flag-domains` | Red Flag Domains |
| `ti-stopforumspam` | Stopforumspam |
| `ti-malwarebazaar` | MalwareBazaar |
| `ti-feodotracker` | Feodo Tracker |
| `ti-malpedia-families` | Malpedia 惡意程式家族 |
| `ti-malpedia-actors` | Malpedia 威脅行為者 |

### 停用個別情報來源

```env
TI_MISP_CIRCL_ENABLED=false           # 停用 CIRCL MISP
TI_MISP_BOTVRIJ_ENABLED=false         # 停用 Botvrij MISP
TI_ABUSEIPDB_ENABLED=false            # 停用 AbuseIPDB 黑名單
TI_URLHAUS_ENABLED=false              # 停用 URLhaus
TI_THREATFOX_ENABLED=false            # 停用 ThreatFox
TI_SSLBL_ENABLED=false                # 停用 SSL 黑名單
TI_ALIENVAULT_ENABLED=false           # 停用 AlienVault OTX
TI_FEODOTRACKER_ENABLED=false         # 停用 Feodo Tracker
TI_RED_FLAG_DOMAINS_ENABLED=false     # 停用 Red Flag Domains
TI_STOPFORUMSPAM_ENABLED=false        # 停用 Stopforumspam
TI_VIRUSTOTAL_ENABLED=false           # 停用 VirusTotal 增補
TI_MALWAREBAZAAR_ENABLED=false        # 停用 MalwareBazaar
TI_MALPEDIA_ENABLED=false             # 停用 Malpedia
```

---

## 企業部署 —— OpenSearch 叢集 + Dashboards

標準堆疊執行單一 OpenSearch 節點（`isms-core-opensearch`）。若生產部署需要更高的搜尋容量或 HA 需求，請啟用 3 節點叢集設定檔。OpenSearch Dashboards 可獨立於叢集設定檔之外另行加入。

> **⚠️ 啟動堆疊前先設定 `.env` 裡的 `COMPOSE_PROFILES`。** Docker Compose 在啟動時讀取 `.env` —— 變更只有在完整重啟後才會生效（`docker compose down && docker compose up -d`）。

### 硬體規模

| 組態 | 最低記憶體 | 建議 |
|---------------|---------|-------------|
| 單節點（預設） | 總計 6 GB | 8 GB |
| 3 節點叢集 | 總計 16 GB | 32 GB（4 GB 堆積 × 3 個節點） |

OpenSearch 堆積的經驗法則：分配給 OpenSearch 的記憶體 ≤ RAM 的 50%，每個節點絕不超過 31 GB。

### 選項 A — 標準（單一 OpenSearch 節點，無 Dashboards）

除了基本設定外，不需要變更 `.env`。預設的 `COMPOSE_PROFILES=opensearch-single` 已設定好。執行：

```bash
docker compose up -d
```

預期的 `docker compose ps` 輸出：10 個容器 —— `isms-core-opensearch` 是唯一的搜尋節點。

### 選項 B — 3 節點叢集，無 Dashboards

**在 `.env` 中：**
```env
COMPOSE_PROFILES=opensearch-cluster
OPENSEARCH_HEAP=4g   # 每節點堆積 —— 例如 16 GB 主機用 2g，32 GB 用 4g
```

然後執行 `docker compose up -d`。預期：12 個容器 —— 由 `isms-core-os01/02/03` 取代單一節點。

```
NAME                        STATUS
isms-core-nginx             Up (healthy)
isms-core-backend           Up (healthy)
isms-core-frontend          Up (healthy)
isms-core-postgres          Up (healthy)
isms-core-redis             Up (healthy)
isms-core-os01              Up (healthy)
isms-core-os02              Up (healthy)
isms-core-os03              Up (healthy)
isms-core-worker            Up (healthy)
isms-core-connectors        Up (healthy)
isms-core-feeds             Up (healthy)
isms-core-beat              Up
```

> `isms-core-os01` 是獲選的叢集管理器。三個節點構成名為 `isms-core-cluster` 的單一叢集。後端連線至 `isms-core-os01:9200` —— 後端設定無須變更。

### 選項 C — 3 節點叢集 + OpenSearch Dashboards

**在 `.env` 中：**
```env
COMPOSE_PROFILES=opensearch-cluster,dashboards
OPENSEARCH_HEAP=4g
DASHBOARDS_BIND=0.0.0.0   # 0.0.0.0 = 可從區域網路連線；127.0.0.1 = 僅限本機
```

然後執行 `docker compose up -d`。Dashboards 介面：`http://{HOST_IP}:5601` —— 當 `OPENSEARCH_DISABLE_SECURITY=true`（預設）時無須登入。

> Dashboards 用於基礎設施監控與索引檢視。`https://{HOST_IP}` 的平台 WebUI 不依賴它。

### 選項 D — 單節點 + OpenSearch Dashboards

**在 `.env` 中：**
```env
COMPOSE_PROFILES=opensearch-single,dashboards
DASHBOARDS_BIND=0.0.0.0   # 0.0.0.0 = 可從區域網路連線；127.0.0.1 = 僅限本機
```

然後執行 `docker compose up -d`。Dashboards 介面：`http://{HOST_IP}:5601`

當你想要索引能見度、又不想承擔 3 節點叢集的資源開銷時很有用。

### 加入 Garage S3 物件儲存

Garage 是選用的 S3 相容儲存，用於證據檔案與索引快照。它的運作與 OpenSearch 設定檔的選擇無關。

**步驟 1 —— 產生密鑰：**
```bash
openssl rand -hex 32
# → 將結果貼為 GARAGE_RPC_SECRET

python3 -c "import secrets; print('GK'+secrets.token_hex(12))"
# → 將結果貼為 GARAGE_ACCESS_KEY（必須是 GK + 24 個十六進位字元）

python3 -c "import secrets; print(secrets.token_hex(32))"
# → 將結果貼為 GARAGE_SECRET_KEY（必須是 64 個十六進位字元）
```

**步驟 2 —— 在 `.env` 中，將 `garage` 加入 `COMPOSE_PROFILES` 並設定密鑰：**
```env
# 標準 + Garage：
COMPOSE_PROFILES=opensearch-single,garage
# 企業版（完整堆疊）：
# COMPOSE_PROFILES=opensearch-cluster,garage,dashboards,threat-intel

GARAGE_RPC_SECRET=<generated above>
GARAGE_ACCESS_KEY=<generated above>
GARAGE_SECRET_KEY=<generated above>
GARAGE_BIND=127.0.0.1   # 僅在需要外部 S3 存取時才設為 0.0.0.0
```

然後執行 `docker compose up -d`。Garage 會在首次開機時透過 `isms-core-garage-setup` 容器自動初始化其桶（`isms-evidence`、`isms-snapshots`、`isms-exports`）。S3 API 在連接埠 3900 上監聽。

---

## 營運參考

### 重新同步內容

```bash
bash bootstrap.sh         # CLI —— 任何時候都能安全執行，具冪等性
# 或：管理 → 系統 → 立即同步
```

### 更新平台

```bash
git pull
docker compose pull
docker compose up -d
```

不會遺失資料 —— PostgreSQL 與 OpenSearch 的資料存放在具名的 Docker 磁碟區中。參考資料集會在每次容器啟動時自動重新載入。

### 檢視日誌

```bash
docker compose logs -f                        # 所有容器
docker compose logs -f isms-core-backend      # 特定容器
docker compose logs -f isms-core-worker
docker compose logs -f isms-core-feeds
```

### 自動化磁碟區備份

**`isms-core-backup`** 是選用的設定檔服務（[offen/docker-volume-backup](https://github.com/offen/docker-volume-backup)），依每日 cron 排程執行。

**啟用：** 在 `.env` 中將 `backup` 加入 `COMPOSE_PROFILES`：
```bash
COMPOSE_PROFILES=opensearch-single,backup
```

**備份內容：** `postgres-data`、`garage-meta` 與 `garage-data` 磁碟區（不含 OpenSearch 資料 —— 由 ISM 快照至 Garage S3 涵蓋）。

**設定：** 啟動前先複製 `backup.env.example` → `backup.env` 並編輯：

```bash
cp backup.env.example backup.env
# 編輯 BACKUP_CRON_EXPRESSION、BACKUP_RETENTION_DAYS，並視需要
# 取消註解 SSH 或 S3 遠端目的地區塊。
```

`backup.env` 中的重要設定：

| 變數 | 預設值 | 說明 |
|----------|---------|-------------|
| `BACKUP_CRON_EXPRESSION` | `30 3 * * *` | 每日 03:30 UTC |
| `BACKUP_FILENAME` | `isms-backup-%Y-%m-%dT%H-%M-%S.tar.gz` | 封存檔名樣式 |
| `BACKUP_COMPRESSION` | `gz` | 壓縮演算法 |
| `BACKUP_RETENTION_DAYS` | `7` | 早於此天數的封存檔會被清除 |
| `BACKUP_PRUNING_PREFIX` | `isms-backup-` | 僅清除符合此前置字元的檔案 |

主機上的封存目的地是在 `.env` 中設定：

```bash
BACKUP_ARCHIVE_PATH=/var/backups/isms-core    # 必須在啟動堆疊前存在
```

建立該目錄一次：
```bash
sudo mkdir -p /var/backups/isms-core
```

**僅 PostgreSQL 的手動備份（一次性或 CI）：**

```bash
docker exec isms-core-postgres \
  pg_dump -U isms_user isms_db > backup_$(date +%Y%m%d).sql

# 還原：
docker exec -i isms-core-postgres \
  psql -U isms_user isms_db < backup_YYYYMMDD.sql
```

### 停止堆疊

```bash
docker compose down       # 停止容器，保留磁碟區（資料完好）
docker compose down -v    # 銷毀所有資料 —— 僅用於乾淨重新安裝
```

---

## RBAC —— 角色

| 角色 | 能力 |
|------|-------------|
| **超級管理員** | 跨組織存取 —— 建立並管理組織，檢視所有組織的指標組合。 |
| **管理員** | 在其組織內的完整存取 —— 使用者管理、系統設定、同步觸發、內容核准、管理面板。 |
| **ISMS 經理** | 所有控制措施、評鑑、缺口、證據。無法管理使用者或系統設定。 |
| **稽核員** | 對所有內容的唯讀存取。可匯出報告。 |
| **控制措施擁有者** | 僅對被指派控制群組的讀寫權。 |
| **檢視者** | 對非機密項目的唯讀權。 |

---

## API 說明文件

- **Swagger UI：** `https://{HOST_IP}/api/docs`
- **ReDoc：** `https://{HOST_IP}/api/redoc`

需要身分驗證的端點必須帶有來自 `POST /api/v1/auth/login` 的 Bearer 權杖。

---

## 疑難排解

### OpenSearch 容器在 Linux 上立即結束

```bash
sudo sysctl -w vm.max_map_count=262144
docker compose restart isms-core-opensearch
# 永久生效：echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```

### 後端容器不斷重啟

```bash
docker compose logs isms-core-backend --tail=50
```

常見原因：`.env` 中未設定 `POSTGRES_PASSWORD` 或 `SECRET_KEY`；資料庫尚未就緒（60 秒內會解決 —— entrypoint 會重試）。

### bootstrap.sh 之後顯示「0 files imported」

```bash
docker exec isms-core-backend ls /app/isms-framework
docker exec isms-core-backend ls /app/isms-operational
```

若為空或不存在，表示 `docker-compose.yml` 中的磁碟區掛載指向不存在的路徑。請更新它們以符合你實際的目錄結構。

### bootstrap.sh 因驗證錯誤而失敗

1. 在 `.env` 設定 `ADMIN_EMAIL` 與 `ADMIN_PASSWORD`
2. `docker compose restart isms-core-backend`
3. 重新執行 `bash bootstrap.sh`

### 瀏覽器顯示憑證警告

使用自簽憑證時屬預期情況。請見上方的 [TLS 憑證選項](#tls-憑證選項)。

### Celery Beat 沒有 `(healthy)` 標籤

正常 —— Celery Beat 沒有 HTTP 端點。`Up` 狀態即確認它正常運作。

```bash
docker compose logs isms-core-beat --tail=20   # 確認排程器正在運作
```

---

## 環境變數參考

| 變數 | 必要 | 說明 |
|----------|----------|-------------|
| `COMPOSE_PROFILES` | 是 | 啟用服務群組 —— 請見上方的[部署設定檔](#服務)表格 |
| `HOST_IP` | 是 | 伺服器 IP —— 用於 nginx 自簽憑證的 SAN 與前端 API URL |
| `FQDN` | 否 | 網域名稱 —— 設定後即啟用 Let's Encrypt TLS |
| `PLATFORM_URL` | 是 | 完整 URL（例如 `https://10.0.0.112`） |
| `CORS_ORIGINS` | 是 | CORS 允許的來源 —— 通常與 `PLATFORM_URL` 相同 |
| `POSTGRES_PASSWORD` | 是 | PostgreSQL 密碼 |
| `REDIS_PASSWORD` | 是 | Redis 密碼 |
| `SECRET_KEY` | 是 | JWT 簽署金鑰 —— 至少 32 個字元的隨機十六進位 |
| `ADMIN_EMAIL` | 是 | 管理員帳戶電子郵件 |
| `ADMIN_PASSWORD` | 是 | 管理員帳戶密碼 —— **無預設值；留空則平台拒絕啟動** |
| `CONNECTORS_WORKER_SECRET` | 是 | 連接器執行器與後端 API 身分驗證共用的密鑰 |
| `ANTHROPIC_API_KEY` | 否 | 啟用 ISMS Compass AI 缺口分析 |
| `FEEDS_RUN_ON_START` | 否 | 設為 `true` 可讓所有情報來源在容器啟動時立即執行（預設：true） |
| `FEEDS_CVE_ENABLED` | 否 | 設為 `true` 可啟用 NVD CVE 匯入（預設：false —— 首次下載量很大） |
| `FEEDS_CPE_FULL` | 否 | 設為 `true` 可啟用 NVD CPE Option B |
| `FEEDS_EUVD_ENABLED` | 否 | 設為 `false` 可停用 ENISA EUVD 情報來源（預設：true） |
| `FEEDS_EXPLOITDB_ENABLED` | 否 | 設為 `false` 可停用 Exploit-DB 情報來源（預設：true） |
| `FEEDS_VULNCHECK_ENABLED` | 否 | 設為 `false` 可停用 VulnCheck KEV 情報來源（預設：true —— 未設 `VULNCHECK_API_KEY` 時會乾淨地不做事） |
| `VULNCHECK_API_KEY` | 否 | VulnCheck KEV 情報來源 —— 免費 Community 方案（1,000 次請求／分鐘）；請至 console.vulncheck.com 註冊 |
| `NIST_API_KEY` | 否 | NVD API 金鑰 —— 將速率上限從 5 次提升至 50 次／30 秒；請至 nvd.nist.gov 免費註冊 |
| `THREAT_INTEL_ENABLED` | 否 | 設為 `true` 可在前端啟用 IOC 瀏覽器／IP 增補／惡意程式圖鑑／威脅暴露 —— 需在 `COMPOSE_PROFILES` 中包含 `threat-intel` |
| `ABUSEIPDB_API_KEY` | 否 | 拉取 AbuseIPDB 黑名單與隨選 IP 增補所需 |
| `SHODAN_API_KEY` | 否 | 用於 IP 增補的 Shodan 付費 API —— 未設定時使用免費 InternetDB 備援 |
| `OTX_API_KEY` | 否 | AlienVault OTX 情報來源 —— 匯入 OTX IOC 所需 |
| `OTX_IMPORT_DAYS` | 否 | 首次執行的 OTX 歷史深度（預設：`90` 天） |
| `THREATFOX_API_KEY` | 否 | ThreatFox API 金鑰 —— 選填，可提高速率上限 |
| `MALWAREBAZAAR_API_KEY` | 否 | MalwareBazaar API 金鑰 —— 該情報來源所需 |
| `VT_API_KEY` | 否 | VirusTotal API 金鑰 —— 啟用每日 IOC 信心增補（免費方案：約 500 次請求／日） |
| `VT_DAILY_LIMIT` | 否 | 每次 VirusTotal 執行增補的 IOC 上限（預設：`450`） |
| `MAXMIND_ACCOUNT_ID` / `MAXMIND_LICENSE_KEY` | 否 | GeoLite2 —— IP 地理位置增補（國家、城市、ASN） |
| `IPINFO_API_KEY` | 否 | IPInfo —— IP 隱私偵測（VPN/proxy/Tor/hosting） |
| `GREYNOISE_API_KEY` | 否 | GreyNoise —— 隨選的網際網路雜訊／掃描器 IP 分類（免費方案：每週 50 次查詢，需商務電子郵件；僅限手動查詢，非排程情報來源） |
| `TI_MISP_IMPORT_FROM_DATE` | 否 | MISP 首次執行的日期下限（預設：`2024-01-01`；設為 `2000-01-01` 可取得完整歷史） |
| `TI_RUN_ON_START` | 否 | 設為 `true` 可強制所有 OSINT 情報來源在容器啟動時立即執行 |
| `TI_MISP_CIRCL_ENABLED` | 否 | 設為 `false` 可停用 CIRCL MISP 情報來源（預設：true） |
| `TI_MISP_BOTVRIJ_ENABLED` | 否 | 設為 `false` 可停用 Botvrij MISP 情報來源（預設：true） |
| `TI_ABUSEIPDB_ENABLED` | 否 | 設為 `false` 可停用 AbuseIPDB 黑名單拉取（預設：true） |
| `TI_ALIENVAULT_ENABLED` | 否 | 設為 `false` 可停用 AlienVault OTX 情報來源（預設：true） |
| `TI_VIRUSTOTAL_ENABLED` | 否 | 設為 `false` 可停用 VirusTotal 增補（預設：設定 `VT_API_KEY` 時為 true） |
| `TI_MALPEDIA_ENABLED` | 否 | 設為 `false` 可停用 Malpedia 情報來源（預設：true）—— 無須 API 金鑰 |
| `MAIL_HOST` | 否 | SMTP 主機 —— 留空即停用電子郵件（預設） |
| `MAIL_PORT` | 否 | SMTP 連接埠（預設：1025） |
| `NOTIFICATION_EMAIL` | 否 | 通知收件者 —— 預設為管理員帳戶電子郵件 |
| `SMTP_BRIDGE_TENANT_ID` | 否 | Azure AD 租用戶 ID —— 當 `COMPOSE_PROFILES` 含 `smtp-bridge` 時必要 |
| `SMTP_BRIDGE_CLIENT_ID` | 否 | Azure AD 應用程式用戶端 ID —— 當 `COMPOSE_PROFILES` 含 `smtp-bridge` 時必要 |
| `SMTP_BRIDGE_CLIENT_SECRET` | 否 | Azure AD 應用程式密鑰 —— 當 `COMPOSE_PROFILES` 含 `smtp-bridge` 時必要 |
| `SMTP_BRIDGE_FROM_ADDRESS` | 否 | 寄件者位址 —— 當 `COMPOSE_PROFILES` 含 `smtp-bridge` 時必要 |
| `OPENSEARCH_HEAP` | 否 | 每個 OpenSearch 節點的堆積 —— 例如 `1g`（預設）或 3 節點叢集的 `4g` |
| `OPENSEARCH_DISABLE_SECURITY` | 否 | 設為 `false` 可啟用 OpenSearch Security 外掛（需要 `OPENSEARCH_ADMIN_PASSWORD`） |
| `OPENSEARCH_ADMIN_PASSWORD` | 否 | 當 `OPENSEARCH_DISABLE_SECURITY=false` 時必要（OpenSearch 2.12+） |
| `EVIDENCE_STORE` | 否 | `postgres`（預設）或 `opensearch` —— opensearch 需要在 `COMPOSE_PROFILES` 中包含 `garage` + `opensearch-cluster` |
| `GARAGE_RPC_SECRET` | 否 | Garage 叢集密鑰 —— 當 `COMPOSE_PROFILES` 含 `garage` 時必要 |
| `GARAGE_ACCESS_KEY` | 否 | Garage S3 存取金鑰 —— 當 `COMPOSE_PROFILES` 含 `garage` 時必要 |
| `GARAGE_SECRET_KEY` | 否 | Garage S3 私密金鑰 —— 當 `COMPOSE_PROFILES` 含 `garage` 時必要 |
| `GARAGE_BUCKET_EVIDENCE` | 否 | 存放證據檔案的 Garage 桶（預設：`isms-evidence`） |
| `GARAGE_BIND` | 否 | Garage S3 API 綁定位址 —— `0.0.0.0` 對外暴露（預設：`127.0.0.1`） |
| `DASHBOARDS_BIND` | 否 | OpenSearch Dashboards 綁定位址 —— `0.0.0.0` 在區域網路上暴露（預設：`127.0.0.1`） |

---

## 上線檢核表

- [ ] **僅限 Linux：** 已設定 `vm.max_map_count=262144` —— 立即（`sysctl -w`）與永久（`/etc/sysctl.conf`）兩種皆完成
- [ ] 已從 `.env.example` 建立 `.env`，並填妥所有必要變數
- [ ] 已設定 `COMPOSE_PROFILES` —— 標準用 `opensearch-single`，企業用 `opensearch-cluster,...`
- [ ] `POSTGRES_PASSWORD` 已設為強隨機值
- [ ] `REDIS_PASSWORD` 已設為強隨機值
- [ ] `SECRET_KEY` 已設定 —— 至少 32 個字元的隨機十六進位
- [ ] `CONNECTORS_WORKER_SECRET` 已設定 —— 至少 32 個字元的隨機十六進位
- [ ] `ADMIN_PASSWORD` 已設定 —— **無預設值；留空則平台拒絕啟動**
- [ ] `HOST_IP` 已設為你伺服器的 IP 位址
- [ ] `docker compose up -d` 已完成 —— 所有容器已啟動
- [ ] `docker compose ps` 顯示所有服務容器為 `healthy`，且 `isms-core-beat` 為 `Up`
- [ ] `bootstrap.sh` 已執行一次 —— 匯入統計顯示非零數量
- [ ] `curl -k https://localhost/health` 回傳 `{"status":"ok","database":"ok","opensearch":"ok"}`
- [ ] 可在瀏覽器存取 `https://{HOST_IP}` —— 儀表板顯示合規資料
- [ ] 已變更管理員密碼（**管理 → 使用者 → 編輯管理員使用者**）
- [ ] 已設定 TLS 模式（自簽／自訂憑證／Let's Encrypt）
- [ ] 視需要已設定電子郵件 —— 在 `.env` 中設定 `COMPOSE_PROFILES=opensearch-single,mailpit`（開發）或 `opensearch-single,smtp-bridge`（生產）
- [ ] 若使用 ISMS Compass，已設定 `ANTHROPIC_API_KEY`
- [ ] 已為所有管理員帳戶啟用 MFA（**系統 → 兩步驟驗證**）

---

<p align="center">
  <a href="https://isms-core.com/platform">isms-core.com/platform</a> · <a href="https://isms-core.com">isms-core.com</a>
</p>

<p align="center">
<strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
<em>竹子天線真正管用的地方。</em> 🎋
</p>
