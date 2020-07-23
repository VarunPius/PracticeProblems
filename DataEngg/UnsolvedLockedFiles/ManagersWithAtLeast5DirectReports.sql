/*
Create table If Not Exists Employee (Id int, Name varchar(255), Department varchar(255), ManagerId int)
Truncate table Employee
insert into Employee (Id, Name, Department, ManagerId) values ('101', 'John', 'A', 'None')
insert into Employee (Id, Name, Department, ManagerId) values ('102', 'Dan', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('103', 'James', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('104', 'Amy', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('105', 'Anne', 'A', '101')
insert into Employee (Id, Name, Department, ManagerId) values ('106', 'Ron', 'B', '101')
*/
/*
570. Managers with at Least 5 Direct Reports
Medium
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

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

*/

/*
Leetcode solution:
Approach: Using JOIN and a temporary table [Accepted]

Algorithm

First, we can get the Id of the manager having more than 5 direct reports just using this ManagerId column.

Then, we can get the name of this manager by join that table with the Employee table.

MySQL

SELECT
    Name
FROM
    Employee AS t1 JOIN
    (SELECT
        ManagerId
    FROM
        Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) AS t2
    ON t1.Id = t2.ManagerId
;
*/

select name from employee
where id in
(select managerId from Employee
group by managerId
having count(managerId)>=5) ;

select name
from Employee e,
(   select ManagerId
    from Employee
    group by ManagerId having count(*)>4
) as m
where e.id = m.ManagerId;
