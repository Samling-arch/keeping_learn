好的，小白同学你好！这节课苑昊老师讲的是 `GROUP BY` 分组查询，这块确实是 SQL 查询里比较绕的一个点，但是别担心，我们一步一步来拆解，让你彻底明白它！

# 1 MySQL从基础到进阶 - 第四节: GROUP BY 分组查询

## 1.1 什么是 GROUP BY 语句？

通俗来说：**`GROUP BY` 就像是给数据分类贴标签，把具有相同特征的数据（比如同一个部门的员工）归拢到一起，方便我们对每一类数据进行统一处理。**

*   **概念细究**：
    *   `GROUP BY` 语句用于根据一个或多个列（也叫字段）对结果集进行分组。
    *   "结果集" 指的是我们查询出来的数据记录。它可以是整张表的所有记录，也可以是经过 `WHERE` 条件筛选后剩下的记录。比如，我们可以先用 `WHERE` 挑出工资大于 $5000$ 的员工，然后再对这些高薪员工按部门进行分组。
*   **为什么需要分组？**
    *   很多时候，我们不关心单条记录的细节，而是想知道某一类数据的整体情况。比如，想知道“每个部门”的平均工资，而不是“张三”的工资。这个“每个”就是分组的信号！
*   **分组后做什么？**
    *   分组后，通常需要配合**聚合函数**来对每个组进行计算或统计。

## 1.2 聚合函数：分组后的神算手

通俗来说：**聚合函数就是用在分组数据上的计算器，能帮我们快速算出每个组的总和、平均数、最大值、最小值或者数量等。**

MySQL 中常用的聚合函数有以下几个（老师提到了6个，但通常核心是这5个，第6个可能是 `GROUP_CONCAT` 等，但视频里主要演示了前5个）：

1.  `MAX(列名)`: 求指定列在每个组中的最大值。
    *   来源：数学中的求最大值的概念。
    *   例如：`MAX(salary)` 就是找出每个组里最高的工资。
2.  `MIN(列名)`: 求指定列在每个组中的最小值。
    *   来源：数学中的求最小值的概念。
    *   例如：`MIN(age)` 就是找出每个组里年龄最小的员工。
3.  `AVG(列名)`: 求指定列在每个组中的平均值。
    *   来源：数学中的求平均值的概念。
    *   例如：`AVG(salary)` 就是计算每个组的平均工资。
4.  `SUM(列名)`: 求指定列在每个组中的总和。
    *   来源：数学中的求和概念。
    *   例如：`SUM(salary)` 就是计算每个组的工资总支出。
5.  `COUNT(列名或*)`: 统计每个组中的记录数量。
    *   来源：计数、点数的概念。
    *   `COUNT(*)`: 统计每个组有多少条记录（即多少个员工）。
    *   `COUNT(列名)`: 统计指定列在每个组中非空值的数量。

## 1.3 袁老师的“灵魂画图”：`GROUP BY` 到底干了啥？

通俗来说：**`GROUP BY` 的过程就像分拣快递，你拿到一个快递（一条记录），看一下它的目的地（分组字段的值，比如“部门”），然后把它放进对应目的地的框子里（分组）。**

我们用老师的例子来模拟一下，假设我们有一张员工表 `emp`，里面有 `name` (姓名), `department` (部门), `salary` (工资), `age` (年龄) 等字段。

原始数据（老师拿了前六条举例）：

| name   | department | salary | age | ... |
| :----- | :--------- | :----- | :-- | :-- |
| 乔治   | 教学部     | 8000   | 24  | ... |
| (员工B) | 运营部     | 7000   | 19  | ... |
| SARAH  | 运营部     | 12000  | 28  | ... |
| ECHO   | 运营部     | 6500   | 22  | ... |
| ABL    | 销售部     | 9000   | 24  | ... |
| JOHN   | 教学部     | 9800   | 30  | ... |
| ...    | ...        | ...    | ... | ... |

现在我们要执行 `SELECT * FROM emp GROUP BY department;` （虽然实际中 `SELECT *` 和 `GROUP BY` 直接用会有点问题，但这里是为了理解分组过程）

**分组过程揭秘：**

1.  **拿出第一条记录**：
    *   `乔治`, `教学部`, ...
    *   按什么分组？`department` (部门)。
    *   `department` 的值是 "教学部"。
    *   当前有 "教学部" 这个组吗？没有。
    *   **动作**：创建一个新的组，命名为 "教学部"，把这条记录放进去。
    *   **当前分组情况**：
        *   教学部组：[ (乔治, 教学部, ...) ]

2.  **拿出第二条记录**：
    *   `(员工B)`, `运营部`, ...
    *   `department` 的值是 "运营部"。
    *   当前有 "运营部" 这个组吗？没有。
    *   **动作**：创建一个新的组，命名为 "运营部"，把这条记录放进去。
    *   **当前分组情况**：
        *   教学部组：[ (乔治, 教学部, ...) ]
        *   运营部组：[ ((员工B), 运营部, ...) ]

3.  **拿出第三条记录**：
    *   `SARAH`, `运营部`, ...
    *   `department` 的值是 "运营部"。
    *   当前有 "运营部" 这个组吗？有！
    *   **动作**：把这条记录放进已有的 "运营部" 组。
    *   **当前分组情况**：
        *   教学部组：[ (乔治, 教学部, ...) ]
        *   运营部组：[ ((员工B), 运营部, ...), (SARAH, 运营部, ...) ]

4.  **拿出第四条记录**：
    *   `ECHO`, `运营部`, ...
    *   `department` 的值是 "运营部"。
    *   当前有 "运营部" 这个组吗？有！
    *   **动作**：把这条记录放进已有的 "运营部" 组。
    *   **当前分组情况**：
        *   教学部组：[ (乔治, 教学部, ...) ]
        *   运营部组：[ ((员工B), 运营部, ...), (SARAH, 运营部, ...), (ECHO, 运营部, ...) ]

5.  **拿出第五条记录**：
    *   `ABL`, `销售部`, ...
    *   `department` 的值是 "销售部"。
    *   当前有 "销售部" 这个组吗？没有。
    *   **动作**：创建一个新的组，命名为 "销售部"，把这条记录放进去。
    *   **当前分组情况**：
        *   教学部组：[ (乔治, 教学部, ...) ]
        *   运营部组：[ ((员工B), 运营部, ...), (SARAH, 运营部, ...), (ECHO, 运营部, ...) ]
        *   销售部组：[ (ABL, 销售部, ...) ]

6.  **拿出第六条记录**：
    *   `JOHN`, `教学部`, ...
    *   `department` 的值是 "教学部"。
    *   当前有 "教学部" 这个组吗？有！
    *   **动作**：把这条记录放进已有的 "教学部" 组。
    *   **当前分组情况**：
        *   教学部组：[ (乔治, 教学部, ...), (JOHN, 教学部, ...) ]
        *   运营部组：[ ((员工B), 运营部, ...), (SARAH, 运营部, ...), (ECHO, 运营部, ...) ]
        *   销售部组：[ (ABL, 销售部, ...) ]

... 以此类推，直到所有记录都被分配到相应的组中。

**分组完成后的样子：**

*   **教学部组**：包含所有 `department` 为 "教学部" 的员工记录。
    *   (乔治, 教学部, $8000$, $24$)
    *   (JOHN, 教学部, $9800$, $30$)
*   **运营部组**：包含所有 `department` 为 "运营部" 的员工记录。
    *   ((员工B), 运营部, $7000$, $19$)
    *   (SARAH, 运营部, $12000$, $28$)
    *   (ECHO, 运营部, $6500$, $22$)
*   **销售部组**：包含所有 `department` 为 "销售部" 的员工记录。
    *   (ABL, 销售部, $9000$, $24$)

**分完组之后干什么？用聚合函数对每个组进行计算！**

*   **求每个部门的平均工资 `AVG(salary)`**：
    *   教学部组：($8000 + 9800$) / $2 = 8900$
    *   运营部组：($7000 + 12000 + 6500$) / $3 \approx 8500$
    *   销售部组：($9000$) / $1 = 9000$
*   **求每个部门的最高工资 `MAX(salary)`**：
    *   教学部组：$MAX(8000, 9800) = 9800$
    *   运营部组：$MAX(7000, 12000, 6500) = 12000$
    *   销售部组：$MAX(9000) = 9000$
*   **求每个部门的最低年龄 `MIN(age)`**：
    *   教学部组：$MIN(24, 30) = 24$
    *   运营部组：$MIN(19, 28, 22) = 19$
    *   销售部组：$MIN(24) = 24$

**重点**：如果我们改变分组的依据，比如按 `province` (省份) 分组，那么整个分组的“篮子”就会完全不同，得到的统计结果也会是“每个省份”的统计数据。

## 1.4 `GROUP BY` 的 SQL 语法和实际操作

通俗来说：**写 `GROUP BY` 查询时，`SELECT` 后面通常只放分组的那个字段和聚合函数计算出来的结果，因为我们关心的是每个“组”的特征，而不是组里某个具体成员的单一信息。**

### 1.4.1 基本语法结构

```sql
SELECT 分组字段, 聚合函数(计算字段)
FROM 表名
WHERE 过滤条件  -- 可选，先筛选再分组
GROUP BY 分组字段;
```

### 1.4.2 示例1：查询每个部门的平均工资

*   **需求**：查询每个部门的平均工资。
*   **分析**：“每个部门”提示我们要按 `department` 分组。
*   **SQL 语句**：

    ```sql
    SELECT
        department, -- 显示部门名称，这是分组的依据
        AVG(salary) -- 计算每个部门的平均工资
    FROM
        emp -- 从 emp 表
    GROUP BY
        department; -- 按 department 字段进行分组
    ```

*   **为什么 `SELECT name` 会报错？**
    *   老师提到，如果写 `SELECT name, AVG(salary) FROM emp GROUP BY department;` 或者 `SELECT *, AVG(salary) FROM emp GROUP BY department;` 会报错。
    *   原因：当你按 `department` 分组后，比如 "教学部" 有 $11$ 条员工记录，这 $11$ 条记录的 `name` 都是不同的。数据库不知道在结果中应该显示哪一个 `name` 来代表整个 "教学部" 组。`AVG(salary)` 是对这 $11$ 个人的工资进行计算后得出的一个值，是代表整个组的。
    *   **规则**：`SELECT` 子句中出现的列，要么是 `GROUP BY` 子句中用于分组的列，要么是包含在聚合函数中的列。

*   **执行结果（示意）**：

| department | AVG(salary)        |
| :--------- | :----------------- |
| 教学部        | $8909.09090909...$ |
| 运营部        | $8500.33333333...$ |
| 销售部        | $8200.00000000...$ |

### 1.4.3 示例2：格式化平均工资并使用别名

通俗来说：**我们可以用 `FORMAT` 函数让数字更好看（比如保留两位小数），用别名让列名更易懂。**

*   **需求**：查询每个部门的平均工资，平均工资保留两位小数，并且列名显示为中文。
*   **`FORMAT(数值, 小数位数)` 函数**：
    *   这是 MySQL 的一个内置函数，用于格式化数字。
    *   `FORMAT(AVG(salary), 2)` 意味着将计算出来的平均工资保留 $2$ 位小数。
*   **列别名 `AS` 或直接空格**：
    *   `department AS 部门名称` 或者 `department 部门名称`：将 `department` 列在结果中显示为 "部门名称"。
    *   `FORMAT(AVG(salary), 2) AS 平均工资` 或者 `FORMAT(AVG(salary), 2) 平均工资`：将计算和格式化后的平均工资列显示为 "平均工资"。
*   **SQL 语句**：

    ```sql
    SELECT
        department AS 部门, -- 给 department 列起别名 "部门"
        FORMAT(AVG(salary), 2) AS 平均工资 -- 计算平均工资，格式化，起别名 "平均工资"
    FROM
        emp
    GROUP BY
        department;
    ```

*   **执行结果（示意）**：

| 部门  | 平均工资      |
| :-- | :-------- |
| 教学部 | $8909.09$ |
| 运营部 | $8500.33$ |
| 销售部 | $8200.00$ |

### 1.4.4 示例3：查询每个部门的最高工资

*   **需求**：查询每个部门的最高工资。
*   **分析**：聚合函数从 `AVG()` 换成 `MAX()`。
*   **SQL 语句**：

    ```sql
    SELECT
        department AS 部门,
        MAX(salary) AS 最高工资
    FROM
        emp
    GROUP BY
        department;
    ```

*   **执行结果（示意）**：

    | 部门   | 最高工资 |
    | :----- | :------- |
    | 教学部 | $15000$   |
    | 运营部 | $12000$   |
    | 销售部 | $9000$    |
    *注意：这里的最高工资值是虚构的，以匹配老师视频中可能的数值范围。`MAX()` 不需要 `FORMAT()` 因为它通常是整数。*

### 1.4.5 示例4：查询每个部门的工资总和（成本核算）

*   **需求**：查询每个部门的工资总和。
*   **分析**：聚合函数用 `SUM()`。
*   **SQL 语句**：

    ```sql
    SELECT
        department AS 部门,
        SUM(salary) AS 工资总和
    FROM
        emp
    GROUP BY
        department;
    ```

*   **执行结果（示意，根据老师口述的值）**：

| 部门  | 工资总和     |                           |
| :-- | :------- | ------------------------- |
| 教学部 | $98000$  |                           |
| 运营部 | $102000$ | -- 老师口误或数据有调整，视频中说是10万多一点 |
| 销售部 | $74000$  |                           |

### 1.4.6 示例5：查询每个部门的员工个数

*   **需求**：查询每个部门有多少员工。
*   **分析**：用 `COUNT()` 聚合函数来数数。
*   **`COUNT()` 的使用**：
    *   `COUNT(*)`: 统计每个组的总行数，推荐使用，因为它不关心具体列是否有 `NULL` 值。
    *   `COUNT(列名)`: 例如 `COUNT(name)`，统计 `name` 列在每个组中非 `NULL` 值的数量。如果 `name` 列不可能为 `NULL`，结果和 `COUNT(*)` 一样。
    *   老师演示了 `COUNT(name)` 和 `COUNT(age)` 甚至 `COUNT(*)`，结果是一样的，因为在这个场景下，每个员工都有姓名和年龄，且每一行代表一个员工。
*   **SQL 语句**：

    ```sql
    SELECT
        department AS 部门,
        COUNT(*) AS 员工个数 -- 统计每个部门的记录数（即员工数）
    FROM
        emp
    GROUP BY
        department;
    ```

*   **执行结果（示意，根据老师口述的值）**：

| 部门  | 员工个数 |
| :-- | :--- |
| 教学部 | $11$ |
| 运营部 | $12$ |
| 销售部 | $9$  |

## 1.5 总结一下

*   `GROUP BY` 的核心思想是**先分组，再对每组进行聚合计算**。
*   看到“每个XXX的YYY”这类需求，通常就要想到用 `GROUP BY`。
*   `SELECT` 子句中只能出现分组字段和聚合函数。
*   常用的聚合函数有 `MAX`, `MIN`, `AVG`, `SUM`, `COUNT`。
*   可以用 `FORMAT()` 美化数字显示，用别名 `AS` (或空格) 优化列名。

这节课的内容确实需要多练习才能熟练掌握。老师说下节课会带大家做大量练习，这非常重要！通过不断练习，你就能把 `GROUP BY` 这个“小魔王”给驯服啦！希望这些解释对你有帮助！