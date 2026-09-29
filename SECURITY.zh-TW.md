# 安全政策

<p align="center"><a href="SECURITY.md">English</a> · <strong>繁體中文</strong> · <a href="SECURITY.zh-CN.md">简体中文</a></p>

ISMS CORE 嚴肅看待安全。若你發現本儲存庫中的漏洞——包括可能導致不安全結果的腳本、活頁簿產生器、範本或文件——或執行中的 ISMS CORE 平台本身（後端 API 與以本儲存庫 `docker-compose.yml` 所參照之 Docker 映像散布的服務）有漏洞，請負責任地回報。

## 回報漏洞

請寄送電子郵件至：**info@isms-core.com**
主旨：**ISMS CORE Security — Vulnerability Report**

請包含：
- 問題的清楚描述與潛在影響
- 重現步驟（若可取得，請附概念驗證）
- 受影響的檔案／資料夾（若相關，請附控制項套件名稱）
- 任何建議的補救措施

若你偏好加密回報，請以電子郵件索取 PGP 金鑰，我們將提供。

## 我們會如何處理

我們將會：
- 在 **3 個工作日**內確認收到
- 在 **10 個工作日**內提供狀態更新
- 在適當情況下，與你協調揭露時程

## 範圍

**納入範圍：**
- ISMS CORE 平台本身——本儲存庫 `docker-compose.yml` 所拉取的 Docker 映像內含的
  後端 API 與服務，包括身分驗證、授權，以及多租戶
  （組織層級）資料隔離
- `SCR/` 中的 Python 腳本與產生器
- 儲存庫提供的邏輯可能不安全的活頁簿範本與輸出
- 晉升／QA 腳本與自動化
- 相依套件引入的供應鏈風險（於適用時）

**不在範圍內：**
- 未隨 ISMS CORE 散布的第三方工具或服務中的漏洞
- 社交工程、垃圾訊息或實體攻擊

## 身分驗證安全

ISMS CORE 為所有使用者帳號支援 TOTP 式 MFA（RFC 6238）。我們建議：
- 在正式使用前，為所有 admin 與 super_admin 帳號啟用 MFA
- 部署至新環境時輪替 `SECRET_KEY` 環境變數
- 為 `POSTGRES_PASSWORD` 與 `SECRET_KEY` 使用強度足夠且唯一的值（至少 32 個字元，隨機產生）

## 主動安全審查

除了回應外部回報之外，我們定期將平台自身的程式碼庫送交 [Visa 的 Vulnerability
Agentic Harness (VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness)——
一套開源的代理式 SAST 工具——並在出貨前修正每一項經獨立驗證的發現。
最近一次完整掃描（後端、前端，以及每一個連接器／情報源／
威脅情報／SMTP 橋接服務）已隨 v1.1 發布——摘要見
[isms-core-platform/CHANGELOG.md](isms-core-platform/CHANGELOG.md)。

## 安全處理

- 請勿在漏洞回報中包含機密、權杖、私密金鑰或客戶資料。
- 在審查完成前，請將產生的成品視為可能敏感。

感謝你協助改善 ISMS CORE。
