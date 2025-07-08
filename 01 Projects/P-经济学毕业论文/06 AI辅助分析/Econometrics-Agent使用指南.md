# Econometrics-Agent 使用指南

## 📚 项目简介
[Econometrics-Agent](https://github.com/FromCSUZhou/Econometrics-Agent) 是一个专门用于计量经济学分析的 AI 智能体，能够自动化复杂的计量经济学分析任务，支持零样本学习，在专家级任务中表现优于通用 AI。

## 🔧 配置信息
- **模型**: gpt-4o-mini
- **API 端点**: https://api.chatanywhere.tech
- **API 密钥**: sk-gy8uADFcwBRy4qiWqO7nvpNMxMPBTfxrtycgKxozb3mAak2sh
- **配置状态**: ✅ 已配置完成

## 🚀 主要功能
1. **专业计量经济学工具集**
   - IV-2SLS (工具变量两阶段最小二乘法)
   - DID (双重差分法)
   - RDD (断点回归设计)
   - 倾向得分匹配方法

2. **智能分析能力**
   - 零样本学习
   - 自动化数据处理
   - 结果可视化
   - 多轮对话支持

## 📁 文件结构
```
Econometrics-Agent/
├── .env                    # 环境变量配置 (已配置)
├── config/
│   └── config2.yaml       # 主配置文件 (已配置)
├── agent/                 # AI 智能体核心代码
├── web/                   # 前端界面
├── chatpilot/            # 对话系统
├── requirements.txt       # Python 依赖
├── start.sh              # Linux/Mac 启动脚本
└── start_windows.bat     # Windows 启动脚本
```

## 🛠 安装和启动

### 前提条件
- Python 3.11+
- Node.js 18+
- Git

### 安装步骤
1. **安装 Python 依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **安装前端依赖**
   ```bash
   cd web
   npm install
   npm run build
   cd ..
   ```

3. **启动应用**
   ```bash
   # Windows
   start_windows.bat
   
   # Linux/Mac
   bash start.sh
   ```

4. **访问应用**
   - 浏览器打开: http://localhost:1280

## 📊 使用场景

### 1. 论文数据分析
- 上传数据集
- 选择合适的计量经济学方法
- 获得自动化分析结果
- 生成可视化图表

### 2. 方法验证
- 测试不同的估计方法
- 比较模型结果
- 稳健性检验

### 3. 学习辅助
- 理解计量经济学概念
- 学习分析方法
- 获得代码示例

## 📝 使用日志

### 2025-01-27
- ✅ 成功克隆仓库到本地
- ✅ 配置 API 密钥和端点
- ✅ 修改模型为 gpt-4o-mini
- 🔄 待测试：启动和运行验证

### 待办事项
- [ ] 测试应用启动
- [ ] 验证 API 连接
- [ ] 上传样本数据测试
- [ ] 生成第一个分析报告

## 🔗 相关资源
- [GitHub 仓库](https://github.com/FromCSUZhou/Econometrics-Agent)
- [论文引用](https://arxiv.org/abs/2506.00856)
- [[经济学毕业论文MOC]]
- [[03 数据分析]]

## ⚠️ 注意事项
1. 确保网络连接稳定，API 调用需要联网
2. 第一次启动可能需要较长时间下载依赖
3. 建议定期备份分析结果和日志
4. API 使用可能产生费用，请合理控制使用量

## 🐛 故障排除
- **端口冲突**: 默认端口 1280，如被占用可修改配置
- **依赖安装失败**: 检查 Python 和 Node.js 版本
- **API 调用失败**: 验证网络连接和 API 密钥
- **前端加载问题**: 重新构建前端项目

---
#AI工具 #计量经济学 #数据分析 #自动化 