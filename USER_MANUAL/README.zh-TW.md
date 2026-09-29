<p align="center">
  <img src="../screenshots/light/01_isms_core_login_light.png" width="120" alt="ISMS CORE"/>
</p>

<h1 align="center">ISMS CORE 平台 — 使用者說明書</h1>

<p align="center"><a href="README.md">English</a> · <strong>繁體中文</strong> · <a href="README.zh-CN.md">简体中文</a></p>

<p align="center">
  <strong>版本 1.1 &nbsp;·&nbsp; 適用於 ISMS 經理、稽核人員與控制措施擁有者</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-v1.1-00AA00?style=flat-square" alt="v1.1"/>
  <img src="https://img.shields.io/badge/Audience-ISMS_Manager_%7C_Auditor_%7C_Control_Owner-0066CC?style=flat-square" alt="Audience"/>
</p>

---

> 本說明書涵蓋 ISMS CORE 平台的**營運使用**——你在應用程式中每天實際進行的工作。它不是部署指南，也不是開發者指南。安裝說明請參閱 [PLATFORM.zh-TW.md](../PLATFORM.zh-TW.md)。

---

## 目錄

| # | 章節 | 涵蓋內容 |
|---|---------|----------------|
| [01](01-introduction.zh-TW.md) | 簡介 | ISMS CORE 是什麼、五項產品、平台如何融入 |
| [02](02-getting-started.zh-TW.md) | 開始使用 | 首次登入、儀表板概觀、導覽、產品切換器 |
| [03](03-control-library.zh-TW.md) | 控制措施庫 | 瀏覽控制措施、解讀評分、理解涵蓋範圍 |
| [04](04-projects-workspace.zh-TW.md) | 專案工作區 | 建立專案、新增政策、編輯文件、文件變數、SCR 檢核表 |
| [05](05-policies-documents.zh-TW.md) | 政策與文件 | 政策瀏覽器、篩選、全文搜尋、文件類型 |
| [06](06-compliance-assessments.zh-TW.md) | 合規評鑑 | ISMS／Privacy／Cloud／AI 檢核表、逐項評分 |
| [07](07-assessment-frameworks.zh-TW.md) | 評鑑框架 | 全部 29 個框架：NIS2、DORA、NIST CSF 2.0、BSI、TISAX、COBIT 等 |
| [08](08-gap-management.zh-TW.md) | 缺口管理 | 建立缺口、指派擁有者、SLA 追蹤、補救 |
| [09](09-evidence-management.zh-TW.md) | 證據管理 | 手動證據、連接器證據、到期、驗證 |
| [10](10-connectors.zh-TW.md) | 自動化證據連接器 | 連接器的功能、支援的 44 個系統、如何設定 |
| [11](11-risk-register.zh-TW.md) | 風險登錄表 | 風險情境、5×5 熱圖、處理流程、風險接受 |
| [12](12-bia.zh-TW.md) | 營運衝擊分析 | 資產、RTO/RPO/MTPD、衝擊評分、復原測試 |
| [13](13-tprm.zh-TW.md) | 第三方風險（TPRM） | 供應商登錄表、DORA ICT 欄位、評鑑、合約追蹤 |
| [14](14-ebios-rm.zh-TW.md) | EBIOS RM | 5 場工作坊方法論、預期事件、攻擊路徑、安全措施 |
| [15](15-cross-framework-mapping.zh-TW.md) | 跨框架對應 | 涵蓋矩陣、推斷對應、對照檢視器 |
| [16](16-threat-intelligence.zh-TW.md) | 威脅情報 | MITRE ATT&CK、CISA KEV、EPSS、CVE 探索器、A.8.8 KEV 稽核 |
| [17](17-isms-compass.zh-TW.md) | ISMS Compass | 對照 ISMS CORE 黃金標準的 AI 驅動缺口分析 |
| [18](18-qa-engine.zh-TW.md) | QA 引擎 | 存在性檢查器、語料庫驗證、多語言支援 |
| [19](19-kpi-dashboard.zh-TW.md) | KPI 儀表板 | 9 項具名指標、走勢圖、稽核準備度分數 |
| [20](20-organisations-users.zh-TW.md) | 組織與使用者 | RBAC 角色、MFA、組織設定、多租戶管理 |
| [21](21-reports-exports.zh-TW.md) | 報告與匯出 | 各區段提供哪些匯出及其格式 |

---

## 本說明書的對象

| 角色 | 主要章節 |
|---------|-----------------|
| **ISMS Manager** | 全部章節——這是你的日常工具 |
| **Auditor** | 03、05、06、07、09、15、18、19、21 |
| **Control Owner** | 03、04、08、09、11 |
| **CISO** | 02、06、07、11、14、19 |

---

## 關於五項產品的說明

ISMS CORE 平台把五個產品家族整合在同一屋簷下。你在多數頁面頂端都會看到產品切換器。每個產品對應一項 ISO 標準：

| 產品 | ISO 標準 | 涵蓋內容 |
|---------|-------------|----------------|
| **ISMS Framework** | ISO 27001:2022 | 54 個 ISMS 控制群組——核心 |
| **ISMS Operational** | ISO 27001:2022 | 給中小企業的輕量政策 |
| **Privacy** | ISO 27701:2025 | 21 個隱私控制群組（控管者＋處理者） |
| **Cloud** | ISO 27018:2025 | 12 個雲端 PII 控制群組 |
| **AI** | ISO 42001:2023 + ISO 42005:2025 | 12 個 AI 管理系統控制群組 |

---

<p align="center">
<strong>Copyright &copy; 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>
