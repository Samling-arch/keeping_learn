
---
title: SQL语言之PARTITION BY 窗口函数
source: Bilibili
url: https://www.bilibili.com/video/BV1cK411k7zi/
date: 2023-01-16
tags: [SQL, 窗口函数, PARTITION BY, SQL优化, 应试考点]


# 📚 SQL语言之PARTITION BY 窗口函数 核心问题汇总

本节内容为应试考点，所有知识点都将毫无差别地呈现。

| 问题 (Q)                                       | 核心概念 (Key Concept)        | 答案/解决方案 (A/Solution)                                                                               |
| :------------------------------------------- | :------------------------ | :------------------------------------------------------------------------------------------------- |
| SQL中 `WHERE` 条件能否直接使用 `PARTITION BY` 窗口函数别名？ | SQL执行顺序 (`WHERE` vs 窗口函数) | **不能**。`WHERE` 条件在 `PARTITION BY` 窗口函数生成结果之前执行，因此无法识别窗口函数定义的别名。                                    |
| 如何在 `WHERE` 条件中引用 `PARTITION BY` 窗口函数的计算结果？  | 子查询 (`FROM` 子句)           | 将包含 `PARTITION BY` 窗口函数的查询作为**子查询**放入 `FROM` 子句中，形成一个临时表，然后在外部查询的 `WHERE` 条件中引用该临时表的列（包括窗口函数生成的列）。 |
| 当排序值相等时，`RANK()` 函数如何处理并返回序号？                | 排序函数 (`RANK()` 与并列)       | `RANK()` 会为相等的值返回**相同的序号**（并列），并**跳过**后续的序号。例如，如果有两个并列的第 $2$ 名，则下一名将是第 $4$ 名，跳过了第 $3$ 名。           |
| 当排序值相等时，如何实现序号连续（不跳过）？                       | 排序函数 (`DENSE_RANK()` 与并列) | 使用 `DENSE_RANK()`。它会为相等的值返回**相同的序号**（并列），但**不会跳过**后续的序号。例如，如果有两个并列的第 $2$ 名，则下一名仍将是第 $3$ 名。         |
| `ROW_NUMBER()` 与 `RANK()` 的区别是什么？            | 排序函数 (`ROW_NUMBER()` 与并列) | `ROW_NUMBER()` 在遇到排序值相等时，仍会返回**不同的、连续的序号**，不会出现并列。而 `RANK()` 会并列并跳号。                               |
| 在练习题中，为何查询每个部门第二位入职的员工时，无法找到 $3$ 号部门的记录？     | 排序函数 (`RANK()` 的应用)       | 因为 $3$ 号部门的两名员工是**同时入职**的。如果使用 `RANK()` 函数，他们的入职序号都为 $1$（并列第一）。因此，查询序号为 $2$ 的记录自然找不到。              |
| 聚合函数（如 `SUM`, `COUNT`, `AVG`）如何处理 `NULL` 值？  | `NULL` 值处理                | **所有的聚合函数都会忽略 `NULL` 值**，不将其计入计算。例如，`COUNT(column_with_nulls)` 只会统计非 `NULL` 的行数。                   |

---

## 🚀 PARTITION BY 窗口函数 概述

这一节学习 `PARTITION BY` 窗口函数。`PARTITION BY` 函数与 `GROUP BY` 函数有些类似，但功能比 `GROUP BY` 强大得多，适用场景也更多。

### 1. PARTITION BY 与 GROUP BY 的区别

*   **`GROUP BY` 的特点：**
    *   对数据进行分组，并为每个分组返回**一个**聚合函数的统计值。
    *   例子：查询每个部门的工资合计。

    ```sql
    SELECT department_no, SUM(salary)
    FROM employees
    GROUP BY department_no;
    ```

    执行结果示例（假设有空部门号）：
    ```
    department_no | SUM(salary)
    --------------+------------
    NULL          | $90000$
    $1$           | $71000$
    $2$           | $35000$
    $3$           | $20000$
    ```

*   **`PARTITION BY` 的特点：**
    *   同样对数据进行分区（分组），但它会为分区中的**每一条记录**都返回其对应的聚合函数的统计值。
    *   它不是将多行压缩成一行，而是将聚合结果**附加**到每一行。
    *   语法：`聚合函数() OVER (PARTITION BY 列名)`
    *   `OVER` 关键词表示采取分区的意思。
    *   例子：使用 `PARTITION BY` 查询每个部门的工资合计。

    ```sql
    SELECT
        e.*,
        SUM(salary) OVER (PARTITION BY department_no) AS dept_total_salary
    FROM
        employees e;
    ```

    执行结果示例（部分）：
    ```
    employee_id | name | department_no | salary | dept_total_salary
    ------------+------+---------------+--------+------------------
    $101$       | A    | $1$           | $15000$| $71000$
    $102$       | B    | $1$           | $9100$ | $71000$
    $103$       | C    | $1$           | $21900$| $71000$
    $104$       | D    | $1$           | $25000$| $71000$
    $201$       | E    | $2$           | $9700$ | $35000$
    $202$       | F    | $2$           | $25300$| $35000$
    ...
    ```
    比较发现：`PARTITION BY` 返回的信息更多，每条员工记录都带有其所在部门的总工资。

### 2. PARTITION BY 支持的聚合函数

`PARTITION BY` 支持与 `GROUP BY` 相同的传统聚合函数，例如：
*   `SUM()`：汇总
*   `MAX()`：最大值
*   `MIN()`：最小值
*   `AVG()`：平均值
*   `COUNT()`：计数

这些函数在 `PARTITION BY` 中使用时，同样是针对每个分区进行计算，并将结果附加到分区内的每条记录上。

**示例：在 Oracle 数据库上使用 `MAX()`**

```sql
SELECT
    e.*,
    MAX(salary) OVER (PARTITION BY department_no) AS dept_max_salary
FROM
    employees e;
```

结果示例：部门 $1$ 的所有记录都显示部门最高工资 `$25000$`。

**示例：在 PostgreSQL 数据库上使用 `MIN()`**

```sql
SELECT
    e.*,
    MIN(salary) OVER (PARTITION BY department_no) AS dept_min_salary
FROM
    employees e;
```

结果示例：
*   $1$ 号部门的最小值为 `$9100$`。
*   $2$ 号部门的最小值为 `$9700$`。
*   $3$ 号部门的最小值为 `$8900$`。
*   空部门号的最小值为 `$90000$`（因为只有 $1$ 条记录）。

**示例：在 SQL Server 上使用 `AVG()`**

```sql
SELECT
    e.*,
    AVG(salary) OVER (PARTITION BY department_no) AS dept_avg_salary
FROM
    employees e;
```

结果示例：每条记录都会列出其所在部门的平均工资。

**示例：在 MySQL 上使用 `COUNT()`**

```sql
SELECT
    e.*,
    COUNT(salary) OVER (PARTITION BY department_no) AS dept_employee_count
FROM
    employees e;
```

结果示例：
*   $1$ 部门有 $4$ 条记录。
*   $2$ 部门有 $2$ 条记录。
*   $3$ 部门有 $2$ 条记录。

### 3. NULL 值在聚合函数中的处理

**重要考点：所有的聚合函数（`SUM`, `AVG`, `COUNT`, `MAX`, `MIN` 等）在计算时都**不计算 `NULL` 值**。**

*   `COUNT(salary)`：如果 `salary` 字段没有空值，计算结果是准确的。
*   `COUNT(department_no)`：如果 `department_no` 字段有空值，该空值对应的计数将为 $0$。

**示例：COUNT(department_no) 演示空值不被计算**

```sql
SELECT
    e.*,
    COUNT(department_no) OVER (PARTITION BY department_no) AS dept_count_by_dept_no
FROM
    employees e;
```

结果示例：对于部门号为 `NULL` 的记录，`COUNT(department_no)` 统计结果为 $0$，因为它不计算 `NULL`。
这不仅限于 `COUNT`，所有聚合函数（如 `SUM`, `AVG` 等）遇到 `NULL` 值时，都会忽略它。

### 4. PARTITION BY 的分区字段

`PARTITION BY` 不仅限于使用部门号，可以使用任何字段进行分区。

*   **单个字段分区：**
    *   例如，使用 `name` 字段分区。如果 `name` 字段唯一（没有重名），那么每条记录都将自成一个分区，分区内的聚合结果就是它自己的值。
    *   `PARTITION BY` 字段可以是姓名、工资、入职时间等。但 `department_no` 是一个比较合适的选择，因为它通常会形成有意义的分组。

*   **多个字段分区：**
    *   `PARTITION BY` 也可以使用两个或更多字段进行组合分区。
    *   语法：`PARTITION BY 字段1, 字段2, ...`
    *   **实际应用示例：房价数据分析**
        *   可以按照 `城市名` 进行分区（如北京、上海）。
        *   还可以进一步增加 `年份` 作为分区字段，例如：`PARTITION BY city_name, year`。这样可以分析北京 $2020$ 年、上海 $2020$ 年、北京 $2021$ 年、上海 $2021$ 年等不同分区的数据，计算各自的平均房价等。
        *   所以，分区字段不一定是一个，可以是多个。

### 5. 无分区（`OVER ()`）

`PARTITION BY` 字段也可以不指定，即 `OVER ()`。
*   语法：`聚合函数() OVER ()`
*   这种情况下，整个表的所有记录会被视为**一个完整的 `PARTITION`**。
*   所有聚合函数将对**整个表**的数据进行计算，并把这个计算结果附加到表中的每一条记录上。
*   这相当于只有一个组，没有多个组。

**示例：对整个表求最小值**

```sql
SELECT
    e.*,
    MIN(salary) OVER () AS overall_min_salary
FROM
    employees e;
```

结果：所有记录的 `overall_min_salary` 字段都会显示整个表中员工的最低工资。

### 6. PARTITION BY 结合 ORDER BY

除了分区，`PARTITION BY` 还可以结合 `ORDER BY` 对分区内的记录进行排序。
*   语法：`聚合函数() OVER (PARTITION BY 分区字段 ORDER BY 排序字段)`
*   `ORDER BY` 仅在**当前分区**内进行排序，而不是对整个表进行排序。
*   **关键点：** 加上 `ORDER BY` 后，聚合函数的值会变成**从分区开始到当前行**的累计统计值。

**示例：计算部门内员工工资的累计平均值 (SQL Server)**

```sql
SELECT
    e.*,
    AVG(salary) OVER (PARTITION BY department_no ORDER BY salary ASC) AS cumulative_avg_salary
FROM
    employees e;
```

结果示例 (部门 $1$ 内部按工资升序排序)：
*   第一条记录（工资最低，如 `$9100$`）：`cumulative_avg_salary` = `$9100$`
*   第二条记录（工资次低，如 `$15000$`）：`cumulative_avg_salary` = (`$9100$` + `$15000$`) / $2$ = `$12050$`
*   第三条记录（工资更高，如 `$21900$`）：`cumulative_avg_salary` = (`$9100$` + `$15000$` + `$21900$`) / $3$ = `$15333.33$`
*   第四条记录（工资最高，如 `$25000$`）：`cumulative_avg_salary` = (`$9100$` + `$15000$` + `$21900$` + `$25000$`) / $4$ = `$17750$`

`2` 号部门和 `3` 号部门也遵循同样的规律。

**示例：计算部门内员工的累计数量 (COUNT)**

```sql
SELECT
    e.*,
    COUNT(salary) OVER (PARTITION BY department_no ORDER BY salary ASC) AS cumulative_count
FROM
    employees e;
```

结果示例 (部门 $1$ 内部按工资升序排序)：
*   第一条记录：`cumulative_count` = $1$
*   第二条记录：`cumulative_count` = $2$
*   第三条记录：`cumulative_count` = $3$
*   第四条记录：`cumulative_count` = $4$

**对比：有无 `ORDER BY` 的区别**
*   **有 `ORDER BY`：** 聚合函数返回的是**从分区开始到当前行**的累计统计值。
*   **无 `ORDER BY`：** 聚合函数返回的是**整个分区**的统计值（分区内的所有记录都相同）。

### 7. PARTITION BY 相关的特定窗口函数

除了聚合函数，`PARTITION BY` 还可以与一些特定的分析函数一起使用。

#### 7.1 `FIRST_VALUE()` 和 `LAST_VALUE()`

*   `FIRST_VALUE(column)`：返回分区内排序后的**第一个值**。
*   `LAST_VALUE(column)`：返回分区内排序后**到当前记录为止的最后一个值**。
    *   注意：`LAST_VALUE` 的默认行为是在当前窗口帧（默认为分区开始到当前行）内计算，所以如果只用 `ORDER BY`，它通常返回当前行自己的值。若想获取分区内的真实最后一个值，需要明确指定窗口帧（如 `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`）。

**示例：查询分区内入职最早和最晚（到目前）的员工入职日期**

```sql
SELECT
    e.*,
    FIRST_VALUE(hire_date) OVER (PARTITION BY department_no ORDER BY hire_date) AS first_hire_date_in_dept,
    LAST_VALUE(hire_date) OVER (PARTITION BY department_no ORDER BY hire_date) AS last_hire_date_to_current
FROM
    employees e;
```

结果示例 (以部门 $1$ 为例，按入职时间排序)：
*   第一条记录：`first_hire_date_in_dept` = `2008-01-01` (部门最早)；`last_hire_date_to_current` = `2008-01-01` (当前记录)
*   第二条记录：`first_hire_date_in_dept` = `2008-01-01`；`last_hire_date_to_current` = `2009-01-01` (当前记录)
*   第三条记录：`first_hire_date_in_dept` = `2008-01-01`；`last_hire_date_to_current` = `2013-01-01` (当前记录)
*   第四条记录：`first_hire_date_in_dept` = `2008-01-01`；`last_hire_date_to_current` = `2015-01-01` (当前记录)

**实际应用场景：**
*   了解某个分区（如捐款项目）中的最低捐款额和最高捐款额（到目前为止）。

#### 7.2 `LEAD()` 和 `LAG()`

这两个是基于 `PARTITION BY` 和 `ORDER BY` 的分析函数，用于查找当前记录的**上一条**或**下一条**记录的值。

*   `LAG(column, offset, default_value)`：
    *   `column`：要查找的列名。
    *   `offset`：偏移量，表示要往前（上一条）多少行，默认是 $1$。
    *   `default_value`：如果超出分区边界（没有上一条记录），返回的默认值，默认为 `NULL`。
    *   作用：返回当前行**前**第 `offset` 行的 `column` 值。

*   `LEAD(column, offset, default_value)`：
    *   `column`：要查找的列名。
    *   `offset`：偏移量，表示要往后（下一条）多少行，默认是 $1$。
    *   `default_value`：如果超出分区边界（没有下一条记录），返回的默认值，默认为 `NULL`。
    *   作用：返回当前行**后**第 `offset` 行的 `column` 值。

**示例：查询员工的上一条和下一条入职时间**

```sql
SELECT
    e.*,
    LAG(hire_date, 1, NULL) OVER (PARTITION BY department_no ORDER BY hire_date) AS prev_hire_date,
    LEAD(hire_date, 1, NULL) OVER (PARTITION BY department_no ORDER BY hire_date) AS next_hire_date
FROM
    employees e;
```

结果示例 (以部门 $1$ 为例，按入职时间排序)：
*   第一条记录 (`2008-01-01`)：`prev_hire_date` 为 `NULL` (没有上一条)；`next_hire_date` 为 `2009-01-01`
*   第二条记录 (`2009-01-01`)：`prev_hire_date` 为 `2008-01-01`；`next_hire_date` 为 `2013-01-01`
*   ...
*   最后一条记录 (`2015-01-01`)：`prev_hire_date` 为 `2013-01-01`；`next_hire_date` 为 `NULL` (没有下一条)

**实际应用场景：**
*   **计算网站活跃用户数：** 通过 `LEAD` 和 `LAG` 计算用户两次登录之间的时间差。如果时间差小于 $1$ 个月，则可认为是活跃用户。
    *   `DATEDIFF(next_login_date, current_login_date)` 或 `DATEDIFF(current_login_date, prev_login_date)`。

### 8. PARTITION BY 的序号函数 (Rank Functions)

`PARTITION BY` 不仅对数据分组和排序，还可以返回记录在分区内的序号。有三种常用的序号函数：`RANK()`, `ROW_NUMBER()`, `DENSE_RANK()`。它们在处理相同值时的序号生成规则不同。

#### 8.1 `RANK()` 函数

*   功能：为分区内的每条记录返回其排序后的序号。
*   语法：`RANK() OVER (PARTITION BY 分区字段 ORDER BY 排序字段)`

**示例：查询员工在部门内的工资排名**

```sql
SELECT
    e.*,
    RANK() OVER (PARTITION BY department_no ORDER BY salary DESC) AS salary_rank_in_dept
FROM
    employees e;
```

结果示例 (部门 $1$)：
*   员工 $A$ (工资 `$25000$`): rank $1$
*   员工 $B$ (工资 `$21900$`): rank $2$
*   员工 $C$ (工资 `$15000$`): rank $3$
*   员工 $D$ (工资 `$9100$`): rank $4$

**`RANK()` 处理并列值的情况：**
*   如果存在相同值（并列），`RANK()` 会为这些相同值分配**相同的序号**。
*   然后，它会**跳过**后续的序号。

**示例：修改数据，使两条记录工资相同（假设 $1$ 号部门有两人工资都为 `$15000$`）**

```sql
-- 假设已执行 UPDATE employees SET salary = $15000$ WHERE employee_id = ... (使某人与另一人工资相同)
SELECT
    e.*,
    RANK() OVER (PARTITION BY department_no ORDER BY salary DESC) AS salary_rank_in_dept
FROM
    employees e;
```

结果示例 (部门 $1$ 假设工资为 `$25000, 21900, 15000, 15000, 9100$` (共 $5$ 人))：
*   工资 `$25000$`：`salary_rank_in_dept` = $1$
*   工资 `$21900$`：`salary_rank_in_dept` = $2$
*   工资 `$15000$`：`salary_rank_in_dept` = $3$
*   工资 `$15000$`：`salary_rank_in_dept` = $3$
*   工资 `$9100$`：`salary_rank_in_dept` = $5$ (跳过了 $4$ 号)

#### 8.2 `ROW_NUMBER()` 函数

*   功能：为分区内的每条记录返回一个**唯一的、连续的序号**。
*   特点：即使排序值相同，`ROW_NUMBER()` 也会给它们分配不同的序号（通常是根据内部的某种顺序，如插入顺序或物理存储顺序）。
*   语法：`ROW_NUMBER() OVER (PARTITION BY 分区字段 ORDER BY 排序字段)`

**示例：使用 `ROW_NUMBER()` 处理并列工资**

```sql
SELECT
    e.*,
    ROW_NUMBER() OVER (PARTITION BY department_no ORDER BY salary DESC) AS salary_row_num
FROM
    employees e;
```

结果示例 (部门 $1$ 假设工资为 `$25000, 21900, 15000, 15000, 9100$` (共 $5$ 人))：
*   工资 `$25000$`：`salary_row_num` = $1$
*   工资 `$21900$`：`salary_row_num` = $2$
*   工资 `$15000$`：`salary_row_num` = $3$
*   工资 `$15000$`：`salary_row_num` = $4$
*   工资 `$9100$`：`salary_row_num` = $5$

#### 8.3 `DENSE_RANK()` 函数

*   功能：为分区内的每条记录返回其排序后的序号。
*   特点：
    *   当存在相同值时，`DENSE_RANK()` 会为这些相同值分配**相同的序号**（并列）。
    *   但它**不会跳过**后续的序号，而是紧密地（dense）分配下一个序号。
*   语法：`DENSE_RANK() OVER (PARTITION BY 分区字段 ORDER BY 排序字段)`

**示例：使用 `DENSE_RANK()` 处理并列工资**

```sql
SELECT
    e.*,
    DENSE_RANK() OVER (PARTITION BY department_no ORDER BY salary DESC) AS salary_dense_rank
FROM
    employees e;
```

结果示例 (部门 $1$ 假设工资为 `$25000, 21900, 15000, 15000, 9100$` (共 $5$ 人))：
*   工资 `$25000$`：`salary_dense_rank` = $1$
*   工资 `$21900$`：`salary_dense_rank` = $2$
*   工资 `$15000$`：`salary_dense_rank` = $3$
*   工资 `$15000$`：`salary_dense_rank` = $3$
*   工资 `$9100$`：`salary_dense_rank` = $4$ (没有跳过 $4$ 号)

**总结三种序号函数的区别：**

| 函数       | 值相同时的序号 | 后续序号是否跳过 | 举例 ($1, 1, 2, 3$) |
| :--------- | :------------- | :--------------- | :------------------ |
| `RANK()`   | 相同           | 跳过             | $1, 1, 3, 4$        |
| `ROW_NUMBER()` | 不同           | 不跳过           | $1, 2, 3, 4$        |
| `DENSE_RANK()` | 相同           | 不跳过           | $1, 1, 2, 3$        |

### 9. PARTITION BY 序号函数应用案例 (重要考点)

**案例：查询每个部门工资最高的员工信息**

**首次尝试 (错误示例):**
思路：使用 `RANK()` 为员工排名，然后通过 `WHERE` 条件筛选 `rank = 1`。

```sql
SELECT
    e.*,
    RANK() OVER (PARTITION BY department_no ORDER BY salary DESC) AS sal_rank_no
FROM
    employees e
WHERE
    sal_rank_no = 1; -- 错误！
```

**执行结果：** 报错，提示别名 `sal_rank_no` 无效。

**错误原因解释 (重要考点)：**
SQL 的执行顺序决定了此错误。`WHERE` 条件是在 `PARTITION BY` 窗口函数执行**之前**进行处理的。在 `WHERE` 条件执行时，`sal_rank_no` 这个别名还没有被生成，所以无法识别。这与 `GROUP BY` 后面不能直接用 `WHERE` 筛选聚合函数结果（需要用 `HAVING`）是类似的逻辑。然而，`PARTITION BY` 后面并没有 `HAVING` 这样的子句。

**解决方案：使用子查询**
将包含 `PARTITION BY` 窗口函数的查询结果作为一个临时表（或子查询），然后在外层查询中对这个临时表进行筛选。

```sql
SELECT
    e.*
FROM
    (
        SELECT
            *, -- 或者 e.*, RANK(...) AS sal_rank_no 明确列出
            RANK() OVER (PARTITION BY department_no ORDER BY salary DESC) AS sal_rank_no
        FROM
            employees
    ) AS e
WHERE
    e.sal_rank_no = 1;
```

**执行结果：** 成功。这会返回每个部门中工资最高的员工的所有信息。
*   通过这种方式，我们可以在 `FROM` 子句中生成一个包含 `sal_rank_no` 字段的临时表，然后在外部查询中，该字段已经存在，就可以在 `WHERE` 条件中进行筛选了。
*   这个例子中查询的是序号为 $1$ 的（最高工资），同样也可以查询序号为 $2$ 的、序号为 $3$ 的等等。

## 🎯 总结 (PPT 知识点回顾)

`PARTITION BY` 是一个功能强大的分析函数，主要有两大功能：

1.  **支持分组后的聚合函数：**
    *   例如 `SUM`, `COUNT`, `MAX`, `MIN`, `AVG`。
    *   与 `GROUP BY` 类似，但核心区别在于 `PARTITION BY` 会为分组内的**每一条记录**都返回其对应的聚合函数的统计值，而 `GROUP BY` 只是为每个组返回**一条**记录。
    *   如果**不加 `ORDER BY`**，它会返回所有记录所在分区的聚合函数的统计值（分区内相同）。
    *   如果**加上 `ORDER BY`**，它会返回从分区开始到当前行的累计统计值。

2.  **支持分组内的排序和返回序号：**
    *   与普通的 `ORDER BY` 类似，但它仅对**分组（分区）内部**的记录进行排序，而不是对整个符合条件的记录进行排序。
    *   它还可以返回记录在分区内的序号（`RANK`, `ROW_NUMBER`, `DENSE_RANK`），这是普通 `ORDER BY` 无法做到的。

### `PARTITION BY` 支持的传统聚合函数

*   支持 `SUM`, `MAX`, `MIN`, `AVG`, `COUNT`。
*   不加 `ORDER BY`：返回所有记录所在分区的聚合函数统计值，每条记录都会返回。
*   加上 `ORDER BY`：返回从分区开始到当前行的累计统计值。

### `PARTITION BY` 支持的特定分析函数

*   **`FIRST_VALUE(column)`:** 返回分区内排序后的第一个值。
*   **`LAST_VALUE(column)`:** 返回分区内排序后到当前行的最后一个值。

*   **`LAG(column, offset, default_value)`:** 返回当前记录前 `offset` 行的 `column` 值。
    *   `offset` 默认是 $1$。
    *   `default_value` 默认是 `NULL` (超出窗口时)。
*   **`LEAD(column, offset, default_value)`:** 返回当前记录后 `offset` 行的 `column` 值。
    *   `offset` 默认是 $1$。
    *   `default_value` 默认是 `NULL` (超出窗口时)。

### `PARTITION BY` 的序号函数

这三个序号函数在处理相同值时返回的序号规则不同：

1.  **`RANK()`:**
    *   最常用。
    *   相同值返回相同序号。
    *   **跳过**后续序号。
    *   例如：$1, 1, 3$ (跳过 $2$)。
2.  **`ROW_NUMBER()`:**
    *   即使排序值相同，也返回**不同**的、连续的序号。
    *   例如：$1, 2, 3$。
3.  **`DENSE_RANK()`:**
    *   相同值返回相同序号。
    *   **不跳过**后续序号，序号是连续的。
    *   例如：$1, 1, 2$ (不跳过)。

### 案例回顾：查询每个部门工资最高的员工信息

*   通过 `RANK()` 函数为每条记录返回一个序号。
*   **错误做法：** 在 `WHERE` 条件中直接判断该序号（`WHERE sal_rank_no = 1`）。原因在于 `WHERE` 条件在序号生成前执行。
*   **正确做法：** 将 `PARTITION BY` 查询的结果作为子查询放入 `FROM` 子句中，形成一个临时表。然后对这个临时表进行 `WHERE` 条件判断。
*   这个例子不仅可以查询序号为 $1$ 的（最高），也可以查询序号为 $2$ 的、 $3$ 的等。

## 📝 练习

**练习题目：查询每个部门第二位入职的员工的信息**

**预期结果示例：**

```
employee_id | name | department_no | salary | hire_date  | rank_date
------------+------+---------------+--------+------------+----------
$105$       | E    | $1$           | $15000$| $2009-01-01$| $2$
$203$       | F    | $2$           | $9700$ | $2010-01-01$| $2$
```
*(注意：这个结果中没有 $3$ 号部门的记录。)*

**思考与解答提示：**
*   您需要使用 `PARTITION BY department_no ORDER BY hire_date` 来对每个部门的员工按入职时间进行排序。
*   然后使用一个序号函数来找出第二位入职的员工。
*   记住前面案例中 `WHERE` 条件筛选窗口函数结果的方法。

**为什么 $3$ 号部门没有记录？**
在 $3$ 号部门中，有两名员工是同时入职的。如果使用 `RANK()` 函数进行排序，他们两人的序号都将是 $1$（并列第一）。由于查询条件是寻找序号为 $2$ 的员工，因此在 $3$ 号部门中找不到符合条件的记录。这正是 `RANK()` 函数在处理并列值时会跳过后续序号的特点的体现。

将本节所讲的知识点弄清楚，特别是前面查询工资最高员工的例子，稍微修改一下就可以解决这个练习题。请先自己尝试完成。
```