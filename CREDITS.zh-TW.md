# 致謝與鳴謝

<p align="center"><a href="CREDITS.md">English</a> · <strong>繁體中文</strong> · <a href="CREDITS.zh-CN.md">简体中文</a></p>

ISMS CORE 的連接器架構、非同步工作者模式（Celery beat/worker 分離）、服務拓撲
與 Docker Compose 結構，取材自 [Filigran](https://filigran.io) 及其開源專案所
建立的生產級模式：

- **OpenCTI** — [https://github.com/OpenCTI-Platform/docker](https://github.com/OpenCTI-Platform/docker)
- **OpenAEV** — [https://github.com/OpenAEV-Platform/docker](https://github.com/OpenAEV-Platform/docker)

這些實作為 ISMS CORE 平台節省了大量工程時間，並提供了經過實戰驗證的
基礎。

## 安全工具

ISMS CORE 平台的 v1.1 安全強化（後端、前端，以及每一個連接器／情報源／
威脅情報／SMTP 橋接服務）採用 [Visa 的 Vulnerability Agentic
Harness (VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness) 執行，
這是一套由 Visa 安全工程團隊開源、以 Apache-2.0 授權的代理式 SAST 工具。
VVAH 的威脅建模、呼叫圖分解與對抗式驗證流程，在整個平台上找出 141 項
真實且經獨立驗證的發現——摘要見 [CHANGELOG.md](isms-core-platform/CHANGELOG.md)，
完整說明見
[部落格文章](https://isms-core.com/blog/isms-core-vvah-security-sweep/)。
全部功勞歸於 Visa 的建置與開源。
