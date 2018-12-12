The Employee table holds the salary information in a year.

Write a SQL to get the cumulative sum of an employee's salary over a period of 3 months but exclude the most recent month.

The result should be displayed by 'Id' ascending, and then by 'Month' descending.

Example
Input

| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
Output

| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
Explanation
Employee '1' has 3 salary records for the following 3 months except the most recent month '4': salary 40 for month '3', 30 for month '2' and 20 for month '1'
So the cumulative sum of salary of this employee over 3 months is 90(40+30+20), 50(30+20) and 20 respectively.

| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
Employee '2' only has one salary record (month '1') except its most recent month '2'.
| Id | Month | Salary |
|----|-------|--------|
| 2  | 1     | 20     |
Employ '3' has two salary records except its most recent pay month '4': month '3' with 60 and month '2' with 40. So the cumulative salary is as following.
| Id | Month | Salary |
|----|-------|--------|
| 3  | 3     | 100    |
| 3  | 2     | 40     |


> Liyou:

1. windows function - SUM(), partition by Id and order by month rolling sum
2. exclude the last month for each Id
3. limit the history to last 4 months for each id
4. end: order by id ascending, by 'month" descending

SELECT Id, Month, Salary
FROM
(SELECT Id, Month, SUM(Salary)OVER(PARTITION BY Id ORDER BY Month) AS Salary, MAX(Month)OVER(PARTITION BY Id) AS current_month
FROM Employee) Master
WHERE Month IN (current_month-1, current_month-2, current_month-3)
ORDER BY 1, 2 DESC
;


**Not sure if my solution is right because leetcode doesn't support WINDOWS FUNCTION**

> leetcode solutions:

SELECT
    E1.id,
    E1.month,
    (IFNULL(E1.salary, 0) + IFNULL(E2.salary, 0) + IFNULL(E3.salary, 0)) AS Salary
FROM
    (SELECT
        id, MAX(month) AS month
    FROM
        Employee
    GROUP BY id
    HAVING COUNT(*) > 1) AS maxmonth
        LEFT JOIN
    Employee E1 ON (maxmonth.id = E1.id
        AND maxmonth.month > E1.month)
        LEFT JOIN
    Employee E2 ON (E2.id = E1.id
        AND E2.month = E1.month - 1)
        LEFT JOIN
    Employee E3 ON (E3.id = E1.id
        AND E3.month = E1.month - 2)
ORDER BY id ASC , month DESC
;