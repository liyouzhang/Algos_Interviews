'''
Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.

Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table.

 

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

The query result format is in the following example:

Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

Result table:
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50

'''

-- group by project, average years to two decimles
-- first join the table so project table has employee years 
-- then aggaregate to project level 

select 
    project_id
    , round(avg(experience_years),2) as average_years
from project p 
join employee e 
    on p.employee_id = e.employee_id
group by project_id

'''
Write an SQL query that reports all the projects that have the most employees.
Result table:
+-------------+
| project_id  |
+-------------+
| 1           |
+-------------+
'''

-- only need the project table
-- aggregate to project level, and count distinct employee_id per project 
-- since it is to return all the projects when there is a match
-- I can use join tables at last to return all

with project_cnt as (
    select 
        project_id
        , count (distinct employee_id) as num_employees
    from project p 
    group by 1 
),

max_num as (
    select 
        num_employees
    from project_cnt
    order by 2 DESC
    limit 1
)
select 
    distinct project_id
from max_num mn 
join project_cnt pc 
    on mx.num_employees = pc.num_employees

-- not sure if it right because of syntax 

-- another solution: use windows function where i can use rank or dense_rank 
with project_cnt as (
    select 
        project_id
        , count (distinct employee_id) as num_employees
    from project p 
    group by 1 
),

ranks as (
select 
    project_id
    , rnak()over(order by num_employees DESC) as ranks 
from project_cnt
)

select 
    project_id 
from ranks 
where ranks = 1 

-- optimizaiton: I can put "count (distinct employee_id) as num_employees" directly in the ranks CTE
-- , rnak()over(order by (count (distinct employee_id)) DESC) as ranks 

'''
Write an SQL query that reports the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.
Result table:
+-------------+---------------+
| project_id  | employee_id   |
+-------------+---------------+
| 1           | 1             |
| 1           | 3             |
| 2           | 1             |
+-------------+---------------+
Both employees with id 1 and 3 have the most experience among the employees of the first project. For the second project, the employee with id 1 has the most experience.
'''

-- I will need to join table so each project employee has years info
-- then I will have to use windows function to rank years of experience partition by each project 
-- lastly, I will limit to ranks = 1 
with t1 as (
    select 
        project_id
        , employee_id
        , experience_years
    from project p 
    join employee e 
        on p.employee_id  = e.employee_id 
),

t2 as (
    select 
        project_id
        , employee_id 
        , ranks()over (partition by project_id order by experience_years DESC) as ranks 
    from t1
)

select 
    project_id
    , employee_id
from t2 
where 1=1
     and ranks = 1 
group by 1,2 
order by 1 

