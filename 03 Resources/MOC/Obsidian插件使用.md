# Obsidian 插件使用指南 MOC

## 概述
这个 MOC (Map of Content) 用于组织和管理所有与 Obsidian 插件相关的笔记。包括插件的安装、配置、使用技巧和最佳实践。

## 插件分类
### 核心功能增强
- [[Dataview插件使用指南]] - 数据查询与展示
- [[Templates插件使用指南]] - 模板系统
- [[Quickadd插件使用指南]] - 快速添加内容

### 可视化与图表
- [[Excalidraw插件使用指南]] - 手绘风格图表
- [[Canvas插件使用指南]] - 可视化布局

### 知识管理
- [[Spaced Repetition插件使用指南]] - 间隔重复
- [[Outliner插件使用指南]] - 大纲管理

### 美化与主题
- [[Minimal Theme插件使用指南]] - 极简主题
- [[Style Settings插件使用指南]] - 主题设置

## 使用状态
```dataview
TABLE 
    status as "状态",
    rating as "评分",
    frequency as "使用频率"
FROM "03 Resources/Zettelkasten"
WHERE contains(tags, "plugin")
SORT rating DESC
```

## 相关链接
- [[插件安装最佳实践]]
- [[插件配置备份与同步]]
- [[常见插件问题解决]]

## 标签
#tool/obsidian #type/reference #status/evergreen 