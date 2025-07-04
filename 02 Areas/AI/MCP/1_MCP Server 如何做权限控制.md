
# 1 MCP Server 如何做权限控制？
> **原视频链接**：[阿里二面：MCPServer如何做权限控制？问倒一大片。。面试前一定要看完！！](https://www.bilibili.com/video/BV13mJVz4ENX/)
> **UP主**：徐庶架构师
> **发布时间**：2025-05-18 20:06:46
`tags: #MCP #AI #SpringAI #权限控制 #面试题 #架构`
## 1.1 核心问题汇总
| 问题                                             | 核心要点/解决方案                                                                                                                                      |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. 如何为 MCP Server 实现用户级的权限控制？                  | 不能简单依赖系统提示词，需要从连接方式入手，区分 `STDIO` 和 `SSE` 两种模式。                                                                                                 |
| 2. 为什么系统提示词 (System Prompt) 不足以做权限控制？          | 用户可以通过 Prompt Injection/Manipulation 的方式，在对话中指定查询其他用户，绕过权限限制。                                                                                  |
| 3. 如何为 `STDIO` 模式的 MCP Server 实现权限控制？          | 通过**环境变量**传递认证信息（如 `username`, `token`），Server 端从环境变量中获取用户身份。                                                                                  |
| 4. `STDIO` 模式下动态切换用户有什么问题？                     | **并发问题**。`STDIO` 是本地进程，多个客户端共享一个环境变量，并发修改会导致数据错乱。Spring AI 官方也未提供动态切换 API，需自行扩展。                                                               |
| 5. 如何为 `SSE` 模式的 MCP Server 实现权限控制？（**推荐方案**）  | `SSE` 基于 HTTP，是外部 Web 服务。使用标准 Web 认证方案，如在**请求头 (Header)** 中携带 `JWT Token`。                                                                     |
| 6. 为何 `SSE` 方案中需要特别设置 `SecurityContextHolder`？ | Spring AI 的 Tool 方法调用是在**子线程**中执行的，而 Spring Security 默认将安全上下文 (`SecurityContext`) 存在主线程的 `ThreadLocal` 中。必须设置为**子线程共享模式**，才能在 Tool 方法内获取到用户信息。 |
| 7. `SSE` 模式下，客户端如何传递认证信息？                      | Spring AI 底层使用 `WebClient`。虽然官方未提供直接设置请求头的 API，但可以**扩展 `WebClient` 的定制器 (Customizer)**，为其设置默认的 `Authorization` 请求头。                            |
| 8. Spring AI 中动态切换用户（Token）的现状如何？              | 无论是 `STDIO` 还是 `SSE`，Spring AI 目前版本**均未提供官方 API** 进行动态用户/Token 切换。实现该功能需要自行基于底层进行扩展，比较复杂。但社区已有相关提案，未来版本可能会支持。                                  |

## 1.2 一、问题的提出：用户级数据隔离
最近有同学在开发企业级的 MCP Server 时遇到一个需求：
1.  不想让**没有授权**的用户访问 MCP Server。
2.  需要根据**不同的用户**返回不同的 MCP Server 数据。
## 1.3 二、方案一（错误示范）：使用系统提示词 (System Prompt)
很多人的第一反应是使用系统提示词来传递当前用户信息。
### 1.3.1 实现思路
通过 Spring AI 设置一个系统提示词，告诉大模型当前的用户名是什么，并传递一个动态变量。
```java
// 示例伪代码
ChatClient.builder(chatModel)
    .defaultSystem("当前登录的用户是：{username}")
    .build();
// 对话时动态传入
chatClient.prompt()
    .user("我的分数是多少")
    .param("username", "徐庶") // 动态传递当前登录用户
    .call()
    .content();
```
在 MCP Server 端，定义一个 Tool (Function) 来根据用户名获取分数。
```java
// MCP Server 端的 Tool
@Bean
public Function<Request, Response> getUserScore() {
    return request -> {
        String username = request.username;
        // 根据用户名查询分数
        Map<String, Double> scores = Map.of("徐庶", 99.0, "张三", 2.0);
        if (scores.containsKey(username)) {
            return new Response(scores.get(username));
        }
        return new Response("未检索到当前用户");
    };
}
```
### 1.3.2 测试与问题
-   **正常查询**：当我问 “我的分数是多少？”
    -   传递的用户是 “徐庶”。
    -   大模型调用 `getUserScore` 方法，查询到徐庶的分数。
    -   返回结果：“徐庶的分数是 $99$”。看起来是成功的。
-   **致命问题**：用户可以随意查询其他用户的数据。
    -   当我问：“查询张三的分数是多少？”
    -   大模型依然会理解意图，调用 `getUserScore` 方法，并将 “张三” 作为参数。
    -   返回结果：“张三的分数是 $2.0$”。
    -   **结论**：通过提示词的方式，虽然可以将当前用户传递到 MCP Server，但是**并不能做到权限的控制**。
---
## 1.4 三、两种请求 MCP Server 的方式：STDIO 和 SSE
要正确实现权限控制，首先要了解请求 MCP Server 的两种方式，它们的鉴权方式也不同。
1.  **STDIO** (Standard Input/Output)：本地进程通信方式。
2.  **SSE** (Server-Sent Events)：基于 HTTP 的长链接方式。
## 1.5 四、方案二：基于 STDIO 的权限控制
### 1.5.1 实现原理：环境变量
对于 `STDIO` 方式，我们通常会配置一个 JSON 文件来描述 MCP Server 信息。其中，可以通过**环境变量**来传递授权信息。
```json
// 示例配置
{
  "command": ["java", "-jar", "mcp-server.jar"],
  "env": {
    "USERNAME": "徐庶" // 或传递 token、密钥等
  }
}
```
在 MCP Server 端，不再通过方法参数获取用户名，而是直接从环境变量中读取。
```java
// MCP Server 端从环境变量获取用户
String username = System.getenv("USERNAME");
// ...后续查询逻辑
```
通过这种方式，用户在客户端的对话无法影响到 Server 端获取的用户身份，从而实现了权限控制。
### 1.5.2 STDIO 的动态环境变量切换难题
**问题**：如果我想在登录后，动态切换这里的 `username` 怎么办？
**解决方案（复杂且不推荐）**：
Spring AI 在上层并没有提供对应的 API，我们只能自己去扩展。徐庶老师的实现思路如下（见招拆招）：
1.  定义一个 `login` 接口，接收新的用户名。
2.  **销毁**掉之前的 `STDIO` 连接。
3.  修改对应环境变量中的 `username` 值。
4.  **重新创建**一个新的 `STDIO` 连接。
5.  销毁 Spring 容器中对应的旧 Bean，注册新 Bean。
这个过程相当于重新建立 MCP Server 的连接。
### 1.5.3 ⚠️ STDIO 方案的并发问题（核心缺陷）
这种动态切换方式更建议用于**一次性授权**，而不是频繁的动态切换。
-   **原理**：`STDIO` 属于**本地 MCP Server**。一个 MCP 客户端只会创建一个 `STDIO` 进程。
-   **并发竞争**：如果多个客户端（例如多个 Web 请求线程）同时登录和操作，它们会并发地修改和读取**同一个共享的环境变量**。这必然会导致**数据错乱**（Race Condition）。
-   **规避方法**：除非为每一个客户端都创建一个独立的 `STDIO` 连接进程，让它们的环境变量相互隔离。但这会涉及更多底层源码的扩展，非常复杂。
**结论**：如果你想实现用户的动态切换，MCP 更推荐使用 `SSE` 方式。
---
## 1.6 五、方案三（推荐）：基于 SSE 的权限控制
### 1.6.1 架构优势
-   **模式**：`SSE` 是基于 HTTP 的方式，我们会将 MCP Server 单独部署成一个**外部 Web 服务**。
-   **连接**：多个客户端同时登录时，会和 MCP Server 建立多个独立的 HTTP 长链接。
-   **线程安全**：每个请求都有自己的上下文，因此**不存在线程安全问题**。
> **区分**：
> - `STDIO`: 客户端的 MCP Server (Client-side MCP Server)
> - `SSE`: 外部的 MCP Server (External MCP Server)
对于同一个 MCP Client 需要支持多个用户鉴权的场景，`SSE` 方式更加合适。
### 1.6.2 实现原理：HTTP 请求头 + Token
既然是 HTTP 连接，我们就可以使用标准的 Web 鉴权方案：通过**请求头 (Header)** 结合 `JWT` 等技术传入用户 `token`。
### 1.6.3 SSE Server 端实现 (Spring Security)
Spring AI 官方提供了解决方案，我们可以集成 `Spring Security` 和 `OAuth2`。
1.  **添加依赖**：引入 Spring Security 和 OAuth2 相关依赖。
2.  **配置安全策略**：
    -   **关键点**：需要把 `SecurityContextHolder` 设置为**子线程共享模式**。
        ```java
        // 必须设置，否则子线程拿不到安全上下文
        SecurityContextHolder.setStrategyName(SecurityContextHolder.MODE_INHERitableThreadLocal);
        ```
    -   **原因**：Spring AI 调用 Tool 方法时，是通过**子线程**方式执行的。而 Spring Security 默认将安全上下文 (`SecurityContext`) 存储在**主线程**的 `ThreadLocal` 中。如果不设置为共享，Tool 方法内将无法获取到当前请求的用户信息。
3.  **配置用户名/密码**：在配置文件中配置用于测试的用户名和密码。
**演示流程**：
4.  直接请求 MCP Server 接口 -> 得到 `$401$` Unauthorized。
5.  请求 OAuth2 的 `token` 接口，传入用户名和密码 -> 得到一串 `access_token`。
6.  将 `access_token` 放入请求头的 `Authorization` 字段中，再次请求 MCP Server -> 正常访问。
### 1.6.4 SSE Client 端实现 (WebClient Customizer)
**问题**：客户端如何把 `token` 加到每次请求的 Header 中？
**解决方案**：
Spring AI 的底层是通过 `WebClient` 来发起远程 HTTP 请求的。虽然官方没有直接提供设置请求头的 API，但它提供了一个 `WebClient` 的**定制器 (Customizer)**。我们可以基于这个定制器来设置默认的请求头。
```java
// 伪代码：定制 WebClient 添加默认 Header
@Bean
public WebClient.Builder webClientBuilder() {
    String token = "从认证服务获取到的token...";
    return WebClient.builder()
            .defaultHeader(HttpHeaders.AUTHORIZATION, "Bearer " + token);
}
```
这样，MCP 客户端启动时就会与 MCP Server 建立带 `token` 的连接，并且后续的每一次调用也都会带上这个 `token` 来完成鉴权。
**演示流程**：
1.  客户端配置切换为 `SSE` 模式。
2.  启动 `SSE` 模式的 MCP Server。
3.  启动配置了 `token` 的 MCP Client。
4.  客户端提问：“我的分数是多少？”
5.  由于客户端携带的是 “徐庶” 的 `token`，Server 端的 `SecurityContextHolder` 能获取到用户是 “徐庶”。
6.  返回结果：“检索到的分数是 $99$”。
### 1.6.5 SSE 客户端的动态 Token 切换
与 `STDIO` 类似，要实现动态切换 `token`（即用户切换登录），依然比较复杂。
-   **现状**：Spring AI 目前没有提供这块的 API，需要自己去扩展，动态地去修改 `WebClient` 的默认请求头。
-   **未来**：徐庶老师观察到 MCP 的 Java SDK 开源社区里，已经提交了很多关于鉴权、动态切换的功能提案（Issue/PR）。相信在未来的版本中，这些功能会被官方支持，不再需要我们自己基于底层去扩展。