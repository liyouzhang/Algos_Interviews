'''
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

'''
-- 20200414
-- only 1 table, the output is 1 column with 1 row

-- TRY ONE 
-- i can use the ranking function where I filter on rank = 2 
-- there is probably an easier way that calculates faster 
select 
    salary as SecondHighestSalary
from (
    select 
        Salary
        , Rank() Over (order by Salary) as ranks 
    from Employee e 
) t 
where 1=1 
    and ranks = 2 

-- TRY TWO
-- try without using windows function
-- assume no duplicates account

with t1 as (
    select 
        Salary
    from Employee e 
    order by Salary 
    limit 2 
)

select 
    salary
from t1 
order by salary DESC 
limit 1 


-- solution
-- TRY TWO didn't consider edge cases where there is only 1 row. 
-- then my answer returns null 
-- need to clarify in interviews 
-- also I put the DESC in the wrong place

-- to overcome the null issue when there is only 1 row, put it as a subquery
-- or, ifnull()
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
