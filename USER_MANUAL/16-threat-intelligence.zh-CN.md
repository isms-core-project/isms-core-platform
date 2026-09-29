# 威胁情报

<p align="center"><a href="16-threat-intelligence.md">English</a> · <a href="16-threat-intelligence.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<!-- ISMS-CORE:USER-MANUAL:16-threat-intelligence:v1.3:2026-08-22 -->

---

## 概览

威胁情报章节让您即时取用 18+ 个直接整合至平台的威胁与漏洞情报来源。此功能支持 ISO 27001:2022 控制措施 A.5.7（威胁情报），并提供所需的技术深度，以评估您对当前对手技术、已遭利用的漏洞，以及来自公开 OSINT 情报源的实际 IOC 数据的曝险程度。

在侧边栏前往 **Intelligence**。

> 当 `isms-core-threat-intel` 选用设置档未启用时，所有 Intelligence 侧边栏项目仍会显示，但呈现灰色。

---

## 情报源容器

平台执行两个专用的情报源容器：

- **`isms-core-feeds`** —— 漏洞与对手情报（标准堆叠下永远启用）
- **`isms-core-threat-intel`** —— OSINT IOC 情报源（选用；以 `--profile threat-intel` 加上 `.env` 中的 `THREAT_INTEL_ENABLED=true` 启用）

---

## 情报源计划 —— 漏洞与对手情报

这些情报源在 `isms-core-feeds` 容器中执行，且永远启用。

| 情报源 | 计划（UTC） | 提供内容 |
|------|----------------|-----------------|
| **MITRE ATT&CK v19** | 每周，周日 00:00 | 完整 ATT&CK 框架 —— 战术、技术、子技术、缓解措施、对手组织、软件、攻击行动 |
| **MITRE ATLAS** | 每周，周日 00:30 | AI/ML 专属的对手技术（对抗式机器学习威胁态势） |
| **CISA KEV** | 每日 02:00 | CISA 的已知遭利用漏洞目录 —— 已遭实际利用的 CVE |
| **FIRST EPSS** | 每日 02:30 | 漏洞利用预测评分系统 —— 每个 CVE 在未来 30 天内遭利用的机率分数（0–1） |
| **NVD CVE** | 每日差异 03:00 / 每周全量 周日 01:00 | 来自 NIST NVD 的约 250,000 个 CVE，含 CVSS v2/v3/v4 分数、CWE 与 CPE 适用性 |
| **NVD CPE** | 每周，周日 01:30 | 软件／硬件产品识别码 —— 可将 CVE 关联至特定产品 |
| **ENISA EUVD** | 每日 | 欧洲漏洞数据库 —— 带已遭利用旗标的 CVE，以及高严重度（CVSS ≥ 4.0）的欧盟指派项目；以 `in_euvd` 旗标交叉充实至 NVD CVE 文件 |
| **Exploit-DB** | 每日 | 约 52,000 个公开攻击程式；以 `edb_id`、`edb_verified`（Metasploit 旗标）与 `edb_description` 交叉充实 CVE |
| **VulnCheck KEV** | 每日 04:45 | VulnCheck 自家的已知遭利用漏洞目录 —— 范围比 CISA 更广；约 67% 的项目不在 CISA KEV 中。在 CVE 浏览器上加入 `in_vulncheck_kev` 旗标，与 CISA 的 `in_kev` 分开。需要 `VULNCHECK_API_KEY`（免费 Community 方案） |
| **MaxMind GeoLite2** | 每周，周二 01:00 | 用于所有情报源 IP 对国家解析的 GeoIP 数据库 |

---

## 情报源计划 —— OSINT IOC 情报源

这些情报源在 `isms-core-threat-intel` 容器中执行。若先前没有成功的执行记录，所有情报源会在首次开机时自动执行。

| 情报源 | 计划（UTC） | API 密钥 | 提供内容 |
|------|----------------|---------|-----------------|
| **CIRCL MISP** | 每 6 小时：00:00、06:00、12:00、18:00 | 无 | 来自卢森堡 CIRCL 的公开 OSINT MISP 情报源 —— 附 ATT&CK TID、Malpedia 家族与行为者标签的 IOC（IP、网域、URL、哈希） |
| **Botvrij MISP** | 每 6 小时：01:00、07:00、13:00、19:00（错开） | 无 | 公开 OSINT 情报源（botvrij.eu）—— 结构定义与 CIRCL 相同，以 IOC 值加来源去重 |
| **AbuseIPDB** | 每日 02:00 | `ABUSEIPDB_API_KEY` | 前 10,000 个最高信心的滥用 IP；单一 IP 随选充实，缓存 24 小时 |
| **URLhaus** | 每日 03:00 | 无 | 代管恶意程序载荷的恶意 URL，来自 abuse.ch |
| **ThreatFox** | 每 6 小时：03:00、09:00、15:00、21:00 | `THREATFOX_API_KEY`（选用） | 连结至具名恶意程序家族并附信心分数的 IOC（IP、网域、URL、哈希） |
| **SSLBL** | 每日 04:00 | 无 | SSL 凭证黑名单 —— 恶意程序 C2 基础设施所用凭证的 SHA1 指纹 |
| **AlienVault OTX** | 每日 04:30 | `OTX_API_KEY` | Open Threat Exchange pulses —— 带 TLP 标记、ATT&CK TID 的 IOC，以及由 pulse 订阅人数推得的信心分数 |
| **Feodo Tracker** | 每 6 小时：04:30、10:30、16:30、22:30 | 无 | Emotet、QakBot、TrickBot 与 Dridex 僵尸网络的 C2 IP 黑名单（信心值 85） |
| **Red Flag Domains** | 每日 05:00 | 无 | 因网络钓鱼、恶意程序与 C2 而标记的新注册可疑网域 |
| **Stopforumspam** | 每日 05:30 | 无 | 约 140,000 个因垃圾消息、僵尸网络活动与论坛滥用而通报的 IP |
| **MalwareBazaar** | 每 6 小时：02:00、08:00、14:00、20:00 | `MALWAREBAZAAR_API_KEY` | 近期恶意程序样本哈希（MD5/SHA1/SHA256）与家族归因 |
| **Malpedia** | 每周，周日 03:00 | 无 | 恶意程序家族知识库（别名、ATT&CK TID、关联行为者）与威胁行为者目录 |
| **VirusTotal**（充实） | 每日 07:00 | `VT_API_KEY`（选用） | 以 VT 检测比例充实既有 IOC —— 仅更新 `confidence` 字段；不会新增 IOC |
| **IPInfo**（充实） | AbuseIPDB 之后 | `IPINFO_API_KEY`（选用） | 以城市、国家与 ASN 对 AbuseIPDB 的 IP 进行地理充实；每次执行 120 秒时间预算 |

> **首次开机注意事项：** 所有 OSINT 情报源会在启动时立即执行一次，以充填数据库。大型情报源（CIRCL MISP 约 133K 个 IOC、Stopforumspam 约 140K 个 IP、AlienVault OTX 约 90K 个 IOC）各需数分钟。计划器会自动处理后续的差异更新。

---

## 情报源状态

情报源执行历程与状态可见于：

- **Dashboard** —— Intelligence Cards 面板（CVE 数量、KEV 数量、IOC 数量、MITRE 同步状态、整体情报源健康状态）
- **Intelligence → Threat Feeds** —— 完整的情报源执行历程，含所有情报源的最后执行时间戳、状态与记录笔数
- **Header banner** —— 若任何情报源或连接器在过去 24 小时内回报错误，每个页面顶端会出现可关闭的警告横幅

若某个情报源显示错误标记（Intelligence 侧边栏群组上的红点），请前往 **Intelligence → Threat Feeds** 查看错误详情。管理员可使用 **RUN** 按钮随选触发任何情报源，或使用 **CANCEL** 中止执行中的情报源。

---

## MITRE ATT&CK

前往 **Intelligence → MITRE ATT&CK**。

### 技术浏览器

依战术浏览完整的 ATT&CK 框架。每项技术显示：

- 技术 ID 与名称（例如 T1190 —— Exploit Public-Facing Application）
- 战术（Initial Access、Execution、Persistence 等）
- 子技术清单
- 描述与检测指南
- 缓解措施 —— 因应此技术的 ISO 27001 控制措施

### 行为者情报

前往 **Groups** 分页浏览对手组织。每个组织显示：

- 归因与别名
- 目标产业与地理区域
- 此组织使用的技术
- 关联软件与攻击行动
- 连往 MITRE ATT&CK 官方页面的连结

运用行为者情报为您 EBIOS RM 工作坊 2 的风险来源提供脉络 —— 若您运营的产业是已知组织的目标，其技术组合会告诉您哪些控制措施最受考验。

### 热图

前往 **Heatmap** 分页，取得 MITRE ATT&CK Navigator 风格的技术热图。热图显示：

- 以您所属产业为目标的组织使用了哪些技术
- 您的 EBIOS RM 攻击路径引用了哪些技术
- 涵盖范围叠加 —— 哪些技术已由您的 ISO 27001 控制措施因应

---

## 威胁曝险

前往 **Intelligence → Threat Exposure**。

> 需要 `isms-core-threat-intel` 容器已启用并已充填数据。

Threat Exposure 页面显示您的哪些 ISO 27001 控制措施曝露于即时 OSINT 情报源中观察到的活跃威胁技术。它会把 `ti_iocs` 中附加至 IOC 的 ATT&CK 技术 ID 与 ATT&CK → ISO 27001 对照表结合，再交叉参照您的框架评估分数。

### 摘要列

| 指标 | 意义 |
|--------|---------|
| **活跃技术** | 即时 IOC 情报源中出现的不同 ATT&CK TID |
| **受影响控制措施** | 对应至那些技术的 ISO 27001 控制措施 |
| **辨识出的缺口** | 评估分数偏低，或状态为 "non_compliant" / "not_assessed" 的受影响控制措施 |

### 技术 → 控制措施对照表

| 字段 | 意义 |
|--------|---------|
| 技术 | ATT&CK TID（例如 T1190） |
| IOC 数量 | 标记此技术的活跃 IOC 数量 |
| 来源 | 为此技术提供 IOC 的情报源 |
| ISO 27001 控制措施 | 对应至此技术的控制措施，依评估分数上色（绿色 ≥ 70%、橘色 40–69%、红色 < 40%、灰色 = 未评估） |
| 缺口 | 此技术处于缺口状态的控制措施数量 |

使用 Threat Exposure 页面排定修复优先顺序：IOC 数量高且控制措施呈红色／灰色的技术，代表您最高风险的曝险。

---

## CVE / CPE 浏览器

前往 **Intelligence → CVE Explorer**。

### CVE 搜寻

搜寻与筛选 NVD CVE 索引（约 250,000 笔）：

| 筛选条件 | 选项 |
|--------|---------|
| 关键字 | CVE ID 或描述中的关键字 |
| 严重度 | 严重 / 高 / 中 / 低（CVSS v3 基本分数） |
| EPSS 分数 | 滑杆（0.00–1.00）—— 依利用机率筛选 |
| 仅 KEV | 仅显示 CISA KEV 清单上的 CVE |
| 仅 VulnCheck | 仅显示 VulnCheck 自家、范围更广的 KEV 目录中的 CVE |
| EUVD 旗标 | 仅显示存在于欧洲漏洞数据库中的 CVE |
| 仅 EDB | 仅显示在 Exploit-DB 中有已知公开攻击程式的 CVE |
| 年份 | CVE 发布年份 |

### CVE 详情面板

点选任何 CVE 以开启详情面板：

- CVSS v2、v3 与 v4 分数及向量字符串
- CWE（漏洞类型）分类
- CPE 适用性清单（哪些产品受影响）
- EPSS 分数与百分位
- KEV 状态与加入 KEV 清单的日期
- VulnCheck KEV 状态（独立于 CISA KEV —— 一个 CVE 可能在其中之一、另一个，或两者皆是）
- EUVD 旗标，以及（若有）欧盟指派的识别码
- EDB 标签 —— 若有公开攻击程式则为 `EDB`，若有 Metasploit 模块则为 `EDB✓`
- NVD 参照连结

### CPE 分页

CPE 分页可让您搜寻软件／硬件产品目录。适合用来找出环境中影响特定产品的所有 CVE。

---

## ENISA EUVD 浏览器

前往 **Intelligence → EUVD Explorer**。

EUVD 浏览器提供 ENISA 欧洲漏洞数据库的访问 —— 这是欧盟的权威来源，收录与 NIS2 及 DORA 义务下欧洲运营者相关的漏洞信息。

- 浏览标记为**已遭实际利用**的漏洞（修补的最高优先顺序）
- 依 CVSS 严重度筛选 —— 聚焦于严重与高严重度的项目
- 切换 **Exploited only** 或 **Critical only** 以浮现最高风险的子集
- 同时查看欧盟指派的 EUVD 识别码与 CVE ID
- 详情面板显示受影响的厂商、产品、别名、EPSS 分数与 CVSS 数据
- 将筛选后的集合导出为 CSV，作为 ISO 27001 A.8.8 的审计证据

EUVD 情报源会交叉充实 NVD CVE 索引：每个出现在 EUVD 中的 CVE 都会取得 `in_euvd` 旗标与 `euvd_id` 字段，可在 CVE 浏览器中看到。

---

## KEV 审计报告（A.8.8）

前往 **Intelligence → Threat Feeds → A.8.8 KEV Audit Report**。

KEV 审计报告是为 ISO 27001:2022 A.8.8（技术漏洞管理）量身打造的证据产物。它显示：

- 所有 CISA KEV 项目依状态分类 —— 未处理、已修补、进行中、不适用
- 依 CVE 区分的修复状态明细
- 各厂商摘要（每个厂商的产品受多少 KEV 影响）
- 修复时间统计

选择审查区间（3／6／12 个月）。将报告导出为 CSV，纳入您的审计证据包。此报告为审计人员提供可辩护的观点，描述您的组织如何追踪与修复已遭利用的漏洞。

---

## MITRE ATLAS（AI/ML 威胁）

前往 **Intelligence → ATLAS** 取得 AI/ML 专属的威胁框架。ATLAS 记载用于攻击机器学习系统的技术 —— 培训数据污染、对抗式样本、模型萃取等。

ATLAS 与 AI 扩充套件（ISO 42001:2023）相关 —— 特别是涵盖 AI 风险评估、稳健性与事件管理的控制措施。

---

## IOC 浏览器

前往 **Intelligence → IOC Explorer**。

IOC 浏览器提供可搜寻的表格，汇整自 12 个 OSINT 情报源收集到的所有入侵指标。这需要 `isms-core-threat-intel` 容器正在执行。

### 筛选条件

| 筛选条件 | 选项 |
|--------|---------|
| 搜寻 | IOC 值自由文本搜寻（子字符串比对） |
| 类型 | IP / Domain / URL / MD5 / SHA1 / SHA256 |
| 来源 | CIRCL MISP / Botvrij MISP / AbuseIPDB / URLhaus / ThreatFox / SSL Blacklist / AlienVault OTX / Feodo Tracker / Red Flag Domains / Stopforumspam / MalwareBazaar / Malpedia |

### 表格字段

| 字段 | 描述 |
|--------|-------------|
| 类型 | IOC 类型标签 |
| 值 | 指标值（会截断 —— 展开该列以查看完整值） |
| 来源 | 提供此 IOC 的情报源 |
| 信心 | 检测比例（0–100%）；来自情报源中介数据或 VirusTotal 充实 |
| TLP | 红绿灯协议标记（WHITE / GREEN / AMBER / RED）—— 取自 MISP 事件与 AlienVault OTX pulses |
| 最后出现 | 此 IOC 在情报源中最近被观察到的日期 |
| 归因 | 恶意程序家族、威胁行为者与 ATT&CK TID 标签（每类最多行内显示 2 个） |

点选任何一列以展开完整详情检视 —— 显示完整的 IOC 值、首次出现日期、所有家族／行为者／TID 关联，以及来源情报源的完整标签清单。

关联模型会在导入时把 ATT&CK TID、Malpedia 家族代号与行为者代号标记到 IOC 上 —— 执行期不会进行任何联结。这表示一个 IP 位址可以在单一记录中同时带有其滥用分数、曾被观察到散布的恶意程序家族、归因至该家族的威胁行为者组织，以及该行为者使用的 ATT&CK 技术。

> **Malpedia 注意事项：** Malpedia 不会对 IOC 浏览器贡献任何列 —— 它改为充填恶意程序图鉴（家族、行为者、工具）。Malpedia 的 IOC 数量为 0 是正确的。

---

## IP 充实

前往 **Intelligence → IP Enrichment**。

输入任何 IP 位址，以从五个来源取得随选充实：

### AbuseIPDB 检查

- **滥用信心分数**（0–100）：该 IP 为恶意的机率
- AbuseIPDB 数据库中的**通报总数**
- **最后通报时间**时间戳
- **使用类型**（ISP／数据中心／VPN 等）
- 通报滥用的**类别**（连接埠扫描、暴力破解、网页垃圾消息等）

### Shodan 数据

若已设置 `SHODAN_API_KEY`：

- 开放连接埠与服务横幅
- 主机名称与反向 DNS
- ASN 与组织
- 主机上检测到的 CVE（来自 Shodan 扫描）
- 最后扫描日期

若未设置 Shodan API 密钥，则会改用 **Shodan InternetDB** 免费服务作为备援 —— 不需账户即可提供开放连接埠、CPE、标签、主机名称与 CVE 清单。

若某个 IP 未被 Shodan 索引（对传输 IP 与私人范围而言很常见），小工具会显示 "IP not indexed"，而非错误。

### MaxMind GeoLite2

若已设置 `MAXMIND_ACCOUNT_ID` 与 `MAXMIND_LICENSE_KEY`：来自 MaxMind GeoLite2 City 网络服务的国家、城市与 ASN。

### IPInfo 隐私

若已设置 `IPINFO_API_KEY`：隐私分类（Clean / VPN / Proxy / Tor / Relay / Hosting）以及底层服务名称。

### GreyNoise

若已设置 `GREYNOISE_API_KEY`：互联网噪音／扫描器分类（benign / malicious / unknown）、该 IP 是否为已知的全互联网扫描器，以及 RIOT 状态（已知的合法业务服务 —— 搜寻引擎、CDN 等 —— 而非威胁）。GreyNoise 的免费 Community 方案每周上限 50 次查询（API 密钥需企业电子邮件），因此此来源刻意仅供随选查询，永不属于计划的批次情报源。

充实结果会被缓存，以尊重每个来源的速率限制 —— AbuseIPDB 与 Shodan 为 24 小时，MaxMind、IPInfo 与 GreyNoise 为 30 天（这些都是流量较低或配额较严格的来源）。

---

## 恶意程序图鉴

前往 **Intelligence → Malware Atlas**。

恶意程序图鉴呈现由威胁情报容器导入的 Malpedia 知识库。它需要 `isms-core-threat-intel` 容器正在执行，且 `TI_MALPEDIA_ENABLED=true`。

### 恶意程序家族

浏览完整的 Malpedia 家族目录：

- **家族名称**与常见别名
- **描述** —— 来源、目标、首次出现、能力
- **ATT&CK TID** —— 与此家族相关的 ATT&CK 技术
- **关联行为者** —— 已知使用此恶意程序的威胁组织
- 连往 Malpedia 来源页面的连结

### 威胁行为者

浏览威胁行为者目录：

- **行为者名称**与别名
- **国家归因**（疑似国家资助来源）
- **动机** —— 间谍活动／财务／骇客行动主义／未知
- **描述** —— 活动摘要与已知目标

> **注意：** 恶意程序家族与威胁行为者数据来自 MISP galaxy 开放 GitHub 数据集 —— 不需 API 密钥。

### 关联用途

恶意程序图鉴是 IOC 关联的查询端点。当 MISP 事件包含如 `misp-galaxy:malpedia="win.emotet"` 的 galaxy 标签时，导入流水线会把 Malpedia 代号解析为家族记录并标记到该 IOC 上。您可以从以下方向枢纽分析：

- IOC → 恶意程序家族 → ATT&CK 技术
- IOC → 恶意程序家族 → 威胁行为者 → 来源国家
- 威胁行为者 → 所有关联恶意程序家族 → 使用的所有 ATT&CK 技术

---

## 情报与证据

威胁情报数据与证据追踪器整合：

- 当新的 KEV 项目符合与您环境相关的 CVE 时，会产生通知
- KEV 修复状态可晋升为证据追踪器中的项目，作为 A.8.8 下主动漏洞管理的证明
- IOC 浏览器结果可在缺口备注与修复行动中被引用，作为遭受主动威胁锁定的证据
- Threat Exposure 页面提供即时 IOC 情报源与您的 ISO 27001 控制措施评估分数之间的直接连结

---

## 情报源设置

情报源设置属于管理员职能。若某个情报源未执行，或您需要变更情报源设置，请洽您的管理员。

| 变数 | 用途 | 免费注册 |
|----------|-------------|-------------------|
| `NIST_API_KEY` | 更快的 NVD 初始充填（将速率限制从 5→50 次请求／30 秒） | nvd.nist.gov |
| `ABUSEIPDB_API_KEY` | AbuseIPDB 黑名单 + IP 充实 | abuseipdb.com |
| `SHODAN_API_KEY` | Shodan 付费充实（若未设置则使用 InternetDB 免费备援） | shodan.io |
| `OTX_API_KEY` | AlienVault OTX 情报源 | otx.alienvault.com |
| `OTX_IMPORT_DAYS` | 首次执行时的 OTX 历史深度（预设：`90` 天） | — |
| `THREATFOX_API_KEY` | ThreatFox 的更高速率限制（无密钥时以较低限制运作） | threatfox.abuse.ch |
| `MALWAREBAZAAR_API_KEY` | MalwareBazaar 样本情报源 | bazaar.abuse.ch |
| `VT_API_KEY` | VirusTotal IOC 充实（免费方案：约 500 次请求／日） | virustotal.com |
| `VT_DAILY_LIMIT` | 每次 VT 执行充实的 IOC 上限（预设：`450`，免费方案的安全上限） | — |
| `MAXMIND_ACCOUNT_ID` / `MAXMIND_LICENSE_KEY` | 用于 IP 地理定位的 GeoLite2 数据库 | maxmind.com |
| `IPINFO_API_KEY` | 对 AbuseIPDB IP 的强化地理 + ASN 充实 | ipinfo.io |
| `VULNCHECK_API_KEY` | VulnCheck KEV 情报源（免费方案：1,000 次请求／分钟） | console.vulncheck.com |
| `GREYNOISE_API_KEY` | IP 充实页面上的 GreyNoise 随选 IP 查询（免费方案：每周 50 次查询，需企业电子邮件） | greynoise.io |
| `TI_MISP_IMPORT_FROM_DATE` | MISP 首次执行的日期下限（预设 `2024-01-01`） | — |
| `TI_RUN_ON_START` | 强制所有 OSINT 情报源在每次容器启动时执行 | — |

> **VirusTotal 充实：** VT 不会新增 IOC —— 它查询数据库中既有的 IOC（先取 `confidence` 为 NULL 者，再取最久未检查者），且仅在 VT 分数高于现有值时更新其 `confidence` 字段。IOC 每 30 天重新检查一次。免费方案允许约 500 次请求／日；预设上限 450 安全地低于该限制。

**Intelligence → Threat Feeds** 中的 **CPE Option B** 切换可让管理员在 KEV 厂商 CPE（轻量）与完整 CPE 数据库（全面）之间切换 NVD CPE 拉取策略，无需重新启动容器。此设置储存在平台数据库中，并会覆写 `FEEDS_CPE_FULL` 环境变数。

<!-- QA_VERIFIED: 2026-05-02 -->
