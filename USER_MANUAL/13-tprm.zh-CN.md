# 第三方风险管理（TPRM）

<p align="center"><a href="13-tprm.md">English</a> · <a href="13-tprm.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<!-- ISMS-CORE:USER-MANUAL:13-tprm:v1.0:2026-04-16 -->

---

## 概览

**TPRM** 模块依 ISO 27001:2022 控制措施 A.5.19（供应商关系中的信息安全）至 A.5.22（供应商服务的监控与审查），管理第三方与供应商风险。它包含专为金融业组织设计的 DORA ICT 第三方风险字段。

在侧边栏前往 **Risk & Operations → TPRM**。

---

## 供应商登记册

供应商登记册是所有可访问您信息资产或提供 ICT 服务的供应商、第三方服务供应商与业务伙伴的目录。

### 新增供应商

1. 按一下 **New Vendor**
2. 填写供应商表单：

| 字段 | 描述 |
|-------|-------------|
| **Vendor name** | 法定或交易名称 |
| **Category** | Software / Cloud / Outsourcing / Professional Services / Hardware / Other |
| **Criticality** | Critical / High / Medium / Low —— 您对该供应商重要性的评估 |
| **Services provided** | 该供应商为您的组织做什么 |
| **Data access** | 该供应商是否可访问个人数据？机密数据？ |
| **Contract owner** | 供应商关系的内部拥有者 |
| **Review date** | 下次排定的供应商审查 |

### DORA ICT 字段

针对受 DORA 规范的金融业组织，每笔供应商记录上另有额外字段：

| 字段 | 描述 |
|-------|-------------|
| **ICT service type** | Software-as-a-Service / Infrastructure / Platform / Data analytics / Other ICT |
| **ICT provider entity type** | DORA 第 3 条所定义的供应商类型（credit institution、payment institution 等） |
| **Substitutability** | Easy / Medium / Difficult / Impossible —— 此供应商的可替换程度为何？ |
| **Systemic relevance** | 此供应商是否具系统性相关（可能造成全市场影响）？ |
| **Contract reference** | ICT 服务合同的参照 |

DORA 登记册检视（见下文）会汇总所有已填写 DORA 字段的供应商，并计算您的 ICT 集中度风险轮廓。

---

## 供应商评估

针对每一供应商，记录定期的安全评估：

1. 开启供应商记录并前往 **Assessments** 分页
2. 按一下 **New Assessment**
3. 记录：
   - 评估日期
   - 评估类型（questionnaire / on-site / remote / certification review）
   - 评估人员（internal 或 external）
   - 整体评等（Satisfactory / Needs Improvement / Unsatisfactory）
   - 主要发现事项与必要行动
   - 下次评审日期

评估历程会永久保留 —— 向审计人员展示多个时间点的评估周期，可证明 A.5.22 下持续进行的供应商监控。

---

## 合同追踪

针对每一供应商，追踪相关的合同：

1. 开启供应商记录并前往 **Contracts** 分页
2. 按一下 **New Contract**
3. 记录：
   - 合同参照编号
   - 开始与到期日期
   - 自动续约条款（yes / no）
   - 通知期间（天）
   - 主要义务（数据保护条款、审计权、SLA）
   - 合同拥有者

即将到期的合同会被醒目提示，且若跨越到期门槛，可触发健康状态通知横幅。

---

## DORA ICT 登记册检视

前往 **TPRM → DORA Register**，查看 DORA 第 28 条所要求之所有 ICT 第三方关系的专属检视。

此检视显示：

- 所有已填写 ICT 服务类型的供应商
- 可替代性分布（DORA 集中度风险指标）
- 被标记为系统性相关的供应商
- 合同将于 90 天内到期的供应商

DORA 登记册可导出为 XLSX，以便必要时提交给您的主管机关。

---

## TPRM 与缺口管理

若供应商评估发现安全缺陷，可直接从供应商评估检视建立一项缺口。该缺口会连结至供应商记录，以及相关的 ISO 控制措施群组（A.5.19–A.5.22），以实现完整可追溯性。

---

## TPRM 导出

将供应商登记册与评估历程导出为：

- **CSV** —— 所有供应商记录与 DORA 字段
- **XLSX** —— 含评估状态与合同到期日的格式化供应商登记册

<!-- QA_VERIFIED: 2026-04-16 -->
