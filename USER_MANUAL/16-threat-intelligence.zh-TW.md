# 威脅情報

<p align="center"><a href="16-threat-intelligence.md">English</a> · <strong>繁體中文</strong> · <a href="16-threat-intelligence.zh-CN.md">简体中文</a></p>

<!-- ISMS-CORE:USER-MANUAL:16-threat-intelligence:v1.3:2026-08-22 -->

---

## 概觀

威脅情報章節讓您即時取用 18+ 個直接整合至平台的威脅與弱點情報來源。此功能支援 ISO 27001:2022 控制措施 A.5.7（威脅情報），並提供所需的技術深度，以評鑑您對當前對手技術、已遭利用的弱點，以及來自公開 OSINT 情報源的實際 IOC 資料的曝險程度。

在側邊欄前往 **Intelligence**。

> 當 `isms-core-threat-intel` 選用設定檔未啟用時，所有 Intelligence 側邊欄項目仍會顯示，但呈現灰色。

---

## 情報源容器

平台執行兩個專用的情報源容器：

- **`isms-core-feeds`** —— 弱點與對手情報（標準堆疊下永遠啟用）
- **`isms-core-threat-intel`** —— OSINT IOC 情報源（選用；以 `--profile threat-intel` 加上 `.env` 中的 `THREAT_INTEL_ENABLED=true` 啟用）

---

## 情報源排程 —— 弱點與對手情報

這些情報源在 `isms-core-feeds` 容器中執行，且永遠啟用。

| 情報源 | 排程（UTC） | 提供內容 |
|------|----------------|-----------------|
| **MITRE ATT&CK v19** | 每週，週日 00:00 | 完整 ATT&CK 框架 —— 戰術、技術、子技術、緩解措施、對手組織、軟體、攻擊行動 |
| **MITRE ATLAS** | 每週，週日 00:30 | AI/ML 專屬的對手技術（對抗式機器學習威脅態勢） |
| **CISA KEV** | 每日 02:00 | CISA 的已知遭利用弱點目錄 —— 已遭實際利用的 CVE |
| **FIRST EPSS** | 每日 02:30 | 弱點利用預測評分系統 —— 每個 CVE 在未來 30 天內遭利用的機率分數（0–1） |
| **NVD CVE** | 每日差異 03:00 / 每週全量 週日 01:00 | 來自 NIST NVD 的約 250,000 個 CVE，含 CVSS v2/v3/v4 分數、CWE 與 CPE 適用性 |
| **NVD CPE** | 每週，週日 01:30 | 軟體／硬體產品識別碼 —— 可將 CVE 關聯至特定產品 |
| **ENISA EUVD** | 每日 | 歐洲弱點資料庫 —— 帶已遭利用旗標的 CVE，以及高嚴重度（CVSS ≥ 4.0）的歐盟指派項目；以 `in_euvd` 旗標交叉充實至 NVD CVE 文件 |
| **Exploit-DB** | 每日 | 約 52,000 個公開攻擊程式；以 `edb_id`、`edb_verified`（Metasploit 旗標）與 `edb_description` 交叉充實 CVE |
| **VulnCheck KEV** | 每日 04:45 | VulnCheck 自家的已知遭利用弱點目錄 —— 範圍比 CISA 更廣；約 67% 的項目不在 CISA KEV 中。在 CVE 瀏覽器上加入 `in_vulncheck_kev` 旗標，與 CISA 的 `in_kev` 分開。需要 `VULNCHECK_API_KEY`（免費 Community 方案） |
| **MaxMind GeoLite2** | 每週，週二 01:00 | 用於所有情報源 IP 對國家解析的 GeoIP 資料庫 |

---

## 情報源排程 —— OSINT IOC 情報源

這些情報源在 `isms-core-threat-intel` 容器中執行。若先前沒有成功的執行紀錄，所有情報源會在首次開機時自動執行。

| 情報源 | 排程（UTC） | API 金鑰 | 提供內容 |
|------|----------------|---------|-----------------|
| **CIRCL MISP** | 每 6 小時：00:00、06:00、12:00、18:00 | 無 | 來自盧森堡 CIRCL 的公開 OSINT MISP 情報源 —— 附 ATT&CK TID、Malpedia 家族與行為者標籤的 IOC（IP、網域、URL、雜湊） |
| **Botvrij MISP** | 每 6 小時：01:00、07:00、13:00、19:00（錯開） | 無 | 公開 OSINT 情報源（botvrij.eu）—— 結構定義與 CIRCL 相同，以 IOC 值加來源去重 |
| **AbuseIPDB** | 每日 02:00 | `ABUSEIPDB_API_KEY` | 前 10,000 個最高信心的濫用 IP；單一 IP 隨選充實，快取 24 小時 |
| **URLhaus** | 每日 03:00 | 無 | 代管惡意程式酬載的惡意 URL，來自 abuse.ch |
| **ThreatFox** | 每 6 小時：03:00、09:00、15:00、21:00 | `THREATFOX_API_KEY`（選用） | 連結至具名惡意程式家族並附信心分數的 IOC（IP、網域、URL、雜湊） |
| **SSLBL** | 每日 04:00 | 無 | SSL 憑證黑名單 —— 惡意程式 C2 基礎設施所用憑證的 SHA1 指紋 |
| **AlienVault OTX** | 每日 04:30 | `OTX_API_KEY` | Open Threat Exchange pulses —— 帶 TLP 標示、ATT&CK TID 的 IOC，以及由 pulse 訂閱人數推得的信心分數 |
| **Feodo Tracker** | 每 6 小時：04:30、10:30、16:30、22:30 | 無 | Emotet、QakBot、TrickBot 與 Dridex 殭屍網路的 C2 IP 黑名單（信心值 85） |
| **Red Flag Domains** | 每日 05:00 | 無 | 因網路釣魚、惡意程式與 C2 而標記的新註冊可疑網域 |
| **Stopforumspam** | 每日 05:30 | 無 | 約 140,000 個因垃圾訊息、殭屍網路活動與論壇濫用而通報的 IP |
| **MalwareBazaar** | 每 6 小時：02:00、08:00、14:00、20:00 | `MALWAREBAZAAR_API_KEY` | 近期惡意程式樣本雜湊（MD5/SHA1/SHA256）與家族歸因 |
| **Malpedia** | 每週，週日 03:00 | 無 | 惡意程式家族知識庫（別名、ATT&CK TID、關聯行為者）與威脅行為者目錄 |
| **VirusTotal**（充實） | 每日 07:00 | `VT_API_KEY`（選用） | 以 VT 偵測比例充實既有 IOC —— 僅更新 `confidence` 欄位；不會新增 IOC |
| **IPInfo**（充實） | AbuseIPDB 之後 | `IPINFO_API_KEY`（選用） | 以城市、國家與 ASN 對 AbuseIPDB 的 IP 進行地理充實；每次執行 120 秒時間預算 |

> **首次開機注意事項：** 所有 OSINT 情報源會在啟動時立即執行一次，以充填資料庫。大型情報源（CIRCL MISP 約 133K 個 IOC、Stopforumspam 約 140K 個 IP、AlienVault OTX 約 90K 個 IOC）各需數分鐘。排程器會自動處理後續的差異更新。

---

## 情報源狀態

情報源執行歷程與狀態可見於：

- **Dashboard** —— Intelligence Cards 面板（CVE 數量、KEV 數量、IOC 數量、MITRE 同步狀態、整體情報源健康狀態）
- **Intelligence → Threat Feeds** —— 完整的情報源執行歷程，含所有情報源的最後執行時間戳、狀態與紀錄筆數
- **Header banner** —— 若任何情報源或連接器在過去 24 小時內回報錯誤，每個頁面頂端會出現可關閉的警告橫幅

若某個情報源顯示錯誤標記（Intelligence 側邊欄群組上的紅點），請前往 **Intelligence → Threat Feeds** 查看錯誤詳情。管理員可使用 **RUN** 按鈕隨選觸發任何情報源，或使用 **CANCEL** 中止執行中的情報源。

---

## MITRE ATT&CK

前往 **Intelligence → MITRE ATT&CK**。

### 技術瀏覽器

依戰術瀏覽完整的 ATT&CK 框架。每項技術顯示：

- 技術 ID 與名稱（例如 T1190 —— Exploit Public-Facing Application）
- 戰術（Initial Access、Execution、Persistence 等）
- 子技術清單
- 說明與偵測指引
- 緩解措施 —— 因應此技術的 ISO 27001 控制措施

### 行為者情報

前往 **Groups** 分頁瀏覽對手組織。每個組織顯示：

- 歸因與別名
- 目標產業與地理區域
- 此組織使用的技術
- 關聯軟體與攻擊行動
- 連往 MITRE ATT&CK 官方頁面的連結

運用行為者情報為您 EBIOS RM 工作坊 2 的風險來源提供脈絡 —— 若您營運的產業是已知組織的目標，其技術組合會告訴您哪些控制措施最受考驗。

### 熱圖

前往 **Heatmap** 分頁，取得 MITRE ATT&CK Navigator 風格的技術熱圖。熱圖顯示：

- 以您所屬產業為目標的組織使用了哪些技術
- 您的 EBIOS RM 攻擊路徑引用了哪些技術
- 涵蓋範圍疊加 —— 哪些技術已由您的 ISO 27001 控制措施因應

---

## 威脅曝險

前往 **Intelligence → Threat Exposure**。

> 需要 `isms-core-threat-intel` 容器已啟用並已充填資料。

Threat Exposure 頁面顯示您的哪些 ISO 27001 控制措施曝露於即時 OSINT 情報源中觀察到的活躍威脅技術。它會把 `ti_iocs` 中附加至 IOC 的 ATT&CK 技術 ID 與 ATT&CK → ISO 27001 對照表結合，再交叉參照您的框架評鑑分數。

### 摘要列

| 指標 | 意義 |
|--------|---------|
| **活躍技術** | 即時 IOC 情報源中出現的不同 ATT&CK TID |
| **受影響控制措施** | 對應至那些技術的 ISO 27001 控制措施 |
| **辨識出的缺口** | 評鑑分數偏低，或狀態為 "non_compliant" / "not_assessed" 的受影響控制措施 |

### 技術 → 控制措施對照表

| 欄位 | 意義 |
|--------|---------|
| 技術 | ATT&CK TID（例如 T1190） |
| IOC 數量 | 標記此技術的活躍 IOC 數量 |
| 來源 | 為此技術提供 IOC 的情報源 |
| ISO 27001 控制措施 | 對應至此技術的控制措施，依評鑑分數上色（綠色 ≥ 70%、橘色 40–69%、紅色 < 40%、灰色 = 未評鑑） |
| 缺口 | 此技術處於缺口狀態的控制措施數量 |

使用 Threat Exposure 頁面排定修復優先順序：IOC 數量高且控制措施呈紅色／灰色的技術，代表您最高風險的曝險。

---

## CVE / CPE 瀏覽器

前往 **Intelligence → CVE Explorer**。

### CVE 搜尋

搜尋與篩選 NVD CVE 索引（約 250,000 筆）：

| 篩選條件 | 選項 |
|--------|---------|
| 關鍵字 | CVE ID 或說明中的關鍵字 |
| 嚴重度 | 嚴重 / 高 / 中 / 低（CVSS v3 基本分數） |
| EPSS 分數 | 滑桿（0.00–1.00）—— 依利用機率篩選 |
| 僅 KEV | 僅顯示 CISA KEV 清單上的 CVE |
| 僅 VulnCheck | 僅顯示 VulnCheck 自家、範圍更廣的 KEV 目錄中的 CVE |
| EUVD 旗標 | 僅顯示存在於歐洲弱點資料庫中的 CVE |
| 僅 EDB | 僅顯示在 Exploit-DB 中有已知公開攻擊程式的 CVE |
| 年份 | CVE 發布年份 |

### CVE 詳情面板

點選任何 CVE 以開啟詳情面板：

- CVSS v2、v3 與 v4 分數及向量字串
- CWE（弱點類型）分類
- CPE 適用性清單（哪些產品受影響）
- EPSS 分數與百分位
- KEV 狀態與加入 KEV 清單的日期
- VulnCheck KEV 狀態（獨立於 CISA KEV —— 一個 CVE 可能在其中之一、另一個，或兩者皆是）
- EUVD 旗標，以及（若有）歐盟指派的識別碼
- EDB 標籤 —— 若有公開攻擊程式則為 `EDB`，若有 Metasploit 模組則為 `EDB✓`
- NVD 參照連結

### CPE 分頁

CPE 分頁可讓您搜尋軟體／硬體產品目錄。適合用來找出環境中影響特定產品的所有 CVE。

---

## ENISA EUVD 瀏覽器

前往 **Intelligence → EUVD Explorer**。

EUVD 瀏覽器提供 ENISA 歐洲弱點資料庫的存取 —— 這是歐盟的權威來源，收錄與 NIS2 及 DORA 義務下歐洲營運者相關的弱點資訊。

- 瀏覽標記為**已遭實際利用**的弱點（修補的最高優先順序）
- 依 CVSS 嚴重度篩選 —— 聚焦於嚴重與高嚴重度的項目
- 切換 **Exploited only** 或 **Critical only** 以浮現最高風險的子集
- 同時查看歐盟指派的 EUVD 識別碼與 CVE ID
- 詳情面板顯示受影響的廠商、產品、別名、EPSS 分數與 CVSS 資料
- 將篩選後的集合匯出為 CSV，作為 ISO 27001 A.8.8 的稽核證據

EUVD 情報源會交叉充實 NVD CVE 索引：每個出現在 EUVD 中的 CVE 都會取得 `in_euvd` 旗標與 `euvd_id` 欄位，可在 CVE 瀏覽器中看到。

---

## KEV 稽核報告（A.8.8）

前往 **Intelligence → Threat Feeds → A.8.8 KEV Audit Report**。

KEV 稽核報告是為 ISO 27001:2022 A.8.8（技術弱點管理）量身打造的證據產物。它顯示：

- 所有 CISA KEV 項目依狀態分類 —— 未處理、已修補、進行中、不適用
- 依 CVE 區分的修復狀態明細
- 各廠商摘要（每個廠商的產品受多少 KEV 影響）
- 修復時間統計

選擇審查區間（3／6／12 個月）。將報告匯出為 CSV，納入您的稽核證據包。此報告為稽核人員提供可辯護的觀點，說明您的組織如何追蹤與修復已遭利用的弱點。

---

## MITRE ATLAS（AI/ML 威脅）

前往 **Intelligence → ATLAS** 取得 AI/ML 專屬的威脅框架。ATLAS 記載用於攻擊機器學習系統的技術 —— 訓練資料汙染、對抗式樣本、模型萃取等。

ATLAS 與 AI 擴充套件（ISO 42001:2023）相關 —— 特別是涵蓋 AI 風險評鑑、穩健性與事件管理的控制措施。

---

## IOC 瀏覽器

前往 **Intelligence → IOC Explorer**。

IOC 瀏覽器提供可搜尋的表格，彙整自 12 個 OSINT 情報源收集到的所有入侵指標。這需要 `isms-core-threat-intel` 容器正在執行。

### 篩選條件

| 篩選條件 | 選項 |
|--------|---------|
| 搜尋 | IOC 值自由文字搜尋（子字串比對） |
| 類型 | IP / Domain / URL / MD5 / SHA1 / SHA256 |
| 來源 | CIRCL MISP / Botvrij MISP / AbuseIPDB / URLhaus / ThreatFox / SSL Blacklist / AlienVault OTX / Feodo Tracker / Red Flag Domains / Stopforumspam / MalwareBazaar / Malpedia |

### 表格欄位

| 欄位 | 說明 |
|--------|-------------|
| 類型 | IOC 類型標籤 |
| 值 | 指標值（會截斷 —— 展開該列以查看完整值） |
| 來源 | 提供此 IOC 的情報源 |
| 信心 | 偵測比例（0–100%）；來自情報源中介資料或 VirusTotal 充實 |
| TLP | 紅綠燈協議標示（WHITE / GREEN / AMBER / RED）—— 取自 MISP 事件與 AlienVault OTX pulses |
| 最後出現 | 此 IOC 在情報源中最近被觀察到的日期 |
| 歸因 | 惡意程式家族、威脅行為者與 ATT&CK TID 標籤（每類最多行內顯示 2 個） |

點選任何一列以展開完整詳情檢視 —— 顯示完整的 IOC 值、首次出現日期、所有家族／行為者／TID 關聯，以及來源情報源的完整標籤清單。

關聯模型會在匯入時把 ATT&CK TID、Malpedia 家族代號與行為者代號標記到 IOC 上 —— 執行期不會進行任何聯結。這表示一個 IP 位址可以在單一紀錄中同時帶有其濫用分數、曾被觀察到散布的惡意程式家族、歸因至該家族的威脅行為者組織，以及該行為者使用的 ATT&CK 技術。

> **Malpedia 注意事項：** Malpedia 不會對 IOC 瀏覽器貢獻任何列 —— 它改為充填惡意程式圖鑑（家族、行為者、工具）。Malpedia 的 IOC 數量為 0 是正確的。

---

## IP 充實

前往 **Intelligence → IP Enrichment**。

輸入任何 IP 位址，以從五個來源取得隨選充實：

### AbuseIPDB 檢查

- **濫用信心分數**（0–100）：該 IP 為惡意的機率
- AbuseIPDB 資料庫中的**通報總數**
- **最後通報時間**時間戳
- **使用類型**（ISP／資料中心／VPN 等）
- 通報濫用的**類別**（連接埠掃描、暴力破解、網頁垃圾訊息等）

### Shodan 資料

若已設定 `SHODAN_API_KEY`：

- 開放連接埠與服務橫幅
- 主機名稱與反向 DNS
- ASN 與組織
- 主機上偵測到的 CVE（來自 Shodan 掃描）
- 最後掃描日期

若未設定 Shodan API 金鑰，則會改用 **Shodan InternetDB** 免費服務作為備援 —— 不需帳戶即可提供開放連接埠、CPE、標籤、主機名稱與 CVE 清單。

若某個 IP 未被 Shodan 索引（對傳輸 IP 與私人範圍而言很常見），小工具會顯示 "IP not indexed"，而非錯誤。

### MaxMind GeoLite2

若已設定 `MAXMIND_ACCOUNT_ID` 與 `MAXMIND_LICENSE_KEY`：來自 MaxMind GeoLite2 City 網路服務的國家、城市與 ASN。

### IPInfo 隱私

若已設定 `IPINFO_API_KEY`：隱私分類（Clean / VPN / Proxy / Tor / Relay / Hosting）以及底層服務名稱。

### GreyNoise

若已設定 `GREYNOISE_API_KEY`：網際網路噪音／掃描器分類（benign / malicious / unknown）、該 IP 是否為已知的全網際網路掃描器，以及 RIOT 狀態（已知的合法業務服務 —— 搜尋引擎、CDN 等 —— 而非威脅）。GreyNoise 的免費 Community 方案每週上限 50 次查詢（API 金鑰需企業電子郵件），因此此來源刻意僅供隨選查詢，永不屬於排程的批次情報源。

充實結果會被快取，以尊重每個來源的速率限制 —— AbuseIPDB 與 Shodan 為 24 小時，MaxMind、IPInfo 與 GreyNoise 為 30 天（這些都是流量較低或配額較嚴格的來源）。

---

## 惡意程式圖鑑

前往 **Intelligence → Malware Atlas**。

惡意程式圖鑑呈現由威脅情報容器匯入的 Malpedia 知識庫。它需要 `isms-core-threat-intel` 容器正在執行，且 `TI_MALPEDIA_ENABLED=true`。

### 惡意程式家族

瀏覽完整的 Malpedia 家族目錄：

- **家族名稱**與常見別名
- **說明** —— 來源、目標、首次出現、能力
- **ATT&CK TID** —— 與此家族相關的 ATT&CK 技術
- **關聯行為者** —— 已知使用此惡意程式的威脅組織
- 連往 Malpedia 來源頁面的連結

### 威脅行為者

瀏覽威脅行為者目錄：

- **行為者名稱**與別名
- **國家歸因**（疑似國家資助來源）
- **動機** —— 間諜活動／財務／駭客行動主義／未知
- **說明** —— 活動摘要與已知目標

> **注意：** 惡意程式家族與威脅行為者資料來自 MISP galaxy 開放 GitHub 資料集 —— 不需 API 金鑰。

### 關聯用途

惡意程式圖鑑是 IOC 關聯的查詢端點。當 MISP 事件包含如 `misp-galaxy:malpedia="win.emotet"` 的 galaxy 標籤時，匯入流水線會把 Malpedia 代號解析為家族紀錄並標記到該 IOC 上。您可以從以下方向樞紐分析：

- IOC → 惡意程式家族 → ATT&CK 技術
- IOC → 惡意程式家族 → 威脅行為者 → 來源國家
- 威脅行為者 → 所有關聯惡意程式家族 → 使用的所有 ATT&CK 技術

---

## 情報與證據

威脅情報資料與證據追蹤器整合：

- 當新的 KEV 項目符合與您環境相關的 CVE 時，會產生通知
- KEV 修復狀態可晉升為證據追蹤器中的項目，作為 A.8.8 下主動弱點管理的證明
- IOC 瀏覽器結果可在缺口備註與修復行動中被引用，作為遭受主動威脅鎖定的證據
- Threat Exposure 頁面提供即時 IOC 情報源與您的 ISO 27001 控制措施評鑑分數之間的直接連結

---

## 情報源設定

情報源設定屬於管理員職能。若某個情報源未執行，或您需要變更情報源設定，請洽您的管理員。

| 變數 | 用途 | 免費註冊 |
|----------|-------------|-------------------|
| `NIST_API_KEY` | 更快的 NVD 初始充填（將速率限制從 5→50 次請求／30 秒） | nvd.nist.gov |
| `ABUSEIPDB_API_KEY` | AbuseIPDB 黑名單 + IP 充實 | abuseipdb.com |
| `SHODAN_API_KEY` | Shodan 付費充實（若未設定則使用 InternetDB 免費備援） | shodan.io |
| `OTX_API_KEY` | AlienVault OTX 情報源 | otx.alienvault.com |
| `OTX_IMPORT_DAYS` | 首次執行時的 OTX 歷史深度（預設：`90` 天） | — |
| `THREATFOX_API_KEY` | ThreatFox 的更高速率限制（無金鑰時以較低限制運作） | threatfox.abuse.ch |
| `MALWAREBAZAAR_API_KEY` | MalwareBazaar 樣本情報源 | bazaar.abuse.ch |
| `VT_API_KEY` | VirusTotal IOC 充實（免費方案：約 500 次請求／日） | virustotal.com |
| `VT_DAILY_LIMIT` | 每次 VT 執行充實的 IOC 上限（預設：`450`，免費方案的安全上限） | — |
| `MAXMIND_ACCOUNT_ID` / `MAXMIND_LICENSE_KEY` | 用於 IP 地理定位的 GeoLite2 資料庫 | maxmind.com |
| `IPINFO_API_KEY` | 對 AbuseIPDB IP 的強化地理 + ASN 充實 | ipinfo.io |
| `VULNCHECK_API_KEY` | VulnCheck KEV 情報源（免費方案：1,000 次請求／分鐘） | console.vulncheck.com |
| `GREYNOISE_API_KEY` | IP 充實頁面上的 GreyNoise 隨選 IP 查詢（免費方案：每週 50 次查詢，需企業電子郵件） | greynoise.io |
| `TI_MISP_IMPORT_FROM_DATE` | MISP 首次執行的日期下限（預設 `2024-01-01`） | — |
| `TI_RUN_ON_START` | 強制所有 OSINT 情報源在每次容器啟動時執行 | — |

> **VirusTotal 充實：** VT 不會新增 IOC —— 它查詢資料庫中既有的 IOC（先取 `confidence` 為 NULL 者，再取最久未檢查者），且僅在 VT 分數高於現有值時更新其 `confidence` 欄位。IOC 每 30 天重新檢查一次。免費方案允許約 500 次請求／日；預設上限 450 安全地低於該限制。

**Intelligence → Threat Feeds** 中的 **CPE Option B** 切換可讓管理員在 KEV 廠商 CPE（輕量）與完整 CPE 資料庫（全面）之間切換 NVD CPE 拉取策略，無需重新啟動容器。此設定儲存在平台資料庫中，並會覆寫 `FEEDS_CPE_FULL` 環境變數。

<!-- QA_VERIFIED: 2026-05-02 -->
