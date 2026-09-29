# 致谢与鸣谢

<p align="center"><a href="CREDITS.md">English</a> · <a href="CREDITS.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

ISMS CORE 的连接器架构、异步工作者模式（Celery beat/worker 分离）、服务拓扑
与 Docker Compose 结构，取材自 [Filigran](https://filigran.io) 及其开源项目所
建立的生产级模式：

- **OpenCTI** — [https://github.com/OpenCTI-Platform/docker](https://github.com/OpenCTI-Platform/docker)
- **OpenAEV** — [https://github.com/OpenAEV-Platform/docker](https://github.com/OpenAEV-Platform/docker)

这些实作为 ISMS CORE 平台节省了大量工程时间，并提供了经过实战验证的
基础。

## 安全工具

ISMS CORE 平台的 v1.1 安全强化（后端、前端，以及每一个连接器／情报源／
威胁情报／SMTP 桥接服务）采用 [Visa 的 Vulnerability Agentic
Harness (VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness) 执行，
这是一套由 Visa 安全工程团队开源、以 Apache-2.0 授权的代理式 SAST 工具。
VVAH 的威胁建模、调用图分解与对抗式验证流程，在整个平台上找出 141 项
真实且经独立验证的发现——摘要见 [CHANGELOG.md](isms-core-platform/CHANGELOG.md)，
完整描述见
[部落格文章](https://isms-core.com/blog/isms-core-vvah-security-sweep/)。
全部功劳归于 Visa 的建置与开源。
