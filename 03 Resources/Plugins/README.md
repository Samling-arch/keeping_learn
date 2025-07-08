# Obsidian 插件集

这个文件夹用于集中管理所有 Obsidian 插件的使用笔记和配置说明。

## 文件夹结构
- `核心插件/` - Obsidian 自带的核心插件说明
- `社区插件/` - 第三方社区插件使用指南
- `主题美化/` - 主题和 CSS 片段相关
- `配置备份/` - 插件配置文件备份
- `_templates/` - 插件笔记模板
- `指南文档/` - 综合性使用指南和教程

## 使用说明
1. 新增插件笔记时使用 `_templates/Plugin Note Template.md` 模板
2. 按照插件类型分类存放到对应子文件夹
3. 定期更新插件版本和使用状态
4. 重要配置变更时及时备份
5. 综合性指南和教程放在 `指南文档/` 文件夹

## 插件概览
```dataview
TABLE 
    status as "状态",
    rating as "评分",
    frequency as "使用频率",
    file.folder as "分类"
FROM "03 Resources/Plugins" and #plugin 
SORT rating DESC
```

## 指南文档
```dataview
TABLE 
    file.size as "大小",
    file.mtime as "最后修改"
FROM "03 Resources/Plugins/指南文档"
WHERE file.name != "README"
SORT file.name ASC
```

## 标签说明
- #plugin/core - 核心插件
- #plugin/community - 社区插件
- #plugin/theme - 主题相关
- #status/active - 正在使用
- #status/archived - 已归档
- #status/testing - 测试中 