import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from fast_mcp import MCP, ToolContext

from llama_index.core.workflows import Workflow, step
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from duckduckgo_search import DDGS

# --- 1. 初始化与设置 ---

# 从 .env 文件加载环境变量 (例如 OPENAI_API_KEY)
# 请确保在项目根目录创建 .env 文件并填入您的 OpenAI API 密钥
load_dotenv()

# 全局变量，用于存储 RAG 工作流实例
# This will hold our initialized RAG workflow
rag_workflow = None
DATA_DIR = "./data"

# --- 2. 定义 LlamaIndex RAG 工作流 ---

class MyRagWorkflow(Workflow):
    """
    一个自定义的 RAG 工作流，包含两个主要步骤：
    1. ingest: 读取'data'目录下的文档，并构建向量索引。
    2. query: 接收用户查询，并从索引中检索相关信息以生成答案。
    """
    def __init__(self):
        self.index = None

    @step
    def ingest(self):
        """
        数据导入步骤：加载文档并构建索引。
        这个步骤在服务器启动时执行。
        """
        print(f"开始从 '{DATA_DIR}' 文件夹导入文档...")
        # 检查'data'目录是否存在
        if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
            print(f"'{DATA_DIR}' 文件夹不存在或为空。RAG 工具将不可用。")
            print("请在该文件夹中添加您的文档。")
            return

        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        # LlamaIndex 需要 OPENAI_API_KEY 环境变量来构建索引
        if os.getenv("OPENAI_API_KEY") is None:
            print("警告：OPENAI_API_KEY 环境变量未设置。")
            print("RAG 工具可能无法正常工作。")
        
        self.index = VectorStoreIndex.from_documents(documents)
        print("文档导入完成，索引构建成功！")

    @step
    def query(self, user_query: str) -> str:
        """
        查询步骤：使用构建好的索引来回答问题。
        """
        if self.index is None:
            return "错误：知识库索引未初始化。请检查服务器启动日志以及'data'文件夹中是否有文档。"
        
        print(f"正在使用知识库查询：{user_query}")
        query_engine = self.index.as_query_engine()
        response = query_engine.query(user_query)
        return str(response)

# --- 3. FastAPI 应用和 MCP 服务器设置 ---

# 创建 FastAPI 应用实例
app = FastAPI()

# 创建 MCP 服务器实例
# 这与视频中提到的 `MCP(name="...")` 相对应
mcp = MCP(
    name="my_mcp_server_demo",
    description="一个拥有网页搜索和本地知识库问答功能的 MCP 服务器。",
    # 定义工具在API schema中的路径
    tools_path_in_schema="/mcp/tools"
)


# --- 4. 定义 MCP 工具 ---

@mcp.tool()
def web_search(query: str, context: ToolContext):
    """
    使用 DuckDuckGo 进行网页搜索，以获取最新信息。
    适用于查询近期事件、新闻或任何需要当前信息的场景。
    对应视频中的第一个工具。
    
    :param query: 搜索关键词。
    """
    print(f"正在执行网页搜索：{query}")
    try:
        with DDGS() as ddgs:
            # 获取最多5个结果
            results = [r for r in ddgs.text(query, max_results=5)]
        
        if not results:
            return f"没有找到关于 '{query}' 的搜索结果。"
            
        # 格式化搜索结果
        formatted_results = "\n\n".join(
            [f"标题: {res['title']}\n链接: {res['href']}\n摘要: {res['body']}" for res in results]
        )
        return f"这是关于 '{query}' 的网页搜索结果：\n\n{formatted_results}"
    except Exception as e:
        return f"网页搜索时发生错误: {e}"


@mcp.tool()
def knowledge_base_search(query: str, context: ToolContext):
    """
    在本地知识库（'data'文件夹中的文档）中进行搜索来回答问题。
    使用此工具查询您本地文件中的信息。
    对应视频中基于 LlamaIndex 的 RAG 工具。
    
    :param query: 向知识库提出的问题。
    """
    print(f"开始在知识库中搜索：{query}")
    if rag_workflow is None:
        return "知识库工具未初始化。请检查服务器日志。"
    
    # 异步执行工作流的 query 步骤
    response = rag_workflow.query(user_query=query)
    return response


# --- 5. 服务器启动事件 ---

@app.on_event("startup")
def startup_event():
    """
    FastAPI 启动时执行的事件。
    我们在这里初始化 RAG 工作流并执行数据导入。
    """
    global rag_workflow
    print("服务器启动中...")
    
    # 初始化工作流
    rag_workflow = MyRagWorkflow()
    
    # 运行数据导入步骤
    # 这是异步运行的，但对于启动过程来说，我们等待它完成
    rag_workflow.ingest()
    
    print("服务器已准备就绪！")


# --- 6. 挂载 MCP 应用并运行服务器 ---

# 将 MCP 服务器挂载到 FastAPI 应用的 /mcp 路径下
app.mount("/mcp", mcp)

# 主程序入口
# 允许直接通过 `python server.py` 运行
if __name__ == "__main__":
    print("启动 Uvicorn 服务器，监听 http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000) 