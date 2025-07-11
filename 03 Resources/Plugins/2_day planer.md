
### 0.1.1 插件 `Day Planner` 解决的问题汇总

| 问题分类      | 具体问题描述                                    |
| :-------- | :---------------------------------------- |
| **日程可视化** | 看不到任务的具体时间安排，只能靠脑补。                       |
| **执行力**   | 不清楚自己什么时候该做什么，容易瞎忙活。                      |
| **信息孤岛**  | 多个任务来源（日历、Daily Note、Tasks插件）数据分散，不好统一查看。 |
| **时间追踪**  | 想记录时间投入，但手动创建表格太麻烦，不知从何开始。                |
| **工具限制**  | Obsidian 原生的时间轴功能太原始，Canvas 又太重，不够轻量。     |

---

# 1 写得出日程，还能看得见时间线？Obsidian Day Planner 太懂我了

> [!info] 笔记来源
> **鬼哥的教程**：[写得出日程，还能看得见时间线？Obsidian Day Planner 太懂我了](https://www.example.com) (此处为示意链接，请替换为实际原文链接)

咱们搞技术搞久了，就知道一个事儿：时间，不是钱，是命！每天想着高效、想着计划，结果一打开 Obsidian，一看 Daily Notes 一堆待办，脑壳子嗡嗡的，最后计划赶不上变化，变成“瞎忙活一天”。如果你也有类似困扰，那今天鬼哥要安利的这个插件——**Day Planner**，简直就是时间管理星人梦中的神器。

鬼哥用下来最大的感受就是：**它让我的笔记活了！**不是单纯写写写，而是看得见、排得上、调得动、追得了。

---

### 1.1.1 🧠 插件简介：Day Planner 是个啥？

Day Planner 是 Obsidian 的社区插件，主打两大功能：

1.  基于 Daily Notes 的日程展示和可视化时间轴 (Timeline)
2.  基础的时间追踪 (Time Tracking) 功能

它可以整合：
- Obsidian 自带的 Daily Notes (或 Periodic Notes)
- Tasks 插件 (支持 `scheduled::` 属性)
- 在线日历 (Google, iCloud, Outlook)
- Dataview 插件 (展示、解析属性)
- 任务打卡 (开始/结束计时)
- 多日视图、状态栏迷你时间轴...

> [!quote] 核心价值
> Day Planner 的核心价值就是两个字：**清晰**。
> - 把你写的时间线任务自动提取，拉成时间轴。
> - 多个来源统一展示，任务不再分散。
> - 提供计时器，实时记录时间投入。
> - 所有信息还是保存在 Markdown，完全本地、私有、安全。


### 1.1.2 🛠️ 插件下载 & 安装方法

Day Planner 是社区插件，需要手动安装。

> [!todo] 安装步骤
> 1.  **开启社区插件**
>     - 打开 Obsidian 设置 (左下角齿轮图标) → `Community plugins`
>     - 关闭 `Safe mode (安全模式)`
>     - 点击 `Browse`，打开插件市场
> 2.  **搜索并安装 Day Planner**
>     - 在搜索框输入 `Day Planner`
>     - 找到插件，点击 `Install`
>     - 安装完成后，点击 `Enable` 启用插件
> 3.  **推荐配合插件**
>     - **Dataview**：用于读取和展示属性数据 (如 `scheduled::`)
>     - **Tasks**：社区任务插件，可用于更强大的任务管理
>     - **Daily Notes** (核心插件)：开启后才能识别每日任务
> 4.  **离线安装** (国内用户专属通道)
>     - 如果你无法在线安装插件，别担心，我已经把热门插件下载好了
>     - 点击下方公众号，回复关键字：`Obsidian`，获取Obsidian资料合集。

---

### 1.1.3 🧭 使用方法详解（功能一个个讲）

#### 1.1.3.1 1️⃣ 从 Daily Notes 里展示任务

这是 Day Planner 的基础功能。在你的 Daily Note 中这样写：
```markdown
# 2025-06-21

## Day planner

- [ ] 08:30 - 09:00 起床
- [ ] 09:00 - 10:30 写代码
- [ ] 11:00 - 12:00 开会
```
然后打开插件提供的时间轴视图：
- **方式一**：左侧栏点击 “🗓️ 时间轴”图标
- **方式二**：命令面板 (`Ctrl/Cmd + P`) 执行 `Show Timeline`

你就能在侧边栏看到漂亮的时间分布块，颜色分明，任务一目了然。

> [!warning] 注意
> 必须用标准时间格式：`hh:mm - hh:mm`，才能正确解析。

#### 1.1.3.2 2️⃣ 整合 Tasks 插件任务 (Vault 全局任务)

如果你用 Tasks 插件来处理任务 (推荐！)，Day Planner 同样支持：
```markdown
- [ ] 10:00 - 11:30 #任务名 ⏳ 2025-06-21
- [ ] 13:00 - 14:00 #会议 [scheduled:: 2025-06-21]
```
Day Planner 会自动识别出含有时间和日期的任务，在时间轴中按天分类显示。这一点简直太舒服，特别适合多项目并行的工作模式！

#### 1.1.3.3 3️⃣ 同步 Google / iCloud / Outlook 日历

这玩意也太狠了，居然连线上日历都能接进来！只需要提供 `.ics` 格式的订阅链接。

> [!faq] 如何获取 .ics 链接？
> - **Google Calendar**：日历设置 → 整合日历 → 公开地址 → 选择 `.ics` 链接
> - **iCloud**：日历 → 共享日历 → 获取公共地址
> - **Outlook**：网页端 → 设置 → 共享日历 → 选择公开格式

只要填入插件设置里的对应字段，你就能把网盘上的活动也显示在时间轴中！

#### 1.1.3.4 4️⃣ 多日视图 / 迷你时间轴

有时候一天搞不定，要看几天的安排？可以打开多日视图！
- **命令面板**：`Show multi-day planner`
- **图标栏**：点击相应图标

而且状态栏还会有迷你时间轴，显示接下来的 `$3$` 小时安排。这就叫“随时掌握节奏”。

#### 1.1.3.5 5️⃣ 计时追踪功能 (Time Tracking)

这个功能是个小隐藏彩蛋，鬼哥很爱：

> [!tip] 如何使用计时器
> 1.  **开始计时**：在编辑器里右键任务 → 选择 `Start Clock`，任务条会变颜色。
> 2.  **结束或取消**：再右键任务 → 选择 `Stop Clock` or `Cancel Clock`。
> 3.  **自动记录**：任务会多出一个属性，例如 `time-tracked:: 1h20m`。
> 4.  **复盘对照**：在设置中可以开启“时钟轨道”，会并排显示计划任务时间和实际花费时间，特别适合对照复盘。

---

### 1.1.4 🧨 使用技巧 & 注意事项

-   **格式标准很重要**：时间段必须是 `hh:mm - hh:mm`，否则时间轴解析失败。
-   **任务来源多样但统一展示**：Daily Notes / Tasks 插件 / 日历等都能合并。
-   **注意插件依赖**：`Dataview` 和 `Tasks` 插件装好会更丝滑。
-   **推荐多视图切换**：写任务在 Daily Notes，计划看 Timeline，效率更高。
-   **旧版本慎用**：`$0.7.0$` 之后的版本有大改动，如果你想回滚，得去找社区分支，用 `BRAT` 插件安装。

---

### 1.1.5 🧃 鬼哥的使用体验

> [!quote]
> 说实话，Day Planner 是我用 Obsidian 时间管理流里最爱的一环，真正把“时间”落到纸面（准确来说，是落到 Markdown 里）。以前我搞时间安排，要在 Google Calendar 和 Obsidian 之间来回跳，现在直接一屏搞定，爽得一批。
> 
> 打工人最怕什么？怕忙了一整天，结果连自己都说不清“我今天到底干了啥”。有了这个插件，一切都记录在案，回顾的时候一清二楚。
> 
> 还有一点，鬼哥很喜欢这个插件“中立不喧宾夺主”的设计——它不会打乱你的笔记逻辑，而是悄悄帮你“做笔记的助理”。它只需要你养成一点点时间标注的习惯，就能回馈一整套时间管理能力。

所以，无论你是时间焦虑党、习惯拖延症、还是想提高生产力的自律星人，这个插件都值得你装上用用。

---

### 1.1.6 ✅ 总结与推荐

如果你已经在用 Obsidian 作为主力笔记工具，那 Day Planner 能大幅提升你的笔记含金量；如果你还没深入时间管理系统，那这插件也能给你一个最好的入门仪式。

别想太多，装上它，你的时间线也许就此改变⬇️

-   **插件地址** (社区搜索即可)：`Day Planner`
-   **推荐搭配使用**：`Tasks` 插件、`Dataview` 插件、`Daily Notes` 插件