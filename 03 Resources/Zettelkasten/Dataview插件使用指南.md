---
aliases: [Dataview]
tags: [plugin, tool/obsidian, type/reference]
status: active
rating: 5
frequency: daily
created: 2024-03-20
modified: 2024-03-20
---

# Dataview 插件使用指南

## 插件信息
- 名称：Dataview
- 作者：Michael Brenan
- 版本：0.5.64
- 仓库链接：https://github.com/blacksmithgu/obsidian-dataview

## 主要功能
- 通过类SQL语法查询笔记数据
- 支持JavaScript API进行高级数据处理
- 自动提取YAML frontmatter中的元数据
- 支持表格、列表、任务列表等多种显示格式

## 安装配置
### 安装步骤
1. 打开 Obsidian 设置
2. 进入社区插件市场
3. 搜索 "Dataview" 并安装
4. 启用插件

### 基本配置
```settings
Enable JavaScript Queries: true
Enable Inline Queries: true
Enable Inline Fields: true
```

## 使用方法
### 基础用法
- 基本查询语法：
```dataview
TABLE file.ctime as 创建时间
FROM "03 Resources"
WHERE contains(tags, "plugin")
```

- 常用字段：
  - file.name：文件名
  - file.path：文件路径
  - file.tags：标签列表
  - file.ctime：创建时间
  - file.mtime：修改时间

### 进阶技巧
- 使用 FLATTEN 展开数组
- 使用 GROUP BY 进行分组统计
- 通过 JS 查询实现复杂数据处理
- 使用 TASK 进行任务管理

### 快捷键设置
- Ctrl + Click：快速预览链接
- 自定义代码片段快捷键

## 使用场景
- 场景1：生成项目进度报告
- 场景2：追踪学习笔记统计
- 场景3：任务和待办事项管理
- 场景4：知识关联分析

## 注意事项
- 大量查询可能影响性能
- 建议给重要字段添加索引
- 定期清理无用的查询缓存
- 注意数据类型的一致性

## 个人评价
### 优点
- 强大的数据查询能力
- 灵活的显示格式
- 活跃的社区支持
- 与其他插件良好集成

### 缺点
- 学习曲线较陡
- 复杂查询可能影响性能
- 需要良好的数据组织习惯

### 替代方案
- QuickAdd
- MetaEdit
- DB Folder

## 相关链接
- [[Dataview实战示例]]
- [[Dataview常见问题解决]]
- [[如何用Dataview构建个人知识仪表盘]]

## 更新日志
- 2024-03-20: 首次记录
- 2024-03-20: 添加基础使用示例 