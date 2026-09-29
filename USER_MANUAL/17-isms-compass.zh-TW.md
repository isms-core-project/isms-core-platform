# ISMS Compass

<p align="center"><a href="17-isms-compass.md">English</a> · <strong>繁體中文</strong> · <a href="17-isms-compass.zh-CN.md">简体中文</a></p>

<!-- ISMS-CORE:USER-MANUAL:17-isms-compass:v1.0:2026-04-16 -->

---

## 什麼是 ISMS Compass？

ISMS Compass 是一套由 AI 驅動的缺口分析工具。貼上或上傳任何政策、程序或安全文件，Compass 會將其與 ISMS CORE 黃金標準——精選的 ISO 27001:2022 政策與實施內容語料庫——進行比對。它會回傳一份結構化的缺口分析，指出哪些內容已具備、哪些缺失，以及哪些未對齊。

請在側邊欄前往 **Tools → ISMS Compass**。

> ISMS Compass 需要由您的管理員設定 `ANTHROPIC_API_KEY` 環境變數。若 Compass 顯示「not available」訊息，請聯絡您的管理員。

---

## Compass 的用途

Compass 是為三種使用情境而設計：

**評鑑現有文件：** 您的政策是在採用 ISMS CORE 之前撰寫的。把它們貼進 Compass，即可在決定要採用 ISMS CORE 政策、還是調整現有政策之前，了解它們與黃金標準相較之下的差異。

**審查草稿：** 您撰寫了一份新的政策或程序。Compass 會在它進入審查之前，找出缺口、缺少的條款以及未對齊的用語。

**稽核前健檢：** 將任何要交付稽核人員的文件貼進 Compass，在稽核前取得對其涵蓋範圍的第二意見。

---

## 使用 ISMS Compass

1. 前往 **Tools → ISMS Compass**
2. 選擇文件所屬的 **product family**（ISMS / Privacy / Cloud / AI）
3. 視需要選擇特定的 **control group** —— 縮小情境範圍可得到更精確的結果
4. 將文件文字貼進輸入區，或上傳檔案（純文字、Markdown 或 PDF）
5. 點選 **Analyse**

Compass 會依據已建立索引的 ISMS CORE 政策與實施指引語料庫來處理文件。視文件長度而定，需時 10–30 秒。

---

## 解讀 Compass 報告

Compass 報告分為三個部分：

### 對齊摘要

簡要評鑑文件整體與黃金標準的對齊程度——高度對齊、部分涵蓋，或有重大缺口。這是執行摘要。

### 已具備且對齊

列出您的文件中已具備、且與 ISMS CORE 黃金標準對齊的條款、主題或要求。這些是稽核人員會認為合格的項目。

### 缺失或未對齊

缺口清單——黃金標準所預期、但您的文件中缺少或處理不足的項目。每個缺口項目會顯示：

- 缺少或未對齊的內容
- 為何重要（它所支援的 ISO 控制措施）
- 建議的改善方式

### 建議新增

可讓文件更接近黃金標準的具體用語新增或結構調整。這些是建議而非強制要求——您的專業判斷優先。

---

## Compass 不是什麼

**Compass 不是合規驗證工具。** 一份全綠的 Compass 報告並不代表您的 ISMS 已通過驗證。它代表您的文件與 ISMS CORE 內容基準對齊良好。

**Compass 無法存取您的環境。** 它只分析您提供的文字，無法得知您所述的政策是否真的落實。

**Compass 是撰寫輔助工具，不是稽核人員。** 用它來提升文件品質、及早發現缺口——而不是取代妥善的稽核準備。

---

## 參考語料庫

Compass 會將您的文件與一份精選語料庫比對，該語料庫由 ISMS CORE 政策與實施指引庫衍生出的約 12,987 個已建立索引的區塊組成。語料庫依產品系列與控制群組編排。

每當管理員以更新後的內容重新載入語料庫時（透過 **Admin → System → Reload QA Corpus**），語料庫就會更新。

<!-- QA_VERIFIED: 2026-04-16 -->
