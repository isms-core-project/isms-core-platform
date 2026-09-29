<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Paradigm_Guide-2E8B57?style=for-the-badge" alt="ISMS CORE Paradigm Guide"/>
</p>

<h1 align="center">🧭 认识范式</h1>

<p align="center"><a href="PARADIGM.md">English</a> · <a href="PARADIGM.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<p align="center">
  <strong>为何 ISMS CORE 的工程做法与众不同——以及如何在它的各项产品之间做选择</strong>
</p>

<p align="center">
  <a href="https://www.iso.org/standard/27001"><img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square" alt="ISO 27001:2022"/></a>
  <a href="https://www.iso.org/standard/71670.html"><img src="https://img.shields.io/badge/ISO_27701-2025-7030A0?style=flat-square" alt="ISO 27701:2025"/></a>
  <a href="https://www.iso.org/standard/76559.html"><img src="https://img.shields.io/badge/ISO_27018-2025-00897B?style=flat-square" alt="ISO 27018:2025"/></a>
  <a href="https://www.iso.org/standard/82878.html"><img src="https://img.shields.io/badge/ISO_27017-2026-0288D1?style=flat-square" alt="ISO 27017:2026"/></a>
  <a href="#framework-sse--secure-systems-engineering"><img src="https://img.shields.io/badge/🏗️_FRAMEWORK-SSE_Engineering-9400D3?style=flat-square" alt="FRAMEWORK SSE"/></a>
  <a href="#-operational中小企业的基础-isms"><img src="https://img.shields.io/badge/⚡_OPERATIONAL-SME_Foundation-FF6600?style=flat-square" alt="OPERATIONAL"/></a>
  <a href="PHILOSOPHY.zh-CN.md"><img src="https://img.shields.io/badge/Anti--Cargo--Cult-Engineering-DC143C?style=flat-square" alt="Anti-Cargo-Cult"/></a>
</p>

<p align="center">
  <em>长得快。能弯，但不会断。为长久而生。</em> 🎋
</p>

---

> **给只想快速扫过的人，重点摘要：**
> - ISMS CORE 把合规判断从审计阶段前移到设计阶段——政策陈述明确、可测试的要求；审计人员验证已文件化的决策，而不是替你做出决策
> - 五项内容产品：**FRAMEWORK**（完整 SSE 工程、受监管行业、多框架）、**OPERATIONAL**（聚焦中小企业、ISO 27001 + GDPR、实用检查表）、**PRIVACY**（ISO 27701:2025 隐私信息管理）、**CLOUD**（ISO 27018:2025 云端 PII 保护），以及 **AI**（ISO 42001:2023 人工智慧管理系统）
> - FRAMEWORK 与 OPERATIONAL 以 53 个控制套件涵盖 ISO 27001:2022 附录 A 全部 93 项控制措施；PRIVACY 增加 21 个控制群组；CLOUD 增加 12 个控制群组；AI 增加 12 个控制群组
> - **平台**（WebUI + API）架构在其上，把静态文件变成可运作的合规管理系统——五项产品集中一处管理
> - 自架、以地端部署为设计前提——你的合规证据始终在自己的掌控与司法管辖之下
> - 这不是随插即用。你需要合格 CISO、Python 执行能力，以及把决策文件化的意愿

---

> *「第一原则是，你绝不能欺骗自己——而你自己正是最容易受骗的人。」*
> — Richard Feynman

> *「当旧范式再也无法容纳在其中累积的异常时，科学革命就会发生。」*
> — Thomas Kuhn，《科学革命的结构》

---

## 关于「范式」一词的描述

Kuhn 把「范式转移」保留给整个学科围绕新框架重建的时刻——当累积的异常使旧模型再也站不住脚，而由新模型取而代之。这里谈的不是那种情况。

ISO 27001 并没有坏掉。认证机构仍然使用同一套附录 A 准则进行审计。标准的用语——「适当的控制措施」、「充分的措施」——并没有改变。ISMS CORE 完全在 ISO 27001:2022 之内运作，而非在其之外。

但在 ISMS *实施* 的领域里，存在一个真正的架构选择：**专业判断施加于何处**——在设计阶段还是在审计阶段。这个选择会实际影响证据如何产生、审计如何进行，以及合规究竟代表真正的安全，还是合规表演。本文要描述的就是这件事。

---

## 🎯 什么是 ISMS CORE？

<p>
<img src="https://img.shields.io/badge/🏗️_FRAMEWORK-SSE_Engineering-9400D3?style=flat-square" alt="FRAMEWORK"/>
<img src="https://img.shields.io/badge/⚡_OPERATIONAL-SME_Foundation-FF6600?style=flat-square" alt="OPERATIONAL"/>
<img src="https://img.shields.io/badge/🔒_PRIVACY-ISO_27701_2025-7030A0?style=flat-square" alt="PRIVACY"/>
<img src="https://img.shields.io/badge/☁️_CLOUD-ISO_27018_2025-00897B?style=flat-square" alt="CLOUD"/>
<img src="https://img.shields.io/badge/🤖_AI-ISO_42001_2023-FF6B35?style=flat-square" alt="AI"/>
<img src="https://img.shields.io/badge/Controls-99_Groups_/_4_Standards-32CD32?style=flat-square" alt="99 Groups"/>
</p>

ISMS CORE 提供**五项各自不同的合规产品**，针对不同的组织需求设计：

- **FRAMEWORK (SSE — Secure Systems Engineering)**：为具有复杂多重法规要求的受监管行业而设计的工程化合规系统（ISO 27001:2022）
- **OPERATIONAL**：为寻求 ISO 27001 认证的中小企业而设计的古典 ISMS，搭配自动化辅助的合规作业（ISO 27001:2022）
- **PRIVACY**：隐私信息管理系统延伸模块，涵盖 21 个控制群组（ISO 27701:2025），横跨控管者、处理者与共同责任领域
- **CLOUD**：云端服务中的 PII 保护延伸模块，涵盖 12 个 ISO 27018:2025 附录 A 控制群组，适用于云服务提供商与处理者
- **AI**：人工智慧管理系统延伸模块，涵盖 12 个控制群组（ISO 42001:2023），适用于开发或部署 AI 系统的组织

五项产品全都采用代码驱动、证据自动化、工程师设计的做法。如果你要找的是 Word 文件模板、「实施适当的安全措施」这类泛泛指南，或是靠人工搜集证据的年度合规快照——那这不是适合你的工具。

---

## 📊 传统 ISMS 与 ISMS CORE 的对比

<p>
<img src="https://img.shields.io/badge/Judgment-At_Design_Time-00AA00?style=flat-square" alt="Design Time"/>
<img src="https://img.shields.io/badge/Evidence-Automated-0066CC?style=flat-square" alt="Automated"/>
<img src="https://img.shields.io/badge/Requirements-Testable-DC143C?style=flat-square" alt="Testable"/>
</p>

| 面向 | 传统 ISMS | ISMS CORE（两种版本） |
|--------|-----------------|---------------------------|
| **文件格式** | Word/PDF 文件、人工模板 | Markdown 政策 + Python 脚本 + 产出的工作簿 |
| **证据收集** | 人工搜集（萤幕截图、日志、批准记录） | 结构化工作簿产出（FRAMEWORK：由控制措施衍生、对照系统现况人工完成的评估工作簿；OPERATIONAL：由政策衍生的合规检查表） |
| **要求具体程度** | 「定期备份」、「适当的加密」 | 「以 AES-256 加密的备份，每季度透过评估工作簿验证」（可测试、可度量） |
| **专业判断的位置** | 审计讨论（由审计人员解释「充分」） | 模型设计（组织把解释文件化，审计人员负责验证） |
| **合规验证** | 年度快照（单一时点的评估） | 周期性验证（工作簿可随需重新产生，由评估人员依既定计划完成） |
| **政策更新** | 人工修订文件，以档名做版本控制 | 版控的 Markdown，可重新产生并与政策保持同步的工作簿 |
| **例外处理** | 与审计人员临时讨论 | 结构化流程（FRAMEWORK：POL-01 五步骤；OPERATIONAL：内嵌于控制措施政策） |
| **法规适用性** | 含糊（「我们在适用范围内遵循 GDPR」） | 明确（FRAMEWORK：POL-00 第 1/2/3 级；OPERATIONAL：控制措施政策中界定聚焦的范围） |
| **审计准备** | 花数周搜集本应早已存在的证据 | 数小时即可汇整——前提是评估已按计划完成（工作簿已预先产生、证据已预先文件化） |
| **控制措施实施证据** | 「我们有防火墙」（相信我们） | 评估工作簿载明每项要求项目的合规状态、上次评估日期与佐证文件（请自行验证） |

---

## ⚙️ 范式转移：专业判断发生在哪里？

这是 ISMS CORE 背后的核心构想。在传统 ISMS 中，专业判断往往发生在审计期间——由审计人员决定什么叫「充分」。在 ISMS CORE 中，专业判断发生在政策设计期间——由组织决定、明确文件化，审计人员则验证这项已文件化的决策。

### ❌ 传统 ISMS（判断发生于审计期间）

1. 撰写政策：「备份应以适当的演算法加密」
2. 实施：安装备份系统、启用加密
3. 审计阶段：
   - 审计人员：「用什么演算法？」
   - 你：「厂商的预设值，没特别改」
   - 审计人员：「这样适当吗？」
   - 你：「我们觉得应该可以？」
   - 审计人员：*[开立发现事项]*「加密的充分性未文件化」
4. 结果：开立发现事项、必须矫正、改写政策、重新举证

### ✅ ISMS CORE（判断发生于模型设计期间）

1. 撰写政策：「备份应至少使用 AES-256 加密，每季度测试恢复能力」
2. 实施：设置备份系统、将设置文件化、记录实际使用的演算法
3. 建立评估：Python 脚本依政策范围中的明确要求产生结构化工作簿——评估人员逐项标记为合规／部分合规／不符合／不适用，并记录佐证证据（设置撷取、上次测试日期、恢复结果）
4. 审计阶段：
   - 审计人员：「让我看备份加密的合规情形」
   - 你：「这是已完成评估的工作簿、它据以评估的政策，以及设置证据。两边都载明演算法为 AES-256。」
   - 审计人员：*[检视工作簿与证据]*「……合规。」
5. 结果：这项控制措施未开立发现事项。审计顺利推进。

**差别在哪里：**「用什么演算法？这样适当吗？」这个问题在**政策设计期间**就已回答（CISO 载明「至少 AES-256」），并在**评估期间**完成验证（工作簿确认两者一致）。审计人员验证这项已文件化决策的品质——他们不会替你做出决策。

---

## 🔀 四项产品：依你的需求选择

### ⚡ OPERATIONAL（中小企业的基础 ISMS）

<p>
<img src="https://img.shields.io/badge/Target-SME_/_Startup-FF6600?style=flat-square" alt="SME"/>
<img src="https://img.shields.io/badge/Effort-3–6_months-FFD700?style=flat-square" alt="3-6 months"/>
<img src="https://img.shields.io/badge/Regulatory-ISO_27001_+_nFADP-0066CC?style=flat-square" alt="ISO 27001"/>
<img src="https://img.shields.io/badge/Python-Basic-32CD32?style=flat-square" alt="Basic Python"/>
</p>

**适用对象：**
- 寻求 ISO 27001 认证的中小型企业
- 法规范围聚焦的组织（ISO 27001 + 瑞士 nFADP + 有条件适用 GDPR）
- 想要古典 ISMS 结构、同时享有自动化好处的团队

**你会拿到什么：**
- **架构**：OP-POL（政策）→ Python 脚本（工作簿生成器）→ 评估工作簿（合规检查表）
- **涵盖范围**：53 个控制套件，涵盖附录 A 全部 93 项控制措施
- **自动化**：由 Python 产生的 Excel 合规检查表，反映 OP-POL 中定义的要求
- **证据**：透过工作簿进行的每季度／每年合规评估，由评估人员人工完成
- **方法论**：古典 ISMS 结构，政策以 1:1 堆叠（相关控制措施共用政策）
- **法规支持**：ISO 27001:2022 + 瑞士 nFADP + GDPR（于适用时）
- **治理**：内嵌于控制措施政策（没有独立的 POL-00/POL-01 中继层）

**工作簿如何建立：**

每份 OP-POL 的撰写方式，都是依中小企业的情境与范围，按比例回应该控制措施的目标。Python 脚本产生结构化评估工作簿，其中的要求对应 OP-POL——这是因为脚本在撰写时就反映了那些要求，而不是因为它在执行时解析政策。工作簿是**由政策衍生**：OP-POL 是唯一真实来源。评估人员人工完成工作簿，逐项要求标记为合规／部分合规／不符合／不适用，并记录佐证证据。

**适用性声明（SoA）：**SoA 是 ISO 27001:2022 条款 6.1.3(d) 下的强制认证产物。ISMS CORE 不会自动产生 SoA——它是组织的决策文件，把控制措施的适用性对应到你的情境、排除项目与理由。53 个控制套件（涵盖 93 项附录 A 控制措施）为产出 SoA 提供结构化输入；完成 SoA 是组织的责任。如果你是 ISMS 新手，请确认你的实施包含合格从业人员提供的 SoA 指南。

**前置条件：**
- 基本的 Python 执行能力（执行脚本以产生检查表）
- 理解 ISO 27001 附录 A 控制措施
- 愿意明确地把决策文件化（可测试的要求，而非含糊的陈述）
- 每季度评估的纪律（完成工作簿、追踪合规状态）

**最适合：**「我们需要 ISO 27001 认证，希望合规追踪有自动化协助，但不需要多重法规治理的复杂度。」

---

### 🏗️ FRAMEWORK (SSE — Secure Systems Engineering)

<p>
<img src="https://img.shields.io/badge/Target-Regulated_Industries-9400D3?style=flat-square" alt="Regulated"/>
<img src="https://img.shields.io/badge/Effort-6–12_months-FF4500?style=flat-square" alt="6-12 months"/>
<img src="https://img.shields.io/badge/Regulatory-Multi--Framework-DC143C?style=flat-square" alt="Multi-Framework"/>
<img src="https://img.shields.io/badge/Python-Intermediate-0066CC?style=flat-square" alt="Intermediate Python"/>
</p>

**适用对象：**
- 受监管行业（金融服务、医疗照护、关键基础设施）
- 具有复杂多重法规要求的组织（GDPR + DORA + NIS2 + PCI DSS + FINMA）
- 能胜任全面、证据驱动的合规工作与 Python 产生的评估工具的技术团队

**你会拿到什么：**
- **基础治理**：
  - **POL-00**（法规适用性架构）：第 1/2/3 级分类、每季度监控、触发式评估
  - **POL-01**（ISMS 治理架构）：权责界线、能力要求、五步骤例外流程、六步骤变更控制、内部挑战协议
- **架构**：POL（政策）→ IMP（实施规格）→ Python（工作簿生成器）→ 工作簿（证据）
- **每个控制套件**：POL + IMP (UG/TG) + SCR + WKBK + REF + FORM + INS + CTX
- **涵盖范围**：53 个控制套件，涵盖附录 A 全部 93 项控制措施。评分 4–5 的控制措施拥有最结构化、最全面的工作簿，以及最客观的可度量准则。评分 1–3 的控制措施则使用依该控制措施本身可度量程度调整规模的工作簿。
- **证据**：由 Python 脚本产生的结构化评估工作簿，由评估人员周期性完成。评分反映的是工作簿的深度与证据的客观性，而不是基础设施查询的自动化程度。
- **方法论**：评分 1–5 系统（见下文）
- **法规支持**：多框架（ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA）

**工作簿如何建立：**

FRAMEWORK 的工作簿是**由控制措施衍生**：直接且全面地对照该控制措施所处理的每一个面向而建立，涵盖 ISO 27001 所要求的完整范围。POL 本身也以同样的范围撰写。政策与工作簿是对照控制措施要求共同设计的，不经过中小企业比例原则的筛选。结果是比 OPERATIONAL 同类工作簿更详尽、更结构化的评估。评估人员人工完成每本工作簿，逐项要求标记为合规／部分合规／不符合／不适用，并附上佐证证据（设置、凭证、日志、批准记录）。审计人员对照政策所陈述的要求，验证已完成的工作簿与佐证文件。

**前置条件：**
- Python 3.11+ 执行能力（执行脚本以产生工作簿）
- 理解 ISO 27001 附录 A 控制措施与 SSE 方法论
- 愿意完成附带佐证证据的结构化评估的技术团队
- 有意愿投入全面、证据驱动的合规（而非打勾式合规）

**评分 1–5 系统（仅 FRAMEWORK）：**

<p>
<img src="https://img.shields.io/badge/Score_5-Highest_Objectivity-00AA00?style=flat-square" alt="Score 5"/>
<img src="https://img.shields.io/badge/Score_4-High_Objectivity-32CD32?style=flat-square" alt="Score 4"/>
<img src="https://img.shields.io/badge/Score_3-Moderate-FFD700?style=flat-square" alt="Score 3"/>
<img src="https://img.shields.io/badge/Score_2-Lower-FF6600?style=flat-square" alt="Score 2"/>
<img src="https://img.shields.io/badge/Score_1-Attestation--Based-DC143C?style=flat-square" alt="Score 1"/>
</p>

每项附录 A 控制措施都依**证据客观性**评分——评分反映的是该控制措施的要求能被多直接、多可度量地验证，因而也反映所产生的工作簿能有多全面、多客观。这是对证据品质的评分，不是组织原则；FRAMEWORK 与 OPERATIONAL 都使用相同的 A.5/A.6/A.7/A.8 结构与 53 个控制套件。

- **评分 5**：最高证据客观性（日志保留、备份状态、实际使用的演算法——要求可直接度量，通过／不通过的准则明确无疑）
- **评分 4**：高证据客观性（访问审查、修补合规——多数要求可客观验证，少数需要人工判断）
- **评分 3**：中等证据客观性（事件响应——流程与结果可文件化并追踪，但无法完全化约为通过／不通过）
- **评分 2**：较低证据客观性（安全培训、供应商审查——以人工判断为核心，证据以声明为基础）
- **评分 1**：最低证据客观性（物理安全、人资流程——评估主要依赖观察与声明）

FRAMEWORK 在所有评分等级都优先讲求严谨。评分较高的控制措施产生的工作簿具有更客观、可度量的准则。评分较低的控制措施所产生的工作簿同样全面且结构化，但更依赖评估人员的判断与佐证文件。评分描述的是**控制措施本身的可度量程度**，而不是脚本目前的能力。

**最适合：**「我们是金融机构，需要遵循 DORA + FINMA + ISO 27001 + GDPR，也具备结构化证据自动化的技术能力。」

---

### 🔒 PRIVACY（ISO 27701:2025——隐私信息管理）

<p>
<img src="https://img.shields.io/badge/Standard-ISO_27701_2025-7030A0?style=flat-square" alt="ISO 27701:2025"/>
<img src="https://img.shields.io/badge/Groups-21_Control_Groups-9400D3?style=flat-square" alt="21 Groups"/>
<img src="https://img.shields.io/badge/Scope-PIMS_Extension-7030A0?style=flat-square" alt="PIMS"/>
</p>

**适用对象：**
- 以控管者、处理者或共同责任身分处理个人数据的组织
- 把 ISO 27001 ISMS 扩充到纳入隐私信息管理系统（PIMS）的组织
- 在 ISO 27001 认证之外，同时寻求 ISO 27701:2025 合规的团队

**你会拿到什么：**
- **架构**：PRIV-POL（政策）→ 合规检查表工作簿（Python 产生）
- **涵盖范围**：21 个控制群组（ISO 27701:2025）
  - 控管者（8 个群组）：A.1.x——同意、目的正当性、搜集、数据主体权利
  - 处理者（5 个群组）：A.2.x——处理义务、再处理者、记录
  - 共同（8 个群组）：A.3.x——数据最少化、正确性、透明性、安全控制措施
- **治理**：PRIV-POL-00（架构导论）+ PRIV-POL-01（隐私政策基线）+ 21 份针对特定控制措施的 PRIV-POL 文件
- **证据**：由 Python 产生的合规检查表工作簿，每个控制群组一本

**前置条件：**
- 基本的 Python 执行能力
- 理解 GDPR／隐私法下数据控管者与处理者的角色差异
- 已建置 ISO 27001 ISMS（PIMS 是延伸模块，不是独立产品）

**最适合：**「我们已通过 ISO 27001 认证，需要延伸到 ISO 27701，向客户与监管机关展现结构化的隐私管理。」

---

### ☁️ CLOUD（ISO 27018:2025——云端服务中的 PII）

<p>
<img src="https://img.shields.io/badge/Standard-ISO_27018_2025-00897B?style=flat-square" alt="ISO 27018:2025"/>
<img src="https://img.shields.io/badge/Groups-12_Control_Groups-00897B?style=flat-square" alt="12 Groups"/>
<img src="https://img.shields.io/badge/Scope-Cloud_PII_Processor-00897B?style=flat-square" alt="Cloud PII"/>
</p>

**适用对象：**
- 代表客户处理 PII 的云服务提供商（CSP）
- 依 GDPR 或类似隐私法担任云端处理者的组织
- 需要展现云端环境特有 PII 控制措施的团队

**你会拿到什么：**
- **架构**：CLD-POL（政策）→ 合规检查表工作簿（Python 产生）
- **涵盖范围**：12 个控制群组，涵盖 ISO 27018:2025 附录 A 控制措施
  - A.1 一般 | A.2 同意 | A.3 目的 | A.4 搜集 | A.5 数据最少化
  - A.6 使用／保留／揭露 | A.7 正确性 | A.8 公开性 | A.9 个人参与
  - A.10 当责 | A.11 信息安全 | A.12 隐私合规
- **治理**：12 份 CLD-POL 文件，每个控制群组一份
- **证据**：由 Python 产生的合规检查表工作簿

**前置条件：**
- 基本的 Python 执行能力
- 云端服务交付的情境（该标准处理的是 CSP 特有的义务）
- 已建置 ISO 27001 ISMS（ISO 27018 是在 ISO 27001 之上的叠加层）

**最适合：**「我们是处理客户 PII 的云服务提供商——需要向企业客户与监管机关展现 ISO 27018 合规。」

---

## 📋 产品比较

| 功能 | FRAMEWORK (SSE) | OPERATIONAL | PRIVACY | CLOUD | AI |
|---------|----------------|-------------|---------|-------|----|
| **标准** | ISO 27001:2022 | ISO 27001:2022 | ISO 27701:2025 | ISO 27018:2025 | ISO 42001:2023 |
| **目标对象** | 受监管行业 | 中小企业 | PII 控管者／处理者 | 云端 PII 处理者 | AI 开发者／部署者 |
| **控制群组** | 53 个群组／93 项控制措施 | 53 个群组／93 项控制措施 | 21 个群组 | 12 个群组 | 12 个群组 |
| **政策格式** | POL + IMP (UG/TG) | OP-POL | PRIV-POL | CLD-POL | AI-POL |
| **工作簿类型** | 由控制措施衍生的评估工作簿 | 由政策衍生的检查表 | 隐私合规检查表 | 云端 PII 合规检查表 | AI 治理政策 |
| **基础治理** | POL-00 + POL-01（第 1/2/3 级、权责界线、例外处理） | 古典 ISMS（无中继层） | PRIV-POL-00 + PRIV-POL-01 | 内嵌于 CLD-POL | AI-POL-00 + AI-POL-01 |
| **法规范围** | ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA | ISO 27001 + nFADP + 有条件适用 GDPR | ISO 27701:2025（PIMS 延伸） | ISO 27018:2025（云端叠加） | ISO 42001:2023 + EU AI Act |
| **Python 技能** | 中阶 | 基本 | 基本 | 基本 | 基本 |
| **实施投入** | 高（6–12 个月） | 中等（3–6 个月） | 中等（ISMS 的加挂元件） | 低（ISMS 的加挂元件） | 中等（ISMS 的加挂元件） |
| **可独立使用？** | 是 | 是 | 否——延伸 ISO 27001 ISMS | 否——延伸 ISO 27001 ISMS | 否——延伸 ISO 27001 ISMS |

**可以组合产品吗？**可以——这是设计上的安排：
- ISO 27001 基础 → 使用 FRAMEWORK (SSE) 或 OPERATIONAL
- 加上隐私义务 → 加上 PRIVACY（ISO 27701）
- 加上云端 PII 处理 → 加上 CLOUD（ISO 27018）
- 加上 AI 系统治理 → 加上 AI（ISO 42001）
- 平台以单一整合仪表板管理全部五项产品

**不要混用：**OPERATIONAL 是自成一体的。把 POL-00/POL-01 加到 OPERATIONAL，会让中小企业的实施过度复杂。

---

## 🏛️ 基础治理详解

### 🏗️ FRAMEWORK (SSE) 基础

<p>
<img src="https://img.shields.io/badge/POL--00-Regulatory_Applicability-9400D3?style=flat-square" alt="POL-00"/>
<img src="https://img.shields.io/badge/POL--01-Governance_Framework-0066CC?style=flat-square" alt="POL-01"/>
</p>

当你要应对**6 个以上的法规框架**（ISO 27001、GDPR、DORA、NIS2、PCI DSS、FINMA）时：

**POL-00 解决：**「这些法规中，哪些才真正适用于我们？」
- **第 1 级（强制）**：法律义务（ISO 27001、瑞士 nFADP、适用范围内的 GDPR）
- **第 2 级（有条件）**：由业务情境触发（若为金融机构则适用 DORA，若处理卡片则适用 PCI DSS）
- **第 3 级（参考信息）**：最佳实务（NIST、CIS、OWASP）
- 每季度监控可检测第 2 级何时变成第 1 级（业务扩张、法规变动）

**POL-01 解决：**「内部由谁决定我们如何合规，以及我们如何处理复杂度？」
- **权责界线**：CISO（技术）、法务／合规（法规）、高级管理层（策略）
- **例外处理**：当控制措施在不同框架间冲突时（例如 GDPR 的删除与 FINMA 的保留要求）所采行的五步骤内部流程
- **变更管理**：法规要求演进时所采行的六步骤流程
- **挑战协议**：当 ISMS 利害关系人质疑多框架解释时，用以解决内部分歧的结构化流程

> **注意：**内部挑战协议规范的是 ISMS 设计与运作期间，你自己组织内 CISO、法务与高阶管理团队之间的分歧。外部审计的分歧则依认证机构的标准申诉与异议程序处理——挑战协议不约束认证机构审计人员，也不适用于他们。

**结果：**为复杂的法规环境提供明确的治理。没有 POL-00/POL-01，要一致地调和 6 个框架在结构上就很困难。

### ⚡ OPERATIONAL 基础

<p>
<img src="https://img.shields.io/badge/Governance-Classical_ISMS-FF6600?style=flat-square" alt="Classical ISMS"/>
<img src="https://img.shields.io/badge/No_Meta--Layer-By_Design-32CD32?style=flat-square" alt="No Meta-Layer"/>
</p>

**为什么 OPERATIONAL 没有 POL-00/POL-01：**

当你只实施 **ISO 27001**（或有条件地加上 GDPR）时：
- 法规范围清楚且有限（没有第 1/2/3 级的复杂度）
- 控制措施的适用性记载于 SoA（ISO 27001 条款 6.1.3 流程，标准 ISMS 做法）
- 例外处理内嵌于控制措施政策（每份 OP-POL 依 ISO 27001 指南处理「若控制措施无法实施」的情形）
- 治理采古典 ISMS 结构（依条款 5、9.2、9.3，CISO → 管理评审 → 内部审计）

**结果：**中小企业不需要治理中继层。古典 ISMS 结构就能处理 ISO 27001 的复杂度，不必额外增加治理负担。

**如果中小企业成长为受监管行业**（成为受 DORA 规范的金融机构，或受理需要 PCI DSS 的支付卡）：
- 从 OPERATIONAL 转换到 FRAMEWORK (SSE)
- 加上 POL-00（此时需要第 1/2/3 级的法规追踪）
- 加上 POL-01（此时需要针对多框架冲突的正式例外处理）

---

## 🔬 关键创新

### 1. 第 1/2/3 级法规框架（POL-00——仅 FRAMEWORK）

<p>
<img src="https://img.shields.io/badge/Tier_1-Mandatory-DC143C?style=flat-square" alt="Tier 1 Mandatory"/>
<img src="https://img.shields.io/badge/Tier_2-Conditional-FF6600?style=flat-square" alt="Tier 2 Conditional"/>
<img src="https://img.shields.io/badge/Tier_3-Informational-0066CC?style=flat-square" alt="Tier 3 Informational"/>
</p>

**解决的问题：**「GDPR 适用吗？PCI DSS 适用吗？那 DORA 呢？」

**传统 ISMS：**含糊的引用、审计期间的争论、范围混淆

**FRAMEWORK (SSE) 的做法：**
- **第 1 级（强制）**：法律义务（ISO 27001、瑞士 nFADP、适用范围内的 GDPR）
- **第 2 级（有条件）**：由业务情境触发（若为金融机构则适用 DORA，若处理卡片则适用 PCI DSS）
- **第 3 级（参考信息）**：最佳实务（NIST、CIS、OWASP）
- 每季度监控、文件化的评估、高级管理层批准

**OPERATIONAL：**法规范围较简单（ISO 27001 + nFADP + 有条件适用 GDPR），直接记载于控制措施政策，不采分级架构。

**结果（FRAMEWORK）：**零含糊。若 X 已被记载为第 2 级——不适用，并有每季度监控证明触发条件尚未发生——审计人员就无法主张「你们应该遵循 X」。

---

### 2. 具备能力要求的治理（POL-01——仅 FRAMEWORK）

<p>
<img src="https://img.shields.io/badge/FRAMEWORK-Only-9400D3?style=flat-square" alt="Framework Only"/>
<img src="https://img.shields.io/badge/Authority-Boundaries_Defined-0066CC?style=flat-square" alt="Authority Boundaries"/>
</p>

**解决的问题：**「内部由谁决定什么叫充分？如果利害关系人对解释有分歧怎么办？」

**传统 ISMS：**权责界线未定义、主观解释、过时的决策

**FRAMEWORK (SSE) 的做法：**
- **权责界线**：CISO（技术）、法务／合规（法规）、高级管理层（策略）
- **能力要求**：CISO = CISSP/CISM + 5 年经验 + ISO 27001 知识（已文件化、可验证）
- **内部挑战协议**：解决内部分歧的结构化流程（以证据为基础，须引用 ISO 27001 条款）
- **例外处理**：五步骤内部流程（记录 → 评估风险 → 提出方案 → 取得批准 → 记载于 SoA）

**OPERATIONAL：**采用古典 ISMS 治理（依 ISO 27001 条款 5、9.2、9.3，CISO → 管理评审 → 内部审计）。例外处理内嵌于控制措施政策。

**结果（FRAMEWORK）：**内部治理决策已文件化、可追溯、可辩护。审计人员验证这些决策的品质与可追溯性——而不是取代它们。

---

### 3. 结构化证据产生

<p>
<img src="https://img.shields.io/badge/Evidence-Control--Derived_(FW)-9400D3?style=flat-square" alt="Control Derived"/>
<img src="https://img.shields.io/badge/Evidence-Policy--Derived_(OP)-FF6600?style=flat-square" alt="Policy Derived"/>
<img src="https://img.shields.io/badge/Format-Python_+_Excel-32CD32?style=flat-square" alt="Python Excel"/>
</p>

**解决的问题：**「证明你的控制措施已实施。证明你的设置是合规的。」

**传统 ISMS：**萤幕截图、人工日志、「这里有个样本」——每次审计前才匆忙搜集

**FRAMEWORK (SSE)：**
- Python 脚本产生全面的评估工作簿，对照完整的控制措施范围建立
- 工作簿涵盖该控制措施所处理的每一个面向——不经中小企业比例原则的筛选
- 评估人员完成评估：逐要求领域标记合规／部分合规／不符合／不适用，并附上佐证文件（设置、凭证、日志、批准记录）
- 评分 4–5 的控制措施所产生的工作簿，多数准则可直接度量——评估人员从系统取出数值并记录（已设置的保留期间、实际使用的演算法、上次测试日期）
- 评分 1–3 的控制措施所产生的工作簿同样全面，但更依赖评估人员的判断与以声明为基础的证据
- 证据：已完成的工作簿 + 佐证文件。审计人员可对照政策所陈述的要求，逐项验证。

**OPERATIONAL：**
- Python 脚本产生结构化合规检查表，反映 OP-POL 中定义的要求
- 评估人员每季度完成：逐项要求标记合规／部分合规／不符合／不适用
- 证据：已完成的工作簿 + 佐证文件（凭证、设置、声明）

**真正重要的区别：**OPERATIONAL 的工作簿是**由政策衍生**——检查表反映 OP-POL 所定义的内容，范围依中小企业情境界定。FRAMEWORK 的工作簿是**由控制措施衍生**——对照该控制措施要求的完整范围全面建立。起点不同、深度不同、审计对话也不同。

**结果：**证据结构化、可追溯，且可随需重新产生。审计人员对照明确、可测试的要求客观验证合规——而不是靠「相信我」。

---

### 4. 控制套件整并

<p>
<img src="https://img.shields.io/badge/53_Packs-93_Controls-0066CC?style=flat-square" alt="53 Packs"/>
<img src="https://img.shields.io/badge/DRY-Don't_Repeat_Yourself-FF6600?style=flat-square" alt="DRY"/>
</p>

**解决的问题：**「为什么 93 项附录 A 控制措施要有 93 份各自独立的政策？这根本是文件地狱。」

**传统 ISMS：**93 份各自独立的 Word 文件，或一份 300 页的庞大政策（两者都不好）

**ISMS CORE 的做法（两种版本）：**
- **53 个控制套件**涵盖 **93 项附录 A 控制措施**
- 当相关控制措施处理共同的流程或技术时，会共用政策：
  - A.5.15-16-18：身分与访问管理（IAM 横跨多项控制措施）
  - A.8.1-7-18-19：端点安全（共用端点管理）
  - A.5.30-8.13-14：业务连续性与灾难恢复（BC/DR 生命周期跨越界线）
- 堆叠理由记载于每份政策
- 每项控制措施的特定 ISO 27001 要求都分别处理（不会在泛用套装中消失）

**结果：**合乎逻辑的分组（不是任意凑合）。维护更容易（更新一份政策，连带影响相关控制措施）。审计人员仍可逐项验证每一项控制措施（要求可追溯）。

---

### 5. 可测试的要求

<p>
<img src="https://img.shields.io/badge/Requirements-Explicit_Pass/Fail-00AA00?style=flat-square" alt="Pass Fail"/>
<img src="https://img.shields.io/badge/No_More-%22Appropriate_Measures%22-DC143C?style=flat-square" alt="No Vague"/>
</p>

**解决的问题：**「我们的政策写著『适当的安全措施』。审计人员说这样不够。」

**传统 ISMS：**含糊的要求（「定期审查」、「足够的加密」、「充分的监控」）

**ISMS CORE：**具备明确通过／不通过准则的可测试要求：

| 含糊（传统） | 可测试（ISMS CORE） |
|---------------------|---------------------|
| 「备份应定期执行」 | 「备份应每日执行，以 AES-256 加密，每季度测试恢复能力」 |
| 「访问应定期审查」 | 「访问权限应每季度审查，记载于访问审查工作簿，并由系统拥有者批准」 |
| 「应使用适当的加密」 | 「加密应使用 AES-256（对称）、RSA-4096（非对称）、TLS 1.3（传输）。禁止使用：DES、3DES、MD5、SHA-1、TLS 1.0/1.1」 |
| 「安全事件应予以处理」 | 「事件应在 4 小时内分级（A.5.25），响应在 24 小时内启动（A.5.26），事件后检讨在 7 天内完成（A.5.27）」 |

**结果：**审计人员客观验证。不必再争论「这样适当吗？」——要求明确，证据自会显示合规或不合规。

---

## 🖥️ 部署模式：地端优先

<p>
<img src="https://img.shields.io/badge/Deployment-On--Premises-2E8B57?style=flat-square" alt="On-Premises"/>
<img src="https://img.shields.io/badge/Data_Sovereignty-By_Design-0066CC?style=flat-square" alt="Data Sovereignty"/>
<img src="https://img.shields.io/badge/CLOUD_Act-Risk_Mitigated-DC143C?style=flat-square" alt="CLOUD Act"/>
</p>

ISMS CORE 的设计是**自架、地端部署的平台**。这是刻意的架构决策，不是产品路线图上的限制。

你的 ISMS 证据反映你的基础设施设置、组织决策与控制措施实施情形。这是敏感的运营数据——而在 2025–2026 年，这些数据存放在哪里、受哪个司法管辖权规范，本身已成为重大的安全与合规议题。

**欧洲数据主权的背景：**

欧洲对美国云端基础设施的依赖，已因为具体的法律风险而成为董事会层级的议题。美国 2018 年的 CLOUD Act 允许美国当局强制美国科技公司提供被要求的数据，不论该数据实际储存在何处——包括存放在欧盟数据中心的数据。截至 2026 年，欧盟没有任何法律废除这项域外效力。在欧洲经营主权云服务的美国大型超大规模云端业者已确认，他们无法绝对保证存放在欧盟的数据永远不会被美国当局要求提供。

欧盟以《欧洲数位主权宣言》（2025 年 11 月）回应，这是欧盟成员国强化欧洲对数位基础设施掌控的共同承诺。欧洲主权云投资预计在 2025 至 2027 年间成长超过三倍。云端回流——把工作负载从公有云移回地端或欧洲运营的基础设施——是正在成长的趋势，对受监管行业、政府与安全敏感的工作负载尤其如此。

ISMS 平台——保存贵组织的安全控制措施证据、合规状态、风险评估、缺口分析与审计产物——正好落在不应受外国司法管辖法律访问的那一类数据里。

**地端部署对 ISMS CORE 的意义：**
- Python 脚本在你的环境中执行，对你的系统运作
- 产出的工作簿留在你的基础设施内
- 没有数据离开你的组织到第三方平台
- 评估计划、储存与访问都由你掌控
- 你的合规证据不依赖任何厂商

**关于未来托管服务的附注：**

ISMS CORE 的托管或可透过 SaaS 访问的版本并未排除在产品路线图之外。然而，在任何这类架构中，数据主权都是设计变数——而不是事后补上的考量。未来任何托管服务都必须以架构上可验证、而非商业上片面宣称的方式，处理司法管辖权、数据存放地、法律访问风险与运营控制。对于受监管行业或上述顾虑重大的司法管辖区内的组织，地端模式仍是预设选择。

---

## ⚖️ 这不是什么

<p>
<img src="https://img.shields.io/badge/NOT-Plug_and_Play-DC143C?style=flat-square" alt="Not Plug and Play"/>
<img src="https://img.shields.io/badge/NOT-Beginner_Friendly-DC143C?style=flat-square" alt="Not Beginner Friendly"/>
<img src="https://img.shields.io/badge/IS-Engineering_Driven-00AA00?style=flat-square" alt="Engineering Driven"/>
<img src="https://img.shields.io/badge/IS-Audit_Optimised-00AA00?style=flat-square" alt="Audit Optimised"/>
</p>

**这不是：**
- ❌ **随插即用的模板**：你必须理解 ISO 27001、依自己的情境调整、做出并记录决策（不是填空）
- ❌ **顾问的替代品**：你需要能力（具备 ISO 27001 知识的 CISO、负责法规解释的法务／合规人员）。平台加速实施——但不取代专业能力。
- ❌ **神奇认证按钮**：你仍然要实施控制措施、搜集证据、通过审计。平台让这件事变得系统化，而不是自动化。
- ❌ **对初学者友善**：如果你不具备风险评估、控制目标或基本 Python 的理解，请先从 ISO 27001 培训开始。
- ❌ **与厂商无关的通用样板**：政策引用具体技术（AES-256、TLS 1.3、MFA）。你必须依自己的技术堆叠调整（AWS、Azure、地端、混合）。
- ❌ **零维护的解决方案**：基础设施变更时脚本需要更新，政策需要年度审查，证据必须周期性重新产生。

**这是：**
- ✅ **工程驱动的合规**：以系统化、代码为基础、证据自动化的做法推动 ISMS
- ✅ **有主见的框架**：我们做了决定（至少 AES-256、TLS 1.3、每季度审查）。你可以改，但这些决定是明确的——不含糊。
- ✅ **为审计最佳化**：透过把专业判断前移到模型设计来减少审计期间的含糊——审计人员验证已文件化的决策，而不是去解释含糊的内容
- ✅ **可维护**：版控的 Markdown、可重新产生的工作簿、可测试（而不是在 SharePoint 上腐烂的静态 Word 文件）
- ✅ **持续改进**：经验学习登录表、治理审查、变更控制流程（ISMS 会演进，不会停滞）
- ✅ **以设计确保数据主权**：地端部署让你的合规证据始终在自己的掌控与司法管辖之下

---

## 👥 谁该使用？

<p>
<img src="https://img.shields.io/badge/✅_Good_Fit-See_Below-00AA00?style=flat-square" alt="Good Fit"/>
<img src="https://img.shields.io/badge/❌_Bad_Fit-See_Below-DC143C?style=flat-square" alt="Bad Fit"/>
</p>

### ✅ 适合

<p>
<img src="https://img.shields.io/badge/⚡_OPERATIONAL-SMEs_seeking_certification-FF6600?style=flat-square" alt="OPERATIONAL Good Fit"/>
<img src="https://img.shields.io/badge/🏗️_FRAMEWORK-Regulated_industries-9400D3?style=flat-square" alt="FRAMEWORK Good Fit"/>
</p>

**OPERATIONAL：**
- 想要以明确、可测试的要求取得 ISO 27001 认证的中小企业
- 想要自动化协助（检查表产生），但不愿投入完整 DevOps 的团队
- 受够了含糊政策（「适当」、「定期」、「足够」）的组织
- 想要客观合规证据（而不是「相信我」这类声明）的 CISO

**FRAMEWORK (SSE)：**
- 需要多框架合规的受监管行业（金融服务：DORA + FINMA + ISO 27001）
- 想要全面、由控制措施衍生的评估，而不是中小企业范围检查表的组织
- 想要涵盖每项控制措施要求完整深度的结构化、详尽工作簿的团队
- 想要具备逐项要求明确通过／不通过准则之客观、可追溯证据的 CISO

### ❌ 不适合（两种版本）

- 想要零努力取得认证的组织
- 不具备 Python 能力的团队（脚本必须可执行，即使不大幅客制）
- 期待顾问全程呵护的 CISO（由你做决定，平台提供结构）
- 想要主观弹性的组织（「我们会在审计时决定什么叫『适当』」——不行，现在就决定，并记录下来）
- 不想被指点该怎么做的团队（平台是有主见的：AES-256，而不是「自己选加密方式」）

---

## ❓ 开立 issue 之前

**「有 SaaS 或托管版本吗？」**

目前没有。ISMS CORE 是让你在自己的环境中部署与执行的平台。这是基于数据主权的刻意设计决策——你的 ISMS 证据是敏感的运营数据，而在当前的欧洲法规环境下，自架部署是架构上稳妥的预设选择。托管版本并未排除在路线图之外，但在任何这类服务中，数据主权都会是设计要求，而不是事后补上的考量。

**「为什么评分较高的控制措施，工作簿比评分较低的更详细？」**

评分反映证据客观性——该控制措施的要求能被多直接、多可度量地验证。评分 4–5 的控制措施处理的是可以精确检查的要求（保留期间、演算法规格），因此工作簿可以逐项建立明确的通过／不通过准则。评分 1–3 的控制措施处理的要求更依赖流程、判断与声明，因此工作簿虽然全面，但更依赖评估人员的记录。两者都是完整的评估——评分描述的是证据的性质，而不是所需投入的心力。

**「我可以先用 OPERATIONAL，之后再加 POL-00/POL-01 吗？」**

可以，但不建议。OPERATIONAL 的设计就是自成一体的古典 ISMS。在实施途中加入 POL-00/POL-01，会形成比两种纯粹版本都更复杂的混合体。如果你认为自己需要 POL-00/POL-01，请直接从 FRAMEWORK 开始。如果你是中小企业，且确实只需要 ISO 27001 + GDPR，那么 OPERATIONAL 不加它们就已足够。

**「Python 脚本在我的环境中跑不起来。」**

脚本需要 Python 3.11+ 以及 `requirements.txt` 中列出的相依套件。它们在 Linux 与 macOS 上测试过。Windows PowerShell 环境可能需要调整。这是前置条件，不是支持问题。执行任何东西之前，请先读前置条件一节。

**「我可以在没有顾问的情况下用它取得 ISO 27001 认证吗？」**

技术上可以，前提是你有合格的 CISO（具备 ISO 27001 知识与相关经验），以及能做法规判定的法务／合规能力。平台加速实施——但不取代做出良好安全决策所需的专业能力。如果你不知道适用性声明是什么，请先找顾问。

**「政策引用瑞士法律（nFADP），但我不在瑞士。」**

法规框架以瑞士为主（nFADP、FINMA），因为那是设计时的情境。第 1 级的强制法规会因你所处的司法管辖区而不同。POL-00 提供做出这些判定的架构——你把第 1 级替换成自己适用的强制法规。控制措施政策（附录 A）与司法管辖区无关。治理架构（POL-00/POL-01）并未锁定特定司法管辖区，而是以司法管辖区为参数。

**「我发现政策有错，或脚本有误。」**

请开 issue，并附上：(1) 具体的文件或脚本，(2) 确切的错误或错误文本，(3) 正确的文本或预期行为，并附参考依据（ISO 27001 条款、法规条文等）。没有具体参考依据的 issue 会被关闭。「这看起来不太对」无法处理。

---

## 🖥️ 第三层：ISMS CORE 平台

FRAMEWORK 与 OPERATIONAL 是**内容产品**——政策、工作簿与指南，以静态文件的形式就能完整运作。你可以复制本储存库、执行 Python 生成器、填写 Excel 工作簿，不需要其他东西，就能拥有功能完整、可接受审计的 ISMS。

**ISMS CORE 平台**是建构在其上的运营层。它导入这两项产品，并把它们变成可运作的合规管理系统：

| 没有平台 | 有平台 |
|-----------------|---------------|
| 把政策当文件阅读 | 依关键字或控制措施跨所有政策搜寻 |
| 逐一开启 Excel 工作簿 | 查看各节与各控制群组的汇总合规分数 |
| 在试算表中人工追踪缺口 | 缺口生命周期管理，含严重度、负责人、SLA 与矫正追踪 |
| 没有跨框架的可见性 | ISO 27001 ↔ NIST CSF ↔ MITRE ATT&CK ↔ GDPR ↔ DORA 对应，即时呈现 |
| 人工搜集证据 | 具备到期追踪与新鲜度警示的证据项目 |
| 没有审计跟踪 | 完整且不可窜改的日志，记录谁在何时做了什么 |

平台是以 Docker Compose 部署于地端的技术堆叠。核心服务包括 FastAPI + PostgreSQL + Redis + OpenSearch + Celery + Angular 22 + nginx TLS + Celery Beat + 专用的漏洞情报来源容器（MITRE ATT&CK、CISA KEV、EPSS、NVD CVE、ENISA EUVD、Exploit-DB）+ 自动化连接器执行器（44 个原生连接器）。选用的 OSINT 情报来源容器另增加 12 个即时威胁情报来源。**v1.1 已上线。**同样的数据主权原则依然适用——你的合规数据不会离开你的基础设施。

平台也包含 44 个原生连接器（Microsoft、网络、身分、漏洞、ITSM、监控、云端态势、威胁情报），可把即时证据直接推送进合规数据库——支持的系统不需要人工搜集证据。

**平台是加值项，绝非必要项。**FRAMEWORK 与 OPERATIONAL 才是产品。平台是让它在规模上真正运作的引擎。

架构细节、功能与部署指南请见 [PLATFORM.zh-CN.md](PLATFORM.zh-CN.md)。

---

<p align="center">
<strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
<em>在这里，竹天线真的能用。</em> 🎋
</p>
