
# 


### 表格总结：OSM模型核心概览

| 概念 (Concept) | 英文全称 (Full Name) | 中文含义 (Meaning) | 通俗解释 (Simple Explanation) | 在指标体系中的作用 (Role in System) |
| :--- | :--- | :--- | :--- | :--- |
| **O** | **Object** | **目标** | 我们最终想达成的那个最大的、最核心的业务目的。 | 确立方向，是所有指标的最终归宿，通常体现为==北极星指标==。 |
| **S** | **Strategy** | **策略** | 为了实现那个大目标，我们具体要走哪些路、做哪些事。 | 拆解目标，将宏大目标分解为可执行的步骤和路径，通常体现为==用户旅程地图==。 |
| **M** | **Measure** | **度量** | 用数字来衡量我们走的每一步路、做的每一件事效果好不好。 | 量化策略，为每个关键步骤设置具体的、可追踪的==量化指标==，用于评估和优化。 |

---

# OSM模型：搭建指标体系的方法论

## # O - Object (目标)：找到你的北极星

> **一句话概括：** 目标（Object）就是公司或业务在现阶段最想达成的那一件核心大事，是所有努力的最终方向。

我们搭建指标体系的第一步，就是要明确我们的终极目标是什么。这个目标不是越多越好，而是要找到那个“唯一重要的指标”（One Metric That Matters），我们称之为**北极星指标**。

#### 什么是北极星指标？
北极星指标，就像夜空中最亮的北极星，为所有船只指引方向。在公司里，它就是那个最核心、最能主动影响业务增长的指标。公司里上上下下所有人，都应该朝着这个指标去努力，只要它增长了，就代表公司的核心价值增长了。

#### 什么时候需要北极星指标？
- **当你的业务是独立的**：一个完整的产品或公司，需要一个北极星指标来统一所有人的目标。
- **当你的业务是大业务中的一个分支时**：你可能不需要独立的北极星指标，因为你的核心目标是服务于更大的业务。你的成功，由主业务的成功来定义。

#### 举个例子
- **知乎 (内容社区)**：它的核心是知识问答，所以它的北极星指标可以是 `问题总数` 或 `高质量回答数`。
- **电商平台 (如淘宝)**：核心是交易，北极星指标就是 `GMV` (Gross Merchandise Volume，总成交额)。
- **网约车 (如滴滴)**：核心是连接司机和乘客，北极星指标可以是 `日活跃用户数` 或 `日完成订单量`。
- **反例 - 饿了么的配送业务**：配送是饿了么这个大平台的一个功能分支，它的存在是为了支撑主平台的订单交易。它自己不能独立设定一个北极星指标（比如“配送员人均配送时长”），它的好坏最终要看是否促进了整个饿了么平台的 `GMV` 和 `用户满意度`。

---

## # S - Strategy (策略)：描绘用户的行动地图

> **一句话概括：** 策略（Strategy）就是站在用户的角度，把他们从认识我们到了解我们，再到完成核心目标的每一步都画出来，形成一张“寻宝图”。

确定了北极星指标（比如电商的`GMV`）后，我们就要思考：用户是怎么一步步帮我们完成这个指标的？他们经历了什么？这就是策略层要解决的问题。我们常用一个强大的工具——**用户旅程地图 (User Journey Map)**。

#### 什么是用户旅程地图？
它是一种可视化工具，用来描绘一个“典型用户”为了实现某个目标（比如下单购物），与我们的产品（比如APP）进行交互的全过程。我们把这个过程拆解成一个个关键阶段和关键节点，从而理解用户的行为和痛点。

> **注意：** 这里的“用户”是广义的。对于制造业来说，“用户”可以是“一辆汽车”，它的旅程就是从一个螺丝钉开始，经历组装、喷漆、质检，最终成为一辆完整的汽车。

#### 举个例子：长视频APP（如优爱腾）的用户旅程

很多人会觉得，看视频的路径很简单：`打开APP -> 搜索《甄嬛传》 -> 观看`。
这太粗糙了！这叫“流水账”，你根本看不出用户在哪一步流失了。

**正确的、详细的用户旅程地图应该是这样的：**

| 阶段 (Stage) | 用户行为描述 (User Actions) | APP界面/功能 (App Interaction) |
| :--- | :--- | :--- |
| **来 (Arrive)** | 用户通过朋友分享、应用商店推荐、广告等方式，了解到并下载了APP。 | 下载页面、APP首次打开引导页 |
| **逛 (Browse)** | 打开APP后，在首页漫无目的地滑动，看看有什么热门推荐、新剧上线。 | 首页信息流、Banner推荐、下拉刷新 |
| **搜 (Search)** | 有了明确想看的内容后，主动使用搜索功能查找。 | 搜索框、搜索结果页、搜索联想词 |
| **看 (Watch)** | 找到视频并点击播放，进入观看环节。这是核心环节。 | 视频播放页、播放器功能（暂停、快进等） |
| **连续看 (Binge)** | 看完一集后，被自动推荐或主动点击下一集，或者看了相关推荐的其他视频。 | 播放结束页推荐、自动连播功能 |
| **买 (Purchase)** | 无法忍受广告，或者想看会员专属内容，最终决定付费成为会员。 | 会员购买页、支付流程 |

#### 梳理用户旅程的三大原则
1.  **必须有产出节点**：不能记流水账，每个阶段都要能提炼出可以衡量的关键行为节点（如：“来”阶段的`下载`，“逛”阶段的`点击Banner`）。
2.  **必须围绕核心指标**：整个旅程地图的设计，最终都要服务于北极星指标。比如视频APP的核心是 `观看时长` 和 `活跃人数`，那么“逛”、“搜”、“看”这些环节都要能体现这两点。
3.  **必须是单一视角**：分析用户旅程，就只站在用户的角度；如果分析商家，就只站在商家的角度。不能混在一起，否则逻辑会混乱。

---

## # M - Measure (度量)：给每一步都配上记分牌

> **一句话概KOMM** 度量（Measure）就是为用户旅程的每一个关键节点，都设置一个具体的数字指标，用来量化用户的行为，告诉我们每个环节做得怎么样。

有了用户旅程地图，我们就要给每个节点配上具体的指标，把用户的行为变成可以测量和分析的数据。

#### 案例深化：长视频APP的指标体系

我们以前面的用户旅程为基础，（暂时忽略“买”这个最终转化环节），为每个节点配置指标：

- **来 (Arrive)**
    - **核心指标：**
        - `DAU (日活跃用户数)`：今天有多少人打开了APP。
        - `渠道新增用户数`: 从各个广告/推荐渠道分别来了多少新用户。
- **逛 (Browse)**
    - **流量指标：**
        - `首页PV (Page View)`：首页被浏览了多少次。
        - `首页UV (Unique Visitor)`：多少个独立用户浏览了首页。
    - **行为指标：**
        - `人均浏览时长`: 平均每个用户在首页停留了多久。
        - `首页内容点击PV/UV`：首页上的推荐位被点击了多少次/多少人。
        - `人均点击节目数`：平均每个用户在首页点击了几个不同的推荐内容。
- **搜 (Search)**
    - **流量指标：**
        - `搜索PV/UV`：搜索功能被使用了多少次/多少人。
    - **转化指标：**
        - `搜索-播放转化率`：搜索了内容的用户中，有多大比例成功点击并播放了视频。
        - $$ 搜索-播放转化率 = \frac{成功播放视频的用户数}{使用搜索功能的用户数} \times 100\% $$
- **看 (Watch)**
    - **核心指标：**
        - `总播放时长`：所有用户观看视频的总时长，这是核心中的核心。
        - `人均播放时长`：平均每个活跃用户看了多长时间视频。
        - `总播放VV (Video View)`：视频被播放了多少次。
- **连续看 (Binge)**
    - **行为指标：**
        - `连播次数`: 触发了多少次连续播放。
    - **转化指标：**
        - `连播转化率`：看完一集的用户中，有多大比例接着看了下一集。
        - $$ 连播转化率 = \frac{观看下一集的用户数}{观看上一集的用户数} \times 100\% $$

### 指标的层级：从宏观到微观

我们得到的这些指标不是一盘散沙，而是有层级的。通常可以分为三级：

1.  **一级指标（核心指标）**：最宏观、最概括的指标，直接反映业务的最终成果。
2.  **二级指标（过程指标）**：对一级指标进行拆解，反映了核心过程的效率和质量。通常会加入一些维度（如渠道、周期）。
3.  **三级指标（细节指标）**：对二级指标再细分，加入了更多维度（如时间、地区、用户群），用于定位具体问题。

#### 示例：指标层级体系
![](https://raw.githubusercontent.com/SAMLAY-c/obsidian-photos/university/img/20250708084324906.png)
**1. 用户增长维度**
- **一级指标**：`新注册用户数`
- **二级指标**：`各渠道来源用户占比`、`注册流程转化率`
- **三级指标**：`某日某渠道新用户注册转化率`、`新用户填写资料的平均耗时`

**2. 用户活跃维度**
> **注意：** “活跃”的定义很重要！不能简单地把“打开APP”算作活跃。对于音乐APP，可能是听歌超过 $5$ 秒；对于短视频，可能是观看超过 $1$ 分钟。

- **一级指标**：`DAU/MAU (日/月活跃用户数)`
- **二级指标**：`次日留存率`、`7日留存率`、`核心功能使用频次`（如点赞、评论、发弹幕）
- **三级指标**：`新用户次日留-存率`、`不同用户群体的流失率`、`新手任务完成率`

**3. 用户变现维度**
- **一级指标**：`总营收 (Revenue)`、`付费用户数 (Paying Users)`
- **二级指标**：`ARPU (每用户平均收入)`、`客单价`、`付费转化率`
- **三级指标**：`首次付费用户的客单价`、`不同会员等级的续费率`、`某次促销活动的ROI (投入产出比)`
    - $$ ROI = \frac{活动带来的收入 - 活动投入成本}{活动投入成本} \times 100\% $$

---
![image.png](https://raw.githubusercontent.com/SAMLAY-c/obsidian-photos/university/img/20250708084611400.png)

# 实践与落地：从指标到行动

> **一句话概括：** 建立了指标体系后，就要针对不同的指标，采取不同的运营策略，并用指标的变化来验证策略是否有效。

指标不是用来看的，是用来指导行动的。

#### 案例：长视频APP的策略与行动
- **目标指标：** 提升`DAU (日活)`
    - **错误策略：** 增加 $10$ 个新节目。 (这更能影响`观看时长`，对拉新效果不明显)
    - **正确策略：**
        - 在抖音、微博等平台进行广告==投放==。
        - 给沉睡用户发送==短信/App Push==召回。
        - 与手机厂商合作进行==应用预装==。
- **目标指标：** 提升`人均浏览时长` (让用户在首页逛更久)
    - **错误策略：** 去做广告投放。(这是拉新手段，与站内行为无关)
    - **正确策略：**
        - 设计更吸引人的==Banner==。
        - 推出==专题活动==并放在首页醒目位置。
        - 优化==推荐算法==，让用户总能看到感兴趣的内容。

#### 个人观察：过度优化带来的负面体验
> 这里举一个你提到的腾讯视频的例子，来说明产品决策如何影响度量指标和用户体验。

- **现象1：** 长按屏幕，左半边是 $3$ 倍速后退，右半边是 $3$ 倍速前进。
    - **产品设想：** 提供更精细的控制。
    - **用户实际体验：** 大部分人是单手（尤其是左手）持机，主要需求是快进。左手操作时，大拇指很自然地落在屏幕左侧，一按就变成了倒放，非常反直觉。这增加了误操作，可能导致用户对播放器产生负面情绪，反映在数据上可能是“播放中断率”或“快进/快退功能来回切换次数”异常增高。
- **现象2：** 点击屏幕下方容易点出字幕修改栏。
    - **产品设含：** 利用用户众包来校准AI生成的字幕。
    - **用户实际体验：** 用户只是想看进度条或者暂停，却频繁触发一个不需要的功能，每次都要手动关掉，体验非常糟糕。如果埋了点，数据分析师应该能看到这个“字幕修改栏”的“打开-立即关闭”行为对非常多，停留时间极短，这本身就是一个强烈的负面信号。

这两个例子说明，脱离用户真实场景的功能设计，即使初衷是“优化”，也可能带来负面的用户体验，最终损害核心的`观看时长`和`用户留存`指标。

---

# 写给新手的快速上手指南

> **一句话概括：** 作为一个新人，最快熟悉业务的方法是“**看架构、多沟通、自己试**”。

从零搭建指标体系对新人来说很难，因为你不了解业务。但你可以通过以下技巧，快速融入并理解现有的体系。

#### 1. 快速熟悉业务
- **看公司架构图**：打开钉钉/飞书，第一件事就是看组织架构。重点看**运营团队**是怎么划分的，是按区域、按业务线、还是按用户生命周期？这能帮你理解业务的脉络。【不要泄露给其他人】
- **找运营要报表**：找到对应业务板块的运营同事，礼貌地询问他们平时都看哪些报表，关注哪些指标。这是最直接的资料。
- **多问一个“为什么”**：当运营同事找你要数据时，不要只做个“提数机器”。多问一句：“这个数据您打算用来分析什么问题呀？” “您希望看到什么样的结果？” 通过沟通，你能迅速了解业务方的痛点和目标。

#### 2. 快速熟悉数据表
公司数据库里有成百上千张表，字段名又多又杂，怎么快速弄懂？
- **“人肉”跑通流程**：
    1.  在自己公司的APP上下一个单，或完成一次核心操作。
    2.  记住你的`用户ID`、`订单ID`等关键信息。
    3.  去数据库里，用你的ID在不同的表里 `SELECT * FROM table WHERE user_id = '你的ID'`。
    4.  通过看你自己的这条数据，你就能直观地理解每一张表、每一个字段记录的是什么信息，比看枯燥的文档快一百倍。
- **看别人的代码**：看团队共享的代码库，或者同事们写的查询脚本，看他们最常用哪些表、哪些字段，你就能知道哪些是核心数据。

#### 3. 互联网通用核心流程指标

无论什么业务，以下几个流程的指标都是通用的，需要做到张口就来。

- **用户获取流程**

    - **曝光/传播** -> **下载** -> **注册** -> **注册成功**
    - 在这个漏斗中，每一步都有==转化率==。比如 `下载-注册转化率`， `不同渠道的下载量` 等。

- **用户活跃与流失**
    - **活跃**：用户持续使用产品。（指标：`DAU`、`留存率`）
    - **流失**：用户一段时间不再使用产品。（指标：`流失率`）
    - **回流**：流失的用户又回来了。（指标：`回流率`）

最后，海量的指标谁也记不住。把这份文档和公司提供的指标库当作一本“新华字典”，在需要的时候查阅、理解、应用，并在实践中不断加深对业务的理解，你就能逐渐从一个“看指标”的人，成长为一个“搭建和运用指标”的专家。