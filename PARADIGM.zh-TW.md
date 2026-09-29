<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Paradigm_Guide-2E8B57?style=for-the-badge" alt="ISMS CORE Paradigm Guide"/>
</p>

<h1 align="center">🧭 認識範式</h1>

<p align="center"><a href="PARADIGM.md">English</a> · <strong>繁體中文</strong> · <a href="PARADIGM.zh-CN.md">简体中文</a></p>

<p align="center">
  <strong>為何 ISMS CORE 的工程做法與眾不同——以及如何在它的各項產品之間做選擇</strong>
</p>

<p align="center">
  <a href="https://www.iso.org/standard/27001"><img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square" alt="ISO 27001:2022"/></a>
  <a href="https://www.iso.org/standard/71670.html"><img src="https://img.shields.io/badge/ISO_27701-2025-7030A0?style=flat-square" alt="ISO 27701:2025"/></a>
  <a href="https://www.iso.org/standard/76559.html"><img src="https://img.shields.io/badge/ISO_27018-2025-00897B?style=flat-square" alt="ISO 27018:2025"/></a>
  <a href="https://www.iso.org/standard/82878.html"><img src="https://img.shields.io/badge/ISO_27017-2026-0288D1?style=flat-square" alt="ISO 27017:2026"/></a>
  <a href="#framework-sse--secure-systems-engineering"><img src="https://img.shields.io/badge/🏗️_FRAMEWORK-SSE_Engineering-9400D3?style=flat-square" alt="FRAMEWORK SSE"/></a>
  <a href="#-operational中小企業的基礎-isms"><img src="https://img.shields.io/badge/⚡_OPERATIONAL-SME_Foundation-FF6600?style=flat-square" alt="OPERATIONAL"/></a>
  <a href="PHILOSOPHY.zh-TW.md"><img src="https://img.shields.io/badge/Anti--Cargo--Cult-Engineering-DC143C?style=flat-square" alt="Anti-Cargo-Cult"/></a>
</p>

<p align="center">
  <em>長得快。能彎，但不會斷。為長久而生。</em> 🎋
</p>

---

> **給只想快速掃過的人，重點摘要：**
> - ISMS CORE 把合規判斷從稽核階段前移到設計階段——政策陳述明確、可測試的要求；稽核人員驗證已文件化的決策，而不是替你做出決策
> - 五項內容產品：**FRAMEWORK**（完整 SSE 工程、受監管行業、多框架）、**OPERATIONAL**（聚焦中小企業、ISO 27001 + GDPR、實用檢核表）、**PRIVACY**（ISO 27701:2025 隱私資訊管理）、**CLOUD**（ISO 27018:2025 雲端 PII 保護），以及 **AI**（ISO 42001:2023 人工智慧管理系統）
> - FRAMEWORK 與 OPERATIONAL 以 53 個控制套件涵蓋 ISO 27001:2022 附錄 A 全部 93 項控制措施；PRIVACY 增加 21 個控制群組；CLOUD 增加 12 個控制群組；AI 增加 12 個控制群組
> - **平台**（WebUI + API）架構在其上，把靜態文件變成可運作的合規管理系統——五項產品集中一處管理
> - 自架、以地端部署為設計前提——你的合規證據始終在自己的掌控與司法管轄之下
> - 這不是隨插即用。你需要合格 CISO、Python 執行能力，以及把決策文件化的意願

---

> *「第一原則是，你絕不能欺騙自己——而你自己正是最容易受騙的人。」*
> — Richard Feynman

> *「當舊範式再也無法容納在其中累積的異常時，科學革命就會發生。」*
> — Thomas Kuhn，《科學革命的結構》

---

## 關於「範式」一詞的說明

Kuhn 把「範式轉移」保留給整個學科圍繞新框架重建的時刻——當累積的異常使舊模型再也站不住腳，而由新模型取而代之。這裡談的不是那種情況。

ISO 27001 並沒有壞掉。認證機構仍然使用同一套附錄 A 準則進行稽核。標準的用語——「適當的控制措施」、「充分的措施」——並沒有改變。ISMS CORE 完全在 ISO 27001:2022 之內運作，而非在其之外。

但在 ISMS *實施* 的領域裡，存在一個真正的架構選擇：**專業判斷施加於何處**——在設計階段還是在稽核階段。這個選擇會實際影響證據如何產生、稽核如何進行，以及合規究竟代表真正的安全，還是合規表演。本文要說明的就是這件事。

---

## 🎯 什麼是 ISMS CORE？

<p>
<img src="https://img.shields.io/badge/🏗️_FRAMEWORK-SSE_Engineering-9400D3?style=flat-square" alt="FRAMEWORK"/>
<img src="https://img.shields.io/badge/⚡_OPERATIONAL-SME_Foundation-FF6600?style=flat-square" alt="OPERATIONAL"/>
<img src="https://img.shields.io/badge/🔒_PRIVACY-ISO_27701_2025-7030A0?style=flat-square" alt="PRIVACY"/>
<img src="https://img.shields.io/badge/☁️_CLOUD-ISO_27018_2025-00897B?style=flat-square" alt="CLOUD"/>
<img src="https://img.shields.io/badge/🤖_AI-ISO_42001_2023-FF6B35?style=flat-square" alt="AI"/>
<img src="https://img.shields.io/badge/Controls-99_Groups_/_4_Standards-32CD32?style=flat-square" alt="99 Groups"/>
</p>

ISMS CORE 提供**五項各自不同的合規產品**，針對不同的組織需求設計：

- **FRAMEWORK (SSE — Secure Systems Engineering)**：為具有複雜多重法規要求的受監管行業而設計的工程化合規系統（ISO 27001:2022）
- **OPERATIONAL**：為尋求 ISO 27001 認證的中小企業而設計的古典 ISMS，搭配自動化輔助的合規作業（ISO 27001:2022）
- **PRIVACY**：隱私資訊管理系統延伸模組，涵蓋 21 個控制群組（ISO 27701:2025），橫跨控管者、處理者與共同責任領域
- **CLOUD**：雲端服務中的 PII 保護延伸模組，涵蓋 12 個 ISO 27018:2025 附錄 A 控制群組，適用於雲端服務供應商與處理者
- **AI**：人工智慧管理系統延伸模組，涵蓋 12 個控制群組（ISO 42001:2023），適用於開發或部署 AI 系統的組織

五項產品全都採用程式碼驅動、證據自動化、工程師設計的做法。如果你要找的是 Word 文件範本、「實施適當的安全措施」這類泛泛指引，或是靠人工蒐集證據的年度合規快照——那這不是適合你的工具。

---

## 📊 傳統 ISMS 與 ISMS CORE 的對比

<p>
<img src="https://img.shields.io/badge/Judgment-At_Design_Time-00AA00?style=flat-square" alt="Design Time"/>
<img src="https://img.shields.io/badge/Evidence-Automated-0066CC?style=flat-square" alt="Automated"/>
<img src="https://img.shields.io/badge/Requirements-Testable-DC143C?style=flat-square" alt="Testable"/>
</p>

| 面向 | 傳統 ISMS | ISMS CORE（兩種版本） |
|--------|-----------------|---------------------------|
| **文件格式** | Word/PDF 文件、人工範本 | Markdown 政策 + Python 腳本 + 產出的工作簿 |
| **證據蒐集** | 人工蒐集（螢幕截圖、日誌、核准紀錄） | 結構化工作簿產出（FRAMEWORK：由控制措施衍生、對照系統現況人工完成的評鑑工作簿；OPERATIONAL：由政策衍生的合規檢核表） |
| **要求具體程度** | 「定期備份」、「適當的加密」 | 「以 AES-256 加密的備份，每季透過評鑑工作簿驗證」（可測試、可衡量） |
| **專業判斷的位置** | 稽核討論（由稽核人員解釋「充分」） | 模型設計（組織把解釋文件化，稽核人員負責驗證） |
| **合規驗證** | 年度快照（單一時點的評鑑） | 週期性驗證（工作簿可隨需重新產生，由評鑑人員依既定排程完成） |
| **政策更新** | 人工修訂文件，以檔名做版本控制 | 版控的 Markdown，可重新產生並與政策保持同步的工作簿 |
| **例外處理** | 與稽核人員臨時討論 | 結構化流程（FRAMEWORK：POL-01 五步驟；OPERATIONAL：內嵌於控制措施政策） |
| **法規適用性** | 含糊（「我們在適用範圍內遵循 GDPR」） | 明確（FRAMEWORK：POL-00 第 1/2/3 級；OPERATIONAL：控制措施政策中界定聚焦的範圍） |
| **稽核準備** | 花數週蒐集本應早已存在的證據 | 數小時即可彙整——前提是評鑑已按排程完成（工作簿已預先產生、證據已預先文件化） |
| **控制措施實施證據** | 「我們有防火牆」（相信我們） | 評鑑工作簿載明每項要求項目的合規狀態、上次評鑑日期與佐證文件（請自行驗證） |

---

## ⚙️ 範式轉移：專業判斷發生在哪裡？

這是 ISMS CORE 背後的核心構想。在傳統 ISMS 中，專業判斷往往發生在稽核期間——由稽核人員決定什麼叫「充分」。在 ISMS CORE 中，專業判斷發生在政策設計期間——由組織決定、明確文件化，稽核人員則驗證這項已文件化的決策。

### ❌ 傳統 ISMS（判斷發生於稽核期間）

1. 撰寫政策：「備份應以適當的演算法加密」
2. 實施：安裝備份系統、啟用加密
3. 稽核階段：
   - 稽核人員：「用什麼演算法？」
   - 你：「廠商的預設值，沒特別改」
   - 稽核人員：「這樣適當嗎？」
   - 你：「我們覺得應該可以？」
   - 稽核人員：*[開立發現事項]*「加密的充分性未文件化」
4. 結果：開立發現事項、必須矯正、改寫政策、重新舉證

### ✅ ISMS CORE（判斷發生於模型設計期間）

1. 撰寫政策：「備份應至少使用 AES-256 加密，每季測試復原能力」
2. 實施：設定備份系統、將設定文件化、記錄實際使用的演算法
3. 建立評鑑：Python 腳本依政策範圍中的明確要求產生結構化工作簿——評鑑人員逐項標記為合規／部分合規／不符合／不適用，並記錄佐證證據（設定擷取、上次測試日期、復原結果）
4. 稽核階段：
   - 稽核人員：「讓我看備份加密的合規情形」
   - 你：「這是已完成評鑑的工作簿、它據以評鑑的政策，以及設定證據。兩邊都載明演算法為 AES-256。」
   - 稽核人員：*[檢視工作簿與證據]*「……合規。」
5. 結果：這項控制措施未開立發現事項。稽核順利推進。

**差別在哪裡：**「用什麼演算法？這樣適當嗎？」這個問題在**政策設計期間**就已回答（CISO 載明「至少 AES-256」），並在**評鑑期間**完成驗證（工作簿確認兩者一致）。稽核人員驗證這項已文件化決策的品質——他們不會替你做出決策。

---

## 🔀 四項產品：依你的需求選擇

### ⚡ OPERATIONAL（中小企業的基礎 ISMS）

<p>
<img src="https://img.shields.io/badge/Target-SME_/_Startup-FF6600?style=flat-square" alt="SME"/>
<img src="https://img.shields.io/badge/Effort-3–6_months-FFD700?style=flat-square" alt="3-6 months"/>
<img src="https://img.shields.io/badge/Regulatory-ISO_27001_+_nFADP-0066CC?style=flat-square" alt="ISO 27001"/>
<img src="https://img.shields.io/badge/Python-Basic-32CD32?style=flat-square" alt="Basic Python"/>
</p>

**適用對象：**
- 尋求 ISO 27001 認證的中小型企業
- 法規範圍聚焦的組織（ISO 27001 + 瑞士 nFADP + 有條件適用 GDPR）
- 想要古典 ISMS 結構、同時享有自動化好處的團隊

**你會拿到什麼：**
- **架構**：OP-POL（政策）→ Python 腳本（工作簿產生器）→ 評鑑工作簿（合規檢核表）
- **涵蓋範圍**：53 個控制套件，涵蓋附錄 A 全部 93 項控制措施
- **自動化**：由 Python 產生的 Excel 合規檢核表，反映 OP-POL 中定義的要求
- **證據**：透過工作簿進行的每季／每年合規評鑑，由評鑑人員人工完成
- **方法論**：古典 ISMS 結構，政策以 1:1 堆疊（相關控制措施共用政策）
- **法規支援**：ISO 27001:2022 + 瑞士 nFADP + GDPR（於適用時）
- **治理**：內嵌於控制措施政策（沒有獨立的 POL-00/POL-01 中繼層）

**工作簿如何建立：**

每份 OP-POL 的撰寫方式，都是依中小企業的情境與範圍，按比例回應該控制措施的目標。Python 腳本產生結構化評鑑工作簿，其中的要求對應 OP-POL——這是因為腳本在撰寫時就反映了那些要求，而不是因為它在執行時解析政策。工作簿是**由政策衍生**：OP-POL 是唯一真實來源。評鑑人員人工完成工作簿，逐項要求標記為合規／部分合規／不符合／不適用，並記錄佐證證據。

**適用性聲明（SoA）：**SoA 是 ISO 27001:2022 條款 6.1.3(d) 下的強制認證產物。ISMS CORE 不會自動產生 SoA——它是組織的決策文件，把控制措施的適用性對應到你的情境、排除項目與理由。53 個控制套件（涵蓋 93 項附錄 A 控制措施）為產出 SoA 提供結構化輸入；完成 SoA 是組織的責任。如果你是 ISMS 新手，請確認你的實施包含合格從業人員提供的 SoA 指引。

**前置條件：**
- 基本的 Python 執行能力（執行腳本以產生檢核表）
- 理解 ISO 27001 附錄 A 控制措施
- 願意明確地把決策文件化（可測試的要求，而非含糊的陳述）
- 每季評鑑的紀律（完成工作簿、追蹤合規狀態）

**最適合：**「我們需要 ISO 27001 認證，希望合規追蹤有自動化協助，但不需要多重法規治理的複雜度。」

---

### 🏗️ FRAMEWORK (SSE — Secure Systems Engineering)

<p>
<img src="https://img.shields.io/badge/Target-Regulated_Industries-9400D3?style=flat-square" alt="Regulated"/>
<img src="https://img.shields.io/badge/Effort-6–12_months-FF4500?style=flat-square" alt="6-12 months"/>
<img src="https://img.shields.io/badge/Regulatory-Multi--Framework-DC143C?style=flat-square" alt="Multi-Framework"/>
<img src="https://img.shields.io/badge/Python-Intermediate-0066CC?style=flat-square" alt="Intermediate Python"/>
</p>

**適用對象：**
- 受監管行業（金融服務、醫療照護、關鍵基礎設施）
- 具有複雜多重法規要求的組織（GDPR + DORA + NIS2 + PCI DSS + FINMA）
- 能勝任全面、證據驅動的合規工作與 Python 產生的評鑑工具的技術團隊

**你會拿到什麼：**
- **基礎治理**：
  - **POL-00**（法規適用性架構）：第 1/2/3 級分類、每季監控、觸發式評鑑
  - **POL-01**（ISMS 治理架構）：權責界線、能力要求、五步驟例外流程、六步驟變更控制、內部挑戰協議
- **架構**：POL（政策）→ IMP（實施規格）→ Python（工作簿產生器）→ 工作簿（證據）
- **每個控制套件**：POL + IMP (UG/TG) + SCR + WKBK + REF + FORM + INS + CTX
- **涵蓋範圍**：53 個控制套件，涵蓋附錄 A 全部 93 項控制措施。評分 4–5 的控制措施擁有最結構化、最全面的工作簿，以及最客觀的可衡量準則。評分 1–3 的控制措施則使用依該控制措施本身可衡量程度調整規模的工作簿。
- **證據**：由 Python 腳本產生的結構化評鑑工作簿，由評鑑人員週期性完成。評分反映的是工作簿的深度與證據的客觀性，而不是基礎設施查詢的自動化程度。
- **方法論**：評分 1–5 系統（見下文）
- **法規支援**：多框架（ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA）

**工作簿如何建立：**

FRAMEWORK 的工作簿是**由控制措施衍生**：直接且全面地對照該控制措施所處理的每一個面向而建立，涵蓋 ISO 27001 所要求的完整範圍。POL 本身也以同樣的範圍撰寫。政策與工作簿是對照控制措施要求共同設計的，不經過中小企業比例原則的篩選。結果是比 OPERATIONAL 同類工作簿更詳盡、更結構化的評鑑。評鑑人員人工完成每本工作簿，逐項要求標記為合規／部分合規／不符合／不適用，並附上佐證證據（設定、憑證、日誌、核准紀錄）。稽核人員對照政策所陳述的要求，驗證已完成的工作簿與佐證文件。

**前置條件：**
- Python 3.11+ 執行能力（執行腳本以產生工作簿）
- 理解 ISO 27001 附錄 A 控制措施與 SSE 方法論
- 願意完成附帶佐證證據的結構化評鑑的技術團隊
- 有意願投入全面、證據驅動的合規（而非打勾式合規）

**評分 1–5 系統（僅 FRAMEWORK）：**

<p>
<img src="https://img.shields.io/badge/Score_5-Highest_Objectivity-00AA00?style=flat-square" alt="Score 5"/>
<img src="https://img.shields.io/badge/Score_4-High_Objectivity-32CD32?style=flat-square" alt="Score 4"/>
<img src="https://img.shields.io/badge/Score_3-Moderate-FFD700?style=flat-square" alt="Score 3"/>
<img src="https://img.shields.io/badge/Score_2-Lower-FF6600?style=flat-square" alt="Score 2"/>
<img src="https://img.shields.io/badge/Score_1-Attestation--Based-DC143C?style=flat-square" alt="Score 1"/>
</p>

每項附錄 A 控制措施都依**證據客觀性**評分——評分反映的是該控制措施的要求能被多直接、多可衡量地驗證，因而也反映所產生的工作簿能有多全面、多客觀。這是對證據品質的評分，不是組織原則；FRAMEWORK 與 OPERATIONAL 都使用相同的 A.5/A.6/A.7/A.8 結構與 53 個控制套件。

- **評分 5**：最高證據客觀性（日誌留存、備份狀態、實際使用的演算法——要求可直接衡量，通過／不通過的準則明確無疑）
- **評分 4**：高證據客觀性（存取審查、修補合規——多數要求可客觀驗證，少數需要人工判斷）
- **評分 3**：中等證據客觀性（事件應變——流程與結果可文件化並追蹤，但無法完全化約為通過／不通過）
- **評分 2**：較低證據客觀性（安全訓練、供應商審查——以人工判斷為核心，證據以聲明為基礎）
- **評分 1**：最低證據客觀性（實體安全、人資流程——評鑑主要依賴觀察與聲明）

FRAMEWORK 在所有評分等級都優先講求嚴謹。評分較高的控制措施產生的工作簿具有更客觀、可衡量的準則。評分較低的控制措施所產生的工作簿同樣全面且結構化，但更依賴評鑑人員的判斷與佐證文件。評分描述的是**控制措施本身的可衡量程度**，而不是腳本目前的能力。

**最適合：**「我們是金融機構，需要遵循 DORA + FINMA + ISO 27001 + GDPR，也具備結構化證據自動化的技術能力。」

---

### 🔒 PRIVACY（ISO 27701:2025——隱私資訊管理）

<p>
<img src="https://img.shields.io/badge/Standard-ISO_27701_2025-7030A0?style=flat-square" alt="ISO 27701:2025"/>
<img src="https://img.shields.io/badge/Groups-21_Control_Groups-9400D3?style=flat-square" alt="21 Groups"/>
<img src="https://img.shields.io/badge/Scope-PIMS_Extension-7030A0?style=flat-square" alt="PIMS"/>
</p>

**適用對象：**
- 以控管者、處理者或共同責任身分處理個人資料的組織
- 把 ISO 27001 ISMS 擴充到納入隱私資訊管理系統（PIMS）的組織
- 在 ISO 27001 認證之外，同時尋求 ISO 27701:2025 合規的團隊

**你會拿到什麼：**
- **架構**：PRIV-POL（政策）→ 合規檢核表工作簿（Python 產生）
- **涵蓋範圍**：21 個控制群組（ISO 27701:2025）
  - 控管者（8 個群組）：A.1.x——同意、目的正當性、蒐集、資料主體權利
  - 處理者（5 個群組）：A.2.x——處理義務、再處理者、紀錄
  - 共同（8 個群組）：A.3.x——資料最少化、正確性、透明性、安全控制措施
- **治理**：PRIV-POL-00（架構導論）+ PRIV-POL-01（隱私政策基線）+ 21 份針對特定控制措施的 PRIV-POL 文件
- **證據**：由 Python 產生的合規檢核表工作簿，每個控制群組一本

**前置條件：**
- 基本的 Python 執行能力
- 理解 GDPR／隱私法下資料控管者與處理者的角色差異
- 已建置 ISO 27001 ISMS（PIMS 是延伸模組，不是獨立產品）

**最適合：**「我們已通過 ISO 27001 認證，需要延伸到 ISO 27701，向客戶與監管機關展現結構化的隱私管理。」

---

### ☁️ CLOUD（ISO 27018:2025——雲端服務中的 PII）

<p>
<img src="https://img.shields.io/badge/Standard-ISO_27018_2025-00897B?style=flat-square" alt="ISO 27018:2025"/>
<img src="https://img.shields.io/badge/Groups-12_Control_Groups-00897B?style=flat-square" alt="12 Groups"/>
<img src="https://img.shields.io/badge/Scope-Cloud_PII_Processor-00897B?style=flat-square" alt="Cloud PII"/>
</p>

**適用對象：**
- 代表客戶處理 PII 的雲端服務供應商（CSP）
- 依 GDPR 或類似隱私法擔任雲端處理者的組織
- 需要展現雲端環境特有 PII 控制措施的團隊

**你會拿到什麼：**
- **架構**：CLD-POL（政策）→ 合規檢核表工作簿（Python 產生）
- **涵蓋範圍**：12 個控制群組，涵蓋 ISO 27018:2025 附錄 A 控制措施
  - A.1 一般 | A.2 同意 | A.3 目的 | A.4 蒐集 | A.5 資料最少化
  - A.6 使用／留存／揭露 | A.7 正確性 | A.8 公開性 | A.9 個人參與
  - A.10 當責 | A.11 資訊安全 | A.12 隱私合規
- **治理**：12 份 CLD-POL 文件，每個控制群組一份
- **證據**：由 Python 產生的合規檢核表工作簿

**前置條件：**
- 基本的 Python 執行能力
- 雲端服務交付的情境（該標準處理的是 CSP 特有的義務）
- 已建置 ISO 27001 ISMS（ISO 27018 是在 ISO 27001 之上的疊加層）

**最適合：**「我們是處理客戶 PII 的雲端服務供應商——需要向企業客戶與監管機關展現 ISO 27018 合規。」

---

## 📋 產品比較

| 功能 | FRAMEWORK (SSE) | OPERATIONAL | PRIVACY | CLOUD | AI |
|---------|----------------|-------------|---------|-------|----|
| **標準** | ISO 27001:2022 | ISO 27001:2022 | ISO 27701:2025 | ISO 27018:2025 | ISO 42001:2023 |
| **目標對象** | 受監管行業 | 中小企業 | PII 控管者／處理者 | 雲端 PII 處理者 | AI 開發者／部署者 |
| **控制群組** | 53 個群組／93 項控制措施 | 53 個群組／93 項控制措施 | 21 個群組 | 12 個群組 | 12 個群組 |
| **政策格式** | POL + IMP (UG/TG) | OP-POL | PRIV-POL | CLD-POL | AI-POL |
| **工作簿類型** | 由控制措施衍生的評鑑工作簿 | 由政策衍生的檢核表 | 隱私合規檢核表 | 雲端 PII 合規檢核表 | AI 治理政策 |
| **基礎治理** | POL-00 + POL-01（第 1/2/3 級、權責界線、例外處理） | 古典 ISMS（無中繼層） | PRIV-POL-00 + PRIV-POL-01 | 內嵌於 CLD-POL | AI-POL-00 + AI-POL-01 |
| **法規範圍** | ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA | ISO 27001 + nFADP + 有條件適用 GDPR | ISO 27701:2025（PIMS 延伸） | ISO 27018:2025（雲端疊加） | ISO 42001:2023 + EU AI Act |
| **Python 技能** | 中階 | 基本 | 基本 | 基本 | 基本 |
| **實施投入** | 高（6–12 個月） | 中等（3–6 個月） | 中等（ISMS 的加掛元件） | 低（ISMS 的加掛元件） | 中等（ISMS 的加掛元件） |
| **可獨立使用？** | 是 | 是 | 否——延伸 ISO 27001 ISMS | 否——延伸 ISO 27001 ISMS | 否——延伸 ISO 27001 ISMS |

**可以組合產品嗎？**可以——這是設計上的安排：
- ISO 27001 基礎 → 使用 FRAMEWORK (SSE) 或 OPERATIONAL
- 加上隱私義務 → 加上 PRIVACY（ISO 27701）
- 加上雲端 PII 處理 → 加上 CLOUD（ISO 27018）
- 加上 AI 系統治理 → 加上 AI（ISO 42001）
- 平台以單一整合儀表板管理全部五項產品

**不要混用：**OPERATIONAL 是自成一體的。把 POL-00/POL-01 加到 OPERATIONAL，會讓中小企業的實施過度複雜。

---

## 🏛️ 基礎治理詳解

### 🏗️ FRAMEWORK (SSE) 基礎

<p>
<img src="https://img.shields.io/badge/POL--00-Regulatory_Applicability-9400D3?style=flat-square" alt="POL-00"/>
<img src="https://img.shields.io/badge/POL--01-Governance_Framework-0066CC?style=flat-square" alt="POL-01"/>
</p>

當你要應對**6 個以上的法規框架**（ISO 27001、GDPR、DORA、NIS2、PCI DSS、FINMA）時：

**POL-00 解決：**「這些法規中，哪些才真正適用於我們？」
- **第 1 級（強制）**：法律義務（ISO 27001、瑞士 nFADP、適用範圍內的 GDPR）
- **第 2 級（有條件）**：由業務情境觸發（若為金融機構則適用 DORA，若處理卡片則適用 PCI DSS）
- **第 3 級（參考資訊）**：最佳實務（NIST、CIS、OWASP）
- 每季監控可偵測第 2 級何時變成第 1 級（業務擴張、法規變動）

**POL-01 解決：**「內部由誰決定我們如何合規，以及我們如何處理複雜度？」
- **權責界線**：CISO（技術）、法務／合規（法規）、高階管理層（策略）
- **例外處理**：當控制措施在不同框架間衝突時（例如 GDPR 的刪除與 FINMA 的留存要求）所採行的五步驟內部流程
- **變更管理**：法規要求演進時所採行的六步驟流程
- **挑戰協議**：當 ISMS 利害關係人質疑多框架解釋時，用以解決內部分歧的結構化流程

> **注意：**內部挑戰協議規範的是 ISMS 設計與運作期間，你自己組織內 CISO、法務與高階管理團隊之間的分歧。外部稽核的分歧則依認證機構的標準申訴與異議程序處理——挑戰協議不約束認證機構稽核人員，也不適用於他們。

**結果：**為複雜的法規環境提供明確的治理。沒有 POL-00/POL-01，要一致地調和 6 個框架在結構上就很困難。

### ⚡ OPERATIONAL 基礎

<p>
<img src="https://img.shields.io/badge/Governance-Classical_ISMS-FF6600?style=flat-square" alt="Classical ISMS"/>
<img src="https://img.shields.io/badge/No_Meta--Layer-By_Design-32CD32?style=flat-square" alt="No Meta-Layer"/>
</p>

**為什麼 OPERATIONAL 沒有 POL-00/POL-01：**

當你只實施 **ISO 27001**（或有條件地加上 GDPR）時：
- 法規範圍清楚且有限（沒有第 1/2/3 級的複雜度）
- 控制措施的適用性記載於 SoA（ISO 27001 條款 6.1.3 流程，標準 ISMS 做法）
- 例外處理內嵌於控制措施政策（每份 OP-POL 依 ISO 27001 指引處理「若控制措施無法實施」的情形）
- 治理採古典 ISMS 結構（依條款 5、9.2、9.3，CISO → 管理審查 → 內部稽核）

**結果：**中小企業不需要治理中繼層。古典 ISMS 結構就能處理 ISO 27001 的複雜度，不必額外增加治理負擔。

**如果中小企業成長為受監管行業**（成為受 DORA 規範的金融機構，或受理需要 PCI DSS 的支付卡）：
- 從 OPERATIONAL 轉換到 FRAMEWORK (SSE)
- 加上 POL-00（此時需要第 1/2/3 級的法規追蹤）
- 加上 POL-01（此時需要針對多框架衝突的正式例外處理）

---

## 🔬 關鍵創新

### 1. 第 1/2/3 級法規架構（POL-00——僅 FRAMEWORK）

<p>
<img src="https://img.shields.io/badge/Tier_1-Mandatory-DC143C?style=flat-square" alt="Tier 1 Mandatory"/>
<img src="https://img.shields.io/badge/Tier_2-Conditional-FF6600?style=flat-square" alt="Tier 2 Conditional"/>
<img src="https://img.shields.io/badge/Tier_3-Informational-0066CC?style=flat-square" alt="Tier 3 Informational"/>
</p>

**解決的問題：**「GDPR 適用嗎？PCI DSS 適用嗎？那 DORA 呢？」

**傳統 ISMS：**含糊的引用、稽核期間的爭論、範圍混淆

**FRAMEWORK (SSE) 的做法：**
- **第 1 級（強制）**：法律義務（ISO 27001、瑞士 nFADP、適用範圍內的 GDPR）
- **第 2 級（有條件）**：由業務情境觸發（若為金融機構則適用 DORA，若處理卡片則適用 PCI DSS）
- **第 3 級（參考資訊）**：最佳實務（NIST、CIS、OWASP）
- 每季監控、文件化的評鑑、高階管理層核准

**OPERATIONAL：**法規範圍較簡單（ISO 27001 + nFADP + 有條件適用 GDPR），直接記載於控制措施政策，不採分級架構。

**結果（FRAMEWORK）：**零含糊。若 X 已被記載為第 2 級——不適用，並有每季監控證明觸發條件尚未發生——稽核人員就無法主張「你們應該遵循 X」。

---

### 2. 具備能力要求的治理（POL-01——僅 FRAMEWORK）

<p>
<img src="https://img.shields.io/badge/FRAMEWORK-Only-9400D3?style=flat-square" alt="Framework Only"/>
<img src="https://img.shields.io/badge/Authority-Boundaries_Defined-0066CC?style=flat-square" alt="Authority Boundaries"/>
</p>

**解決的問題：**「內部由誰決定什麼叫充分？如果利害關係人對解釋有分歧怎麼辦？」

**傳統 ISMS：**權責界線未定義、主觀解釋、過時的決策

**FRAMEWORK (SSE) 的做法：**
- **權責界線**：CISO（技術）、法務／合規（法規）、高階管理層（策略）
- **能力要求**：CISO = CISSP/CISM + 5 年經驗 + ISO 27001 知識（已文件化、可驗證）
- **內部挑戰協議**：解決內部分歧的結構化流程（以證據為基礎，須引用 ISO 27001 條款）
- **例外處理**：五步驟內部流程（記錄 → 評鑑風險 → 提出方案 → 取得核准 → 記載於 SoA）

**OPERATIONAL：**採用古典 ISMS 治理（依 ISO 27001 條款 5、9.2、9.3，CISO → 管理審查 → 內部稽核）。例外處理內嵌於控制措施政策。

**結果（FRAMEWORK）：**內部治理決策已文件化、可追溯、可辯護。稽核人員驗證這些決策的品質與可追溯性——而不是取代它們。

---

### 3. 結構化證據產生

<p>
<img src="https://img.shields.io/badge/Evidence-Control--Derived_(FW)-9400D3?style=flat-square" alt="Control Derived"/>
<img src="https://img.shields.io/badge/Evidence-Policy--Derived_(OP)-FF6600?style=flat-square" alt="Policy Derived"/>
<img src="https://img.shields.io/badge/Format-Python_+_Excel-32CD32?style=flat-square" alt="Python Excel"/>
</p>

**解決的問題：**「證明你的控制措施已實施。證明你的設定是合規的。」

**傳統 ISMS：**螢幕截圖、人工日誌、「這裡有個樣本」——每次稽核前才匆忙蒐集

**FRAMEWORK (SSE)：**
- Python 腳本產生全面的評鑑工作簿，對照完整的控制措施範圍建立
- 工作簿涵蓋該控制措施所處理的每一個面向——不經中小企業比例原則的篩選
- 評鑑人員完成評鑑：逐要求領域標記合規／部分合規／不符合／不適用，並附上佐證文件（設定、憑證、日誌、核准紀錄）
- 評分 4–5 的控制措施所產生的工作簿，多數準則可直接衡量——評鑑人員從系統取出數值並記錄（已設定的留存期間、實際使用的演算法、上次測試日期）
- 評分 1–3 的控制措施所產生的工作簿同樣全面，但更依賴評鑑人員的判斷與以聲明為基礎的證據
- 證據：已完成的工作簿 + 佐證文件。稽核人員可對照政策所陳述的要求，逐項驗證。

**OPERATIONAL：**
- Python 腳本產生結構化合規檢核表，反映 OP-POL 中定義的要求
- 評鑑人員每季完成：逐項要求標記合規／部分合規／不符合／不適用
- 證據：已完成的工作簿 + 佐證文件（憑證、設定、聲明）

**真正重要的區別：**OPERATIONAL 的工作簿是**由政策衍生**——檢核表反映 OP-POL 所定義的內容，範圍依中小企業情境界定。FRAMEWORK 的工作簿是**由控制措施衍生**——對照該控制措施要求的完整範圍全面建立。起點不同、深度不同、稽核對話也不同。

**結果：**證據結構化、可追溯，且可隨需重新產生。稽核人員對照明確、可測試的要求客觀驗證合規——而不是靠「相信我」。

---

### 4. 控制套件整併

<p>
<img src="https://img.shields.io/badge/53_Packs-93_Controls-0066CC?style=flat-square" alt="53 Packs"/>
<img src="https://img.shields.io/badge/DRY-Don't_Repeat_Yourself-FF6600?style=flat-square" alt="DRY"/>
</p>

**解決的問題：**「為什麼 93 項附錄 A 控制措施要有 93 份各自獨立的政策？這根本是文件地獄。」

**傳統 ISMS：**93 份各自獨立的 Word 文件，或一份 300 頁的龐大政策（兩者都不好）

**ISMS CORE 的做法（兩種版本）：**
- **53 個控制套件**涵蓋 **93 項附錄 A 控制措施**
- 當相關控制措施處理共同的流程或技術時，會共用政策：
  - A.5.15-16-18：身分與存取管理（IAM 橫跨多項控制措施）
  - A.8.1-7-18-19：端點安全（共用端點管理）
  - A.5.30-8.13-14：營運持續與災難復原（BC/DR 生命週期跨越界線）
- 堆疊理由記載於每份政策
- 每項控制措施的特定 ISO 27001 要求都分別處理（不會在泛用套裝中消失）

**結果：**合乎邏輯的分組（不是任意湊合）。維護更容易（更新一份政策，連帶影響相關控制措施）。稽核人員仍可逐項驗證每一項控制措施（要求可追溯）。

---

### 5. 可測試的要求

<p>
<img src="https://img.shields.io/badge/Requirements-Explicit_Pass/Fail-00AA00?style=flat-square" alt="Pass Fail"/>
<img src="https://img.shields.io/badge/No_More-%22Appropriate_Measures%22-DC143C?style=flat-square" alt="No Vague"/>
</p>

**解決的問題：**「我們的政策寫著『適當的安全措施』。稽核人員說這樣不夠。」

**傳統 ISMS：**含糊的要求（「定期審查」、「足夠的加密」、「充分的監控」）

**ISMS CORE：**具備明確通過／不通過準則的可測試要求：

| 含糊（傳統） | 可測試（ISMS CORE） |
|---------------------|---------------------|
| 「備份應定期執行」 | 「備份應每日執行，以 AES-256 加密，每季測試復原能力」 |
| 「存取應定期審查」 | 「存取權限應每季審查，記載於存取審查工作簿，並由系統擁有者核准」 |
| 「應使用適當的加密」 | 「加密應使用 AES-256（對稱）、RSA-4096（非對稱）、TLS 1.3（傳輸）。禁止使用：DES、3DES、MD5、SHA-1、TLS 1.0/1.1」 |
| 「安全事件應予以處理」 | 「事件應在 4 小時內分級（A.5.25），應變在 24 小時內啟動（A.5.26），事件後檢討在 7 天內完成（A.5.27）」 |

**結果：**稽核人員客觀驗證。不必再爭論「這樣適當嗎？」——要求明確，證據自會顯示合規或不合規。

---

## 🖥️ 部署模式：地端優先

<p>
<img src="https://img.shields.io/badge/Deployment-On--Premises-2E8B57?style=flat-square" alt="On-Premises"/>
<img src="https://img.shields.io/badge/Data_Sovereignty-By_Design-0066CC?style=flat-square" alt="Data Sovereignty"/>
<img src="https://img.shields.io/badge/CLOUD_Act-Risk_Mitigated-DC143C?style=flat-square" alt="CLOUD Act"/>
</p>

ISMS CORE 的設計是**自架、地端部署的平台**。這是刻意的架構決策，不是產品路線圖上的限制。

你的 ISMS 證據反映你的基礎設施設定、組織決策與控制措施實施情形。這是敏感的營運資料——而在 2025–2026 年，這些資料存放在哪裡、受哪個司法管轄權規範，本身已成為重大的安全與合規議題。

**歐洲資料主權的背景：**

歐洲對美國雲端基礎設施的依賴，已因為具體的法律風險而成為董事會層級的議題。美國 2018 年的 CLOUD Act 允許美國當局強制美國科技公司提供被要求的資料，不論該資料實際儲存在何處——包括存放在歐盟資料中心的資料。截至 2026 年，歐盟沒有任何法律廢除這項域外效力。在歐洲經營主權雲服務的美國大型超大規模雲端業者已確認，他們無法絕對保證存放在歐盟的資料永遠不會被美國當局要求提供。

歐盟以《歐洲數位主權宣言》（2025 年 11 月）回應，這是歐盟成員國強化歐洲對數位基礎設施掌控的共同承諾。歐洲主權雲投資預計在 2025 至 2027 年間成長超過三倍。雲端回流——把工作負載從公有雲移回地端或歐洲營運的基礎設施——是正在成長的趨勢，對受監管行業、政府與安全敏感的工作負載尤其如此。

ISMS 平台——保存貴組織的安全控制措施證據、合規狀態、風險評鑑、缺口分析與稽核產物——正好落在不應受外國司法管轄法律存取的那一類資料裡。

**地端部署對 ISMS CORE 的意義：**
- Python 腳本在你的環境中執行，對你的系統運作
- 產出的工作簿留在你的基礎設施內
- 沒有資料離開你的組織到第三方平台
- 評鑑排程、儲存與存取都由你掌控
- 你的合規證據不依賴任何廠商

**關於未來託管服務的附註：**

ISMS CORE 的託管或可透過 SaaS 存取的版本並未排除在產品路線圖之外。然而，在任何這類架構中，資料主權都是設計變數——而不是事後補上的考量。未來任何託管服務都必須以架構上可驗證、而非商業上片面宣稱的方式，處理司法管轄權、資料存放地、法律存取風險與營運控制。對於受監管行業或上述顧慮重大的司法管轄區內的組織，地端模式仍是預設選擇。

---

## ⚖️ 這不是什麼

<p>
<img src="https://img.shields.io/badge/NOT-Plug_and_Play-DC143C?style=flat-square" alt="Not Plug and Play"/>
<img src="https://img.shields.io/badge/NOT-Beginner_Friendly-DC143C?style=flat-square" alt="Not Beginner Friendly"/>
<img src="https://img.shields.io/badge/IS-Engineering_Driven-00AA00?style=flat-square" alt="Engineering Driven"/>
<img src="https://img.shields.io/badge/IS-Audit_Optimised-00AA00?style=flat-square" alt="Audit Optimised"/>
</p>

**這不是：**
- ❌ **隨插即用的範本**：你必須理解 ISO 27001、依自己的情境調整、做出並記錄決策（不是填空）
- ❌ **顧問的替代品**：你需要能力（具備 ISO 27001 知識的 CISO、負責法規解釋的法務／合規人員）。平台加速實施——但不取代專業能力。
- ❌ **神奇認證按鈕**：你仍然要實施控制措施、蒐集證據、通過稽核。平台讓這件事變得系統化，而不是自動化。
- ❌ **對初學者友善**：如果你不具備風險評鑑、控制目標或基本 Python 的理解，請先從 ISO 27001 訓練開始。
- ❌ **與廠商無關的通用樣板**：政策引用具體技術（AES-256、TLS 1.3、MFA）。你必須依自己的技術堆疊調整（AWS、Azure、地端、混合）。
- ❌ **零維護的解決方案**：基礎設施變更時腳本需要更新，政策需要年度審查，證據必須週期性重新產生。

**這是：**
- ✅ **工程驅動的合規**：以系統化、程式碼為基礎、證據自動化的做法推動 ISMS
- ✅ **有主見的框架**：我們做了決定（至少 AES-256、TLS 1.3、每季審查）。你可以改，但這些決定是明確的——不含糊。
- ✅ **為稽核最佳化**：透過把專業判斷前移到模型設計來減少稽核期間的含糊——稽核人員驗證已文件化的決策，而不是去解釋含糊的內容
- ✅ **可維護**：版控的 Markdown、可重新產生的工作簿、可測試（而不是在 SharePoint 上腐爛的靜態 Word 文件）
- ✅ **持續改善**：經驗學習登錄表、治理審查、變更控制流程（ISMS 會演進，不會停滯）
- ✅ **以設計確保資料主權**：地端部署讓你的合規證據始終在自己的掌控與司法管轄之下

---

## 👥 誰該使用？

<p>
<img src="https://img.shields.io/badge/✅_Good_Fit-See_Below-00AA00?style=flat-square" alt="Good Fit"/>
<img src="https://img.shields.io/badge/❌_Bad_Fit-See_Below-DC143C?style=flat-square" alt="Bad Fit"/>
</p>

### ✅ 適合

<p>
<img src="https://img.shields.io/badge/⚡_OPERATIONAL-SMEs_seeking_certification-FF6600?style=flat-square" alt="OPERATIONAL Good Fit"/>
<img src="https://img.shields.io/badge/🏗️_FRAMEWORK-Regulated_industries-9400D3?style=flat-square" alt="FRAMEWORK Good Fit"/>
</p>

**OPERATIONAL：**
- 想要以明確、可測試的要求取得 ISO 27001 認證的中小企業
- 想要自動化協助（檢核表產生），但不願投入完整 DevOps 的團隊
- 受夠了含糊政策（「適當」、「定期」、「足夠」）的組織
- 想要客觀合規證據（而不是「相信我」這類聲明）的 CISO

**FRAMEWORK (SSE)：**
- 需要多框架合規的受監管行業（金融服務：DORA + FINMA + ISO 27001）
- 想要全面、由控制措施衍生的評鑑，而不是中小企業範圍檢核表的組織
- 想要涵蓋每項控制措施要求完整深度的結構化、詳盡工作簿的團隊
- 想要具備逐項要求明確通過／不通過準則之客觀、可追溯證據的 CISO

### ❌ 不適合（兩種版本）

- 想要零努力取得認證的組織
- 不具備 Python 能力的團隊（腳本必須可執行，即使不大幅客製）
- 期待顧問全程呵護的 CISO（由你做決定，平台提供結構）
- 想要主觀彈性的組織（「我們會在稽核時決定什麼叫『適當』」——不行，現在就決定，並記錄下來）
- 不想被指點該怎麼做的團隊（平台是有主見的：AES-256，而不是「自己選加密方式」）

---

## ❓ 開立 issue 之前

**「有 SaaS 或託管版本嗎？」**

目前沒有。ISMS CORE 是讓你在自己的環境中部署與執行的平台。這是基於資料主權的刻意設計決策——你的 ISMS 證據是敏感的營運資料，而在當前的歐洲法規環境下，自架部署是架構上穩妥的預設選擇。託管版本並未排除在路線圖之外，但在任何這類服務中，資料主權都會是設計要求，而不是事後補上的考量。

**「為什麼評分較高的控制措施，工作簿比評分較低的更詳細？」**

評分反映證據客觀性——該控制措施的要求能被多直接、多可衡量地驗證。評分 4–5 的控制措施處理的是可以精確檢查的要求（留存期間、演算法規格），因此工作簿可以逐項建立明確的通過／不通過準則。評分 1–3 的控制措施處理的要求更依賴流程、判斷與聲明，因此工作簿雖然全面，但更依賴評鑑人員的記錄。兩者都是完整的評鑑——評分描述的是證據的性質，而不是所需投入的心力。

**「我可以先用 OPERATIONAL，之後再加 POL-00/POL-01 嗎？」**

可以，但不建議。OPERATIONAL 的設計就是自成一體的古典 ISMS。在實施途中加入 POL-00/POL-01，會形成比兩種純粹版本都更複雜的混合體。如果你認為自己需要 POL-00/POL-01，請直接從 FRAMEWORK 開始。如果你是中小企業，且確實只需要 ISO 27001 + GDPR，那麼 OPERATIONAL 不加它們就已足夠。

**「Python 腳本在我的環境中跑不起來。」**

腳本需要 Python 3.11+ 以及 `requirements.txt` 中列出的相依套件。它們在 Linux 與 macOS 上測試過。Windows PowerShell 環境可能需要調整。這是前置條件，不是支援問題。執行任何東西之前，請先讀前置條件一節。

**「我可以在沒有顧問的情況下用它取得 ISO 27001 認證嗎？」**

技術上可以，前提是你有合格的 CISO（具備 ISO 27001 知識與相關經驗），以及能做法規判定的法務／合規能力。平台加速實施——但不取代做出良好安全決策所需的專業能力。如果你不知道適用性聲明是什麼，請先找顧問。

**「政策引用瑞士法律（nFADP），但我不在瑞士。」**

法規架構以瑞士為主（nFADP、FINMA），因為那是設計時的情境。第 1 級的強制法規會因你所處的司法管轄區而不同。POL-00 提供做出這些判定的架構——你把第 1 級替換成自己適用的強制法規。控制措施政策（附錄 A）與司法管轄區無關。治理架構（POL-00/POL-01）並未鎖定特定司法管轄區，而是以司法管轄區為參數。

**「我發現政策有錯，或腳本有誤。」**

請開 issue，並附上：(1) 具體的文件或腳本，(2) 確切的錯誤或錯誤文字，(3) 正確的文字或預期行為，並附參考依據（ISO 27001 條款、法規條文等）。沒有具體參考依據的 issue 會被關閉。「這看起來不太對」無法處理。

---

## 🖥️ 第三層：ISMS CORE 平台

FRAMEWORK 與 OPERATIONAL 是**內容產品**——政策、工作簿與指引，以靜態文件的形式就能完整運作。你可以複製本儲存庫、執行 Python 產生器、填寫 Excel 工作簿，不需要其他東西，就能擁有功能完整、可接受稽核的 ISMS。

**ISMS CORE 平台**是建構在其上的營運層。它匯入這兩項產品，並把它們變成可運作的合規管理系統：

| 沒有平台 | 有平台 |
|-----------------|---------------|
| 把政策當文件閱讀 | 依關鍵字或控制措施跨所有政策搜尋 |
| 逐一開啟 Excel 工作簿 | 查看各節與各控制群組的彙總合規分數 |
| 在試算表中人工追蹤缺口 | 缺口生命週期管理，含嚴重度、負責人、SLA 與矯正追蹤 |
| 沒有跨框架的可見性 | ISO 27001 ↔ NIST CSF ↔ MITRE ATT&CK ↔ GDPR ↔ DORA 對應，即時呈現 |
| 人工蒐集證據 | 具備到期追蹤與新鮮度警示的證據項目 |
| 沒有稽核軌跡 | 完整且不可竄改的日誌，記錄誰在何時做了什麼 |

平台是以 Docker Compose 部署於地端的技術堆疊。核心服務包括 FastAPI + PostgreSQL + Redis + OpenSearch + Celery + Angular 22 + nginx TLS + Celery Beat + 專用的弱點情報來源容器（MITRE ATT&CK、CISA KEV、EPSS、NVD CVE、ENISA EUVD、Exploit-DB）+ 自動化連接器執行器（44 個原生連接器）。選用的 OSINT 情報來源容器另增加 12 個即時威脅情報來源。**v1.1 已上線。**同樣的資料主權原則依然適用——你的合規資料不會離開你的基礎設施。

平台也包含 44 個原生連接器（Microsoft、網路、身分、弱點、ITSM、監控、雲端態勢、威脅情報），可把即時證據直接推送進合規資料庫——支援的系統不需要人工蒐集證據。

**平台是加值項，絕非必要項。**FRAMEWORK 與 OPERATIONAL 才是產品。平台是讓它在規模上真正運作的引擎。

架構細節、功能與部署指引請見 [PLATFORM.zh-TW.md](PLATFORM.zh-TW.md)。

---

<p align="center">
<strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
<em>在這裡，竹天線真的能用。</em> 🎋
</p>
