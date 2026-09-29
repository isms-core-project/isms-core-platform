# 政策与文件

<p align="center"><a href="05-policies-documents.md">English</a> · <a href="05-policies-documents.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<!-- ISMS-CORE:USER-MANUAL:05-policies-documents:v1.0:2026-04-16 -->

---

## 政策库

前往 **ISMS → Policies** 浏览完整的政策库。这是平台中所有政策与参照文件的全域检视——涵盖所有产品、语言与控制群组。

这与你项目的政策清单不同。在这里，你可以在把文件加入项目之前，浏览完整目录、搜寻并预览文件。

---

## 文件类型

平台处理数种文件类型，每种在 ISMS 中都有特定角色：

| 类型 | 代码 | 描述 |
|------|------|-------------|
| 政策 | POL / OP-POL / PRIV-POL / CLD-POL / AI-POL | 控制群组的「做什么、谁来做、用什么做」文件 |
| 指示 | INS | 基础平台指示与导引文件 |
| 参照 | REF | 支持某控制措施的技术参考数据（强化指南、配置基准） |
| 背景 | CTX | 某控制措施的法规与法律背景文件 |
| 表单 | FORM | 操作该控制措施时使用的模板与表单 |
| 实施指南（用户） | IMP-UG | 如何实施该控制措施——为 ISMS 经理与流程拥有者而写 |
| 实施指南（技术） | IMP-TG | 如何实施该控制措施——为工程师与系统管理员而写 |

---

## 筛选政策库

使用政策库顶端的筛选列缩小清单范围：

- **Product**——ISMS / Privacy / Cloud / AI
- **Type**——POL、REF、CTX、FORM、INS、IMP-UG、IMP-TG
- **Language**——EN、FR、DE、IT
- **Control group**——筛选至特定的附录 A 区段
- **Status**——draft、review、approved、published

多个筛选条件可以合并使用。

---

## 全文搜寻

政策库顶端的搜寻列会搜寻所有政策与实施文件的完整内容——不只是标题与 ID。这由 OpenSearch 驱动，并依相关性排序回传结果。

输入任何关键字、法规词汇或控制措施概念，即可找到相关文件。例如：

- `encryption at rest`——找出所有涵盖静态数据加密的政策与 IMP
- `TOTP MFA`——找出涵盖多重要素验证的实施指南
- `GDPR Article 32`——找出参照此条文的政策
- `vulnerability scanning`——找出所有讨论漏洞管理的文件

将产品筛选与搜寻搭配使用，可将结果缩小至特定产品家族。

---

## 预览文件

点选清单中的任一文件以开启预览面板。预览会显示算绘后的 Markdown——以审计人员或终端用户会看到的格式呈现。

在预览面板中你可以：

- **Copy document ID**——用于在缺口或证据中参照
- **Add to project**——将文件加入你的作用中项目
- **View raw source**——查看底层的 Markdown

---

## 文件状态

从内容库导入的文件起始状态为 **imported**。一旦加入项目，它们就进入项目的批准生命周期（Draft → Review → Approved → Published）。

全域内容库检视会以文件在内容库中的状态显示。项目检视则以文件在该项目中的状态显示。同一份文件在不同的项目中可以处于不同状态。

---

## 语言与在地化

内容库包含最多四种语言的文件。使用 **Language** 筛选以检视特定语言的文件。

当你的组织已设置国家（参阅[组织与用户](20-organisations-users.zh-CN.md)），政策文件在呈现时会自动替换为司法管辖区专属的法规参照。这一切都是透明地进行——底层文件不变；显示内容则会配合你组织的司法管辖区调整。

---

## 基础文件

有两种基础文件类型位于标准控制群组之上：

- **INS-POL-00**——ISMS CORE 平台简介：给所有用户的导引文件
- **INS-POL-01**——ISMS CORE Framework 简介：ISO 27001:2022 控制结构的概览

无论启用哪些产品家族，这些文件一律可用，且通常是加入新项目的第一批文件。

<!-- QA_VERIFIED: 2026-04-16 -->
