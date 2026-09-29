# 政策與文件

<p align="center"><a href="05-policies-documents.md">English</a> · <strong>繁體中文</strong> · <a href="05-policies-documents.zh-CN.md">简体中文</a></p>

<!-- ISMS-CORE:USER-MANUAL:05-policies-documents:v1.0:2026-04-16 -->

---

## 政策庫

前往 **ISMS → Policies** 瀏覽完整的政策庫。這是平台中所有政策與參照文件的全域檢視——涵蓋所有產品、語言與控制群組。

這與你專案的政策清單不同。在這裡，你可以在把文件加入專案之前，瀏覽完整目錄、搜尋並預覽文件。

---

## 文件類型

平台處理數種文件類型，每種在 ISMS 中都有特定角色：

| 類型 | 代碼 | 說明 |
|------|------|-------------|
| 政策 | POL / OP-POL / PRIV-POL / CLD-POL / AI-POL | 控制群組的「做什麼、誰來做、用什麼做」文件 |
| 指示 | INS | 基礎平台指示與導引文件 |
| 參照 | REF | 支援某控制措施的技術參考資料（強化指引、組態基準） |
| 背景 | CTX | 某控制措施的法規與法律背景文件 |
| 表單 | FORM | 操作該控制措施時使用的範本與表單 |
| 實施指引（使用者） | IMP-UG | 如何實施該控制措施——為 ISMS 經理與流程擁有者而寫 |
| 實施指引（技術） | IMP-TG | 如何實施該控制措施——為工程師與系統管理員而寫 |

---

## 篩選政策庫

使用政策庫頂端的篩選列縮小清單範圍：

- **Product**——ISMS / Privacy / Cloud / AI
- **Type**——POL、REF、CTX、FORM、INS、IMP-UG、IMP-TG
- **Language**——EN、FR、DE、IT
- **Control group**——篩選至特定的附錄 A 區段
- **Status**——draft、review、approved、published

多個篩選條件可以合併使用。

---

## 全文搜尋

政策庫頂端的搜尋列會搜尋所有政策與實施文件的完整內容——不只是標題與 ID。這由 OpenSearch 驅動，並依相關性排序回傳結果。

輸入任何關鍵字、法規詞彙或控制措施概念，即可找到相關文件。例如：

- `encryption at rest`——找出所有涵蓋靜態資料加密的政策與 IMP
- `TOTP MFA`——找出涵蓋多重要素驗證的實施指引
- `GDPR Article 32`——找出參照此條文的政策
- `vulnerability scanning`——找出所有討論弱點管理的文件

將產品篩選與搜尋搭配使用，可將結果縮小至特定產品家族。

---

## 預覽文件

點選清單中的任一文件以開啟預覽面板。預覽會顯示算繪後的 Markdown——以稽核人員或終端使用者會看到的格式呈現。

在預覽面板中你可以：

- **Copy document ID**——用於在缺口或證據中參照
- **Add to project**——將文件加入你的作用中專案
- **View raw source**——查看底層的 Markdown

---

## 文件狀態

從內容庫匯入的文件起始狀態為 **imported**。一旦加入專案，它們就進入專案的核准生命週期（Draft → Review → Approved → Published）。

全域內容庫檢視會以文件在內容庫中的狀態顯示。專案檢視則以文件在該專案中的狀態顯示。同一份文件在不同的專案中可以處於不同狀態。

---

## 語言與在地化

內容庫包含最多四種語言的文件。使用 **Language** 篩選以檢視特定語言的文件。

當你的組織已設定國家（參閱[組織與使用者](20-organisations-users.zh-TW.md)），政策文件在呈現時會自動替換為司法管轄區專屬的法規參照。這一切都是透明地進行——底層文件不變；顯示內容則會配合你組織的司法管轄區調整。

---

## 基礎文件

有兩種基礎文件類型位於標準控制群組之上：

- **INS-POL-00**——ISMS CORE 平台簡介：給所有使用者的導引文件
- **INS-POL-01**——ISMS CORE Framework 簡介：ISO 27001:2022 控制結構的概觀

無論啟用哪些產品家族，這些文件一律可用，且通常是加入新專案的第一批文件。

<!-- QA_VERIFIED: 2026-04-16 -->
