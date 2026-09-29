# ISMS Compass

<p align="center"><a href="17-isms-compass.md">English</a> · <a href="17-isms-compass.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<!-- ISMS-CORE:USER-MANUAL:17-isms-compass:v1.0:2026-04-16 -->

---

## 什么是 ISMS Compass？

ISMS Compass 是一套由 AI 驱动的缺口分析工具。贴上或上传任何政策、程序或安全文件，Compass 会将其与 ISMS CORE 黄金标准——精选的 ISO 27001:2022 政策与实施内容语料库——进行比对。它会回传一份结构化的缺口分析，指出哪些内容已具备、哪些缺失，以及哪些未对齐。

请在侧边栏前往 **Tools → ISMS Compass**。

> ISMS Compass 需要由您的管理员设置 `ANTHROPIC_API_KEY` 环境变数。若 Compass 显示「not available」消息，请联系您的管理员。

---

## Compass 的用途

Compass 是为三种使用情境而设计：

**评估现有文件：** 您的政策是在采用 ISMS CORE 之前撰写的。把它们贴进 Compass，即可在决定要采用 ISMS CORE 政策、还是调整现有政策之前，了解它们与黄金标准相较之下的差异。

**审查草稿：** 您撰写了一份新的政策或程序。Compass 会在它进入审查之前，找出缺口、缺少的条款以及未对齐的用语。

**审计前健检：** 将任何要交付审计人员的文件贴进 Compass，在审计前取得对其涵盖范围的第二意见。

---

## 使用 ISMS Compass

1. 前往 **Tools → ISMS Compass**
2. 选择文件所属的 **product family**（ISMS / Privacy / Cloud / AI）
3. 视需要选择特定的 **control group** —— 缩小情境范围可得到更精确的结果
4. 将文件文本贴进输入区，或上传档案（纯文本、Markdown 或 PDF）
5. 点选 **Analyse**

Compass 会依据已建立索引的 ISMS CORE 政策与实施指南语料库来处理文件。视文件长度而定，需时 10–30 秒。

---

## 解读 Compass 报告

Compass 报告分为三个部分：

### 对齐摘要

简要评估文件整体与黄金标准的对齐程度——高度对齐、部分涵盖，或有重大缺口。这是执行摘要。

### 已具备且对齐

列出您的文件中已具备、且与 ISMS CORE 黄金标准对齐的条款、主题或要求。这些是审计人员会认为合格的项目。

### 缺失或未对齐

缺口清单——黄金标准所预期、但您的文件中缺少或处理不足的项目。每个缺口项目会显示：

- 缺少或未对齐的内容
- 为何重要（它所支持的 ISO 控制措施）
- 建议的改善方式

### 建议新增

可让文件更接近黄金标准的具体用语新增或结构调整。这些是建议而非强制要求——您的专业判断优先。

---

## Compass 不是什么

**Compass 不是合规验证工具。** 一份全绿的 Compass 报告并不代表您的 ISMS 已通过验证。它代表您的文件与 ISMS CORE 内容基准对齐良好。

**Compass 无法访问您的环境。** 它只分析您提供的文本，无法得知您所述的政策是否真的落实。

**Compass 是撰写辅助工具，不是审计人员。** 用它来提升文件品质、及早发现缺口——而不是取代妥善的审计准备。

---

## 参考语料库

Compass 会将您的文件与一份精选语料库比对，该语料库由 ISMS CORE 政策与实施指南库衍生出的约 12,987 个已建立索引的区块组成。语料库依产品系列与控制群组编排。

每当管理员以更新后的内容重新载入语料库时（透过 **Admin → System → Reload QA Corpus**），语料库就会更新。

<!-- QA_VERIFIED: 2026-04-16 -->
