# 安全政策

<p align="center"><a href="SECURITY.md">English</a> · <a href="SECURITY.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

ISMS CORE 严肃看待安全。若你发现本储存库中的漏洞——包括可能导致不安全结果的脚本、活页簿生成器、模板或文件——或执行中的 ISMS CORE 平台本身（后端 API 与以本储存库 `docker-compose.yml` 所参照之 Docker 映像散布的服务）有漏洞，请负责任地回报。

## 回报漏洞

请寄送电子邮件至：**info@isms-core.com**
主旨：**ISMS CORE Security — Vulnerability Report**

请包含：
- 问题的清楚描述与潜在影响
- 重现步骤（若可取得，请附概念验证）
- 受影响的档案／文件夹（若相关，请附控制项套件名称）
- 任何建议的补救措施

若你偏好加密回报，请以电子邮件索取 PGP 密钥，我们将提供。

## 我们会如何处理

我们将会：
- 在 **3 个工作日**内确认收到
- 在 **10 个工作日**内提供状态更新
- 在适当情况下，与你协调揭露时程

## 范围

**纳入范围：**
- ISMS CORE 平台本身——本储存库 `docker-compose.yml` 所拉取的 Docker 映像内含的
  后端 API 与服务，包括身份验证、授权，以及多租户
  （组织层级）数据隔离
- `SCR/` 中的 Python 脚本与生成器
- 储存库提供的逻辑可能不安全的活页簿模板与输出
- 晋升／QA 脚本与自动化
- 相依套件引入的供应链风险（于适用时）

**不在范围内：**
- 未随 ISMS CORE 散布的第三方工具或服务中的漏洞
- 社交工程、垃圾消息或实体攻击

## 身份验证安全

ISMS CORE 为所有用户帐号支持 TOTP 式 MFA（RFC 6238）。我们建议：
- 在正式使用前，为所有 admin 与 super_admin 帐号启用 MFA
- 部署至新环境时轮替 `SECRET_KEY` 环境变数
- 为 `POSTGRES_PASSWORD` 与 `SECRET_KEY` 使用强度足够且唯一的值（至少 32 个字符，随机产生）

## 主动安全审查

除了回应外部回报之外，我们定期将平台自身的代码库送交 [Visa 的 Vulnerability
Agentic Harness (VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness)——
一套开源的代理式 SAST 工具——并在出货前修正每一项经独立验证的发现。
最近一次完整扫描（后端、前端，以及每一个连接器／情报源／
威胁情报／SMTP 桥接服务）已随 v1.1 发布——摘要见
[isms-core-platform/CHANGELOG.md](isms-core-platform/CHANGELOG.md)。

## 安全处理

- 请勿在漏洞回报中包含机密、令牌、私钥或客户数据。
- 在审查完成前，请将产生的成品视为可能敏感。

感谢你协助改善 ISMS CORE。
