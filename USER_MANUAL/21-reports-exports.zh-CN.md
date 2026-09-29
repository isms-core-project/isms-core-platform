# 报告与导出

<p align="center"><a href="21-reports-exports.md">English</a> · <a href="21-reports-exports.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<!-- ISMS-CORE:USER-MANUAL:21-reports-exports:v1.0:2026-04-16 -->

---

## 概览

ISMS CORE Platform 在整个应用程序中提供导出与报告功能。本章是一份参考指南，描述各章节可导出的内容及其格式。

---

## 导出格式

| 格式 | 描述 | 最适用于 |
|--------|-------------|---------|
| **CSV** | 以逗号分隔的值——所有字段、原始数据 | 数据分析、导入其他工具 |
| **XLSX** | 以颜色标记的 Excel 试算表 | 管理评审、视觉化报告、审计人员证据 |
| **PDF** | 排版好的 A4 报告 | 正式报告、审计提交、列印 |

---

## 各章节的导出

### Compliance Assessments

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 检查表结果（单一评估） | CSV、XLSX | Assessment detail view → Export |
| 评估汇总结果 | CSV、彩色 XLSX、PDF（A4） | Assessment Collections → Export |
| NIST CSF 2.0 分数 | XLSX（NIST 模板格式）、CSV | NIST CSF 2.0 page → Export |

### Gap Management

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 缺口登记表 | CSV、XLSX | Gaps list → Export |
| 含行动计划的缺口明细 | CSV | Gap detail view → Export |

### Evidence Tracker

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 证据登记表 | CSV、XLSX | Evidence Tracker → Export |

### Risk Register

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 风险登录 | CSV、XLSX | Risk Register → Export |
| 风险热图 | PNG 影像 | Heatmap tab → Download image |

### TPRM

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 供应商登记表 | CSV、XLSX | TPRM list → Export |
| DORA ICT 登录 | XLSX | TPRM → DORA Register → Export |

### EBIOS RM

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 完整 EBIOS RM 研究（全部 5 个工作坊） | PDF（A4） | EBIOS RM summary view → Export PDF |

### BIA

| 项目 | 格式 | 位置 |
|------|--------|-------|
| BIA 登记表 | CSV、XLSX | BIA list → Export |

### KPI Dashboard

| 项目 | 格式 | 位置 |
|------|--------|-------|
| KPI 趋势（选取的日期范围） | XLSX、PDF | KPI Dashboard → Export |

### Threat Intelligence

| 项目 | 格式 | 位置 |
|------|--------|-------|
| KEV 审计报告（A.8.8 证据） | CSV | Intelligence → KEV Audit → Export |
| CVE 搜寻结果 | CSV | CVE Explorer → Export results |

### System Event Log

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 完整事件日志（日期范围） | CSV | Admin → System → Event Log → Export |

### Cross-Framework Mapping

| 项目 | 格式 | 位置 |
|------|--------|-------|
| 跨框架对应表 | CSV | Crosswalk Viewer → Export |
| 推断涵盖范围报告 | CSV、PDF | Inferred Coverage tab → Export |

---

## 审计证据包——建议导出项目

在准备 ISO 27001 第 2 阶段或监督审计时，下列导出项目可提供完整的证据包：

| 文件 | 导出 | 章节 |
|----------|--------|---------|
| 评估检查表结果 | 彩色 XLSX | Compliance Assessments |
| 评估汇总摘要 | PDF | Assessment Collections |
| 缺口登记表（已结案 + 未结） | XLSX | Gap Management |
| 风险登录 | XLSX | Risk Register |
| 证据登记表 | XLSX | Evidence Tracker |
| KEV 审计报告 | CSV | Threat Intelligence |
| QA Engine 结果 | 萤幕截图／萤幕显示 | QA Engine |
| NIST CSF 2.0 设置档 | XLSX | NIST CSF 2.0 |
| KPI 趋势报告 | PDF | KPI Dashboard |
| 事件日志（审计期间） | CSV | Admin → System |

---

## PDF 产生注意事项

PDF 导出采用 A4 格式。它们在服务器端产生，并针对列印排版——不需要使用浏览器的列印功能。

对于 EBIOS RM 与评估汇总的 PDF，平台使用包含下列内容的结构化模板：
- 封面（文件标题、组织名称、日期）
- 目录
- 章节内容
- 含原始数据的附录

大型汇总集（超过 100 个项目）可能需要 15–30 秒产生。

---

## Pandoc 导出（进阶）

您项目中的政策与实施文件以 Markdown 储存，若您需要自定义的 PDF 格式，可导出后交由 Pandoc 处理。请从文件详细检视下载原始 Markdown（Source mode → Copy / Download）。

若要使用 Pandoc 产生排版好的 PDF：
```bash
pandoc policy.md \
  -o Policy_Document.pdf \
  --pdf-engine=xelatex \
  --toc \
  --number-sections \
  -V geometry:margin=2cm \
  -V fontsize=11pt
```

这会产生编号章节、目录与专业排版——适合用来从平台内容产出可直接交付给客户的政策文件。

<!-- QA_VERIFIED: 2026-04-16 -->
