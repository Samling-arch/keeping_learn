好的，没问题！作为一位Zotero小白，这份指南将带你从零开始，彻底搞懂【Jasminum茉莉花】插件的每一个细节。我们将采用对新手最友好的方式，用通俗的比喻和详尽的步骤来讲解。

#Zotero/插件/茉莉花

# Zotero插件精讲：Jasminum (茉莉花) - 零基础完全指南

首先，我们用一个表格来快速了解茉莉花插件最核心的三个功能。

| 功能模块 | 一句话概括 | 核心作用 |
| :--- | :--- | :--- |
| **转换器 (Translator) 管理** | 茉莉花给Zotero配了一副更适合看懂中文文献网站的“眼镜”，让它抓取信息时看得更清、抓得更全。 | 解决从中文网站（如知网）抓取文献信息不完整（如缺少PDF附件、日期格式不规范）的问题。 |
| **PDF附件元数据抓取** | 只要你的PDF文件名是论文标题，把它拖进Zotero，茉莉花就能自动帮你从网上找到它的所有信息并填好。 | 实现从本地PDF文件（特别是中文文献）一键自动生成规范的Zotero条目，极大提高效率。 |
| **中文文献引用信息更新** | 右键点一下，就能给你的中文文献条目加上最新的被引次数、下载量等“战绩”信息。 | 丰富文献条目的附加信息，方便你了解一篇中文文献的影响力。 |

---

## ## 插件简介：茉莉花是做什么的？

> **一句话概括**：茉莉花 (Jasminum) 插件是一个专门为 Zotero 用户打造的“汉化增强包”，主要目标是优化对中文文献的识别、抓取和管理体验。

Zotero 诞生之初，对英文文献的支持非常完美，但对中文文献网站（如知网、万方）的适应性稍有不足。有时我们通过浏览器插件保存文献，会发现抓取到的信息不全。

茉莉花插件就是为了弥补这一“水土不服”的状况而生的。它像一个本地化的助手，让 Zotero 在处理中文文献时变得更智能、更强大。随着 Zotero 自身版本的更新（比如现在的 `$Zotero 7$`），官方对中文的支持越来越好，但茉莉花在很多方面依然是不可或缺的利器。

## ## 核心功能一：转换器 (Translator) 的增强与管理

> **一句话概括**：转换器是 Zotero 用来“阅读”网页的脚本，茉莉花则提供并管理了一套专门为中文网站优化的“阅读脚本”，让信息抓取滴水不漏。

这个部分是茉莉花插件的基石，理解了它，你就理解了茉莉花一半的价值。

### ### 什么是转换器 (Translator)？

当我们在浏览器里打开一篇知网的论文页面，这个页面上包含了标题、作者、摘要、期刊、DOI、PDF附件等各种信息。我们点击浏览器右上角的 Zotero Connector 插件图标，Zotero 是如何“知道”哪个是标题、哪个是作者的呢？

答案就是**转换器 (Translator)**。

*   **它的本质**：转换器其实就是一个个小小的代码文件，后缀名是 `.js` (JavaScript脚本文件)。每个文件都对应着一个或一类网站（比如有专门给知网用的，有专门给 `Elsevier` 用的）。
*   **它的作用**：这个 `.js` 文件里写好了一套规则，告诉 Zotero Connector：“在这个网站上，标题信息通常在 `这个位置`，作者信息在 `那个位置`...”。Zotero Connector 就是靠着这些“说明书”来准确地从五花八门的网页里提取数据的。

*   **它的来源与位置**：这些转换器文件存储在你电脑的本地文件夹里。你可以这样找到它：
    1.  打开 Zotero，点击菜单栏的 `编辑` -> `首选项`。
    2.  在弹出的窗口中，选择 `高级` -> `文件和文件夹`。
    3.  点击 `打开数据文件夹`。
    4.  在弹出的文件夹里，你会看到一个名为 `translators` 的文件夹。里面存放的就是所有的 `.js` 转换器文件。

> [!tip] 新手比喻
> 你可以把 Zotero Connector 想象成一个要去不同人家里（不同文献网站）取东西（文献信息）的机器人。
> *   **Zotero 官方的转换器**：是机器人出厂时自带的“地图”，对国外的房子（网站）很熟悉。
> *   **茉莉花提供的转换器**：是一套为中国特色房屋（中文网站）量身定制的“精细地图”，能让机器人更准确地找到东西，甚至能找到原版地图上没标出的小物件（比如PDF附件）。

### ### 为什么需要茉莉花的转换器？

Zotero 官方自带的转换器库虽然强大，但可能对某些中文网站的更新跟进不及时。这就导致了：

*   **信息抓取不全**：可能只能抓到标题、作者，但抓不到PDF附件。
*   **格式不规范**：作者姓名可能是 `San Zhang` 而不是 `张三`；日期可能只抓取到年份 `2024`，而完整的日期 `2024-07-31` 却丢失了。
*   **附加信息缺失**：一些有用的信息（如基金项目、文献分类号）完全抓不到。

茉莉花插件集成了由 **Zotero 中文社区**维护的一系列高质量中文转换器。安装并更新后，可以完美解决以上问题。

#### **效果对比示例**

| 对比项 | 只用Zotero官方转换器（可能出现的情况） | 使用茉莉花更新后的转换器（推荐） |
| :--- | :--- | :--- |
| **附件** | 常常抓取不到PDF附件，条目下是空的。 | **能够成功抓取PDF附件并自动附在条目下。** |
| **作者格式** | 可能是分开的，或者顺序不对。 | 姓名格式正确，符合中文习惯。 |
| **日期格式** | 可能只抓取到年份，如 `$2024$`。 | 能够抓取到完整的日期，如 `2024-07-31`。 |
| **“其他”字段** | 该字段通常是空的。 | **填充了丰富的附加信息**，如下载次数、基金信息、中图分类号等。 |

### ### 如何用茉莉花更新转换器？（关键步骤）

这是一个两步走的过程：先更新Zotero本地的转换器库，再让浏览器插件同步这些更新。

1.  **第一步：在Zotero中更新**
    *   点击 Zotero 菜单栏的 `编辑` -> `首选项`。
    *   在弹出的窗口中，选择 `茉莉花` 选项卡。
    *   向下滚动，找到 **“非官方维护中文转换器”** 区域。
    *   （初次使用时，这里可能显示感叹号或提示未安装，这很正常）
    *   继续向下滚动到底部，点击 **`全部更新`** 按钮。
    *   等待片刻，茉莉花插件就会把最新的中文转换器下载并安装到你本地的 `translators` 文件夹中。

2.  **第二步：在浏览器中同步**
    *   打开你的浏览器（如 Chrome, Edge, Firefox）。
    *   在浏览器右上角找到 Zotero Connector 插件图标，**右键点击**它，选择 `选项`。
    *   在打开的设置页面中，切换到 `高级` 选项卡。
    *   找到 `转换器` (Translators) 部分，点击 **`更新转换器`** （或类似 `Update Translators` / `重置转换器` 的按钮）。

> [!warning] 重要提示
> 第二步**至关重要**！只在Zotero里更新是不够的，因为真正执行抓取任务的是浏览器插件。你必须手动让浏览器插件去重新加载本地文件夹里最新的转换器，这样更新才能生效。

## ## 核心功能二：PDF附件元数据抓取

> **一句话概括**：只要PDF文件名是论文标题，拖进Zotero，茉莉花就能帮你从网上找到它的所有信息并自动填好。

这是一个极其方便的功能，尤其适合整理本地已经下载好的一堆中文文献。

### ### 功能原理

它的工作逻辑非常简单直接：

1.  你将一个 PDF 文件拖拽到 Zotero 的文献列表区域。
2.  茉莉花插件会立即启动，并**读取这个PDF文件的文件名**。
3.  它拿着这个文件名（假定它就是论文的标题），去访问知网等中文数据库进行搜索。
4.  如果搜索成功并匹配到了唯一的文献，它就会把这篇文献的所有元数据（作者、期刊、年份、摘要等）全部抓取下来。
5.  最后，它在 Zotero 中创建一个全新的文献条目，填上所有抓取到的信息，并将你刚才拖入的那个 PDF 文件作为附件关联到这个新条目下。

### ### 操作演示与注意事项

#### **失败的例子**
假设你有一个从别处下载的PDF，它的名字是 `CNKI_CAJ_Final_20240803.pdf`。
*   **操作**：你把这个文件拖进 Zotero。
*   **结果**：Zotero 只是单纯地把这个 PDF 文件加了进去，它是一个独立的附件，没有作者、标题等任何信息。茉莉花会提示“抓取知网元数据失败”。

#### **成功的例子**
1.  **准备工作**：你先将上面那个文件重命名，改成它真实的论文标题，例如：`《Zotero7插件Jasminum茉莉花功能详解》.pdf`。
2.  **操作**：你再把这个改好名字的 PDF 文件拖进 Zotero。
3.  **结果**：稍等一两秒，你会看到 Zotero 界面闪了一下，然后出现了一个完整的文献条目，包含了标题、作者、期刊信息等，并且 `《Zotero7插件Jasminum茉莉花功能详解》.pdf` 这个文件已经自动成为了它的附件。茉莉花会提示“抓取知网元数据成功”。

> [!danger] 核心要点
> **这个功能成功的关键在于文件名！**
> *   文件名必须**足够准确且干净**，最好就是完整的论文标题。
> *   如果文件名不正确或包含了太多无关字符，抓取就会失败。
> *   反过来说，即使你的PDF内容是一片空白，但只要文件名是一篇真实存在的论文标题，茉莉花依然能成功抓取到元数据并创建条目（尽管附件本身是错的）。

#### **在哪里设置识别规则？**
你可以在茉莉花的设置里看到它的识别依据。
*   `编辑` -> `首选项` -> `茉莉花` -> 找到 **`文件名识别模板`**。
*   默认情况下，它就是通过 `标题` 来识别的。

## ## 核心功能三：更新中文文献引用信息

> **一句话概括**：右键点一下，就能给你的中文文献条目加上最新的被引次数、下载量等“战绩”信息。

### ### 功能与操作

对于已经存在于你库中的中文文献条目，茉莉花可以帮你补充一些动态信息。

*   **操作方法**：
    1.  在 Zotero 中，找到一篇中文文献条目。
    2.  在该条目上**右键点击**。
    3.  在弹出的菜单中选择 `知网工具` -> `更新知网引用次数`。
*   **结果**：
    *   茉莉花会联网到知网查询这篇文献的最新数据。
    *   查询到的信息，如**被引次数、下载次数、期刊影响因子**等，会被自动填写到该条目右侧信息栏的 **`其他`** (Extra) 字段中。

#### **示例**
*   **更新前**：`其他` 字段是空的。
*   **更新后**：`其他` 字段可能会显示如下内容：
    $$
    Cited by: CNKI (88)
    Downloads: CNKI (1024)
    Journal: 北京大学学报(自然科学版)
    Impact Factor: 1.234
    ...
    $$

## ## 其他实用功能

> **一句话概括**：一些方便整理的小工具，比如自动分开或合并作者的中英文姓名。

茉莉花还集成了一些便捷的小功能，通常也在右键菜单里。

*   **拆分/合并姓名**：
    *   有时候抓取到的作者姓名是 `张三`，你希望变成 Zotero 更规范的 `三, 张` 格式，可以右键点击条目 -> `知网工具` -> `拆分姓名`。
    *   反之，也可以进行合并。
*   **统一日期格式**：可以批量将库中的日期格式统一。

这些都是锦上添花的小功能，操作非常直观，你可以自己尝试一下。

---
希望这份超级详细的零基础指南能帮助你完全掌握茉莉花插件！从现在开始，享受丝滑的中文文献管理体验吧！