/*
Create table If Not Exists Employee (EmpId int, Name varchar(255), Supervisor int, Salary int)
Create table If Not Exists Bonus (EmpId int, Bonus int)
Truncate table Employee
insert into Employee (EmpId, Name, Supervisor, Salary) values ('3', 'Brad', 'None', '4000')
insert into Employee (EmpId, Name, Supervisor, Salary) values ('1', 'John', '3', '1000')
insert into Employee (EmpId, Name, Supervisor, Salary) values ('2', 'Dan', '3', '2000')
insert into Employee (EmpId, Name, Supervisor, Salary) values ('4', 'Thomas', '3', '4000')
Truncate table Bonus
insert into Bonus (EmpId, Bonus) values ('2', '500')
insert into Bonus (EmpId, Bonus) values ('4', '2000')
*/

/*
577. Employee Bonus
Easy

Select all employee's name and bonus whose bonus is < 1000.

Table:Employee

+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+
empId is the primary key column for this table.

Table: Bonus

+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
empId is the primary key column for this table.

Example ouput:

+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+

*/

/*
Solution:

Approach: Using OUTER JOIN and WHERE clause [Accepted]

Intuition

Join table Employee with Bonus and then use WHERE clause to get the required records.

Algorithm

Since foreign key Bonus.empId refers to Employee.empId and some employees do not have bonus records, we can use OUTER JOIN to link these two tables as the first step.

SELECT
    Employee.name, Bonus.bonus
FROM
    Employee
        LEFT OUTER JOIN
    Bonus ON Employee.empid = Bonus.empid
;

    Note: "LEFT OUTER JOIN" could be written as "LEFT JOIN".

The output to run this code with the sample data is as below.

| name   | bonus |
|--------|-------|
| Dan    | 500   |
| Thomas | 2000  |
| Brad   |       |
| John   |       |

The bonus value for 'Brad' and 'John' is empty, which is actually NULL in the database. "Conceptually, NULL means “a missing unknown value” and it is treated somewhat differently from other values." Check the Working with NULL Values in MySQL manual for more details. In addition, we have to use IS NULL or IS NOT NULL to compare a value with NULL.

At last, we can add a WHERE clause with the proper conditions to filter these records.

MySQL

SELECT
    Employee.name, Bonus.bonus
FROM
    Employee
        LEFT JOIN
    Bonus ON Employee.empid = Bonus.empid
WHERE
    bonus < 1000 OR bonus IS NULL
;

*/