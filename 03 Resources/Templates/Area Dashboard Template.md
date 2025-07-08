# {{title}} 领域仪表盘

> [!info] 领域信息
> - **创建日期**: {{date}}
> - **重要性**: 
> - **关联生活领域**: 

## 📊 领域概览
- **目标**: 
- **关键指标**: 
- **当前状态**: 

## 📝 相关项目
```dataview
TABLE status as "状态", deadline as "截止日期", progress as "进度"
FROM "01 Projects"
WHERE area = "{{title}}"
SORT status ASC, deadline ASC
```

## ✅ 待办任务
```dataview
TASK
FROM [[{{title}}]]
WHERE !completed
```

## 📚 知识资源
```dataview
LIST
FROM "03 Resources/Zettelkasten"
WHERE contains(tags, "#area/{{title}}")
SORT file.name ASC
```

## 📈 习惯追踪
```dataview
TABLE streak as "连续天数", last_done as "上次完成"
FROM #habit AND [[{{title}}]]
SORT streak DESC
```

## 🔄 最近更新
```dataview
TABLE file.mtime as "更新时间"
FROM [[{{title}}]] OR (FROM "03 Resources/Zettelkasten" WHERE contains(tags, "#area/{{title}}"))
SORT file.mtime DESC
LIMIT 5
```

## 📊 资源分布
```dataview
TABLE length(rows) as "笔记数量"
FROM "03 Resources/Zettelkasten"
WHERE contains(tags, "#area/{{title}}")
GROUP BY tags
SORT length(rows) DESC
```

## 📌 长期目标
- [ ] 

## 🔍 需要关注
```dataview
LIST
FROM [[{{title}}]] AND #status/review
SORT file.mtime ASC
```

## 📑 参考资料
- 

## 📆 定期回顾
- [ ] 每月回顾领域进展
- [ ] 每季度调整领域目标
- [ ] 每年全面评估 