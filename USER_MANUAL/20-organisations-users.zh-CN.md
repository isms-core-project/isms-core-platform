# 组织与用户

<p align="center"><a href="20-organisations-users.md">English</a> · <a href="20-organisations-users.zh-TW.md">繁體中文</a> · <strong>简体中文</strong></p>

<!-- ISMS-CORE:USER-MANUAL:20-organisations-users:v1.0:2026-04-16 -->

---

## 概览

ISMS CORE Platform 支持多租户运作——多个组织可在单一平台执行个体上运行，并具备完整的数据隔离。在每个组织内，角色型访问控制决定每位用户能看到与执行哪些内容。

用户与组织管理属于 **Admin** 功能。本章涵盖与所有角色相关的设置。

---

## 组织

平台中的每个组织代表一个独立的租户——一家公司、子公司或各自独立的组织范围。组织之间不会共用数据。

### 组织设置

管理员可在 **Admin → Organisation** 中针对每个组织设置下列项目：

| 设置 | 描述 |
|---------|-------------|
| **Organisation name** | 法定名称或运营名称 |
| **Country** | 政策本地化所用的司法管辖区（CH、AT、BE、DE、FR、GB、IT、LU） |
| **Industry sector** | 用于框架相关性建议 |
| **Active projects** | 每个产品系列的预设使用中项目是哪一个 |

**国家设置与政策本地化：** 设置国家后，政策文件会以符合该司法管辖区的法规参照呈现。例如，将国家设为 `DE` 时，会让 GDPR 的参照与相关的 BDSG 参照一并出现，并以 Datenschutzbehörde (DSB) 取代通用的「supervisory authority」代称。支持的司法管辖区完整清单请见[简介](01-introduction.zh-CN.md)。

---

## 用户

### 角色

| 角色 | 可执行的操作 |
|------|-----------------|
| **Super Admin** | 跨组织访问——建立与管理组织、检视 Metrics Portfolio。于平台层级指派。 |
| **Admin** | 在其组织内的完整访问权——用户管理、系统设置、内容导入、管理面板 |
| **ISMS Manager** | 所有合规工作：控制措施、评估、缺口、证据、项目、风险、TPRM、EBIOS RM、BIA |
| **Auditor** | 对其组织内所有内容的唯读访问权。可执行 QA 检核与导出。 |
| **Control Owner** | 对指派给自己的控制群组具备读写权。可更新检查表项目，并为其控制措施上传证据。 |
| **Viewer** | 对非机密内容的唯读访问权 |

### 管理用户（仅限 Admin）

前往 **Admin → Users** 即可：

- **Add a user** —— 输入电子邮件、姓名与角色；若已设置电子邮件，系统会寄出邀请信
- **Edit a user** —— 变更角色、姓名或所属组织（仅限 Super Admin）
- **Disable a user** —— 撤销访问权，但不删除账户
- **Reset password** —— 寄出密码重设电子邮件

### 角色指派

每位用户只会有一个角色。若要让某位用户以 Control Owner 的身分访问特定控制群组，请先指派 Control Owner 角色给该用户，再从控制措施库中将特定控制群组指派给他（每个控制群组的详细检视中都有 **Assign Owner** 选项）。

---

## 多重要素验证（MFA）

MFA 采用 TOTP（以时间为基础的一次性密码）——相容于 Google Authenticator、Authy、Microsoft Authenticator，以及任何符合 RFC 6238 的 TOTP 应用程序。

### 设置 MFA

1. 前往 **System → MFA Setup**
2. 使用您的验证器应用程序扫描 QR 码
3. 输入应用程序显示的 6 位数验证码以完成确认
4. **储存 8 组备用码** —— 这些是您的装置无法使用时，供恢复用的一次性验证码

### 使用 MFA 登录

输入电子邮件与密码后，系统会提示您输入 6 位数的 TOTP 验证码。输入满 6 位数后验证码会自动送出——您不需要点选任何按钮。

若您已无法访问验证器应用程序，也没有备用码：
- 请联系您组织的 Admin 重设您的 MFA
- Admin 可从 **Admin → Users → Edit user** 重设 MFA

### MFA 政策

MFA 的强制执行由管理员设置。强制执行时：
- 尚未设置 MFA 的用户，会在下次登录时被提示完成设置
- 用户无法略过 MFA 步骤

---

## System Event Log

前往 **Admin → System → Event Log**，即可取得平台所有动作的不可变审计跟踪。每一个建立、更新、删除、导入与登录事件都会记录下列信息：

- 时间戳记
- 用户身分
- 动作类型
- 受影响的资源（文件编号、用户 ID 等）
- IP 位址

事件日志无法被修改或删除。它是记录谁在何时做了什么的权威记录——对于 ISO 27001:2022 附录 A.8.15（日志记录）与附录 A.5.26（信息安全事件响应）的审计要求至关重要。

请从日志检视将事件日志导出为 CSV。

---

## 管理面板——内容管理

管理面板（**Admin → First-Run Setup**）是导入与重新同步平台内容的地方。这通常是部署时的一次性作业，并在内容更新时重复执行。

若您不是管理员用户，就不需要使用这个面板——它记载于 [PLATFORM.zh-CN.md](../PLATFORM.zh-CN.md) 中，供管理员参考。

<!-- QA_VERIFIED: 2026-04-16 -->
