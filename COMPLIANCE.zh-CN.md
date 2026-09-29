<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Compliance_Assessments-2E8B57?style=for-the-badge" alt="ISMS CORE Compliance Assessments"/>
</p>

<h1 align="center">🎋 ISMS CORE — 合规评估模块</h1>

<p align="center"><a href="COMPLIANCE.md">English</a> · <a href="COMPLIANCE.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<p align="center">
  <strong>29 个内建框架 + 自定义 YAML 导入。单一平台，不需另备工具。</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frameworks-29-2E8B57?style=flat-square" alt="29 Frameworks"/>
  <img src="https://img.shields.io/badge/Requirements-700+-0066CC?style=flat-square" alt="700+ Requirements"/>
  <img src="https://img.shields.io/badge/Export-CSV_%7C_XLSX_%7C_PDF-FF6600?style=flat-square" alt="Export"/>
  <img src="https://img.shields.io/badge/Assessment_Collections-Grouping_%26_Reports-2E7D32?style=flat-square" alt="Collections"/>
</p>

---

## 概览

ISMS CORE Platform 内建一套统一的合规评估层，涵盖欧洲、北美及全球的 29 个框架，并可透过 YAML 导入任何特定产业或专有的控制措施框架。每个模块都提供结构化自我评估、成熟度评分（适用时为 0–4 分）、缺口追踪与导出。

评估结果可归入 **评估集合** —— 具名的组合，可跨多个框架汇总状态以供报告或审计之用，并可导出 CSV、XLSX（依状态上色）与 PDF（A4）。

所有合规评估模块都位于 Platform WebUI 的 **Compliance Assessments** 侧边栏群组下。

---

## 快速参考

| 框架 | 类型 | 要求条目 | 分组 | 评分 | 适用对象 |
|-----------|------|-------------|----------|---------|----------|
| [NIST CSF 2.0](#nist-csf-20) | NIST | 106 个子分类 | 6 项功能 | Tier 1–4 | 任何产业 |
| [NIST AI RMF 1.0](#nist-ai-rmf-10-ai-100-1) | NIST | 72 个子分类 | 4 项功能（GOV/MAP/MSR/MNG） | 0–4 | AI 系统供应商与运营者 —— 任何产业 |
| [NIS2](#nis2-指令-eu-20222555) | EU 指令 | 15 项要求 | 2 条条文 | 0–4 | 欧盟关键实体／重要实体 |
| [DORA](#dora-eu-20222554) | EU 法规 | 27 条条文 | 5 大支柱 | 0–4 | 欧盟金融业 |
| [CIS Controls v8](#cis-critical-security-controls-v8) | 最佳实务 | 153 项防护措施 | 18 项控制措施 | 0–4 | 任何产业 |
| [BSI IT-Grundschutz](#bsi-it-grundschutz-kompendium) | 德国标准 | 111 个 Bausteine | 10 个层级 | 0–4 | 德国／DACH／IT-Grundschutz 认证 |
| [CSRM (NCSC CH)](#csrm-swiss-ncsc-2025) | 瑞士 NCSC | 20 项基线要求 | 5 项 CSF 功能 | 二元 | 瑞士关键基础设施 |
| [Swiss ISG (SR 128)](#swiss-isg-sr-128) | 瑞士法律 | 27 项要求 | 8 个章节 | 0–4 | 瑞士联邦机关与关键基础设施运营者 |
| [TISAX](#tisax--vda-isa-60) | VDA/ENX | 79 项要求 | 9 个领域 | 0–4 | 汽车供应链 |
| [Swiss nDSG](#swiss-ndsg-2023) | 瑞士法律 | 25 项条款 | 6 章 | 0–4 | 处理瑞士个人数据的组织 |
| [EU Cyber Resilience Act](#eu-cyber-resilience-act-20242847) | EU 法规 | 26 项要求 | 6 个群组 | 0–4 | 欧盟产品制造商 |
| [EU AI Act](#eu-ai-act-20241689) | EU 法规 | 9 条条文 | 第 III 章第 2 节 + 第 27 条 | 0–4 | 欧盟 AI 系统提供者／部署者 |
| [EU Cloud Sovereignty Framework](#eu-cloud-sovereignty-framework-v121) | EC DG DIGIT | 8 项主权目标 | 1 个群组（SEAL） | SEAL 0–4 | 欧盟机构／公部门云端采购 |
| [CyberFundamentals (BE)](#cyberfundamentals-ccb) | 比利时法规 | 41 项实务 | 6 项 CSF 功能 | 0–4 | 比利时组织／CCB 认证 |
| [BaFin BAIT (DE)](#bafin-bait-rundschreiben-102017-amended-2021) | 德国 BaFin | 23 项要求 | 12 个模块 | 0–4 | 德国金融业（银行、投资公司） |
| [CSSF Circulaire 20-750 (LU)](#cssf-circulaire-20-750-lu) | 卢森堡 CSSF | 19 项要求 | 7 个领域 | 0–4 | 卢森堡金融业 |
| [ACN Cyber Risk Management (IT)](#acn-cyber-risk-management-it) | 义大利 ACN | 43 项措施／116 项要求 | 10 项法定要素 | 0–4 | 义大利组织／关键基础设施 |
| [UK NIS Regulations](#uk-nis-regulations-2018) | 英国法律 | 13 项要求 | 3 项目标 | 0–4 | 英国网络与信息系统运营者 |
| [UK Operational Resilience (FCA/PRA)](#uk-operational-resilience-fcapra) | UK FCA/PRA | 12 项要求 | 4 项目标 | 0–4 | 英国金融业 —— 银行、保险公司、FMI |
| [COBIT 2019 (ISACA)](#cobit-2019-isaca) | ISACA EGIT | 40 项目标 | 5 个领域（EDM/APO/BAI/DSS/MEA） | 0–4 | 企业 IT 治理、审计、CISM/CISA/CGEIT 持有者 |
| [NIST SP 800-53 R5](#nist-sp-800-53-rev-5) | NIST | 20 个控制措施家族 | 3 个类别（技术／运营／管理） | 0–4 | 美国联邦机关、承包商，以及任何寻求完整安全控制措施的组织 |
| [CSA CCM v4.1](#csa-cloud-controls-matrix-v41) | CSA | 207 项控制措施规格 | 17 个领域 | 0–4 | 云服务提供商、云端消费者 —— 任何产业 |
| [CSA AICM v1.1](#csa-ai-controls-matrix-v11) | CSA | 247 项控制措施 | 18 个领域 | 0–4 | 开发、部署或采购 AI 系统的组织 |
| [NCSC CAF v4.0 (UK)](#ncsc-caf-v40-uk) | NCSC UK | 41 项贡献成果 | 14 项原则／4 项目标 | 0/2/4 | 英国基本服务运营者／CNI |
| [ReCyF v2.5 — France NIS2](#recyf-v25--france-nis2-anssi) | ANSSI | 20 项安全目标 | 4 大支柱 | 0–4 | 法国 NIS2 实体（EI 与 EE）—— 转换法待通过 |
| [BSI C5:2026](#bsi-c52026) | BSI（德国） | 168 项准则 | 17 个领域 | 0–4 | 寻求 C5 查核证明的云服务提供商（DE／EU） |
| [BSI C3A](#bsi-c3a--criteria-enabling-cloud-computing-autonomy) | BSI（德国） | 30 个准则群组 | 6 个 SOV 领域 | 0–4 | 评估云端主权的云端 CSP 与客户 |
| [PCI DSS v4.0.1](#pci-dss-v401) | PCI SSC | 323 项子要求 | 12 项要求／6 个里程碑 | 里程碑 | 处理持卡人数据的组织 |
| [FINMA](#finma) | 瑞士监管机关 | 21 项要求 | 3 份通函／指南 | 0–4 | 瑞士金融机构（银行、保险公司） |
| [Custom (YAML)](#自定义框架yaml-导入) | 用户自定义 | 用户自定义 | 用户自定义 | 用户自定义 | 所有 |

---

## 成熟度量表（多数框架采用）

| 分数 | 标签 | 含义 |
|-------|-------|---------|
| 0 | 不符合 | 尚未实施 |
| 1 | 部分符合 | 临时为之或不完整 |
| 2 | 发展中 | 已有文件但作法不一致 |
| 3 | 已定义 | 一致且有管理 |
| 4 | 已最佳化 | 可度量、持续改进、已内化 |

CSRM 采用不同的模型 —— 参见 [CSRM 一节](#csrm-swiss-ncsc-2025)。

---

## 评估集合

**评估集合** 是具名的评估群组，可跨框架汇总合规状态。用途包括：

- 依年度或审计周期将评估分组
- 针对特定法规范围提出报告（例如「EU regulatory stack 2025」）
- 比较各框架随时间的进展

每个集合都会显示衍生的统计数据：完成百分比、合规百分比、各状态计数、状态汇总（只有当所有成员评估皆合规时，集合才算「合规」）。

**导出格式：** CSV（平面）、XLSX（依状态上色，每份评估一个工作表）、PDF（A4，含各评估分数与不符合项目清单）。

---

## 框架模块

### NIST CSF 2.0

**来源：** NIST Cybersecurity Framework 2.0 版（2024）
**范围：** 6 项功能共 106 个子分类：治理（Govern，GV）、识别（Identify，ID）、保护（Protect，PR）、检测（Detect，DE）、响应（Respond，RS）、恢复（Recover，RC）
**评分：** 每个子分类为 Tier 1–4（部分 → 调适），并含现况与目标层级
**适用对象：** 任何产业与规模 —— 全球普遍用作成熟度评估的基线

**平台功能：**
- 具名设置档（可建立多份评估／随时间追踪）
- 每个设置档都有雷达图与长条图报告页
- 可从官方 NIST CSF 2.0 Excel 模板导入 XLSX
- 可导出 XLSX 与 CSV

**涵盖范围描述：**
- 完整涵盖 106 个子分类，包括 GV（治理）—— CSF 2.0 新增、CSF 1.1 没有的功能
- Crosswalk Viewer 提供 ISO 27001 ↔ NIST CSF 2.0 对照

---

### NIST AI RMF 1.0 (AI 100-1)

**来源：** NIST AI Risk Management Framework 1.0（NIST AI 100-1），2023 年 1 月
**范围：** 4 项核心功能共 72 项子分类层级实务 —— GOVERN（GOV）、MAP（MAP）、MEASURE（MSR）、MANAGE（MNG）—— 分为 19 个类别
**评分：** 每个子分类的成熟度 0–4
**适用对象：** AI 系统供应商、开发者、部署者与运营者 —— 任何产业。自愿采用，不特定司法管辖区。

**功能结构：**
- **GOVERN（19 个子分类）** —— 组织的 AI 风险文化、政策、问责结构、人力实务
- **MAP（18 个子分类）** —— 情境与风险界定：预期用途、分类、效益、成本、社会影响
- **MEASURE（22 个子分类）** —— 以量化、质性与混合方法工具分析、标竿比较与监控 AI 风险
- **MANAGE（13 个子分类）** —— 风险处置、残余风险、事件响应、上市后监督

**平台功能：**
- 72 项子分类实务，依类别分组（GOV-1 至 MNG-4），成熟度 0–4
- 没有 NIST AI RMF ↔ EU AI Act 的直接对照轴 —— 两者透过 ISO 42001 间接连结（NIST AI RMF ↔ ISO 42001：32 项对应；ISO 42001 ↔ EU AI Act：31 项对应），或透过 ISO 27001（NIST AI RMF ↔ ISO 27001：56 项对应；ISO 27001 ↔ EU AI Act：58 项对应）
- 评估集合 —— 可将 AI RMF 评估与 EU AI Act 评估归为同一组

**涵盖范围描述：**
- 子分类描述取自官方 NIST AI RMF Playbook（72 项建议行动）
- 已有 ISO 27001 ↔ AI RMF 对照（56 项对应）；已有 ISO 42001 ↔ AI RMF 对照（32 项对应）—— 两者都是可行的对应路径
- 此框架为自愿性质 —— 在任何司法管辖区都不是法规遵循要求
- 相关：NIST CSF 2.0 的 GOVERN 功能直接对应 AI RMF 的 GOVERN 结构

---

### NIS2 指令 (EU 2022/2555)

**来源：** 指令 (EU) 2022/2555 —— 网络与信息安全 2 (Network and Information Security 2)
**范围：** 15 项要求 —— 10 项第 21(2) 条的技术／组织安全措施，加上 5 项第 23 条的事件通报义务
**评分：** 成熟度 0–4
**适用对象：** 欧盟关键实体（essential entities：能源、运输、银行、医疗、水、数位基础设施）与重要实体（important entities）；各会员国的国内转换法规不一 —— 请依您所在司法管辖区的施行法确认适用性

**涵盖范围描述：**
- 已对应第 21(2) 条 (a) 至 (j) 各项措施
- 第 23 条的通报时限与内容义务
- 未涵盖第 22–24 条（供应链、注册、揭露）—— 仅就技术措施自我评估
- Crosswalk Viewer 提供 NIS2 对 ISO 27001 的对照

---

### DORA (EU 2022/2554)

**来源：** 规则 (EU) 2022/2554 —— 数位运营韧性法 (Digital Operational Resilience Act)
**范围：** 5 大支柱的强制性要求：ICT 风险管理、ICT 事件通报、数位运营韧性测试、ICT 第三方风险管理，以及信息分享。这些支柱共评估 27 条条文（第 II–VI 章）。
**评分：** 成熟度 0–4
**适用对象：** 欧盟金融实体（银行、投资公司、保险、加密资产服务供应商、支付机构）及其关键 ICT 第三方供应商

**涵盖范围描述：**
- 涵盖 DORA 的核心运营韧性义务
- 不取代依 DORA 与国家主管机关（NCA）的往来
- 涵盖第一层级（Level-1）条文 —— 不含所有 RTS/ITS 授权法案（截至 2025 年法规仍在发展中）

---

### CIS Critical Security Controls v8

**来源：** Center for Internet Security，CIS Controls v8（2021）
**范围：** 18 项控制措施共 153 项防护措施
**评分：** 成熟度 0–4
**适用对象：** 任何组织 —— 对中小企业及尚无主要框架者尤其适用。三个实施群组（IG1/IG2/IG3）可协助排定优先顺序。

**涵盖范围描述：**
- 无论属于哪个实施群组，153 项防护措施皆可评估
- Crosswalk Viewer 提供 CIS Controls v8 对 ISO 27001 的对照

---

### BSI IT-Grundschutz Kompendium

**来源：** Bundesamt für Sicherheit in der Informationstechnik（德国联邦信息安全局）—— IT-Grundschutz Kompendium
**范围：** 2023 年版包含 10 个 Schichten（层级）共 111 个官方 Bausteine（模块构件）：ISMS、ORP（组织）、CON（概念）、OPS（运营）、DER（检测）、APP（应用程序）、SYS（系统）、IND（工业）、NET（网络）、INF（基础设施）。ISMS CORE 全部涵盖 111 个。
**评分：** 成熟度 0–4
**适用对象：** 德国公部门（强制）、追求 ISO 27001／IT-Grundschutz 双认证的组织、DACH 地区组织

**对照：**
- ISO 27001:2022 ↔ BSI IT-Grundschutz：386 项对应 —— 依 BSI 官方 Zuordnungstabelle 建立
- ISO 27701:2025 ↔ BSI IT-Grundschutz：101 项对应
- ISO 27018:2025 ↔ BSI IT-Grundschutz：51 项对应
- 合计：538 项跨标准对应 —— 可在 Crosswalk Viewer 检视

**涵盖范围描述：**
- 依公开的 Kompendium 结构；确切要求文本取自完整 BSI Kompendium（bsi.bund.de）
- 所有 10 个层级共 111 个官方 Bausteine 皆已涵盖

---

### CSRM (Swiss NCSC, 2025)

**来源：** Methode CSRM 2025 —— Cyber Security Risk Method，由瑞士国家网络安全中心（NCSC／BACS）于 2025 年发布
**范围：** 20 项强制基线要求、用于报告的 6 项控制目标
**评分：** 二元 —— `met` / `partial` / `not_met` / `exception`（非 0–4 成熟度）
**适用对象：** 瑞士关键基础设施运营者 —— 能源、运输、水、医疗、金融、政府

> **重要：** CSRM 是与所有其他模块截然不同的模型。使用前请仔细阅读本节。

#### CSRM 的运作方式

CSRM 以**对象为中心**。您不是全域评估一份要求清单，而是：

1. 定义 **IT 保护对象** —— 具有相同保护要求的系统、应用程序与数据的汇总群组（而非个别资产）
2. 依取自 NIST CSF 2.0 功能（GV、ID、PR、DE、RS）的 20 项基线要求评估每个保护对象
3. 识别**提升保护对象**（关键性较高者），并记录额外的技术与组织措施（TOM）
4. 将结果对应至 6 项控制目标，以进行结构化报告

CSRM 的五步方法如下：
1. 定义范围与保护对象
2. 分类保护对象（标准／提升）
3. 对每个对象套用 20 项基线要求
4. 为提升对象定义额外的 TOM
5. 透过 6 项控制目标提出报告

#### 与 NIST CSF 2.0 的对齐

CSRM 2025 对齐 **NIST CSF 2.0** —— 具体而言，20 项基线要求对应 GV（治理）、ID（识别）、PR（保护）、DE（检测）与 RS（响应）。ISMS CORE 的实作全程采用 CSF 2.0 的功能代码。

> **备注：** NCSC 自家的比较文件（*Vergleich-Managementsysteme EN*，2025）在其交叉参照表中使用 CSF **1.1** 代码 —— 因为瑞士的 ICT 最低标准仍以 CSF 1.1 为基础。CSRM 方法本身参照 CSF 2.0，ISMS CORE 反映的是正确版本。

#### BACS 自我检讨 —— 已知限制

NCSC 自家的比较文件对 CSRM 的限制异常坦率。以下缺口直接以免责声明形式呈现在 Platform UI 中：

- **IEC 62443 对齐待完成** —— 工业控制系统的涵盖范围尚未定案
- **10 项 ICT 最低标准要求在 CSRM 中无对应项** —— 这些不是 ISMS CORE 实作的缺口，而是 CSRM 本身的缺口（比较文件第 12–13 页已承认）
- **「无政策」标签有误导之嫌** —— CSRM 并未强制以政策作为文件类型，但在其控制目标中要求治理与组织措施
- **并行实施 ISMS = 重复风险** —— 同时运行 ISO 27001 ISMS 与 CSRM 的组织应对应共用控制措施，以免维护两套并行的控制措施

**来源文件（BACS／NCSC 官方）：**
- CSRM 2025 方法：https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infras/Methode-CSRM-2025-EN.pdf
- 管理制度比较：https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infras/Vergleich-Managementsysteme_EN.pdf

---

### TISAX / VDA ISA 6.0

**来源：** Trusted Information Security Assessment Exchange —— VDA Information Security Assessment (ISA) 6.0 版
**范围：** 9 个领域共 79 项要求：信息安全政策与组织、人力资源、物理安全、身分与访问管理、IT／网络安全、供应商关系、合规、原型保护，以及数据保护
**评分：** 成熟度 0–4
**适用对象：** 处理敏感数据（尤其是原型与车辆数据）的汽车产业供应商、OEM 合作伙伴与分包商 —— 对多数主要 OEM（BMW、VW Group、Mercedes、Stellantis 等）而言，参与 TISAX 认证是供应链要求

**涵盖范围描述：**
- 依 VDA ISA 6.0 的领域结构与评估准则
- 完整的 TISAX 评估与标签核发需与 ENX 认可的审计员往来
- 本模块是为准备就绪而设的自我评估工具，不能取代官方 TISAX 评估
- 评估标签（TISAX、AL1/AL2/AL3）仅透过 ENX 认可的评估服务供应商核发

---

### Swiss ISG (SR 128)

**来源：** Bundesgesetz über die Informationssicherheit beim Bund (ISG)／瑞士联邦信息安全法 (LSI) —— SR 128，2024 年 1 月 1 日生效；网络攻击通报义务（第 74a–74h 条）于 2025 年 4 月 1 日生效
**范围：** 8 个章节共 27 项可评估要求：信息安全原则（第 6–10a 条）、信息分类（第 11–15 条）、ICT 安全（第 16–19 条）、人员与访问（第 20–21 条）、物理安全（第 22–23 条）、人员安全查核（第 27–30、43 条）、网络攻击通报义务（第 74a–74h 条）、ISMS 组织（第 81、85 条）
**评分：** 成熟度 0–4
**适用对象：** 瑞士联邦机关（强制）；受第 74b 条网络攻击通报义务约束的关键基础设施运营者（能源、水、金融、运输、医疗、ICT）；自愿对齐瑞士联邦安全标准的民营组织

**主要义务：**
- **24 小时网络攻击通报** —— 在检测到危害运营、涉及数据窜改／外泄、长时间未被发现或涉及勒索的网络攻击后 24 小时内，强制向 BACS／OFCS 通报（第 74d–74e 条）
- **信息分类** —— 三级架构：内部／机密／秘密，并采知悉必要（need-to-know）访问控制（第 11–14 条）
- **ICT 安全类别** —— 基线／提升／极高，各有对应的最低安全措施（第 17–18 条）
- **人员安全查核（PSC）** —— 敏感职务的基本与延伸查核；定期重复办理（第 27–43 条）
- **ISB／RSSI 任命** —— 正式设置信息安全主管，负责咨询、指令与合规监督（第 81 条）
- **行政处罚** —— 未通报网络攻击：最高 100,000 瑞士法郎（第 74h 条）

**ISO 27001 对照：** 40 项对应 —— ISO 27001:2022 的控制措施可直接对应 ISG 要求；实务上 ISO 27001 是公认的 ISG 合规实施载体。

**涵盖范围描述：**
- 本模块主要适用于瑞士联邦机关及第 74b 条所列关键基础设施的运营者
- 不受第 74b 条约束的民营组织并无法律遵循义务，但得自愿采用此框架作为瑞士安全基线
- 网络攻击通报义务（第 74a–74h 条）是关键基础设施运营者最迫切的合规行动 —— 已于 2025 年 4 月 1 日生效

> **备注：** 本模块是自我评估工具。官方合规认定需由合格的瑞士信息安全专业人员审查。

---

### Swiss nDSG 2023

**来源：** Bundesgesetz über den Datenschutz (nDSG)／瑞士联邦数据保护法 —— 2023 年 9 月 1 日生效
**范围：** 6 章共 25 项关键条款：范围与原则、数据主体权利、控管者义务、特殊情形、数据传输、执法
**评分：** 成熟度 0–4
**适用对象：** 处理瑞士居民个人数据或在瑞士设立的任何组织

**涵盖范围描述：**
- nDSG 是瑞士对应 EU GDPR 的法规（范围大致相近，法律基础不同）
- 本模块涵盖核心合规义务 —— 法律解释应咨询瑞士数据保护法律顾问
- 同时受 nDSG 与 GDPR 约束的瑞士组织（例如处理欧盟居民数据者）宜并用本模块与 GDPR 对照

---

### EU Cyber Resilience Act (2024/2847)

**来源：** 规则 (EU) 2024/2847 —— 网络韧性法 (Cyber Resilience Act)
**范围：** 6 个群组共 26 项基本要求：基本网络安全要求、漏洞处理、符合性评估、市场监督、协调揭露、事件通报
**评分：** 成熟度 0–4
**适用对象：** 在欧盟市场销售含数位元素产品（硬件与软件）的制造商与进口商

**涵盖范围描述：**
- CRA 分阶段实施：市场监督条款自 2025 年中适用，漏洞／事件通报自 2025 年底适用，2027 年底全面适用
- 附录 I（第 I 部分与第 II 部分）的基本要求是主要合规标的 —— 本模块两者皆涵盖
- 符合性评估途径取决于产品关键性等级（Class I、II 或关键产品）—— 自我宣告或第三方评估
- 本模块提供就绪状态的自我评估；Class II 与关键产品的正式符合性评估需由公告机构（notified body）进行

---

### EU AI Act (2024/1689)

**来源：** 规则 (EU) 2024/1689 —— 人工智慧法 (Artificial Intelligence Act)
**范围：** 第 III 章（高风险 AI 系统）的 9 条条文：第 2 节的 8 条核心要求条文（第 8 条合规、第 9 条风险管理、第 10 条数据治理、第 11 条技术文件、第 12 条记录保存、第 13 条透明度、第 14 条人为监督、第 15 条准确性／强健性／网络安全），加上第 3 节的第 27 条基本权利影响评估
**评分：** 成熟度 0–4
**适用对象：** 欧盟境内 AI 系统的提供者与部署者 —— 义务依风险分类而异（不可接受风险／禁止、高风险、有限风险、最低风险）

**涵盖范围描述：**
- 本模块涵盖**高风险 AI 系统**的第 3 章义务 —— 最实质的合规层级
- 禁止的 AI 实务（第 5 条）不是评估标的；该等实务必须绝对避免
- 本模块版本未涵盖通用目的 AI 模型义务（第 VIII 篇）
- AI 法分阶段实施：禁止的实务自 2025 年 2 月起适用；高风险义务于 2026–2027 年间分阶段适用
- 高风险 AI 系统的正式符合性评估需由公告机构进行，或采标准化测试的自我评估

---

### EU Cloud Sovereignty Framework (v1.2.1)

**来源：** 欧盟执委会 —— DG DIGIT，EU Cloud Sovereignty Framework v1.2.1（2025 年 10 月）
**范围：** 8 项主权目标（SOV-1 至 SOV-8），以 SEAL-0 至 SEAL-4 等级评估。加权主权分数（权重合计 100%）：SOV-1 策略 15% · SOV-2 法律与管辖 10% · SOV-3 数据与 AI 10% · SOV-4 运营 15% · SOV-5 供应链 20% · SOV-6 技术 15% · SOV-7 安全与合规 10% · SOV-8 环境 5%
**评分：** SEAL-0（无主权）→ SEAL-1（管辖）→ SEAL-2（数据）→ SEAL-3（数位韧性）→ SEAL-4（完整数位主权）
**适用对象：** 依欧盟采购与数位主权要求评估云服务提供商的欧盟机构、公部门机关与受监管实体。参考 Gaia-X、ENISA/NIS2/DORA、CIGREF Trusted Cloud Referential v2、France Cloud de Confiance 与德国 Souveräner Cloud 策略。

**涵盖范围描述：**
- 此框架为各采购层级定义**最低保证等级** —— 本模块支持自我评估及对照该等层级的缺口分析
- SEAL 等级是质性判断；正式采购决策需有供应商审计证据与合同承诺
- SOV-5 供应链评估需能掌握次级供应商链 —— 证据深度可能因供应商透明度而异
- 环境永续（SOV-8）评分仅供参考；正式绿色采购可能需要经认证的能源／碳排数据

---

### CyberFundamentals (CCB)

**来源：** Centre for Cybersecurity Belgium (CCB) —— CyberFundamentals Framework v2025
**范围：** 41 项实务，对齐 NIST CSF 2.0 功能：治理（GV）、识别（ID）、保护（PR）、检测（DE）、响应（RS）、恢复（RC）
**评分：** 成熟度 0–4
**适用对象：** 寻求 CCB CyberFundamentals 认证的比利时组织；比利时境内属 NIS2 范围的实体；在比利时法规情境下使用 NIST CSF 2.0 的任何组织

**涵盖范围描述：**
- CyberFundamentals 使用 NIST CSF 2.0 的控制措施编号（GV.OC-01、ID.AM-01 等）—— ISMS CORE 的对照沿用既有的 ISO→NIST CSF 对应
- 四个保证等级：Small、Basic、Important、Essential（对齐比利时 NIS2 转换法，2024 年 4 月 26 日法）
- 对照：ISO 27001:2022 ↔ CyberFundamentals —— 107 项对应

---

### BaFin BAIT (Rundschreiben 10/2017, amended 2021)

**来源：** Bundesanstalt für Finanzdienstleistungsaufsicht（德国联邦金融监督局）—— Bankaufsichtliche Anforderungen an die IT (BAIT)，Rundschreiben 10/2017，2021 年 8 月 16 日修订
**范围：** 12 个模块共 23 项要求：IT 策略、IT 治理、信息风险管理、信息安全、IT 项目、应用程序开发、IT 运维、IT 外包、IT 紧急管理、IAM、密码学、BCM
**评分：** 成熟度 0–4
**适用对象：** 受 BaFin 监理的德国银行与金融机构；对欧盟受监管实体而言，须与 MaRisk 及 DORA 并同适用

**涵盖范围描述：**
- BAIT 是德国受监理银行主要的 IT 监理通函；VAIT（保险）与 KAIT（资本管理）结构相同
- 2021 年 8 月 16 日修订（非取代性通函）；包含 MaRisk 对齐与云端特定指南
- 对照：ISO 27001:2022 ↔ BaFin BAIT —— 69 项对应

---

### CSSF Circulaire 20-750 (LU)

**来源：** Commission de Surveillance du Secteur Financier (CSSF)，卢森堡 —— Circulaire CSSF 20/750
**范围：** 7 个 ICT 风险领域共 19 项要求：治理、风险管理、ICT 安全、业务连续性、第三方管理、事件管理、审计
**评分：** 成熟度 0–4
**适用对象：** 受 CSSF 监理的卢森堡金融业实体 —— 银行、投资公司、支付机构、基金管理机构

**涵盖范围描述：**
- CSSF 20/750 是 CSSF 受监管实体主要的 ICT 风险管理通函，对齐 EBA/ESMA 指南
- 自 2025 年 1 月起受 DORA 约束的实体宜并用本模块与 DORA 模块
- 对照：ISO 27001:2022 ↔ CSSF 20/750 —— 47 项对应

---

### ACN Cyber Risk Management (IT)

**来源：** Agenzia per la Cybersicurezza Nazionale (ACN) —— *Determinazione obblighi di base*（2025 年 4 月），实施 D.Lgs. 138/2024 第 24(2) 条
**范围：** 两个层级 —— Important 实体（附录 1）37 项措施／87 项要求，Essential 实体（附录 2）43 项措施／116 项要求 —— 围绕第 24(2) 条的 10 项法定要素编排：风险分析与系统安全政策、事件管理、业务连续性、供应链安全、安全采购／开发／维护、风险措施有效性检视、基本网络卫生与培训、密码学政策、人力资源安全／访问控制／资产管理，以及多因子验证／安全通讯
**评分：** 成熟度 0–4
**适用对象：** 义大利组织 —— 公共行政、关键基础设施运营者、义大利境内属 NIS2 范围的实体

**涵盖范围描述：**
- ACN 是义大利国家网络安全局及 NIS2 主管机关；这些基本安全措施对齐义大利的 NIS2 转换法（D.Lgs. 138/2024）
- 同时受 ACN 义务与 NIS2 约束的组织可并用两个模块
- 对照：ISO 27001:2022 ↔ ACN Guidelines —— 43 项对应

---

### UK NIS Regulations 2018

**来源：** The Network and Information Systems (NIS) Regulations 2018 (SI 2018/506) —— 英国对 EU NIS 指令的实施
**范围：** 3 项目标共 13 项要求：治理、风险管理与安全、运营能力
**评分：** 成熟度 0–4
**适用对象：** 英国能源、运输、医疗、水、数位基础设施的基本服务运营者（OES）；相关数位服务供应商（RDSP）

**涵盖范围描述：**
- 英国 NIS 法规在脱欧后仍以国内法效力存续；网络安全与韧性法案（Cyber Security and Resilience Bill，2025，尚待御准）将更新并扩大范围
- NCSC 的 Cyber Assessment Framework（CAF）是 OES 合规的建议工具 —— 本模块涵盖核心 NIS 义务
- 对照：ISO 27001:2022 ↔ UK NIS Regulations —— 51 项对应

---

### UK Operational Resilience (FCA/PRA)

**来源：** FCA 政策声明 PS21/3 + PS26/2；PRA 监理声明 SS1/21；英格兰银行运营韧性政策
**范围：** 4 项目标共 12 项要求：重要业务服务、影响容忍度、情境测试、自我评估
**评分：** 成熟度 0–4
**适用对象：** 英国金融业 —— 银行、房屋互助协会、PRA 指定的投资公司、保险公司、金融市场基础设施（FMI）、支付系统运营者

**涵盖范围描述：**
- 英国运营韧性要求已于 2025 年 3 月全面生效（PS21/3 期限）；PS26/2 将范围扩及更多实体
- 同时受英国运营韧性与 DORA 约束的实体宜并用两个模块
- 重点在于重要业务服务（IBS）与影响容忍度 —— 不能取代与 FCA／PRA 的正式监理往来
- 对照：ISO 27001:2022 ↔ UK Operational Resilience —— 34 项对应

---

### COBIT 2019 (ISACA)

**来源：** ISACA —— COBIT 2019 Framework: Governance and Management Objectives（2018 年 11 月）
**范围：** 5 个领域共 40 项治理与管理目标：EDM（评估、指导与监督）、APO（对齐、规划与组织）、BAI（建置、获取与实施）、DSS（交付、服务与支持）、MEA（监督、评估与评估）
**评分：** 能力等级 0–4（不完整 → 已执行 → 已管理 → 已建立 → 最佳化）
**适用对象：** 企业 IT 治理计划、内部审计职能、IT 策略与董事会层级监督。对 CISM、CISA 与 CGEIT 认证持有者尤其相关。

**涵盖范围描述：**
- EDM 目标（EDM01–EDM05）属治理层级 —— 供董事会／高阶主管监督之用；APO、BAI、DSS、MEA 属管理层级
- APO13（已管理安全）与 DSS05（已管理安全服务）可直接对应 ISO 27001:2022 附录 A 的信息安全控制措施
- COBIT 2019 对齐 ISO/IEC 27001、ISO/IEC 38500、ITIL、NIST CSF 与 PMBOK/PRINCE2
- 完整的 COBIT 能力量表为 0–5（第 5 级：量化管理的最佳化）；本平台采用与所有其他评估模块一致的 0–4 量表
- 取代 COBIT 5（2012）；主要变更包括设计因素、焦点领域，以及与 NIST CSF 2.0 概念的对齐

---

### NIST SP 800-53 Rev. 5

**来源：** NIST Special Publication 800-53 Revision 5 —— Security and Privacy Controls for Information Systems and Organizations（2020 年 9 月）
**范围：** 20 个控制措施家族，涵盖联邦信息系统完整的安全与隐私控制措施目录。家族包括访问控制（AC）、审计与问责（AU）、配置管理（CM）、识别与验证（IA）、事件响应（IR）、系统与通讯保护（SC）等。
**评分：** 成熟度等级 0–4（未实施 → 初始 → 已管理 → 已定义 → 最佳化）
**适用对象：** FISMA 要求的美国联邦机关与承包商；寻求 FedRAMP 授权的组织；任何想要一套完整、以基线驱动的控制措施框架的产业。已与 ISO 27001:2022 附录 A 交叉参照。

**涵盖范围描述：**
- 控制措施家族可直接对应 ISO 27001:2022 附录 A 的领域 —— 平台上将 474+ 项个别控制措施浓缩为 20 个计分家族
- NIST SP 800-53 Rev. 5 首次整合隐私控制措施（先前在 800-53A 中另立）
- Crosswalk Viewer 提供 ISO 27001:2022 ↔ NIST SP 800-53 Rev. 5 对照
- 基线裁剪（Low/Moderate/High）未自动化 —— 平台对全部 20 个家族一律计分

---

### CSA Cloud Controls Matrix v4.1

**来源：** Cloud Security Alliance —— Cloud Controls Matrix v4.1（2023 年 3 月）
**范围：** 17 个安全领域共 207 项控制措施规格：应用与介面安全（AIS）、审计保证与合规（AAC）、业务连续性管理与运营韧性（BCR）、变更控制与配置管理（CCC）、密码学、加密与密钥管理（CEK）、数据中心安全（DCS）、数据安全与隐私生命周期管理（DSP）、治理、风险与合规（GRC）、人力资源（HRS）、身分与访问管理（IAM）、基础设施与虚拟化安全（IVS）、互通性与可携性（IPY）、日志与监控（LOG）、安全事件管理、电子搜证与云端鉴识（SEF）、供应链管理、透明度与问责（STA）、威胁与漏洞管理（TVM）、通用端点管理（UEM）。
**评分：** 成熟度等级 0–4
**适用对象：** 寻求 CSA STAR 认证的云服务提供商；执行供应商尽职调查的云端消费者；采多云或混合环境的组织。

**涵盖范围描述：**
- CCM v4.1 是权威的云端安全控制措施框架 —— 对齐 ISO/IEC 27001、ISO/IEC 27017、ISO/IEC 27018、NIST SP 800-53、CIS Controls v8 与 GDPR
- CSA STAR（Security, Trust, Assurance, and Risk）第 1 级采用 CCM 自我评估；第 2 级采用第三方审计
- ISO 27018:2025（云端产品）与 CCM v4.1 互补 —— CCM 范围较广；ISO 27018 专注于 PII 保护

---

### CSA AI Controls Matrix v1.1

**来源：** Cloud Security Alliance —— AI Controls Matrix (AICM) v1.1
**范围：** 18 个领域共 247 项控制措施，包括：AI 治理与问责（AGA）、数据管理与隐私（DMP）、模型开发与验证（MDV）、安全与韧性（SAR）、透明度与可解释性（TEX）、人为监督与控制（HOC）、法规合规与法律（RCL），以及涵盖 AI 风险管理、伦理、运营、供应链、事件响应等的另外 11 个领域。
**评分：** 成熟度等级 0–4
**适用对象：** 开发、部署或采购 AI 系统的组织；AI 治理团队；提供 AI／ML 服务的云端供应商；负责 EU AI Act 或 ISO 42001 合规的团队。

**涵盖范围描述：**
- AICM 设计为 CCM v4.1 的配套 —— 专注于 AI 系统安全与治理
- 对齐 EU AI Act、ISO/IEC 42001:2023、NIST AI RMF 1.0 与 OECD AI 原则
- ISO 42001（AI 产品）与 AICM 互补 —— ISO 42001 是管理制度标准；AICM 提供详细的技术控制措施
- 与平台的 ISO 42001 对照对应（NIST AI RMF：32、EU AI Act：31、OECD AI：14）并用尤其有用

---

### NCSC CAF v4.0 (UK)

**来源：** 英国国家网络安全中心（NCSC）—— Cyber Assessment Framework v4.0（2024）
**范围：** 14 项原则与 4 项目标（A：管理安全风险、B：防范网络攻击、C：检测网络安全事件、D：降低事件影响）共 41 项贡献成果（Contributing Outcomes）。
**评分：** 多数成果采三栏模型：未达成（0）／部分达成（2）／已达成（4）。九项成果采两栏模型（仅未达成／已达成）。
**适用对象：** 英国基本服务运营者（能源、运输、医疗、水、数位基础设施）、相关数位服务供应商、受 UK NIS Regulations 2018 约束的公部门机关。

**涵盖范围描述：**
- CAF v4.0（2024）新增目标 D（降低影响），并重整 v3.1 的多项成果 —— 平台仅实作 v4.0
- Crosswalk Viewer 提供 65 项 ISO 27001:2022 对照对应（ISO27001_2022 → NCSC_CAF 轴）
- 同时受 NIS 法规与 CAF 约束的组织宜同时维护两个模块 —— NIS 提供法律基线，CAF 提供技术评估方法

---

### ReCyF v2.5 — France NIS2 (ANSSI)

**来源：** ANSSI —— Agence nationale de la sécurité des systèmes d'information。Référentiel de Cybersécurité France v2.5（2026/03/17）。
**范围：** 20 项安全目标（OS-01 至 OS-20），分属 4 大支柱：Gouvernance、Protection、Défense、Résilience。152 项要求（Moyens acceptables de conformité）。OS-01–15 同时适用于 Entités Importantes（EI）与 Entités Essentielles（EE）。OS-16–20 仅适用于 EE。
**评分：** 成熟度等级 0–4
**适用对象：** 受 NIS2 转换法约束的法国组织：由 ANSSI 依法国尚待通过的 NIS2 转换法（PJL 第 14 条 —— 撰写时尚未立法）分类的 Entités Importantes（EI）与 Entités Essentielles（EE）。涵盖所有 NIS2 产业：énergie、transport、santé、eau、infrastructures numériques、services numériques、administrations publiques。

**涵盖范围描述：**
- ANSSI 工作文件 2.5 版（2026/03/17）—— 最终采用前仍可能修订
- Crosswalk Viewer 提供 50 项 ISO 27001:2022 对照对应（ISO27001_2022 → FR_NIS2_RECYF 轴）
- 仅适用 EE 的目标（OS-16 至 OS-20）已纳入评估并清楚标记；仅属 EI 的组织得将其用作期望目标
- 评估介面全程使用 ANSSI 官方法文术语

---

### BSI C5:2026

**来源：** Bundesamt für Sicherheit in der Informationstechnik —— Cloud Computing Compliance Criteria Catalogue (C5:2026)，v1.0.1，2026 年 4 月 7 日发布。取代 C5:2020。
**范围：** 17 个领域共 168 项准则：信息安全组织（OIS）、安全政策与程序（SP）、人员（HR）、资产管理（AM）、物理安全（PS）、运营（OPS）、身分与访问管理（IAM）、密码学与密钥管理（CRY）、通讯安全（COS）、可携性与互通性（PI）、采购／开发／修改（DEV）、服务供应商与供应商控制（SSO）、安全事件管理（SIM）、业务连续性管理（BCM）、合规（COM）、处理政府机关调查请求（INQ）、产品安全与保安（PSS）。
**评分：** 成熟度等级 0–4
**适用对象：** 寻求 BSI C5 查核证明（Type 1 或 Type 2）的云服务提供商（CSP）；在德国与欧盟执行供应商尽职调查的云端客户；公部门采购；有云端依赖项且受 NIS2 或 KRITIS 约束的组织。

**结构描述：**
- 每项准则都有分类为下列类型的子准则：**Basic**（强制门槛）、**Additional-Sharpening**（提高既有要求的水准）与 **Additional-Complementing**（扩大范围）。平台在 168 项顶层准则层级进行评估 —— 子准则仅供叙述参考，不个别计分。
- OIS-01 要求符合 ISO/IEC 27001 的 ISMS —— 因此 C5:2026 是 ISO 27001 之上的云端专属延伸层，而非独立的替代方案。
- 领域 PI（可携性与互通性）是 C5:2026 新增 —— C5:2020 没有。

**涵盖范围描述：**
- 依 BSI 官方机器可读 XLSX（`C5_2026_editable_en.xlsx`，随标准发布）
- 包含完整英文准则文本；德文原文可于 bsi.bund.de 取得
- 正式 C5 查核证明需与合格的 C5 审计员往来；本模块支持内部就绪状态评估

---

### BSI C3A — Criteria enabling Cloud Computing Autonomy

**来源：** Bundesamt für Sicherheit in der Informationstechnik —— Criteria enabling Cloud Computing Autonomy (C3A)，v1.0，2026 年 4 月 27 日发布。
**范围：** 6 个主权（SOV）领域共 30 个准则群组：SOV-1 策略主权、SOV-2 法律与管辖主权、SOV-3 数据主权、SOV-4 运营主权、SOV-5 供应链主权、SOV-6 技术主权。
**评分：** 成熟度等级 0–4
**适用对象：** 展现主权能力的云服务提供商；评估供应商自主性的云端服务客户（政府、KRITIS 运营者、受监管实体）；依数位主权要求的欧盟公部门采购。

**先决条件：** C3A 以云服务提供商符合 BSI C5:2026 准则为前提 —— C5 涵盖 C3A 所立基的安全基础（SOV-7 安全与合规）。两个模块在平台上皆可使用，并可一起评估。

**领域结构：**
- **SOV-1 策略主权（4 个群组）：** 管辖权、注册办事处、CSP 有效控制、CSP 控制权变更通知（90 天前通知）
- **SOV-2 法律与管辖主权（3 个群组）：** 域外曝险（年度非欧盟法律检视）、审计权（本国／德国主管机关访问）、国防状态接管
- **SOV-3 数据主权（5 个群组）：** 数据存放地（EU／DE 选项）、外部密钥管理（IaaS/PaaS/SaaS 的 BYOK）、外部身分提供者、日志与监控（即时 API 访问）、用户端加密
- **SOV-4 运营主权（10 个群组）：** 操作人员（EU／DE 居留）、远端工作（EU／DE 访问路径）、备援连线、SOC（EU／DE 运营）、入口数据控制、更新威胁分析、数据交换监控、数据交换闸道、断线（每年测试）、复线（90 天恢复）
- **SOV-5 供应链主权（5 个群组）：** 软件依赖项（依 BSI TR-03183-2 的 SBOM）、硬件依赖项、外部服务依赖项、出口限制管理、容量管理（EU／DE）
- **SOV-6 技术主权（3 个群组）：** 原始码可取用性（EU 备份，最旧不超过 24 小时，至少 5 个版本）、持续服务交付（响应策略）、软件开发（独立工具链访问）

**涵盖范围描述：**
- EU Cloud Sovereignty Framework 的 SOV-7（安全与合规）与 SOV-8（环境永续）刻意不涵盖 —— SOV-7 由 C5:2026 处理，SOV-8 不在 BSI 的范围内
- 准则变体（C1/C2 = EU 与德国层级；AC = 附加准则）记载于准则群组描述中；平台在准则群组层级计分
- 依官方 PDF（C3A_Cloud_Computing_Autonomy.pdf，BSI，2026 年 4 月）

---

### PCI DSS v4.0.1

**来源：** PCI Security Standards Council —— Payment Card Industry Data Security Standard，v4.0.1，2024 年 6 月发布。
**范围：** 323 项子要求，归为 12 项顶层要求，依 6 个优先实施里程碑编排：(1) 移除敏感的验证数据并限制数据保留、(2) 保护系统与网络并为数据外泄响应做好准备、(3) 保护支付卡应用程序、(4) 监控并控制对系统的访问、(5) 保护储存的持卡人数据、(6) 完成其余合规工作并确保所有控制措施到位。
**评分：** 以里程碑为基础的进度追踪；子要求个别评估，并在平台介面中依里程碑分组。
**适用对象：** 储存、处理或传输持卡人数据的任何组织 —— 特约商店、服务供应商、支付处理机构。

**涵盖范围描述：**
- v4.0.1（2024 年 6 月）是 v4.0 的小幅更正版；ISMS CORE 全程实作 v4.0.1
- PCI DSS 正式评估（SAQ 或 QSA 合规报告）需由合格安全评估员进行或使用批准的 SAQ 表格 —— 本模块是就绪状态的自我评估工具，不能取代正式认证
- ISO 27001 ↔ PCI DSS 4.0 对照：39 项对应，在访问控制、密码学、日志与漏洞管理领域有大量重叠

---

### FINMA

**来源：** FINMA —— 瑞士金融市场监督管理局。涵盖通函 2023/1「Operational Risks and Resilience — Banks」（2024 年 1 月 1 日生效，韧性条款自 2026 年 1 月 1 日起全面拘束）、通函 2018/3「Outsourcing — Banks and Insurance Companies」（2020 年修订，仍现行有效），以及指南 03/2024「Cyber Risks」。
**范围：** 3 个来源共 21 项要求：通函 2023/1（7 项要求 —— 运营风险管理、ICT 风险管理、网络风险管理、关键数据风险管理、业务连续性管理、跨境服务风险、运营韧性）、通函 2018/3（9 项要求 —— 外包清册、选择／监控、集团内外包、保留责任、安全、审计权、跨境外包、合同要求）、指南 03/2024（5 项要求 —— 治理、保护措施、检测／响应／恢复、24 小时向 FINMA 通报、网络演练）。
**评分：** 成熟度等级 0–4
**适用对象：** 瑞士银行、保险公司及其他受 FINMA 监管的金融机构。

**结构描述：**
- 每项要求都可追溯至通函的官方边注编号（Rz）—— 瑞士监理人员审查时直接引用的段落参照
- 在评估检视中，要求依来源通函分组，而非摊平为单一清单
- 涵盖行为义务（2025/2）、流动性（2025/3）、合并监理（2025/4）与气候相关金融风险（2026/1）的新通函不在 ICT／安全评估范围内，未纳入。

**涵盖范围描述：**
- FINMA 明确将通函 2023/1 校准为适用于旗下有欧盟集团子公司并行实施 DORA 的机构 —— 运营韧性、ICT 风险框架、事件管理、第三方风险与网络演练（TLPT）大量重叠
- ISO 27001 对照：60 项对应。另提供 ISO 27018 与 ISO 27701 的对照对应，涵盖云端 PII 与隐私相关的 FINMA 义务（外包、数据位置、关键数据风险）
- 本模块是合规就绪状态的自我评估 —— 不取代 FINMA 本身的监理审查或持照审计

---

### 自定义框架（YAML 导入）

透过 YAML 上传任何自定义、特定产业或专有的控制措施框架。导入后，平台会透过 `iso_mappings` 字段将每项控制措施对应至 ISO 27001:2022，并在 Coverage 页面显示推定的涵盖范围。

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

**每项控制措施的关键字段：** `id`（必填）、`title`（必填）、`category`、`subcategory`、`priority`（HIGH/MEDIUM/LOW）、`iso_mappings`（ISO 27001:2022 附录 A 参照的清单）、`tags`。

**涵盖范围显示：** 导入后，Coverage 页面的 Mapping Matrix 分页会显示自定义框架涵盖范围区块，包含百分比、进度条与各控制措施明细。

**仅限管理员：** 导入与删除需要 admin 或 super_admin 角色。

---

## 对照表整合

所有合规评估模块都受惠于 Platform 的 Crosswalk Viewer，其显示下列跨框架对应：

- ISO 27001:2022 ↔ NIST CSF 2.0
- NIST AI RMF 1.0 ↔ ISO 27001:2022（56 项对应）以及 ↔ ISO 42001:2023（32 项对应）—— 没有 NIST AI RMF ↔ EU AI Act 的直接轴；透过 ISO 42001 间接连结（对 EU AI Act 有 31 项对应）
- ISO 27001:2022 ↔ NIST SP 800-53 Rev. 5
- ISO 27001:2022 ↔ MITRE ATT&CK v19
- ISO 27001:2022 ↔ DORA
- ISO 27001:2022 ↔ NIS2
- ISO 27001:2022 ↔ CIS Controls v8
- ISO 27001:2022 ↔ BSI IT-Grundschutz（386 项对应）
- ISO 27701:2025 ↔ BSI IT-Grundschutz（101 项对应）
- ISO 27018:2025 ↔ BSI IT-Grundschutz（51 项对应）
- ISO 27001:2022 ↔ CyberFundamentals BE（107 项对应）
- ISO 27001:2022 ↔ BaFin BAIT DE（69 项对应）
- ISO 27001:2022 ↔ CSSF 20-750 LU（47 项对应）
- ISO 27001:2022 ↔ ACN Guidelines IT（43 项对应）
- ISO 27001:2022 ↔ UK NIS Regulations（51 项对应）
- ISO 27001:2022 ↔ UK Operational Resilience（34 项对应）
- ISO 27001:2022 ↔ NCSC CAF v4.0（65 项对应）
- ISO 27001:2022 ↔ ReCyF v2.5 / FR NIS2（50 项对应）
- ISO 27017:2026 ↔ CSA CCM v4.1（11）、NIST CSF 2.0（9）、FINMA（7）、ISO 27001:2022（4）、DORA（4）、NIS2（2）—— 为 4 项 CLD 前置词独立控制措施（5.38、5.39、8.35、8.36）精选的对应；没有 Swiss nDSG 轴，因为这些控制措施不含 PII 内容

合计：Crosswalk Viewer 提供 **59 个轴共 4,671 个对照对象**。

---

## 限制与免责声明

**所有合规评估模块：**
- 为供内部就绪状态评估的自我评估工具
- 不构成法律意见或法规见解
- 在强制评估适用之处，不取代与主管机关、公告机构或认可审计员的往来
- 涵盖相关法规／标准发布日当时的要求 —— 法规更新（授权法案、RTS、ITS、实施决定）可能新增此处尚未反映的义务

**特定事项：** CSRM 基线要求与 BACS 限制描述系依 2025 年公开的 NCSC 文件。TISAX 标签需经 ENX 认可的评估。CIS Controls 防护措施文本系依 CIS v8（2021）。BSI IT-Grundschutz 完整要求文本可自 bsi.bund.de 取得。

---

*[ISMS CORE Project](README.zh-CN.md) 的一部分 —— ISO 27001 · ISO 27701 · ISO 27017 · ISO 27018 · ISO 42001* · [合规详情请见 isms-core.com/compliance.html](https://isms-core.com/frameworks)
