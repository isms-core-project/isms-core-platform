<h1 align="center">🎋 為 ISMS CORE 貢獻</h1>

<p align="center"><a href="CONTRIBUTING.md">English</a> · <strong>繁體中文</strong> · <a href="CONTRIBUTING.zh-CN.md">简体中文</a></p>

<p align="center">
  <img src="https://img.shields.io/badge/QA-Engineering_First-2E8B57?style=for-the-badge" alt="QA Engineering First"/>
</p>

<p align="center">
  <a href="#-qa-關卡"><img src="https://img.shields.io/badge/QA_Gates-Enforced-00AA00?style=flat-square" alt="QA Gates"/></a>
  <a href="#-python-腳本標準"><img src="https://img.shields.io/badge/Python-Standardized-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
  <a href="#-線上研究要求"><img src="https://img.shields.io/badge/Research-Required-FF6600?style=flat-square" alt="Research Required"/></a>
  <a href="#-工程原則"><img src="https://img.shields.io/badge/Feynman-Approved-0066CC?style=flat-square" alt="Feynman Approved"/></a>
</p>

<p align="center">
  <em>並非所有文件都需要相同程度的標準化。把嚴謹用在該用的地方。</em>
</p>

---

## 🎯 QA 理念

ISMS CORE 針對**可靠性**、**可維護性**與**正確性**的重點所在，施加適當程度的嚴謹。

> *「標準化是好的。過度標準化是貨櫃崇拜。把嚴謹用在該用的地方。」*

---

## 📋 文件類型與品質標準

<table>
<tr>
<th>類型</th>
<th>一致性</th>
<th>變更頻率</th>
<th>QA 關卡</th>
<th>徽章</th>
</tr>
<tr>
<td><strong>📜 POL</strong>（政策）</td>
<td>🔴 高</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Formal_Approval-9400D3?style=flat-square" alt="Formal"/></td>
</tr>
<tr>
<td><strong>📋 IMP</strong>（實作）</td>
<td>🟡 中等</td>
<td>中</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Living_Document-32CD32?style=flat-square" alt="Living"/></td>
</tr>
<tr>
<td><strong>🐍 SCR</strong>（腳本）</td>
<td>🔴 高</td>
<td>中</td>
<td><code># QA_VERIFIED:</code></td>
<td><img src="https://img.shields.io/badge/Code_Review-3776AB?style=flat-square" alt="Code Review"/></td>
</tr>
<tr>
<td><strong>📚 REF</strong>（參考資料）</td>
<td>🟡 中等</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Technical_Accuracy-FF6600?style=flat-square" alt="Technical"/></td>
</tr>
<tr>
<td><strong>🏢 CTX</strong>（情境）</td>
<td>🟡 中等</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Accuracy_Verified-0066CC?style=flat-square" alt="Verified"/></td>
</tr>
<tr>
<td><strong>📝 FORM</strong>（表單）</td>
<td>🟡 中等</td>
<td>低</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Template_Verified-32CD32?style=flat-square" alt="Template"/></td>
</tr>
</table>

---

### 📋 IMP 文件結構（UG／TG）

每一份 IMP（實作）文件都以**成對組合**的兩個檔案存在——一份使用者指南與一份技術規格。這樣的分離讓稽核人員、實作人員與開發人員各自拿到量身打造的文件，而不互相污染。

```
IMP/
├── ISMS-IMP-A.8.9.1-UG - Baseline Configuration Assessment.md    ← 供實作人員
└── ISMS-IMP-A.8.9.1-TG - Baseline Configuration Assessment.md    ← 供開發人員／稽核人員
```

#### UG — 使用者填寫指南

**適用對象：** 資訊安全分析師、控制措施擁有者、評鑑人員、合規主管

UG 是**由人撰寫**的文件，引導讀者完成一份評鑑工作簿。它回答的問題是：*「我手上有這份 Excel 檔案——該拿它怎麼辦？」*

| 章節 | 用途 |
|---------|---------|
| 評鑑總覽 | 本評鑑涵蓋的範圍、為何重要、範疇界線 |
| 先決條件 | 開始前必須就緒的事項（存取權、資料、核准） |
| 工作簿結構 | 逐一工作表概述 Excel 工作簿 |
| 填寫逐步指引 | 逐步驟說明如何填寫每一張工作表 |
| 證據蒐集 | 該蒐集哪些證據、存放位置、命名慣例 |
| 常見陷阱 | 8-10 個 `MISTAKE:` 範例與修正 |
| 品質檢核表 | 提交前的檢核項目 |
| 審查與核准 | 由誰審查、核准流程、升級處理 |

#### TG — 技術規格

**適用對象：** Python 開發人員、Excel 工作簿開發人員、QA 工程師

TG 是由 Python 產生器腳本（`SCR/generate_*.py`）**自動產生**。它是產生器程式碼的人類可讀版本——每一張工作表、欄位、資料驗證下拉選單、色彩樣式與公式，都以結構化表格記錄。

| 章節 | 用途 |
|---------|---------|
| 工作簿總覽 | 文件編號、輸出檔名、工作表總數、控制項參照 |
| 色彩配置 | 所有色碼、樣式名稱與用途說明 |
| 工作表 N：*名稱* | 逐工作表的規格，含欄位、寬度、驗證、公式 |
| 資料驗證清單 | 產生器中定義的所有下拉選單值清單 |

**重新產生 TG：** 每當產生器變更，工廠腳本就會重新產生 TG 內容：

```bash
python3 generate_tg_from_scr.py --apply          # 全部 252 個 TG
python3 generate_tg_from_scr.py --control a.8.9   # 單一控制群組
```

每一份 TG 技術內容的開頭都會標示其來源：

```
> 由 `generate_a89_1_baseline_configuration.py` 自動產生
> 重新產生指令：`python3 generate_tg_from_scr.py --apply`
```

#### IMP QA 準則（v4.5+）

| 要求 | 說明 |
|-------------|-------------|
| ✅ UG/TG 分離 | 每份 IMP 都以 `-UG` 與 `-TG` 檔案成對存在 |
| ✅ 標準標頭 | 三行格式：粗體標題、副標（UG/TG）、ISO 控制項參照 |
| ✅ 控制措施引文 | 依 ISO 27001:2022 附錄 A，使用 "should"（而非 "shall"） |
| ✅ 英式拼法 | organisation、authorised、standardised |
| ✅ 標準結尾 | `**END OF SPECIFICATION**` + 分隔線 + 以破折號（—）帶出的引文 |
| ✅ QA 標記 | 🎋 標記之後的 `<!-- QA_VERIFIED: YYYY-MM-DD -->` |

---

## 🚦 QA 關卡

<p align="center">
  <img src="https://img.shields.io/badge/Gate-Pass_Required-00AA00?style=for-the-badge" alt="Gate Pass Required"/>
</p>

內容**唯有在 QA 關卡通過後**才會晉升到本儲存庫。每種文件類型都帶有一個 QA 標記，晉升前必須存在：

| 文件 | 必要的 QA 標記 |
|----------|--------------------|
| POL / IMP / REF / CTX / FORM | 檔案結尾的 `<!-- QA_VERIFIED: YYYY-MM-DD -->` |
| SCR（Python 腳本） | `# QA_VERIFIED: YYYY-MM-DD` 頁尾區塊 |

> **維護者注意：** 晉升由私有 `factory_claude_ai` 儲存庫中的內部開發工具（`95-isms-core-factory/promote_control.sh`）處理。本儲存庫中的內容在發佈到此之前，都已通過所有 QA 關卡。

---

## 🐍 Python 腳本標準

### 必要結構

```python
# =============================================================================
# 文件中繼資料
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.X.X.X"
WORKBOOK_NAME = "Assessment Name"
CONTROL_ID = "A.X.X"
CONTROL_NAME = "Control Name"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# 時間戳記
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# 輸出檔名
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"
```

### 日誌

| ❌ 不要 | ✅ 要 |
|----------|-------|
| `print("message")` | `logger.info("message")` |

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)
```

### QA 頁尾

```python
# =============================================================================
# QA_VERIFIED: YYYY-MM-DD
# QA_STATUS: PASSED
# QA_TOOL: Claude Code
# CHANGES: 變更說明
# =============================================================================
```

---

## 📂 資料夾結構

每個控制項都自成一格，包含所有成品類型：

```
isms-a.X.X-control-name/
├── POL/                      # 📜 政策文件
├── IMP/                      # 📋 實作指南（UG + TG 成對）
├── SCR/                      # 🐍 腳本（產生器、正規化器、合併器）
├── WKBK/                     # 📊 產生的 Excel 工作簿
├── REF/                      # 📚 參考資料（如適用）
├── CTX/                      # 🏢 情境文件（如適用）
└── FORM/                     # 📝 表單與範本（如適用）
```

---

## 🔍 線上研究要求

<p align="center">
  <img src="https://img.shields.io/badge/⚠️_Research-MANDATORY-FF0000?style=for-the-badge" alt="Research Mandatory"/>
</p>

**所有 IMP 與 SCR 開發都必須包含線上研究**，以驗證：

- ✅ 該控制措施的最新最佳實務
- ✅ 與 NIST、CIS、MITRE ATT&CK 框架的一致性
- ✅ 實作指引的技術準確性
- ✅ 最新工具能力與整合模式

**關鍵參照框架：**

<p align="center">
  <img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square" alt="ISO"/>
  <img src="https://img.shields.io/badge/NIST_CSF-2.0-FF6600?style=flat-square" alt="NIST"/>
  <img src="https://img.shields.io/badge/CIS_Controls-v8-00AA00?style=flat-square" alt="CIS"/>
  <img src="https://img.shields.io/badge/MITRE_ATT&CK-Enterprise-DC143C?style=flat-square" alt="MITRE"/>
</p>

---

## ⚖️ 工程原則

> *「標準化是好的。過度標準化是貨櫃崇拜。把嚴謹用在該用的地方。」*

**Feynman 會問：** *「這樣的差異有存在的目的嗎？」*

| 答案 | 動作 |
|--------|--------|
| ✅ 是 | 記錄原因並保留 |
| ❌ 否 | 標準化 |
| ⚠️ 破壞功能 | 不要強求一致 |

---

## 🔬 驗證流程

<p align="center">
  <img src="https://img.shields.io/badge/Multi--Stage-QA_Process-DC143C?style=for-the-badge" alt="Multi-Stage QA Process"/>
</p>

每一個控制套件都會經過結構化的多階段驗證流程，以確保品質與正確性。

```
  ┌──────────────────────────┐
  │ ISMS Core 專案           │
  │ （架構師／擁有者）       │
  └─────────────┬────────────┘
                │ 需求 + 領域專業知識
                ▼
  ┌──────────────────────────┐
  │ Claude Code（Sonnet）    │──── 實作
  │ 建置 + 程式碼審查        │     POL, IMP, SCR, REF, CTX
  └─────────────┬────────────┘
                │
                ▼
  ┌──────────────────────────┐
  │ ISMS Copilot X           │──── 稽核審查
  │ （文件 + QA）            │     階段 1：適足性，階段 2：有效性
  └─────────────┬────────────┘
                │
                ▼
  ┌──────────────────────────┐
  │ ISMS Core 專案           │
  │ 最終核准關卡             │
  └──────────────────────────┘
```

| 貢獻者 | 角色 | 重點 |
|-------------|------|-------|
| **Claude Code（Sonnet）** | 實作 + QA | 政策撰寫、Python 產生器、程式碼審查、模式分析 |
| **ISMS Copilot X** | 文件稽核 | 階段 1 文件適足性、階段 2 實作有效性 |
| **ISMS Core 專案** | 架構師 + 最終關卡 | 方法論、領域專業知識、IP 擁有權、核准權限 |

每一個階段都在 ISMS Core 專案撰寫的**專用指令集**下運作——這些結構化提示定義了範疇、限制、輸出格式與稽核準則。它們是受控的營運文件，精確規定必須檢查什麼、忽略什麼（例如佔位日期），以及如何分類發現事項。

### 發現事項分類

| 嚴重性 | 準則 | 動作 |
|----------|----------|--------|
| **嚴重** | 缺少控制措施實作、稽核阻礙 | 晉升前必須解決 |
| **高** | 證據或涵蓋範圍有顯著缺口 | 晉升前必須解決 |
| **中** | 指引不完整、輕微不一致 | 於 QA 階段解決 |
| **低** | 風格、格式、改善機會 | 留待未來迭代追蹤 |

---

## 🤖 AI 輔助開發

<table>
<tr>
<th>貢獻者</th>
<th>角色</th>
</tr>
<tr>
<td><strong>ISMS Core 專案</strong></td>
<td>方法論、架構、領域專業知識、IP 擁有權</td>
</tr>
<tr>
<td><strong>Claude Code（Sonnet）</strong></td>
<td>主要實作夥伴——詳見下方貢獻說明</td>
</tr>
<tr>
<td><strong>ISMS Copilot X</strong></td>
<td>文件稽核、適足性審查、實作有效性</td>
</tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/IP_Ownership-Gregory_Griffin-FFD700?style=flat-square" alt="IP Ownership"/>
</p>

---

## 🧠 Claude Code — 實作貢獻

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Sonnet_4.6-CC785C?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code Sonnet"/>
  <img src="https://img.shields.io/badge/Dec_2025–Ongoing-Continuous-2E8B57?style=for-the-badge" alt="Ongoing"/>
</p>

Claude Code（Anthropic，Sonnet 模型系列）自 2025 年 12 月 31 日起一直是 ISMS CORE 的主要實作夥伴，合作仍在持續。在 ISMS Core 專案指導的持續結對工作階段中——該專案撰寫了所有方法論、架構決策、提示指令集與多模型協作——Claude Code 交付了完整的自動化層、撰寫並精煉了所有文件，並打造了讓本專案得以維護的工廠基礎設施。

### 打造了什麼

<table>
<tr>
<th>類別</th>
<th>成品</th>
<th>規模</th>
</tr>
<tr>
<td><strong>Python 腳本</strong></td>
<td>工作簿產生器</td>
<td><strong>285</strong> 支腳本 — 188 (FW) + 53 (OP) + 21 (PRIV) + 12 (CLD) + 10 (AI) + 1 (AI 產生器工具)</td>
</tr>
<tr>
<td><strong>IMP 文件</strong></td>
<td>每項評鑑的使用者指南（UG）+ 技術規格（TG）</td>
<td><strong>464</strong> 個檔案 — 376 FW（188 UG + 188 TG）+ 42 PRIV + 24 CLD + 20 AI + 2 AI 基礎</td>
</tr>
<tr>
<td><strong>POL 文件</strong></td>
<td>以 "WITH WHAT" 驗證方法論構成的政策框架</td>
<td><strong>53</strong> 份框架 POL + <strong>53</strong> 份營運 OP-POL</td>
</tr>
<tr>
<td><strong>Excel 工作簿</strong></td>
<td>含資料驗證、公式、條件式格式的評鑑工作簿</td>
<td><strong>188</strong> (FRAMEWORK) + <strong>53</strong> (OPERATIONAL)</td>
</tr>
<tr>
<td><strong>工廠自動化</strong></td>
<td>組裝、晉升、備份、同步、拆分、正規化腳本</td>
<td>10+ 項主要工具</td>
</tr>
<tr>
<td><strong>QA 基礎設施</strong></td>
<td>QA 關卡、狀態儀表板、驗證流水線</td>
<td><strong>53/53</strong> 控制項通過</td>
</tr>
</table>

### 歷程

```
2025 年 12 月 31 日：試點控制項建立 -> A.8.24
2026 年 1 月：      ISMS CORE 框架 -> 53 個控制套件完成 93 項控制措施
2026 年 2 月：      ISMS CORE 營運版 -> 53 個控制套件完成 93 項控制措施
2026 年 3 月：      ISMS CORE 隱私（ISO 27701:2025）-> 完成 21 個控制群組
2026 年 3 月：      ISMS CORE 雲端（ISO 27018:2025）-> 完成 12 個控制群組
2026 年 3 月：      ISMS CORE 平台 -> 於 isms-core.com 上線
2026 年 4 月：      ISMS CORE AI（ISO 42001:2023）-> 完成 12 個控制群組
2026 年 4 月：      FR + DE + IT 翻譯 -> 全部 5 個套件完成
2026 年 4 月：      威脅情報擴充 -> 第 39–49 階段
                    各連接器 OpenSearch 索引、ENISA EUVD、Exploit-DB、
                    MITRE ATT&CK v19、AlienVault OTX（第 12 個 OSINT 來源）、
                    VirusTotal 擴充、TLP 標籤、威脅曝險頁面、
                    18 個 OSD 儀表板、EBIOS RM、通知系統、安全稽核
2026 年 5 月：      使用者手冊更新 -> 第 16 章（威脅情報）全面重寫
```

### 平台

**ISMS CORE 平台**（`isms-core-platform/`）已上線——一個 FastAPI 後端，搭配 PostgreSQL、OpenSearch、Docker Compose 部署、nginx TLS 與框架關聯引擎。它把以檔案為基礎的框架轉化為可運作的合規平台：由資料庫驅動、可透過 WebUI 編輯，具備證據追蹤、缺口管理、29 個合規評鑑模組、涵蓋 59 個軸（4,671 個物件）的對照映射，以及 44 個自動化證據連接器，將即時證據推送至各來源的 OpenSearch 索引。

<p align="center">
  <em>懷抱著這樣的信念打造：安全合規應是工程紀律，而非打勾作秀。</em>
</p>

---

<p align="center">
  <strong>Copyright © 2025-2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
  <em>竹子天線真正管用的地方。</em> 🎋
</p>
