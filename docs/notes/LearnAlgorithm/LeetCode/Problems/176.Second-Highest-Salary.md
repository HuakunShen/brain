# 176. Second Highest Salary

https://leetcode.com/problems/second-highest-salary/

Level: Medium

[Official Solution Available](https://leetcode.com/problems/second-highest-salary/solution/)

## Solution

`LIMIT 1 OFFSET 1` should work, but doesn't pass the edge case where the total number of rows is lower than 2.

```sql
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
```

If total number of rows is lower than 2, the result will be empty, but the question expects a null instead.

- Input: `{"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100]]}}`
- Output: `{"headers": ["SecondHighestSalary"], "values": []}`
- Expected: `{"headers": ["SecondHighestSalary"], "values": [[null]]}`

SQL subquery or `IFNULL` keyword could fix the problem.

```sql
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary;

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;
```