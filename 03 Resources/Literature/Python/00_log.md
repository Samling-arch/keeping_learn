# Python日志模块(Logging)超详细学习笔记

```python
# ===== Python logging模块完整示例 =====
import logging

# 1. 基本配置 - 必须在第一次使用logging前调用
logging.basicConfig(
    level=logging.DEBUG,                     # 设置最低显示级别(DEBUG/INFO/WARNING/ERROR/CRITICAL)
    format='[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d]: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S',            # 时间格式
    filename='app.log',                      # 输出到文件(可选)
    filemode='a',                            # 'w'覆盖写入,'a'追加(默认)
    encoding='utf-8'                         # 文件编码
)

# 2. 五个日志级别(从低到高)
logging.debug("调试信息：记录详细的程序运行细节，仅供开发者使用")    # 最详细，默认不显示
logging.info("普通信息：记录程序正常运行状态，确认一切正常")        # 一般信息，默认不显示
logging.warning("警告信息：表示可能有问题，但程序仍能正常工作")     # 默认起始级别
logging.error("错误信息：程序的某个功能无法正常工作")              # 严重问题
logging.critical("严重错误：整个程序可能无法继续运行")             # 最严重

# 3. 在函数中使用
def process_data(data):
    logging.debug(f"开始处理数据: {data}")
    # 处理逻辑...
    logging.info("数据处理完成")
    return result

# 4. 多模块项目中的使用
# main.py中配置一次，其他导入的模块会自动使用相同配置
```

> [!NOTE] 核心纲要
> 这份笔记会带你理解为什么专业的程序不只用 print 来输出信息，而是使用一个更强大、更规范的工具——logging 模块。我们将一步步揭开它的神秘面纱。

## 一、 为什么要用 logging，print 不香吗？

> [!TIP] 一句话概括
> print 就像是随手打的草稿，只能看个大概；logging 则是一本带分类、有时间、标明出处的正式实验记录本，信息更全面，管理更方便。

我们刚开始学编程时，最喜欢用 print() 函数来看变量的值或者程序的执行状态。这对于小程序来说完全没问题。但是，想象一下你写了一个非常复杂的程序，比如一个网站服务器，它需要7天24小时不间断运行。这时 print 的问题就暴露了：
- 信息泛滥：你可能加了上百个 print，程序一跑起来，屏幕上瞬间刷过海量信息，你根本找不到关键的那一条。
- 没有级别：有些 print 是为了调试时看一下变量（调试信息），有些是提示用户操作成功（普通信息），有些是报告一个不太严重的问题（警告信息）。print 输出的内容长得都一样，你无法快速区分它们的"重要程度"。
- 信息不全：一个 print 只能输出你让它输出的内容。但问题发生时，你往往更想知道："这段信息是什么时候发生的？是在哪个文件的哪一行代码产生的？" print 无法自动提供这些"上下文信息"。
- 难以关闭：项目开发完成后，你需要把所有用于调试的 print 语句一个个删掉或注释掉，非常麻烦。而 logging 只需要改一个设置，就能统一关闭所有调试信息。
- 无法持久化：print 的内容显示在控制台里，程序一关就没了。如果你想把几个月前的某次运行记录找出来分析问题，print 无能为力。logging 可以轻松将日志写入文件，永久保存。
logging 模块就是Python官方提供的，用来解决以上所有问题的"终极武器"。

## 二、 logging 的初次登场与"五个等级"

> [!TIP] 一句话概括
> logging 模块内置了从"不重要"到"致命"的五个信息等级，让我们可以对程序说的话进行分类。
要使用 logging，首先要像视频里说的那样，在你的代码开头导入它。
```python
import logging
```
> [!INFO] 来源与细节
> logging 是Python的 内置标准库 (Built-in Standard Library)。这意味着只要你安装了Python，这个模块就已经存在了，你不需要像安装 requests、pandas 那样用 pip install 命令去额外安装它。直接 import 就能用。
logging 最大的特点就是它给信息划分了等级。一共有5个，从低到高分别是：
### DEBUG (调试)
通俗比喻：侦探在案发现场记下的所有琐碎线索。比如"门把手上有指纹"、"地毯下有一根头发丝"。
用途：用于记录程序中最详细、最底层的运行细节，通常只有在程序员诊断特定问题时才会关心这些信息。
例子：记录某个变量在循环中每一轮的值。
### INFO (信息)
通俗比喻：飞船的"航行日志"。比如"引擎启动正常"、"已进入预定轨道"。
用途：用于确认程序正在按预期流程正常运行。它告诉你一切顺利。
例子：记录"用户登录成功"、"数据库连接建立"。
### WARNING (警告)
通俗比喻：汽车仪表盘上亮起的"油量低"警示灯。车还能开，但提醒你该去加油了，否则未来可能会出问题。
用途：表示发生了一些意料之外的小问题，或者暗示未来可能存在风险，但程序本身还能继续正常工作。
例子：记录"磁盘空间即将用完"、"某个API接口即将被弃用"。
### ERROR (错误)
通俗比喻：汽车的某个轮胎爆了。车子的大部分功能还在，但某个重要功能（比如平稳行驶）已经无法执行了。
用途：报告一个比较严重的错误，导致程序的某个功能无法完成。
例子：记录"打开一个不存在的文件失败"、"网络连接中断，无法下载数据"。
### CRITICAL (严重)
通俗比喻：汽车引擎着火了。整个系统即将崩溃，必须马上停车熄火。
用途：表示一个极其严重的错误，它将导致整个程序无法继续运行。
例子：记录"内存耗尽，程序即将崩溃"、"数据库核心组件损坏"。
让我们看看代码怎么写，以及一个奇怪的现象：
```python
import logging
logging.debug("这是一条调试信息，非常琐碎。")
logging.info("程序状态正常，一切安好。")
logging.warning("警告！内存快满了！")
logging.error("完蛋，有个文件找不到了。")
logging.critical("数据库崩了，程序即将退出！")
```
当你运行这段代码，你会惊奇地发现，控制台里只显示了后面3条信息：
```
WARNING:root:警告！内存快满了！
ERROR:root:完蛋，有个文件找不到了。
CRITICAL:root:数据库崩了，程序即将退出！
```
> [!QUESTION] 为什么 DEBUG 和 INFO 没有显示？
> 这是 logging 模块一个非常贴心的 默认设置。它默认的日志级别是 WARNING。这意味着，只有 大于等于 WARNING 级别 的信息才会被显示出来。
来源与设计哲学：设计者认为，对于一个正常运行的程序，用户通常不关心那些"一切正常"或者"底层细节"的信息。只有当程序发出"警告"或更严重的问题时，才需要被关注。这样可以避免在程序正常运行时被海量的低级别日志刷屏。

## 三、 配置你的日志系统 basicConfig

> [!TIP] 一句话概括
> basicConfig 是 logging 模块的"总控制台"，我们通过它来告诉日志系统："嘿，从现在开始，请按照我的规矩来办事！"
为了能看到所有级别的日志，或者把日志存到文件里，我们需要对 logging 进行 基本配置 (Basic Configuration)。这个配置动作要用 logging.basicConfig() 函数来完成。
> [!WARNING] 重要提示
> basicConfig 必须在 第一次 使用 logging 输出日志 之前 调用。它是一次性的初始化设置，一旦日志系统已经开始工作（比如你已经调用了 logging.warning()），再调用 basicConfig 就不会有任何效果了。所以，它通常都写在 import 语句的下面。
### 3.1 level 参数：设置最低显示门槛
想看到 DEBUG 和 INFO 也很简单，在配置里指定 level 就行。
```python
import logging
# 进行基本配置，设置最低显示级别为 DEBUG
logging.basicConfig(level=logging.DEBUG) 
logging.debug("你看，我这次能显示出来了。")
logging.info("我也可以了！")
logging.warning("我一直都在。")
```
运行结果：
```
DEBUG:root:你看，我这次能显示出来了。
INFO:root:我也可以了！
WARNING:root:我一直都在。
```
> [!INFO] 细节与来源
> level=logging.DEBUG 的意思是，将日志系统的"显示门槛"降到最低的 DEBUG 级别。这样一来，任何 大于或等于 DEBUG 级别的日志都会被显示出来，也就是全部5个级别。你也可以设置为 level=logging.INFO，这样就只会显示 INFO 及以上的级别。
### 3.2 filename 和 filemode 参数：把日志存入文件
控制台的信息转瞬即逝，把它们保存到文件里才更可靠。
```python
import logging
logging.basicConfig(
    level=logging.DEBUG,                     # 依然显示所有级别的日志
    filename='my_app.log',                   # 指定日志要写入的文件名
    filemode='w',                            # 指定文件写入模式
    encoding='utf-8'                         # 指定文件编码，确保中文不乱码
)
logging.info("这条信息不会显示在控制台了。")
logging.warning("它会被直接写入到 my_app.log 文件中。")
```
运行后，控制台什么都不会显示。但你会在代码同级目录下发现一个新文件 my_app.log，内容如下：
```
INFO:root:这条信息不会显示在控制台了。
WARNING:root:它会被直接写入到 my_app.log 文件中。
```
> [!INFO] filemode 的细节
> filemode 参数控制了文件写入的方式，它和Python内置的 open() 函数的模式是一样的。
> - filemode='w' (write, 写入模式): 这是视频中使用的模式。每次程序重新运行时，会 清空 my_app.log 文件里的所有旧内容，然后写入新的日志。适合每次都想看全新日志的场景。
> - filemode='a' (append, 追加模式): 这是 默认 的模式。每次程序重新运行时，不会清空旧日志，而是在文件末尾 继续添加 新的日志。适合需要长期跟踪、保留所有历史记录的场景。

## 四、高级玩法：定制你的日志格式

> [!TIP] 一句话概括
> 我们可以像拼乐高一样，用 format 和 datefmt 参数自由组合日志的各个信息部件（如时间、文件名、行号），打造出独一无二的、信息量爆棚的日志格式。
默认的 级别:root:消息 格式太简陋了。我们想让日志包含更多有用的"上下文信息"。这就要用到 basicConfig 里的 format 和 datefmt 参数了。
### 4.1 format 参数：定义日志结构
format 参数接受一个字符串，这个字符串就是你日志的"模板"。模板里可以包含一些特殊的"占位符"，它们会在生成日志时被替换成真实的数据。
> [!INFO] format 占位符的来源
> 这些占位符并不是随便写的，它们都来自于Python官方文档中定义的 LogRecord 属性。LogRecord 是 logging 模块在内部创建的一个对象，专门用来存放一条日志的所有信息。你可以把这些 %(...)s 的占位符看作是提取 LogRecord 对象属性的"钥匙"。点击这里查看所有可用的LogRecord属性 (Python官方文档)
让我们来解析视频中那个复杂的例子：
```
'%(levelname)s - %(asctime)s - %(message)s - [line:%(lineno)d] - [%(filename)s]'
```
- %(levelname)s: 日志的级别名称 (e.g., INFO, WARNING)。
- %(asctime)s: 日志创建的时间，格式是 YYYY-MM-DD HH:MM:SS,ms。
- %(message)s: 我们自己写的日志消息主体 (e.g., "数据库连接成功")。
- %(lineno)d: 这条日志是在源文件的第几行被调用的。d 表示这是一个数字。
- %(filename)s: 这条日志所在的文件名 (e.g., main.py)。
### 4.2 datefmt 参数：定制时间格式
默认的 %(asctime)s 时间格式可能不是你想要的。datefmt 参数就是用来给 asctime "化妆"的。
> [!INFO] datefmt 格式代码的来源
> 它的格式代码遵循Python标准库中 time.strftime() 函数的规则。这是一套标准的时间格式化语言。
我们来解析视频中的例子：
```
'%Y-%m-%d %H:%M:%S %p'
```
- %Y: 4位数的年份 (e.g., 2025)
- %m: 2位数的月份 (e.g., 05)
- %d: 2位数的日期 (e.g., 30)
- %H: 24小时制的小时 (e.g., 16)
- %M: 2位数的分钟 (e.g., 33)
- %S: 2位数的秒钟 (e.g., 48)
- %p: AM 或 PM
### 4.3 终极配置示例
现在我们把所有学到的东西组合起来：
```python
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] [%(asctime)s] [file:%(filename)s] [line:%(lineno)d]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
def calculate_sum(a, b):
    logging.debug(f"开始计算，输入值为 a={a}, b={b}")
    result = a + b
    logging.info(f"计算完成，结果为：{result}")
    return result
calculate_sum(10, 20)
logging.warning("这是一个自定义格式的警告！")
```
运行结果：
```
[DEBUG] [2025-05-30 16:33:48] [file:your_script_name.py] [line:11]: 开始计算，输入值为 a=10, b=20
[INFO] [2025-05-30 16:33:48] [file:your_script_name.py] [line:13]: 计算完成，结果为：30
[WARNING] [2025-05-30 16:33:48] [file:your_script_name.py] [line:16]: 这是一个自定义格式的警告！
```
看，现在的日志是不是信息量满满，又非常整洁？

## 五、 跨模块日志：logging 的真正威力

> [!TIP] 一句话概括
> 只需在主程序入口配置一次logging，所有被它导入的其他模块都能自动"继承"这套配置，实现整个项目日志风格的统一。这是 logging 甩开 print 最远的地方。
假设我们的项目变大了，分成了两个文件：
helper.py (辅助模块):
```python
import logging
def do_something():
    # 注意，这里没有进行任何 basicConfig 配置！
    logging.info("我在 helper 模块里，正在干活...")
```
main.py (主程序入口):
```python
import logging
import helper # 导入我们的辅助模块
# 在主程序中，并且在调用其他模块功能之前，进行全局配置
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] [%(filename)s]: %(message)s'
)
logging.info("主程序开始运行。")
helper.do_something() # 调用辅助模块里的函数
logging.info("主程序运行结束。")
```
当你运行 main.py 时，你会看到：
```
[INFO] [main.py]: 主程序开始运行。
[INFO] [helper.py]: 我在 helper 模块里，正在干活...
[INFO] [main.py]: 主程序运行结束。
```
> [!QUESTION] 哇！helper.py 明明没有配置，为什么它的日志格式和 main.py 一样，而且 %(filename)s 还自动变成了 helper.py？
来源与原理：logging.basicConfig() 配置的是一个叫做 Root Logger (根日志记录器) 的东西。你可以把它想象成整个Python程序的日志系统"总司令"。当 main.py 配置了"总司令"后，项目里任何地方（包括 helper.py）通过 import logging 调用 logging.info() 时，如果它们没有创建自己独立的"小队长"（更高级的用法），就会默认去向这位"总司令"汇报。
"总司令"拿到来自 helper.py 的汇报后，会用自己被设定的格式去处理它。并且，logging 足够智能，它能自动识别出这条汇报的"籍贯"（来自哪个文件，哪一行），所以 %(filename)s 和 %(lineno)d 总是能显示正确的位置信息。
这是一个极其强大的特性，保证了大型项目中日志的高度一致性和可追溯性。

> [!SUCCESS] 总结
> 恭喜你！你已经掌握了Python logging 模块最核心、最实用的部分。现在，你的程序调试和监控能力已经超越了$90%$的新手。
> 
> 别再犹豫了，从今天起，在你的新项目中忘掉 print，全面拥抱 logging 吧！找一个你喜欢的 format 格式，将它变成你的代码标配，你的编程生涯将会因此而变得更加轻松和专业。 