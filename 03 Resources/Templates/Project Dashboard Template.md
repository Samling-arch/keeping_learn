# {{title}} 项目仪表盘

> [!info] 项目信息
> - **开始日期**: {{date}}
> - **截止日期**: 
> - **状态**: active
> - **所属领域**: 
> - **优先级**: 

## 📊 项目概览
- **目标**: 
- **关键成果**: 
- **进度**: 0%

## 📝 项目任务
```dataview
TASK
FROM [[{{title}}]]
WHERE !completed
```

## 📚 相关资源
```dataview
LIST
FROM [[{{title}}]] AND !"03 Resources/Templates"
SORT file.name ASC
```

## 📈 进度追踪
```dataview
TABLE progress as "进度", file.mtime as "最后更新"
FROM [[{{title}}]] AND #status/milestone
SORT progress DESC
```

## 🔄 最近更新
```dataview
TABLE file.mtime as "更新时间"
FROM [[{{title}}]]
SORT file.mtime DESC
LIMIT 5
```

## 🧩 相关笔记
```dataview
LIST
FROM "03 Resources/Zettelkasten"
WHERE contains(file.outlinks, [[{{title}}]]) OR contains(file.inlinks, [[{{title}}]])
```

## 📅 时间线
- {{date}}: 项目启动

## 📌 待办事项
- [ ] 完善项目目标
- [ ] 制定详细计划
- [ ] 收集必要资源
- [ ] 设置里程碑

## 🔗 外部链接
- 

## 📊 项目回顾
### 成功之处
- 

### 挑战
- 

### 经验教训
- 