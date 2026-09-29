<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Compliance_Assessments-2E8B57?style=for-the-badge" alt="ISMS CORE Compliance Assessments"/>
</p>

<h1 align="center">🎋 ISMS CORE — 合規評鑑模組</h1>

<p align="center"><a href="COMPLIANCE.md">English</a> · <strong>繁體中文</strong> · <a href="COMPLIANCE.zh-CN.md">简体中文</a></p>

<p align="center">
  <strong>29 個內建框架 + 自訂 YAML 匯入。單一平台，不需另備工具。</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frameworks-29-2E8B57?style=flat-square" alt="29 Frameworks"/>
  <img src="https://img.shields.io/badge/Requirements-700+-0066CC?style=flat-square" alt="700+ Requirements"/>
  <img src="https://img.shields.io/badge/Export-CSV_%7C_XLSX_%7C_PDF-FF6600?style=flat-square" alt="Export"/>
  <img src="https://img.shields.io/badge/Assessment_Collections-Grouping_%26_Reports-2E7D32?style=flat-square" alt="Collections"/>
</p>

---

## 概觀

ISMS CORE Platform 內建一套統一的合規評鑑層，涵蓋歐洲、北美及全球的 29 個框架，並可透過 YAML 匯入任何特定產業或專有的控制措施框架。每個模組都提供結構化自我評鑑、成熟度評分（適用時為 0–4 分）、缺口追蹤與匯出。

評鑑結果可歸入 **評鑑集合** —— 具名的組合，可跨多個框架彙總狀態以供報告或稽核之用，並可匯出 CSV、XLSX（依狀態上色）與 PDF（A4）。

所有合規評鑑模組都位於 Platform WebUI 的 **Compliance Assessments** 側邊欄群組下。

---

## 快速參考

| 框架 | 類型 | 要求條目 | 分組 | 評分 | 適用對象 |
|-----------|------|-------------|----------|---------|----------|
| [NIST CSF 2.0](#nist-csf-20) | NIST | 106 個子分類 | 6 項功能 | Tier 1–4 | 任何產業 |
| [NIST AI RMF 1.0](#nist-ai-rmf-10-ai-100-1) | NIST | 72 個子分類 | 4 項功能（GOV/MAP/MSR/MNG） | 0–4 | AI 系統供應商與營運者 —— 任何產業 |
| [NIS2](#nis2-指令-eu-20222555) | EU 指令 | 15 項要求 | 2 條條文 | 0–4 | 歐盟關鍵實體／重要實體 |
| [DORA](#dora-eu-20222554) | EU 法規 | 27 條條文 | 5 大支柱 | 0–4 | 歐盟金融業 |
| [CIS Controls v8](#cis-critical-security-controls-v8) | 最佳實務 | 153 項防護措施 | 18 項控制措施 | 0–4 | 任何產業 |
| [BSI IT-Grundschutz](#bsi-it-grundschutz-kompendium) | 德國標準 | 111 個 Bausteine | 10 個層級 | 0–4 | 德國／DACH／IT-Grundschutz 認證 |
| [CSRM (NCSC CH)](#csrm-swiss-ncsc-2025) | 瑞士 NCSC | 20 項基線要求 | 5 項 CSF 功能 | 二元 | 瑞士關鍵基礎設施 |
| [Swiss ISG (SR 128)](#swiss-isg-sr-128) | 瑞士法律 | 27 項要求 | 8 個章節 | 0–4 | 瑞士聯邦機關與關鍵基礎設施營運者 |
| [TISAX](#tisax--vda-isa-60) | VDA/ENX | 79 項要求 | 9 個領域 | 0–4 | 汽車供應鏈 |
| [Swiss nDSG](#swiss-ndsg-2023) | 瑞士法律 | 25 項條款 | 6 章 | 0–4 | 處理瑞士個人資料的組織 |
| [EU Cyber Resilience Act](#eu-cyber-resilience-act-20242847) | EU 法規 | 26 項要求 | 6 個群組 | 0–4 | 歐盟產品製造商 |
| [EU AI Act](#eu-ai-act-20241689) | EU 法規 | 9 條條文 | 第 III 章第 2 節 + 第 27 條 | 0–4 | 歐盟 AI 系統提供者／部署者 |
| [EU Cloud Sovereignty Framework](#eu-cloud-sovereignty-framework-v121) | EC DG DIGIT | 8 項主權目標 | 1 個群組（SEAL） | SEAL 0–4 | 歐盟機構／公部門雲端採購 |
| [CyberFundamentals (BE)](#cyberfundamentals-ccb) | 比利時法規 | 41 項實務 | 6 項 CSF 功能 | 0–4 | 比利時組織／CCB 認證 |
| [BaFin BAIT (DE)](#bafin-bait-rundschreiben-102017-amended-2021) | 德國 BaFin | 23 項要求 | 12 個模組 | 0–4 | 德國金融業（銀行、投資公司） |
| [CSSF Circulaire 20-750 (LU)](#cssf-circulaire-20-750-lu) | 盧森堡 CSSF | 19 項要求 | 7 個領域 | 0–4 | 盧森堡金融業 |
| [ACN Cyber Risk Management (IT)](#acn-cyber-risk-management-it) | 義大利 ACN | 43 項措施／116 項要求 | 10 項法定要素 | 0–4 | 義大利組織／關鍵基礎設施 |
| [UK NIS Regulations](#uk-nis-regulations-2018) | 英國法律 | 13 項要求 | 3 項目標 | 0–4 | 英國網路與資訊系統營運者 |
| [UK Operational Resilience (FCA/PRA)](#uk-operational-resilience-fcapra) | UK FCA/PRA | 12 項要求 | 4 項目標 | 0–4 | 英國金融業 —— 銀行、保險公司、FMI |
| [COBIT 2019 (ISACA)](#cobit-2019-isaca) | ISACA EGIT | 40 項目標 | 5 個領域（EDM/APO/BAI/DSS/MEA） | 0–4 | 企業 IT 治理、稽核、CISM/CISA/CGEIT 持有者 |
| [NIST SP 800-53 R5](#nist-sp-800-53-rev-5) | NIST | 20 個控制措施家族 | 3 個類別（技術／營運／管理） | 0–4 | 美國聯邦機關、承包商，以及任何尋求完整安全控制措施的組織 |
| [CSA CCM v4.1](#csa-cloud-controls-matrix-v41) | CSA | 207 項控制措施規格 | 17 個領域 | 0–4 | 雲端服務供應商、雲端消費者 —— 任何產業 |
| [CSA AICM v1.1](#csa-ai-controls-matrix-v11) | CSA | 247 項控制措施 | 18 個領域 | 0–4 | 開發、部署或採購 AI 系統的組織 |
| [NCSC CAF v4.0 (UK)](#ncsc-caf-v40-uk) | NCSC UK | 41 項貢獻成果 | 14 項原則／4 項目標 | 0/2/4 | 英國基本服務營運者／CNI |
| [ReCyF v2.5 — France NIS2](#recyf-v25--france-nis2-anssi) | ANSSI | 20 項安全目標 | 4 大支柱 | 0–4 | 法國 NIS2 實體（EI 與 EE）—— 轉換法待通過 |
| [BSI C5:2026](#bsi-c52026) | BSI（德國） | 168 項準則 | 17 個領域 | 0–4 | 尋求 C5 查核證明的雲端服務供應商（DE／EU） |
| [BSI C3A](#bsi-c3a--criteria-enabling-cloud-computing-autonomy) | BSI（德國） | 30 個準則群組 | 6 個 SOV 領域 | 0–4 | 評估雲端主權的雲端 CSP 與客戶 |
| [PCI DSS v4.0.1](#pci-dss-v401) | PCI SSC | 323 項子要求 | 12 項要求／6 個里程碑 | 里程碑 | 處理持卡人資料的組織 |
| [FINMA](#finma) | 瑞士監管機關 | 21 項要求 | 3 份通函／指引 | 0–4 | 瑞士金融機構（銀行、保險公司） |
| [Custom (YAML)](#自訂框架yaml-匯入) | 使用者自訂 | 使用者自訂 | 使用者自訂 | 使用者自訂 | 所有 |

---

## 成熟度量表（多數框架採用）

| 分數 | 標籤 | 含義 |
|-------|-------|---------|
| 0 | 不符合 | 尚未實施 |
| 1 | 部分符合 | 臨時為之或不完整 |
| 2 | 發展中 | 已有文件但作法不一致 |
| 3 | 已定義 | 一致且有管理 |
| 4 | 已最佳化 | 可衡量、持續改善、已內化 |

CSRM 採用不同的模型 —— 參見 [CSRM 一節](#csrm-swiss-ncsc-2025)。

---

## 評鑑集合

**評鑑集合** 是具名的評鑑群組，可跨框架彙總合規狀態。用途包括：

- 依年度或稽核週期將評鑑分組
- 針對特定法規範圍提出報告（例如「EU regulatory stack 2025」）
- 比較各框架隨時間的進展

每個集合都會顯示衍生的統計資料：完成百分比、合規百分比、各狀態計數、狀態彙總（只有當所有成員評鑑皆合規時，集合才算「合規」）。

**匯出格式：** CSV（平面）、XLSX（依狀態上色，每份評鑑一個工作表）、PDF（A4，含各評鑑分數與不符合項目清單）。

---

## 框架模組

### NIST CSF 2.0

**來源：** NIST Cybersecurity Framework 2.0 版（2024）
**範圍：** 6 項功能共 106 個子分類：治理（Govern，GV）、識別（Identify，ID）、保護（Protect，PR）、偵測（Detect，DE）、應變（Respond，RS）、復原（Recover，RC）
**評分：** 每個子分類為 Tier 1–4（部分 → 調適），並含現況與目標層級
**適用對象：** 任何產業與規模 —— 全球普遍用作成熟度評鑑的基線

**平台功能：**
- 具名設定檔（可建立多份評鑑／隨時間追蹤）
- 每個設定檔都有雷達圖與長條圖報告頁
- 可從官方 NIST CSF 2.0 Excel 範本匯入 XLSX
- 可匯出 XLSX 與 CSV

**涵蓋範圍說明：**
- 完整涵蓋 106 個子分類，包括 GV（治理）—— CSF 2.0 新增、CSF 1.1 沒有的功能
- Crosswalk Viewer 提供 ISO 27001 ↔ NIST CSF 2.0 對照

---

### NIST AI RMF 1.0 (AI 100-1)

**來源：** NIST AI Risk Management Framework 1.0（NIST AI 100-1），2023 年 1 月
**範圍：** 4 項核心功能共 72 項子分類層級實務 —— GOVERN（GOV）、MAP（MAP）、MEASURE（MSR）、MANAGE（MNG）—— 分為 19 個類別
**評分：** 每個子分類的成熟度 0–4
**適用對象：** AI 系統供應商、開發者、部署者與營運者 —— 任何產業。自願採用，不特定司法管轄區。

**功能結構：**
- **GOVERN（19 個子分類）** —— 組織的 AI 風險文化、政策、問責結構、人力實務
- **MAP（18 個子分類）** —— 情境與風險界定：預期用途、分類、效益、成本、社會影響
- **MEASURE（22 個子分類）** —— 以量化、質性與混合方法工具分析、標竿比較與監控 AI 風險
- **MANAGE（13 個子分類）** —— 風險處理、殘餘風險、事件應變、上市後監督

**平台功能：**
- 72 項子分類實務，依類別分組（GOV-1 至 MNG-4），成熟度 0–4
- 沒有 NIST AI RMF ↔ EU AI Act 的直接對照軸 —— 兩者透過 ISO 42001 間接連結（NIST AI RMF ↔ ISO 42001：32 項對應；ISO 42001 ↔ EU AI Act：31 項對應），或透過 ISO 27001（NIST AI RMF ↔ ISO 27001：56 項對應；ISO 27001 ↔ EU AI Act：58 項對應）
- 評鑑集合 —— 可將 AI RMF 評鑑與 EU AI Act 評鑑歸為同一組

**涵蓋範圍說明：**
- 子分類說明取自官方 NIST AI RMF Playbook（72 項建議行動）
- 已有 ISO 27001 ↔ AI RMF 對照（56 項對應）；已有 ISO 42001 ↔ AI RMF 對照（32 項對應）—— 兩者都是可行的對應路徑
- 此框架為自願性質 —— 在任何司法管轄區都不是法規遵循要求
- 相關：NIST CSF 2.0 的 GOVERN 功能直接對應 AI RMF 的 GOVERN 結構

---

### NIS2 指令 (EU 2022/2555)

**來源：** 指令 (EU) 2022/2555 —— 網路與資訊安全 2 (Network and Information Security 2)
**範圍：** 15 項要求 —— 10 項第 21(2) 條的技術／組織安全措施，加上 5 項第 23 條的事件通報義務
**評分：** 成熟度 0–4
**適用對象：** 歐盟關鍵實體（essential entities：能源、運輸、銀行、醫療、水、數位基礎設施）與重要實體（important entities）；各會員國的國內轉換法規不一 —— 請依您所在司法管轄區的施行法確認適用性

**涵蓋範圍說明：**
- 已對應第 21(2) 條 (a) 至 (j) 各項措施
- 第 23 條的通報時限與內容義務
- 未涵蓋第 22–24 條（供應鏈、註冊、揭露）—— 僅就技術措施自我評鑑
- Crosswalk Viewer 提供 NIS2 對 ISO 27001 的對照

---

### DORA (EU 2022/2554)

**來源：** 規則 (EU) 2022/2554 —— 數位營運韌性法 (Digital Operational Resilience Act)
**範圍：** 5 大支柱的強制性要求：ICT 風險管理、ICT 事件通報、數位營運韌性測試、ICT 第三方風險管理，以及資訊分享。這些支柱共評鑑 27 條條文（第 II–VI 章）。
**評分：** 成熟度 0–4
**適用對象：** 歐盟金融實體（銀行、投資公司、保險、加密資產服務供應商、支付機構）及其關鍵 ICT 第三方供應商

**涵蓋範圍說明：**
- 涵蓋 DORA 的核心營運韌性義務
- 不取代依 DORA 與國家主管機關（NCA）的往來
- 涵蓋第一層級（Level-1）條文 —— 不含所有 RTS/ITS 授權法案（截至 2025 年法規仍在發展中）

---

### CIS Critical Security Controls v8

**來源：** Center for Internet Security，CIS Controls v8（2021）
**範圍：** 18 項控制措施共 153 項防護措施
**評分：** 成熟度 0–4
**適用對象：** 任何組織 —— 對中小企業及尚無主要框架者尤其適用。三個實施群組（IG1/IG2/IG3）可協助排定優先順序。

**涵蓋範圍說明：**
- 無論屬於哪個實施群組，153 項防護措施皆可評鑑
- Crosswalk Viewer 提供 CIS Controls v8 對 ISO 27001 的對照

---

### BSI IT-Grundschutz Kompendium

**來源：** Bundesamt für Sicherheit in der Informationstechnik（德國聯邦資訊安全局）—— IT-Grundschutz Kompendium
**範圍：** 2023 年版包含 10 個 Schichten（層級）共 111 個官方 Bausteine（模組構件）：ISMS、ORP（組織）、CON（概念）、OPS（營運）、DER（偵測）、APP（應用程式）、SYS（系統）、IND（工業）、NET（網路）、INF（基礎設施）。ISMS CORE 全部涵蓋 111 個。
**評分：** 成熟度 0–4
**適用對象：** 德國公部門（強制）、追求 ISO 27001／IT-Grundschutz 雙認證的組織、DACH 地區組織

**對照：**
- ISO 27001:2022 ↔ BSI IT-Grundschutz：386 項對應 —— 依 BSI 官方 Zuordnungstabelle 建立
- ISO 27701:2025 ↔ BSI IT-Grundschutz：101 項對應
- ISO 27018:2025 ↔ BSI IT-Grundschutz：51 項對應
- 合計：538 項跨標準對應 —— 可在 Crosswalk Viewer 檢視

**涵蓋範圍說明：**
- 依公開的 Kompendium 結構；確切要求文字取自完整 BSI Kompendium（bsi.bund.de）
- 所有 10 個層級共 111 個官方 Bausteine 皆已涵蓋

---

### CSRM (Swiss NCSC, 2025)

**來源：** Methode CSRM 2025 —— Cyber Security Risk Method，由瑞士國家網路安全中心（NCSC／BACS）於 2025 年發布
**範圍：** 20 項強制基線要求、用於報告的 6 項控制目標
**評分：** 二元 —— `met` / `partial` / `not_met` / `exception`（非 0–4 成熟度）
**適用對象：** 瑞士關鍵基礎設施營運者 —— 能源、運輸、水、醫療、金融、政府

> **重要：** CSRM 是與所有其他模組截然不同的模型。使用前請仔細閱讀本節。

#### CSRM 的運作方式

CSRM 以**物件為中心**。您不是全域評鑑一份要求清單，而是：

1. 定義 **IT 保護物件** —— 具有相同保護要求的系統、應用程式與資料的彙總群組（而非個別資產）
2. 依取自 NIST CSF 2.0 功能（GV、ID、PR、DE、RS）的 20 項基線要求評鑑每個保護物件
3. 識別**提升保護物件**（關鍵性較高者），並記錄額外的技術與組織措施（TOM）
4. 將結果對應至 6 項控制目標，以進行結構化報告

CSRM 的五步方法如下：
1. 定義範圍與保護物件
2. 分類保護物件（標準／提升）
3. 對每個物件套用 20 項基線要求
4. 為提升物件定義額外的 TOM
5. 透過 6 項控制目標提出報告

#### 與 NIST CSF 2.0 的對齊

CSRM 2025 對齊 **NIST CSF 2.0** —— 具體而言，20 項基線要求對應 GV（治理）、ID（識別）、PR（保護）、DE（偵測）與 RS（應變）。ISMS CORE 的實作全程採用 CSF 2.0 的功能代碼。

> **備註：** NCSC 自家的比較文件（*Vergleich-Managementsysteme EN*，2025）在其交叉參照表中使用 CSF **1.1** 代碼 —— 因為瑞士的 ICT 最低標準仍以 CSF 1.1 為基礎。CSRM 方法本身參照 CSF 2.0，ISMS CORE 反映的是正確版本。

#### BACS 自我檢討 —— 已知限制

NCSC 自家的比較文件對 CSRM 的限制異常坦率。以下缺口直接以免責聲明形式呈現在 Platform UI 中：

- **IEC 62443 對齊待完成** —— 工業控制系統的涵蓋範圍尚未定案
- **10 項 ICT 最低標準要求在 CSRM 中無對應項** —— 這些不是 ISMS CORE 實作的缺口，而是 CSRM 本身的缺口（比較文件第 12–13 頁已承認）
- **「無政策」標籤有誤導之嫌** —— CSRM 並未強制以政策作為文件類型，但在其控制目標中要求治理與組織措施
- **並行實施 ISMS = 重複風險** —— 同時運行 ISO 27001 ISMS 與 CSRM 的組織應對應共用控制措施，以免維護兩套並行的控制措施

**來源文件（BACS／NCSC 官方）：**
- CSRM 2025 方法：https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infras/Methode-CSRM-2025-EN.pdf
- 管理制度比較：https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infras/Vergleich-Managementsysteme_EN.pdf

---

### TISAX / VDA ISA 6.0

**來源：** Trusted Information Security Assessment Exchange —— VDA Information Security Assessment (ISA) 6.0 版
**範圍：** 9 個領域共 79 項要求：資訊安全政策與組織、人力資源、實體安全、身分與存取管理、IT／網路安全、供應商關係、合規、原型保護，以及資料保護
**評分：** 成熟度 0–4
**適用對象：** 處理敏感資料（尤其是原型與車輛資料）的汽車產業供應商、OEM 合作夥伴與分包商 —— 對多數主要 OEM（BMW、VW Group、Mercedes、Stellantis 等）而言，參與 TISAX 認證是供應鏈要求

**涵蓋範圍說明：**
- 依 VDA ISA 6.0 的領域結構與評鑑準則
- 完整的 TISAX 評鑑與標籤核發需與 ENX 認可的稽核員往來
- 本模組是為準備就緒而設的自我評鑑工具，不能取代官方 TISAX 評鑑
- 評鑑標籤（TISAX、AL1/AL2/AL3）僅透過 ENX 認可的評鑑服務供應商核發

---

### Swiss ISG (SR 128)

**來源：** Bundesgesetz über die Informationssicherheit beim Bund (ISG)／瑞士聯邦資訊安全法 (LSI) —— SR 128，2024 年 1 月 1 日生效；網路攻擊通報義務（第 74a–74h 條）於 2025 年 4 月 1 日生效
**範圍：** 8 個章節共 27 項可評鑑要求：資訊安全原則（第 6–10a 條）、資訊分類（第 11–15 條）、ICT 安全（第 16–19 條）、人員與存取（第 20–21 條）、實體安全（第 22–23 條）、人員安全查核（第 27–30、43 條）、網路攻擊通報義務（第 74a–74h 條）、ISMS 組織（第 81、85 條）
**評分：** 成熟度 0–4
**適用對象：** 瑞士聯邦機關（強制）；受第 74b 條網路攻擊通報義務約束的關鍵基礎設施營運者（能源、水、金融、運輸、醫療、ICT）；自願對齊瑞士聯邦安全標準的民營組織

**主要義務：**
- **24 小時網路攻擊通報** —— 在偵測到危害營運、涉及資料竄改／外洩、長時間未被發現或涉及勒索的網路攻擊後 24 小時內，強制向 BACS／OFCS 通報（第 74d–74e 條）
- **資訊分類** —— 三級架構：內部／機密／祕密，並採知悉必要（need-to-know）存取控制（第 11–14 條）
- **ICT 安全類別** —— 基線／提升／極高，各有對應的最低安全措施（第 17–18 條）
- **人員安全查核（PSC）** —— 敏感職務的基本與延伸查核；定期重複辦理（第 27–43 條）
- **ISB／RSSI 任命** —— 正式設置資訊安全主管，負責諮詢、指令與合規監督（第 81 條）
- **行政處罰** —— 未通報網路攻擊：最高 100,000 瑞士法郎（第 74h 條）

**ISO 27001 對照：** 40 項對應 —— ISO 27001:2022 的控制措施可直接對應 ISG 要求；實務上 ISO 27001 是公認的 ISG 合規實施載體。

**涵蓋範圍說明：**
- 本模組主要適用於瑞士聯邦機關及第 74b 條所列關鍵基礎設施的營運者
- 不受第 74b 條約束的民營組織並無法律遵循義務，但得自願採用此框架作為瑞士安全基線
- 網路攻擊通報義務（第 74a–74h 條）是關鍵基礎設施營運者最迫切的合規行動 —— 已於 2025 年 4 月 1 日生效

> **備註：** 本模組是自我評鑑工具。官方合規認定需由合格的瑞士資訊安全專業人員審查。

---

### Swiss nDSG 2023

**來源：** Bundesgesetz über den Datenschutz (nDSG)／瑞士聯邦資料保護法 —— 2023 年 9 月 1 日生效
**範圍：** 6 章共 25 項關鍵條款：範圍與原則、資料主體權利、控管者義務、特殊情形、資料傳輸、執法
**評分：** 成熟度 0–4
**適用對象：** 處理瑞士居民個人資料或在瑞士設立的任何組織

**涵蓋範圍說明：**
- nDSG 是瑞士對應 EU GDPR 的法規（範圍大致相近，法律基礎不同）
- 本模組涵蓋核心合規義務 —— 法律解釋應諮詢瑞士資料保護法律顧問
- 同時受 nDSG 與 GDPR 約束的瑞士組織（例如處理歐盟居民資料者）宜併用本模組與 GDPR 對照

---

### EU Cyber Resilience Act (2024/2847)

**來源：** 規則 (EU) 2024/2847 —— 網路韌性法 (Cyber Resilience Act)
**範圍：** 6 個群組共 26 項基本要求：基本網路安全要求、弱點處理、符合性評鑑、市場監督、協調揭露、事件通報
**評分：** 成熟度 0–4
**適用對象：** 在歐盟市場銷售含數位元素產品（硬體與軟體）的製造商與進口商

**涵蓋範圍說明：**
- CRA 分階段實施：市場監督條款自 2025 年中適用，弱點／事件通報自 2025 年底適用，2027 年底全面適用
- 附錄 I（第 I 部分與第 II 部分）的基本要求是主要合規標的 —— 本模組兩者皆涵蓋
- 符合性評鑑途徑取決於產品關鍵性等級（Class I、II 或關鍵產品）—— 自我宣告或第三方評鑑
- 本模組提供就緒狀態的自我評鑑；Class II 與關鍵產品的正式符合性評鑑需由公告機構（notified body）進行

---

### EU AI Act (2024/1689)

**來源：** 規則 (EU) 2024/1689 —— 人工智慧法 (Artificial Intelligence Act)
**範圍：** 第 III 章（高風險 AI 系統）的 9 條條文：第 2 節的 8 條核心要求條文（第 8 條合規、第 9 條風險管理、第 10 條資料治理、第 11 條技術文件、第 12 條紀錄保存、第 13 條透明度、第 14 條人為監督、第 15 條準確性／強健性／網路安全），加上第 3 節的第 27 條基本權利影響評鑑
**評分：** 成熟度 0–4
**適用對象：** 歐盟境內 AI 系統的提供者與部署者 —— 義務依風險分類而異（不可接受風險／禁止、高風險、有限風險、最低風險）

**涵蓋範圍說明：**
- 本模組涵蓋**高風險 AI 系統**的第 3 章義務 —— 最實質的合規層級
- 禁止的 AI 實務（第 5 條）不是評鑑標的；該等實務必須絕對避免
- 本模組版本未涵蓋通用目的 AI 模型義務（第 VIII 篇）
- AI 法分階段實施：禁止的實務自 2025 年 2 月起適用；高風險義務於 2026–2027 年間分階段適用
- 高風險 AI 系統的正式符合性評鑑需由公告機構進行，或採標準化測試的自我評鑑

---

### EU Cloud Sovereignty Framework (v1.2.1)

**來源：** 歐盟執委會 —— DG DIGIT，EU Cloud Sovereignty Framework v1.2.1（2025 年 10 月）
**範圍：** 8 項主權目標（SOV-1 至 SOV-8），以 SEAL-0 至 SEAL-4 等級評鑑。加權主權分數（權重合計 100%）：SOV-1 策略 15% · SOV-2 法律與管轄 10% · SOV-3 資料與 AI 10% · SOV-4 營運 15% · SOV-5 供應鏈 20% · SOV-6 技術 15% · SOV-7 安全與合規 10% · SOV-8 環境 5%
**評分：** SEAL-0（無主權）→ SEAL-1（管轄）→ SEAL-2（資料）→ SEAL-3（數位韌性）→ SEAL-4（完整數位主權）
**適用對象：** 依歐盟採購與數位主權要求評估雲端服務供應商的歐盟機構、公部門機關與受監管實體。參考 Gaia-X、ENISA/NIS2/DORA、CIGREF Trusted Cloud Referential v2、France Cloud de Confiance 與德國 Souveräner Cloud 策略。

**涵蓋範圍說明：**
- 此框架為各採購層級定義**最低保證等級** —— 本模組支援自我評鑑及對照該等層級的缺口分析
- SEAL 等級是質性判斷；正式採購決策需有供應商稽核證據與合約承諾
- SOV-5 供應鏈評鑑需能掌握次級供應商鏈 —— 證據深度可能因供應商透明度而異
- 環境永續（SOV-8）評分僅供參考；正式綠色採購可能需要經認證的能源／碳排資料

---

### CyberFundamentals (CCB)

**來源：** Centre for Cybersecurity Belgium (CCB) —— CyberFundamentals Framework v2025
**範圍：** 41 項實務，對齊 NIST CSF 2.0 功能：治理（GV）、識別（ID）、保護（PR）、偵測（DE）、應變（RS）、復原（RC）
**評分：** 成熟度 0–4
**適用對象：** 尋求 CCB CyberFundamentals 認證的比利時組織；比利時境內屬 NIS2 範圍的實體；在比利時法規情境下使用 NIST CSF 2.0 的任何組織

**涵蓋範圍說明：**
- CyberFundamentals 使用 NIST CSF 2.0 的控制措施編號（GV.OC-01、ID.AM-01 等）—— ISMS CORE 的對照沿用既有的 ISO→NIST CSF 對應
- 四個保證等級：Small、Basic、Important、Essential（對齊比利時 NIS2 轉換法，2024 年 4 月 26 日法）
- 對照：ISO 27001:2022 ↔ CyberFundamentals —— 107 項對應

---

### BaFin BAIT (Rundschreiben 10/2017, amended 2021)

**來源：** Bundesanstalt für Finanzdienstleistungsaufsicht（德國聯邦金融監督局）—— Bankaufsichtliche Anforderungen an die IT (BAIT)，Rundschreiben 10/2017，2021 年 8 月 16 日修訂
**範圍：** 12 個模組共 23 項要求：IT 策略、IT 治理、資訊風險管理、資訊安全、IT 專案、應用程式開發、IT 營運、IT 委外、IT 緊急管理、IAM、密碼學、BCM
**評分：** 成熟度 0–4
**適用對象：** 受 BaFin 監理的德國銀行與金融機構；對歐盟受監管實體而言，須與 MaRisk 及 DORA 併同適用

**涵蓋範圍說明：**
- BAIT 是德國受監理銀行主要的 IT 監理通函；VAIT（保險）與 KAIT（資本管理）結構相同
- 2021 年 8 月 16 日修訂（非取代性通函）；包含 MaRisk 對齊與雲端特定指引
- 對照：ISO 27001:2022 ↔ BaFin BAIT —— 69 項對應

---

### CSSF Circulaire 20-750 (LU)

**來源：** Commission de Surveillance du Secteur Financier (CSSF)，盧森堡 —— Circulaire CSSF 20/750
**範圍：** 7 個 ICT 風險領域共 19 項要求：治理、風險管理、ICT 安全、營運持續、第三方管理、事件管理、稽核
**評分：** 成熟度 0–4
**適用對象：** 受 CSSF 監理的盧森堡金融業實體 —— 銀行、投資公司、支付機構、基金管理機構

**涵蓋範圍說明：**
- CSSF 20/750 是 CSSF 受監管實體主要的 ICT 風險管理通函，對齊 EBA/ESMA 指引
- 自 2025 年 1 月起受 DORA 約束的實體宜併用本模組與 DORA 模組
- 對照：ISO 27001:2022 ↔ CSSF 20/750 —— 47 項對應

---

### ACN Cyber Risk Management (IT)

**來源：** Agenzia per la Cybersicurezza Nazionale (ACN) —— *Determinazione obblighi di base*（2025 年 4 月），實施 D.Lgs. 138/2024 第 24(2) 條
**範圍：** 兩個層級 —— Important 實體（附錄 1）37 項措施／87 項要求，Essential 實體（附錄 2）43 項措施／116 項要求 —— 圍繞第 24(2) 條的 10 項法定要素編排：風險分析與系統安全政策、事件管理、營運持續、供應鏈安全、安全採購／開發／維護、風險措施有效性檢視、基本網路衛生與訓練、密碼學政策、人力資源安全／存取控制／資產管理，以及多因子驗證／安全通訊
**評分：** 成熟度 0–4
**適用對象：** 義大利組織 —— 公共行政、關鍵基礎設施營運者、義大利境內屬 NIS2 範圍的實體

**涵蓋範圍說明：**
- ACN 是義大利國家網路安全局及 NIS2 主管機關；這些基本安全措施對齊義大利的 NIS2 轉換法（D.Lgs. 138/2024）
- 同時受 ACN 義務與 NIS2 約束的組織可併用兩個模組
- 對照：ISO 27001:2022 ↔ ACN Guidelines —— 43 項對應

---

### UK NIS Regulations 2018

**來源：** The Network and Information Systems (NIS) Regulations 2018 (SI 2018/506) —— 英國對 EU NIS 指令的實施
**範圍：** 3 項目標共 13 項要求：治理、風險管理與安全、營運能力
**評分：** 成熟度 0–4
**適用對象：** 英國能源、運輸、醫療、水、數位基礎設施的基本服務營運者（OES）；相關數位服務供應商（RDSP）

**涵蓋範圍說明：**
- 英國 NIS 法規在脫歐後仍以國內法效力存續；網路安全與韌性法案（Cyber Security and Resilience Bill，2025，尚待御准）將更新並擴大範圍
- NCSC 的 Cyber Assessment Framework（CAF）是 OES 合規的建議工具 —— 本模組涵蓋核心 NIS 義務
- 對照：ISO 27001:2022 ↔ UK NIS Regulations —— 51 項對應

---

### UK Operational Resilience (FCA/PRA)

**來源：** FCA 政策聲明 PS21/3 + PS26/2；PRA 監理聲明 SS1/21；英格蘭銀行營運韌性政策
**範圍：** 4 項目標共 12 項要求：重要業務服務、衝擊容忍度、情境測試、自我評鑑
**評分：** 成熟度 0–4
**適用對象：** 英國金融業 —— 銀行、房屋互助協會、PRA 指定的投資公司、保險公司、金融市場基礎設施（FMI）、支付系統營運者

**涵蓋範圍說明：**
- 英國營運韌性要求已於 2025 年 3 月全面生效（PS21/3 期限）；PS26/2 將範圍擴及更多實體
- 同時受英國營運韌性與 DORA 約束的實體宜併用兩個模組
- 重點在於重要業務服務（IBS）與衝擊容忍度 —— 不能取代與 FCA／PRA 的正式監理往來
- 對照：ISO 27001:2022 ↔ UK Operational Resilience —— 34 項對應

---

### COBIT 2019 (ISACA)

**來源：** ISACA —— COBIT 2019 Framework: Governance and Management Objectives（2018 年 11 月）
**範圍：** 5 個領域共 40 項治理與管理目標：EDM（評估、指導與監督）、APO（對齊、規劃與組織）、BAI（建置、獲取與實施）、DSS（交付、服務與支援）、MEA（監督、評估與評鑑）
**評分：** 能力等級 0–4（不完整 → 已執行 → 已管理 → 已建立 → 最佳化）
**適用對象：** 企業 IT 治理計畫、內部稽核職能、IT 策略與董事會層級監督。對 CISM、CISA 與 CGEIT 認證持有者尤其相關。

**涵蓋範圍說明：**
- EDM 目標（EDM01–EDM05）屬治理層級 —— 供董事會／高階主管監督之用；APO、BAI、DSS、MEA 屬管理層級
- APO13（已管理安全）與 DSS05（已管理安全服務）可直接對應 ISO 27001:2022 附錄 A 的資訊安全控制措施
- COBIT 2019 對齊 ISO/IEC 27001、ISO/IEC 38500、ITIL、NIST CSF 與 PMBOK/PRINCE2
- 完整的 COBIT 能力量表為 0–5（第 5 級：量化管理的最佳化）；本平台採用與所有其他評鑑模組一致的 0–4 量表
- 取代 COBIT 5（2012）；主要變更包括設計因素、焦點領域，以及與 NIST CSF 2.0 概念的對齊

---

### NIST SP 800-53 Rev. 5

**來源：** NIST Special Publication 800-53 Revision 5 —— Security and Privacy Controls for Information Systems and Organizations（2020 年 9 月）
**範圍：** 20 個控制措施家族，涵蓋聯邦資訊系統完整的安全與隱私控制措施目錄。家族包括存取控制（AC）、稽核與問責（AU）、組態管理（CM）、識別與驗證（IA）、事件應變（IR）、系統與通訊保護（SC）等。
**評分：** 成熟度等級 0–4（未實施 → 初始 → 已管理 → 已定義 → 最佳化）
**適用對象：** FISMA 要求的美國聯邦機關與承包商；尋求 FedRAMP 授權的組織；任何想要一套完整、以基線驅動的控制措施框架的產業。已與 ISO 27001:2022 附錄 A 交叉參照。

**涵蓋範圍說明：**
- 控制措施家族可直接對應 ISO 27001:2022 附錄 A 的領域 —— 平台上將 474+ 項個別控制措施濃縮為 20 個計分家族
- NIST SP 800-53 Rev. 5 首次整合隱私控制措施（先前在 800-53A 中另立）
- Crosswalk Viewer 提供 ISO 27001:2022 ↔ NIST SP 800-53 Rev. 5 對照
- 基線裁剪（Low/Moderate/High）未自動化 —— 平台對全部 20 個家族一律計分

---

### CSA Cloud Controls Matrix v4.1

**來源：** Cloud Security Alliance —— Cloud Controls Matrix v4.1（2023 年 3 月）
**範圍：** 17 個安全領域共 207 項控制措施規格：應用與介面安全（AIS）、稽核保證與合規（AAC）、營運持續管理與營運韌性（BCR）、變更控制與組態管理（CCC）、密碼學、加密與金鑰管理（CEK）、資料中心安全（DCS）、資料安全與隱私生命週期管理（DSP）、治理、風險與合規（GRC）、人力資源（HRS）、身分與存取管理（IAM）、基礎設施與虛擬化安全（IVS）、互通性與可攜性（IPY）、日誌與監控（LOG）、安全事件管理、電子蒐證與雲端鑑識（SEF）、供應鏈管理、透明度與問責（STA）、威脅與弱點管理（TVM）、通用端點管理（UEM）。
**評分：** 成熟度等級 0–4
**適用對象：** 尋求 CSA STAR 認證的雲端服務供應商；執行供應商盡職調查的雲端消費者；採多雲或混合環境的組織。

**涵蓋範圍說明：**
- CCM v4.1 是權威的雲端安全控制措施框架 —— 對齊 ISO/IEC 27001、ISO/IEC 27017、ISO/IEC 27018、NIST SP 800-53、CIS Controls v8 與 GDPR
- CSA STAR（Security, Trust, Assurance, and Risk）第 1 級採用 CCM 自我評鑑；第 2 級採用第三方稽核
- ISO 27018:2025（雲端產品）與 CCM v4.1 互補 —— CCM 範圍較廣；ISO 27018 專注於 PII 保護

---

### CSA AI Controls Matrix v1.1

**來源：** Cloud Security Alliance —— AI Controls Matrix (AICM) v1.1
**範圍：** 18 個領域共 247 項控制措施，包括：AI 治理與問責（AGA）、資料管理與隱私（DMP）、模型開發與驗證（MDV）、安全與韌性（SAR）、透明度與可解釋性（TEX）、人為監督與控制（HOC）、法規合規與法律（RCL），以及涵蓋 AI 風險管理、倫理、營運、供應鏈、事件應變等的另外 11 個領域。
**評分：** 成熟度等級 0–4
**適用對象：** 開發、部署或採購 AI 系統的組織；AI 治理團隊；提供 AI／ML 服務的雲端供應商；負責 EU AI Act 或 ISO 42001 合規的團隊。

**涵蓋範圍說明：**
- AICM 設計為 CCM v4.1 的配套 —— 專注於 AI 系統安全與治理
- 對齊 EU AI Act、ISO/IEC 42001:2023、NIST AI RMF 1.0 與 OECD AI 原則
- ISO 42001（AI 產品）與 AICM 互補 —— ISO 42001 是管理制度標準；AICM 提供詳細的技術控制措施
- 與平台的 ISO 42001 對照對應（NIST AI RMF：32、EU AI Act：31、OECD AI：14）併用尤其有用

---

### NCSC CAF v4.0 (UK)

**來源：** 英國國家網路安全中心（NCSC）—— Cyber Assessment Framework v4.0（2024）
**範圍：** 14 項原則與 4 項目標（A：管理安全風險、B：防範網路攻擊、C：偵測網路安全事件、D：降低事件衝擊）共 41 項貢獻成果（Contributing Outcomes）。
**評分：** 多數成果採三欄模型：未達成（0）／部分達成（2）／已達成（4）。九項成果採兩欄模型（僅未達成／已達成）。
**適用對象：** 英國基本服務營運者（能源、運輸、醫療、水、數位基礎設施）、相關數位服務供應商、受 UK NIS Regulations 2018 約束的公部門機關。

**涵蓋範圍說明：**
- CAF v4.0（2024）新增目標 D（降低衝擊），並重整 v3.1 的多項成果 —— 平台僅實作 v4.0
- Crosswalk Viewer 提供 65 項 ISO 27001:2022 對照對應（ISO27001_2022 → NCSC_CAF 軸）
- 同時受 NIS 法規與 CAF 約束的組織宜同時維護兩個模組 —— NIS 提供法律基線，CAF 提供技術評鑑方法

---

### ReCyF v2.5 — France NIS2 (ANSSI)

**來源：** ANSSI —— Agence nationale de la sécurité des systèmes d'information。Référentiel de Cybersécurité France v2.5（2026/03/17）。
**範圍：** 20 項安全目標（OS-01 至 OS-20），分屬 4 大支柱：Gouvernance、Protection、Défense、Résilience。152 項要求（Moyens acceptables de conformité）。OS-01–15 同時適用於 Entités Importantes（EI）與 Entités Essentielles（EE）。OS-16–20 僅適用於 EE。
**評分：** 成熟度等級 0–4
**適用對象：** 受 NIS2 轉換法約束的法國組織：由 ANSSI 依法國尚待通過的 NIS2 轉換法（PJL 第 14 條 —— 撰寫時尚未立法）分類的 Entités Importantes（EI）與 Entités Essentielles（EE）。涵蓋所有 NIS2 產業：énergie、transport、santé、eau、infrastructures numériques、services numériques、administrations publiques。

**涵蓋範圍說明：**
- ANSSI 工作文件 2.5 版（2026/03/17）—— 最終採用前仍可能修訂
- Crosswalk Viewer 提供 50 項 ISO 27001:2022 對照對應（ISO27001_2022 → FR_NIS2_RECYF 軸）
- 僅適用 EE 的目標（OS-16 至 OS-20）已納入評鑑並清楚標示；僅屬 EI 的組織得將其用作期望目標
- 評鑑介面全程使用 ANSSI 官方法文術語

---

### BSI C5:2026

**來源：** Bundesamt für Sicherheit in der Informationstechnik —— Cloud Computing Compliance Criteria Catalogue (C5:2026)，v1.0.1，2026 年 4 月 7 日發布。取代 C5:2020。
**範圍：** 17 個領域共 168 項準則：資訊安全組織（OIS）、安全政策與程序（SP）、人員（HR）、資產管理（AM）、實體安全（PS）、營運（OPS）、身分與存取管理（IAM）、密碼學與金鑰管理（CRY）、通訊安全（COS）、可攜性與互通性（PI）、採購／開發／修改（DEV）、服務供應商與供應商控制（SSO）、安全事件管理（SIM）、營運持續管理（BCM）、合規（COM）、處理政府機關調查請求（INQ）、產品安全與保安（PSS）。
**評分：** 成熟度等級 0–4
**適用對象：** 尋求 BSI C5 查核證明（Type 1 或 Type 2）的雲端服務供應商（CSP）；在德國與歐盟執行供應商盡職調查的雲端客戶；公部門採購；有雲端相依性且受 NIS2 或 KRITIS 約束的組織。

**結構說明：**
- 每項準則都有分類為下列類型的子準則：**Basic**（強制門檻）、**Additional-Sharpening**（提高既有要求的水準）與 **Additional-Complementing**（擴大範圍）。平台在 168 項頂層準則層級進行評鑑 —— 子準則僅供敘述參考，不個別計分。
- OIS-01 要求符合 ISO/IEC 27001 的 ISMS —— 因此 C5:2026 是 ISO 27001 之上的雲端專屬延伸層，而非獨立的替代方案。
- 領域 PI（可攜性與互通性）是 C5:2026 新增 —— C5:2020 沒有。

**涵蓋範圍說明：**
- 依 BSI 官方機器可讀 XLSX（`C5_2026_editable_en.xlsx`，隨標準發布）
- 包含完整英文準則文字；德文原文可於 bsi.bund.de 取得
- 正式 C5 查核證明需與合格的 C5 稽核員往來；本模組支援內部就緒狀態評鑑

---

### BSI C3A — Criteria enabling Cloud Computing Autonomy

**來源：** Bundesamt für Sicherheit in der Informationstechnik —— Criteria enabling Cloud Computing Autonomy (C3A)，v1.0，2026 年 4 月 27 日發布。
**範圍：** 6 個主權（SOV）領域共 30 個準則群組：SOV-1 策略主權、SOV-2 法律與管轄主權、SOV-3 資料主權、SOV-4 營運主權、SOV-5 供應鏈主權、SOV-6 技術主權。
**評分：** 成熟度等級 0–4
**適用對象：** 展現主權能力的雲端服務供應商；評估供應商自主性的雲端服務客戶（政府、KRITIS 營運者、受監管實體）；依數位主權要求的歐盟公部門採購。

**先決條件：** C3A 以雲端服務供應商符合 BSI C5:2026 準則為前提 —— C5 涵蓋 C3A 所立基的安全基礎（SOV-7 安全與合規）。兩個模組在平台上皆可使用，並可一起評鑑。

**領域結構：**
- **SOV-1 策略主權（4 個群組）：** 管轄權、註冊辦事處、CSP 有效控制、CSP 控制權變更通知（90 天前通知）
- **SOV-2 法律與管轄主權（3 個群組）：** 域外曝險（年度非歐盟法律檢視）、稽核權（本國／德國主管機關存取）、國防狀態接管
- **SOV-3 資料主權（5 個群組）：** 資料存放地（EU／DE 選項）、外部金鑰管理（IaaS/PaaS/SaaS 的 BYOK）、外部身分提供者、日誌與監控（即時 API 存取）、用戶端加密
- **SOV-4 營運主權（10 個群組）：** 操作人員（EU／DE 居留）、遠端工作（EU／DE 存取路徑）、備援連線、SOC（EU／DE 營運）、入口資料控制、更新威脅分析、資料交換監控、資料交換閘道、斷線（每年測試）、復線（90 天復原）
- **SOV-5 供應鏈主權（5 個群組）：** 軟體相依性（依 BSI TR-03183-2 的 SBOM）、硬體相依性、外部服務相依性、出口限制管理、容量管理（EU／DE）
- **SOV-6 技術主權（3 個群組）：** 原始碼可取用性（EU 備份，最舊不超過 24 小時，至少 5 個版本）、持續服務交付（應變策略）、軟體開發（獨立工具鏈存取）

**涵蓋範圍說明：**
- EU Cloud Sovereignty Framework 的 SOV-7（安全與合規）與 SOV-8（環境永續）刻意不涵蓋 —— SOV-7 由 C5:2026 處理，SOV-8 不在 BSI 的範圍內
- 準則變體（C1/C2 = EU 與德國層級；AC = 附加準則）記載於準則群組說明中；平台在準則群組層級計分
- 依官方 PDF（C3A_Cloud_Computing_Autonomy.pdf，BSI，2026 年 4 月）

---

### PCI DSS v4.0.1

**來源：** PCI Security Standards Council —— Payment Card Industry Data Security Standard，v4.0.1，2024 年 6 月發布。
**範圍：** 323 項子要求，歸為 12 項頂層要求，依 6 個優先實施里程碑編排：(1) 移除敏感的驗證資料並限制資料留存、(2) 保護系統與網路並為資料外洩應變做好準備、(3) 保護支付卡應用程式、(4) 監控並控制對系統的存取、(5) 保護儲存的持卡人資料、(6) 完成其餘合規工作並確保所有控制措施到位。
**評分：** 以里程碑為基礎的進度追蹤；子要求個別評鑑，並在平台介面中依里程碑分組。
**適用對象：** 儲存、處理或傳輸持卡人資料的任何組織 —— 特約商店、服務供應商、支付處理機構。

**涵蓋範圍說明：**
- v4.0.1（2024 年 6 月）是 v4.0 的小幅更正版；ISMS CORE 全程實作 v4.0.1
- PCI DSS 正式評鑑（SAQ 或 QSA 合規報告）需由合格安全評估員進行或使用核准的 SAQ 表格 —— 本模組是就緒狀態的自我評鑑工具，不能取代正式認證
- ISO 27001 ↔ PCI DSS 4.0 對照：39 項對應，在存取控制、密碼學、日誌與弱點管理領域有大量重疊

---

### FINMA

**來源：** FINMA —— 瑞士金融市場監督管理局。涵蓋通函 2023/1「Operational Risks and Resilience — Banks」（2024 年 1 月 1 日生效，韌性條款自 2026 年 1 月 1 日起全面拘束）、通函 2018/3「Outsourcing — Banks and Insurance Companies」（2020 年修訂，仍現行有效），以及指引 03/2024「Cyber Risks」。
**範圍：** 3 個來源共 21 項要求：通函 2023/1（7 項要求 —— 營運風險管理、ICT 風險管理、網路風險管理、關鍵資料風險管理、營運持續管理、跨境服務風險、營運韌性）、通函 2018/3（9 項要求 —— 委外清冊、選擇／監控、集團內委外、保留責任、安全、稽核權、跨境委外、合約要求）、指引 03/2024（5 項要求 —— 治理、保護措施、偵測／應變／復原、24 小時向 FINMA 通報、網路演練）。
**評分：** 成熟度等級 0–4
**適用對象：** 瑞士銀行、保險公司及其他受 FINMA 監管的金融機構。

**結構說明：**
- 每項要求都可追溯至通函的官方邊註編號（Rz）—— 瑞士監理人員審查時直接引用的段落參照
- 在評鑑檢視中，要求依來源通函分組，而非攤平為單一清單
- 涵蓋行為義務（2025/2）、流動性（2025/3）、合併監理（2025/4）與氣候相關金融風險（2026/1）的新通函不在 ICT／安全評鑑範圍內，未納入。

**涵蓋範圍說明：**
- FINMA 明確將通函 2023/1 校準為適用於旗下有歐盟集團子公司並行實施 DORA 的機構 —— 營運韌性、ICT 風險框架、事件管理、第三方風險與網路演練（TLPT）大量重疊
- ISO 27001 對照：60 項對應。另提供 ISO 27018 與 ISO 27701 的對照對應，涵蓋雲端 PII 與隱私相關的 FINMA 義務（委外、資料位置、關鍵資料風險）
- 本模組是合規就緒狀態的自我評鑑 —— 不取代 FINMA 本身的監理審查或持照稽核

---

### 自訂框架（YAML 匯入）

透過 YAML 上傳任何自訂、特定產業或專有的控制措施框架。匯入後，平台會透過 `iso_mappings` 欄位將每項控制措施對應至 ISO 27001:2022，並在 Coverage 頁面顯示推定的涵蓋範圍。

**YAML 格式：**
```yaml
name: "My Framework"
short_code: "MY_FW"
version: "1.0"
description: "Optional"
controls:
  - id: "MY.1.1"
    title: "Control title"
    category: "Access Control"
    iso_mappings: ["A.5.15", "A.8.2"]
    tags: ["identity"]
```

**每項控制措施的關鍵欄位：** `id`（必填）、`title`（必填）、`category`、`subcategory`、`priority`（HIGH/MEDIUM/LOW）、`iso_mappings`（ISO 27001:2022 附錄 A 參照的清單）、`tags`。

**涵蓋範圍顯示：** 匯入後，Coverage 頁面的 Mapping Matrix 分頁會顯示自訂框架涵蓋範圍區塊，包含百分比、進度條與各控制措施明細。

**僅限管理員：** 匯入與刪除需要 admin 或 super_admin 角色。

---

## 對照表整合

所有合規評鑑模組都受惠於 Platform 的 Crosswalk Viewer，其顯示下列跨框架對應：

- ISO 27001:2022 ↔ NIST CSF 2.0
- NIST AI RMF 1.0 ↔ ISO 27001:2022（56 項對應）以及 ↔ ISO 42001:2023（32 項對應）—— 沒有 NIST AI RMF ↔ EU AI Act 的直接軸；透過 ISO 42001 間接連結（對 EU AI Act 有 31 項對應）
- ISO 27001:2022 ↔ NIST SP 800-53 Rev. 5
- ISO 27001:2022 ↔ MITRE ATT&CK v19
- ISO 27001:2022 ↔ DORA
- ISO 27001:2022 ↔ NIS2
- ISO 27001:2022 ↔ CIS Controls v8
- ISO 27001:2022 ↔ BSI IT-Grundschutz（386 項對應）
- ISO 27701:2025 ↔ BSI IT-Grundschutz（101 項對應）
- ISO 27018:2025 ↔ BSI IT-Grundschutz（51 項對應）
- ISO 27001:2022 ↔ CyberFundamentals BE（107 項對應）
- ISO 27001:2022 ↔ BaFin BAIT DE（69 項對應）
- ISO 27001:2022 ↔ CSSF 20-750 LU（47 項對應）
- ISO 27001:2022 ↔ ACN Guidelines IT（43 項對應）
- ISO 27001:2022 ↔ UK NIS Regulations（51 項對應）
- ISO 27001:2022 ↔ UK Operational Resilience（34 項對應）
- ISO 27001:2022 ↔ NCSC CAF v4.0（65 項對應）
- ISO 27001:2022 ↔ ReCyF v2.5 / FR NIS2（50 項對應）
- ISO 27017:2026 ↔ CSA CCM v4.1（11）、NIST CSF 2.0（9）、FINMA（7）、ISO 27001:2022（4）、DORA（4）、NIS2（2）—— 為 4 項 CLD 前置詞獨立控制措施（5.38、5.39、8.35、8.36）精選的對應；沒有 Swiss nDSG 軸，因為這些控制措施不含 PII 內容

合計：Crosswalk Viewer 提供 **59 個軸共 4,671 個對照物件**。

---

## 限制與免責聲明

**所有合規評鑑模組：**
- 為供內部就緒狀態評估的自我評鑑工具
- 不構成法律意見或法規見解
- 在強制評鑑適用之處，不取代與主管機關、公告機構或認可稽核員的往來
- 涵蓋相關法規／標準發布日當時的要求 —— 法規更新（授權法案、RTS、ITS、實施決定）可能新增此處尚未反映的義務

**特定事項：** CSRM 基線要求與 BACS 限制說明係依 2025 年公開的 NCSC 文件。TISAX 標籤需經 ENX 認可的評鑑。CIS Controls 防護措施文字係依 CIS v8（2021）。BSI IT-Grundschutz 完整要求文字可自 bsi.bund.de 取得。

---

*[ISMS CORE Project](README.zh-TW.md) 的一部分 —— ISO 27001 · ISO 27701 · ISO 27017 · ISO 27018 · ISO 42001* · [合規詳情請見 isms-core.com/compliance.html](https://isms-core.com/frameworks)
