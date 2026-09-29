# 報告與匯出

<p align="center"><a href="21-reports-exports.md">English</a> · <strong>繁體中文</strong> · <a href="21-reports-exports.zh-CN.md">简体中文</a></p>

<!-- ISMS-CORE:USER-MANUAL:21-reports-exports:v1.0:2026-04-16 -->

---

## 概觀

ISMS CORE Platform 在整個應用程式中提供匯出與報告功能。本章是一份參考指南，說明各章節可匯出的內容及其格式。

---

## 匯出格式

| 格式 | 說明 | 最適用於 |
|--------|-------------|---------|
| **CSV** | 以逗號分隔的值——所有欄位、原始資料 | 資料分析、匯入其他工具 |
| **XLSX** | 以顏色標示的 Excel 試算表 | 管理審查、視覺化報告、稽核人員證據 |
| **PDF** | 排版好的 A4 報告 | 正式報告、稽核提交、列印 |

---

## 各章節的匯出

### Compliance Assessments

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 檢核表結果（單一評鑑） | CSV、XLSX | Assessment detail view → Export |
| 評鑑彙總結果 | CSV、彩色 XLSX、PDF（A4） | Assessment Collections → Export |
| NIST CSF 2.0 分數 | XLSX（NIST 範本格式）、CSV | NIST CSF 2.0 page → Export |

### Gap Management

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 缺口登記表 | CSV、XLSX | Gaps list → Export |
| 含行動計畫的缺口明細 | CSV | Gap detail view → Export |

### Evidence Tracker

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 證據登記表 | CSV、XLSX | Evidence Tracker → Export |

### Risk Register

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 風險登錄 | CSV、XLSX | Risk Register → Export |
| 風險熱圖 | PNG 影像 | Heatmap tab → Download image |

### TPRM

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 供應商登記表 | CSV、XLSX | TPRM list → Export |
| DORA ICT 登錄 | XLSX | TPRM → DORA Register → Export |

### EBIOS RM

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 完整 EBIOS RM 研究（全部 5 個工作坊） | PDF（A4） | EBIOS RM summary view → Export PDF |

### BIA

| 項目 | 格式 | 位置 |
|------|--------|-------|
| BIA 登記表 | CSV、XLSX | BIA list → Export |

### KPI Dashboard

| 項目 | 格式 | 位置 |
|------|--------|-------|
| KPI 趨勢（選取的日期範圍） | XLSX、PDF | KPI Dashboard → Export |

### Threat Intelligence

| 項目 | 格式 | 位置 |
|------|--------|-------|
| KEV 稽核報告（A.8.8 證據） | CSV | Intelligence → KEV Audit → Export |
| CVE 搜尋結果 | CSV | CVE Explorer → Export results |

### System Event Log

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 完整事件日誌（日期範圍） | CSV | Admin → System → Event Log → Export |

### Cross-Framework Mapping

| 項目 | 格式 | 位置 |
|------|--------|-------|
| 跨框架對應表 | CSV | Crosswalk Viewer → Export |
| 推斷涵蓋範圍報告 | CSV、PDF | Inferred Coverage tab → Export |

---

## 稽核證據包——建議匯出項目

在準備 ISO 27001 第 2 階段或監督稽核時，下列匯出項目可提供完整的證據包：

| 文件 | 匯出 | 章節 |
|----------|--------|---------|
| 評鑑檢核表結果 | 彩色 XLSX | Compliance Assessments |
| 評鑑彙總摘要 | PDF | Assessment Collections |
| 缺口登記表（已結案 + 未結） | XLSX | Gap Management |
| 風險登錄 | XLSX | Risk Register |
| 證據登記表 | XLSX | Evidence Tracker |
| KEV 稽核報告 | CSV | Threat Intelligence |
| QA Engine 結果 | 螢幕截圖／螢幕顯示 | QA Engine |
| NIST CSF 2.0 設定檔 | XLSX | NIST CSF 2.0 |
| KPI 趨勢報告 | PDF | KPI Dashboard |
| 事件日誌（稽核期間） | CSV | Admin → System |

---

## PDF 產生注意事項

PDF 匯出採用 A4 格式。它們在伺服器端產生，並針對列印排版——不需要使用瀏覽器的列印功能。

對於 EBIOS RM 與評鑑彙總的 PDF，平台使用包含下列內容的結構化範本：
- 封面（文件標題、組織名稱、日期）
- 目錄
- 章節內容
- 含原始資料的附錄

大型彙總集（超過 100 個項目）可能需要 15–30 秒產生。

---

## Pandoc 匯出（進階）

您專案中的政策與實施文件以 Markdown 儲存，若您需要自訂的 PDF 格式，可匯出後交由 Pandoc 處理。請從文件詳細檢視下載原始 Markdown（Source mode → Copy / Download）。

若要使用 Pandoc 產生排版好的 PDF：
```bash
pandoc policy.md \
  -o Policy_Document.pdf \
  --pdf-engine=xelatex \
  --toc \
  --number-sections \
  -V geometry:margin=2cm \
  -V fontsize=11pt
```

這會產生編號章節、目錄與專業排版——適合用來從平台內容產出可直接交付給客戶的政策文件。

<!-- QA_VERIFIED: 2026-04-16 -->
