Create table If Not Exists Employee (Id int, Name varchar(255), Department varchar(255), ManagerId int)
Truncate table Employee
insert into Employee (Id, Name, Department, ManagerId) values ('101', 'John', 'A', 'None')
insert into Employee (Id, Name, Department, ManagerId) values ('102', 'Dan', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('103', 'James', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('104', 'Amy', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('105', 'Anne', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('106', 'Ron', 'B', '101')

+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+

Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:

+-------+
| Name  |
+-------+
| John  |
+-------+
Note:
No one would report to himself.

1. direct reports - ManagerID - group by the same 

|ManagerId| count of unique Id
2. >= 5
3. select the name


WITH Managers AS (
SELECT ManagerId, COUNT (DISTINCT Id)AS Direct_reports
FROM Employee
GROUP BY ManagerId
HAVING Direct_reports >= 5)

SELECT em.Name
FROM Employee em, Managers ma
WHERE em.Id = ma.ManagerId


OTHER SOLUTIONS:
> beats 44%
select a.name from
employee a join
employee b
on a.id = b.managerid
group by a.name
having count(*) >=5

> fast solutions
SELECT Name
FROM EMPLOYEE
WHERE Id in (
SELECT ManagerID
FROM EMPLOYEE
WHERE ManagerID IS NOT NULL
GROUP BY ManagerId
HAVING COUNT(ManagerID) >= 5
);






