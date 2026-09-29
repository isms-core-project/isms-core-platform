# 第三方風險管理（TPRM）

<p align="center"><a href="13-tprm.md">English</a> · <strong>繁體中文</strong> · <a href="13-tprm.zh-CN.md">简体中文</a></p>

<!-- ISMS-CORE:USER-MANUAL:13-tprm:v1.0:2026-04-16 -->

---

## 概觀

**TPRM** 模組依 ISO 27001:2022 控制措施 A.5.19（供應商關係中的資訊安全）至 A.5.22（供應商服務的監控與審查），管理第三方與供應商風險。它包含專為金融業組織設計的 DORA ICT 第三方風險欄位。

在側邊欄前往 **Risk & Operations → TPRM**。

---

## 供應商登記冊

供應商登記冊是所有可存取您資訊資產或提供 ICT 服務的供應商、第三方服務供應商與業務夥伴的目錄。

### 新增供應商

1. 按一下 **New Vendor**
2. 填寫供應商表單：

| 欄位 | 說明 |
|-------|-------------|
| **Vendor name** | 法定或交易名稱 |
| **Category** | Software / Cloud / Outsourcing / Professional Services / Hardware / Other |
| **Criticality** | Critical / High / Medium / Low —— 您對該供應商重要性的評估 |
| **Services provided** | 該供應商為您的組織做什麼 |
| **Data access** | 該供應商是否可存取個人資料？機密資料？ |
| **Contract owner** | 供應商關係的內部擁有者 |
| **Review date** | 下次排定的供應商審查 |

### DORA ICT 欄位

針對受 DORA 規範的金融業組織，每筆供應商記錄上另有額外欄位：

| 欄位 | 說明 |
|-------|-------------|
| **ICT service type** | Software-as-a-Service / Infrastructure / Platform / Data analytics / Other ICT |
| **ICT provider entity type** | DORA 第 3 條所定義的供應商類型（credit institution、payment institution 等） |
| **Substitutability** | Easy / Medium / Difficult / Impossible —— 此供應商的可替換程度為何？ |
| **Systemic relevance** | 此供應商是否具系統性相關（可能造成全市場衝擊）？ |
| **Contract reference** | ICT 服務合約的參照 |

DORA 登記冊檢視（見下文）會彙總所有已填寫 DORA 欄位的供應商，並計算您的 ICT 集中度風險輪廓。

---

## 供應商評鑑

針對每一供應商，記錄定期的安全評鑑：

1. 開啟供應商記錄並前往 **Assessments** 分頁
2. 按一下 **New Assessment**
3. 記錄：
   - 評鑑日期
   - 評鑑類型（questionnaire / on-site / remote / certification review）
   - 評鑑人員（internal 或 external）
   - 整體評等（Satisfactory / Needs Improvement / Unsatisfactory）
   - 主要發現事項與必要行動
   - 下次審查日期

評鑑歷程會永久保留 —— 向稽核人員展示多個時間點的評鑑週期，可證明 A.5.22 下持續進行的供應商監控。

---

## 合約追蹤

針對每一供應商，追蹤相關的合約：

1. 開啟供應商記錄並前往 **Contracts** 分頁
2. 按一下 **New Contract**
3. 記錄：
   - 合約參照編號
   - 開始與到期日期
   - 自動續約條款（yes / no）
   - 通知期間（天）
   - 主要義務（資料保護條款、稽核權、SLA）
   - 合約擁有者

即將到期的合約會被醒目提示，且若跨越到期門檻，可觸發健康狀態通知橫幅。

---

## DORA ICT 登記冊檢視

前往 **TPRM → DORA Register**，查看 DORA 第 28 條所要求之所有 ICT 第三方關係的專屬檢視。

此檢視顯示：

- 所有已填寫 ICT 服務類型的供應商
- 可替代性分布（DORA 集中度風險指標）
- 被標示為系統性相關的供應商
- 合約將於 90 天內到期的供應商

DORA 登記冊可匯出為 XLSX，以便必要時提交給您的主管機關。

---

## TPRM 與缺口管理

若供應商評鑑發現安全缺陷，可直接從供應商評鑑檢視建立一項缺口。該缺口會連結至供應商記錄，以及相關的 ISO 控制措施群組（A.5.19–A.5.22），以實現完整可追溯性。

---

## TPRM 匯出

將供應商登記冊與評鑑歷程匯出為：

- **CSV** —— 所有供應商記錄與 DORA 欄位
- **XLSX** —— 含評鑑狀態與合約到期日的格式化供應商登記冊

<!-- QA_VERIFIED: 2026-04-16 -->
