# 組織與使用者

<p align="center"><a href="20-organisations-users.md">English</a> · <strong>繁體中文</strong> · <a href="20-organisations-users.zh-CN.md">简体中文</a></p>

<!-- ISMS-CORE:USER-MANUAL:20-organisations-users:v1.0:2026-04-16 -->

---

## 概觀

ISMS CORE Platform 支援多租戶運作——多個組織可在單一平台執行個體上運行，並具備完整的資料隔離。在每個組織內，角色型存取控制決定每位使用者能看到與執行哪些內容。

使用者與組織管理屬於 **Admin** 功能。本章涵蓋與所有角色相關的設定。

---

## 組織

平台中的每個組織代表一個獨立的租戶——一家公司、子公司或各自獨立的組織範圍。組織之間不會共用資料。

### 組織設定

管理員可在 **Admin → Organisation** 中針對每個組織設定下列項目：

| 設定 | 說明 |
|---------|-------------|
| **Organisation name** | 法定名稱或營運名稱 |
| **Country** | 政策本地化所用的司法管轄區（CH、AT、BE、DE、FR、GB、IT、LU） |
| **Industry sector** | 用於框架相關性建議 |
| **Active projects** | 每個產品系列的預設使用中專案是哪一個 |

**國家設定與政策本地化：** 設定國家後，政策文件會以符合該司法管轄區的法規參照呈現。例如，將國家設為 `DE` 時，會讓 GDPR 的參照與相關的 BDSG 參照一併出現，並以 Datenschutzbehörde (DSB) 取代通用的「supervisory authority」代稱。支援的司法管轄區完整清單請見[簡介](01-introduction.zh-TW.md)。

---

## 使用者

### 角色

| 角色 | 可執行的操作 |
|------|-----------------|
| **Super Admin** | 跨組織存取——建立與管理組織、檢視 Metrics Portfolio。於平台層級指派。 |
| **Admin** | 在其組織內的完整存取權——使用者管理、系統設定、內容匯入、管理面板 |
| **ISMS Manager** | 所有合規工作：控制措施、評鑑、缺口、證據、專案、風險、TPRM、EBIOS RM、BIA |
| **Auditor** | 對其組織內所有內容的唯讀存取權。可執行 QA 檢核與匯出。 |
| **Control Owner** | 對指派給自己的控制群組具備讀寫權。可更新檢核表項目，並為其控制措施上傳證據。 |
| **Viewer** | 對非機密內容的唯讀存取權 |

### 管理使用者（僅限 Admin）

前往 **Admin → Users** 即可：

- **Add a user** —— 輸入電子郵件、姓名與角色；若已設定電子郵件，系統會寄出邀請信
- **Edit a user** —— 變更角色、姓名或所屬組織（僅限 Super Admin）
- **Disable a user** —— 撤銷存取權，但不刪除帳戶
- **Reset password** —— 寄出密碼重設電子郵件

### 角色指派

每位使用者只會有一個角色。若要讓某位使用者以 Control Owner 的身分存取特定控制群組，請先指派 Control Owner 角色給該使用者，再從控制措施庫中將特定控制群組指派給他（每個控制群組的詳細檢視中都有 **Assign Owner** 選項）。

---

## 多重要素驗證（MFA）

MFA 採用 TOTP（以時間為基礎的一次性密碼）——相容於 Google Authenticator、Authy、Microsoft Authenticator，以及任何符合 RFC 6238 的 TOTP 應用程式。

### 設定 MFA

1. 前往 **System → MFA Setup**
2. 使用您的驗證器應用程式掃描 QR 碼
3. 輸入應用程式顯示的 6 位數驗證碼以完成確認
4. **儲存 8 組備用碼** —— 這些是您的裝置無法使用時，供復原用的一次性驗證碼

### 使用 MFA 登入

輸入電子郵件與密碼後，系統會提示您輸入 6 位數的 TOTP 驗證碼。輸入滿 6 位數後驗證碼會自動送出——您不需要點選任何按鈕。

若您已無法存取驗證器應用程式，也沒有備用碼：
- 請聯絡您組織的 Admin 重設您的 MFA
- Admin 可從 **Admin → Users → Edit user** 重設 MFA

### MFA 政策

MFA 的強制執行由管理員設定。強制執行時：
- 尚未設定 MFA 的使用者，會在下次登入時被提示完成設定
- 使用者無法略過 MFA 步驟

---

## System Event Log

前往 **Admin → System → Event Log**，即可取得平台所有動作的不可變稽核軌跡。每一個建立、更新、刪除、匯入與登入事件都會記錄下列資訊：

- 時間戳記
- 使用者身分
- 動作類型
- 受影響的資源（文件編號、使用者 ID 等）
- IP 位址

事件日誌無法被修改或刪除。它是記錄誰在何時做了什麼的權威紀錄——對於 ISO 27001:2022 附錄 A.8.15（日誌記錄）與附錄 A.5.26（資訊安全事件應變）的稽核要求至關重要。

請從日誌檢視將事件日誌匯出為 CSV。

---

## 管理面板——內容管理

管理面板（**Admin → First-Run Setup**）是匯入與重新同步平台內容的地方。這通常是部署時的一次性作業，並在內容更新時重複執行。

若您不是管理員使用者，就不需要使用這個面板——它記載於 [PLATFORM.zh-TW.md](../PLATFORM.zh-TW.md) 中，供管理員參考。

<!-- QA_VERIFIED: 2026-04-16 -->
