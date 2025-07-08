# 1 Python FastAPI LLM 的交互 - batch 和 流式
- **来源:** [Bilibili - Mingzilla搞软件](https://www.bilibili.com/video/BV1ypTZzMEEF/)
- **UP主:** Mingzilla搞软件
- **发布时间:** 2025-06-12 09:24:30
## 1.1 核心思想：理解交互本质 > 代码实现
> UP主开篇强调：**你得知道你正在干个什么事情，那个才是关键的。** Library会改来改去，但核心问题和它在搞什么东西，你得明明白白。这次我们就是要搞明白LLM的两种核心交互方式：
> 1.  **Batch模式**：那种“啪啪一来一回”的请求。
> 2.  **Streaming模式**：那种“一个词一个词”（其实是一个token/chunk）返回的流式交互。
## 1.2 与 LLM 交互的基础：Message 结构
我们和LLM交互，传递的`Message`有三种主要类型，通过`role`字段区分。
### 1.2.1 ### System Message
- **作用**: 给LLM一个全局指令或设定。
- **`role`**: `"system"`
- **示例**: `{"role": "system", "content": "be nice"}`
- **效果**: 让LLM在接下来的整个对话中都遵循这个指令。
### 1.2.2 ### User Message
- **作用**: 用户发送给LLM的具体问题或对话内容。
- **`role`**: `"user"`
- **示例**: `{"role": "user", "content": "Hi"}`
- **优先级**: 如果User Message和System Message有冲突，系统会默认 **User Message** 拥有更高的优先级（`high priority`），因为它更具体。
### 1.2.3 ### Assistant Message
- **作用**: LLM返回给用户的回复。
- **`role`**: `"assistant"`
- **示例**: `{"role": "assistant", "content": "Hello! How can I help you today?"}`
**核心交互循环**:
> 每一次和LLM交互，你都**必须把你所有的聊天记录 (System + User + Assistant...) 发给LLM**，然后它才能根据完整的上下文，返回新的一句话给你。
## 1.3 发送给 LLM 的请求：Request 结构
我们通过HTTP Request与LLM API交互，请求体（Body）主要包含以下几个关键部分：
- **`provider` (服务提供商)**
  - **决定方式**: 通常由 **URL** 决定。
  - **例子**: `api.openai.com`, `api.deepseek.com` 等。
- **`model` (模型)**
  - **作用**: 指定使用哪个具体的LLM模型。
  - **注意**: 每个`provider`下都有很多`model`，价格和能力都不同。
- **`messages` (消息列表)**
  - **为什么是复数 `messages`**: 因为它包含的是 **整个聊天记录** 的列表（List），而不仅仅是当前这一条。
- **`temperature` (温度)**
  - **作用**: 控制回复的创意性或随机性。
  - **`0`**: 不允许有什么创意，结果非常确定，适合精准、专业的场景。
  - **`1`**: 自由发挥，结果更具扩散性、多样性，适合写作、构思童话故事等。
- **`stream` (流式开关)**
  - **作用**: 决定响应是Batch模式还是Streaming模式。
  - **`False` (或不设置)**: Batch模式，一次性返回完整结果。
  - **`True`**: Streaming模式，一个一个`chunk`地返回结果。
## 1.4 核心交互流程图
### 1.4.1 ### Batch 模式 (一来一回)
1.  **[Client -> Server]** 用户发送一条新消息。
2.  **[Server]** 创建一个 `User Message` 对象。
3.  **[Server]** **把这条 `User Message` 添加到历史记录 (History) 中**。
    - *为什么先加进去？* UP主解释：这样不管是第几轮对话，代码逻辑都一致：从历史里取出所有消息再发送。
4.  **[Server]** 从历史记录中 **读取完整的对话历史** ( `get_history` )。
5.  **[Server -> LLM]** 将完整的 `messages` 列表发送给 LLM。
6.  **[LLM -> Server]** LLM返回一个完整的 `Assistant Message`。
7.  **[Server]** **把这条 `Assistant Message` 也添加到历史记录中**。
8.  **[Server -> Client]** 将LLM的回复返回给用户。
> **Session ID 的作用**: `session_id` 就像一个钥匙（key），它的值（value）就是对应这个聊天会话的完整历史记录（一个`messages`的列表）。换个话题聊天，就换个`session_id`。
### 1.4.2 ### Streaming 模式 (流式)
> **道理其实相似**，只是返回和处理的方式不同。
1.  **[Client -> Server]** 用户发送一条新消息。
2.  **[Server]** 创建 `User Message` 并添加到历史记录 (与Batch模式**完全一样**)。
3.  **[Server]** 从历史记录中读取完整的对话历史 (与Batch模式**完全一样**)。
4.  **[Server -> LLM]** 发送请求，但这次 **额外加一个参数 `stream=True`**。
5.  **[LLM -> Server]** LLM开始一个一个地返回 **数据块 (Chunk)**。
6.  **[Server]** 服务器端需要做两件事：
    - **组合 (Assemble)**: 将收到的所有`chunk`拼接成一个完整的`Assistant Message`。
    - **转发 (Forward)**: **每收到一个`chunk`，就立刻把它转发给前端用户**，实现打字机效果。
7.  **[Server]** 当所有`chunk`接收完毕后 (流结束)，**将拼接好的、完整的 `Assistant Message` 添加到历史记录中**。
## 1.5 Live Demo 演示
UP主在 `9001` 端口启动了FastAPI服务。
### 1.5.1 ### Batch 请求演示
- **命令**: `curl` 请求 `/chat` endpoint。
- **现象**: 等待片刻后，终端一次性打印出完整的回复。
### 1.5.2 ### Streaming 请求演示
- **命令**: `curl` 请求 `/chat/stream` endpoint。
- **现象**: 终端立刻开始陆续打印出一系列的数据块，每个块都是一个独立的JSON片段。
- **流式格式 (SSE - Server-Sent Events)**:
  > UP主解释：你会看到很多代码这样处理，就是检查是不是以`data: `开头，然后减去6个字母...
  - 每一条消息都以 `data: ` 开头。
  - 后面跟着一个JSON字符串，这就是一个`chunk`。
  - 每条消息以两个换行符 `\n\n` 结尾。
  - **示例**:
    ```text
    data: {"content": "I"}
    data: {"content": " am"}
    data: {"content": " a"}
    data: {"content": " bot"}
    data: {"content": null, "finish_reason": "stop"}
    ```
## 1.6 FastAPI 代码详解
> UP主再次强调：这些代码列为其次，你用Java、JS写都没问题，**理解思路最关键**。
### 1.6.1 ### 1. Server & Endpoint Setup (`main.py`)
- 使用 `FastAPI` 创建 `app`。
- 配置 `CORS` 中间件，允许特定来源（如React前端）的跨域请求。
- 定义两个主要 `POST` endpoint：
  - `/chat`: 用于Batch模式。
  - `/chat/stream`: 用于Streaming模式。
### 1.6.2 ### 2. 数据模型 (Pydantic Models)
- **`Message`**: 定义消息结构，包含`role`和`content`。
- **`ChatRequest`**: 定义客户端请求体，包含`message`, `session_id` (optional), `model` (optional)。
- **`ChatResponse`**: 定义Batch模式的响应体。
### 1.6.3 ### 3. Batch 模式: `/chat` Endpoint
```python
# main.py
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # 1. 如果没有session_id，就生成一个
    session_id = request.session_id or str(uuid.uuid4())
    # 2. 创建User Message对象
    user_message = Message(role="user", content=request.message.content)
    # 3. 把新消息添加到历史记录
    history.add_message(session_id, user_message)
    # 4. 从历史记录中获取全部对话
    conversation = history.get_messages(session_id)
    # 5. 调用LLM Client，注意这里的 await
    #    await代表这个函数是异步的，并且我们只等一个最终结果回来
    llm_response = await llm_client.chat_completion(
        model=request.model,
        messages=conversation
    )
    # 6. 把LLM的回复也存到历史记录
    history.add_message(session_id, llm_response)
    # 7. 构造并返回响应
    return ChatResponse(message=llm_response, session_id=session_id)
```
**LLM Client (Batch 实现)**: `llm_client.chat_completion`
```python
# llm_client.py
async def chat_completion(self, model: str, messages: list[Message]) -> Message:
    # 将我们的Message对象列表，转换成OpenAI库需要的字典列表
    # UP主提到这里可以用lambda，但列表推导式写法也一样
    history_as_dicts = [
        {"role": msg.role, "content": msg.content} for msg in messages
    ]
    # 调用OpenAI的API，注意 stream=False
    response = await self.client.chat.completions.create(
        model=model,
        messages=history_as_dicts,
        temperature=0.7,
        stream=False # 关键点
    )
    # 从复杂的response对象中提取出内容
    content = response.choices[0].message.content
    return Message(role="assistant", content=content)
```
### 1.6.4 ### 4. Streaming 模式: `/chat/stream` Endpoint
```python
# main.py
@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    # 前面几步和Batch模式一模一样：获取session_id，创建user_message, 添加到历史
    session_id = request.session_id or str(uuid.uuid4())
    # ... 省略相同代码 ...
    conversation = history.get_messages(session_id)
    # 关键区别：创建一个异步生成器
    async def stream_generator():
        full_response_content = ""
        # 使用 async for 来消费流式数据
        # 这里的llm_client.stream()本身是一个异步生成器
        async for chunk in llm_client.stream(model=request.model, messages=conversation):
            full_response_content += chunk.content or ""
            # yield 将每个chunk作为SSE事件发送出去
            yield {"data": chunk.model_dump_json()}
        # finally确保流结束后，无论成功与否，都将完整消息存入历史
        finally:
            assistant_message = Message(role="assistant", content=full_response_content)
            history.add_message(session_id, assistant_message)
    # 使用FastAPI的EventSourceResponse来处理异步生成器，并返回SSE流
    return EventSourceResponse(stream_generator(), media_type="text/event-stream")
```
**LLM Client (Stream 实现)**: `llm_client.stream`
> UP主讲解：`async for` 对应的是一个返回`yield`的`async def`函数，这就是 **异步生成器 (Async Generator)**。
```python
# llm_client.py
async def stream(self, model: str, messages: list[Message]) -> AsyncGenerator[Chunk, None]:
    history_as_dicts = [
        {"role": msg.role, "content": msg.content} for msg in messages
    ]
    # 调用OpenAI的API，注意 stream=True
    response = await self.client.chat.completions.create(
        model=model,
        messages=history_as_dicts,
        stream=True # 关键点
    )
    # response本身是一个异步迭代器，我们用async for来遍历它
    async for chunk in response:
        # 从复杂的chunk对象中提取内容
        content = chunk.choices[0].delta.content
        # 使用 yield 返回每一个处理过的chunk，而不是return
        yield Chunk(content=content)
```
## 1.7 总结
> UP主最后总结：**核心就是那个流程图 (Flow Diagram)**。代码怎么写，拆成几个函数还是写在一起，都是实现细节。只要你理解了：
> 1.  **用 `session_id` 维护多轮对话历史。**
> 2.  **Batch模式** 是 `await` 一个最终结果。
> 3.  **Streaming模式** 是用 `async for` 循环处理一个由 `yield` 产生的异步生成器，同时在 `finally` 中保存完整结果。
>
> 那么这个交互的本质你就搞明白了。