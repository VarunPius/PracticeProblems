/*
SQL Schema:
Create table If Not Exists Employee (Id int, Company varchar(255), Salary int)
Truncate table Employee
insert into Employee (Id, Company, Salary) values ('1', 'A', '2341')
insert into Employee (Id, Company, Salary) values ('2', 'A', '341')
insert into Employee (Id, Company, Salary) values ('3', 'A', '15')
insert into Employee (Id, Company, Salary) values ('4', 'A', '15314')
insert into Employee (Id, Company, Salary) values ('5', 'A', '451')
insert into Employee (Id, Company, Salary) values ('6', 'A', '513')
insert into Employee (Id, Company, Salary) values ('7', 'B', '15')
insert into Employee (Id, Company, Salary) values ('8', 'B', '13')
insert into Employee (Id, Company, Salary) values ('9', 'B', '1154')
insert into Employee (Id, Company, Salary) values ('10', 'B', '1345')
insert into Employee (Id, Company, Salary) values ('11', 'B', '1221')
insert into Employee (Id, Company, Salary) values ('12', 'B', '234')
insert into Employee (Id, Company, Salary) values ('13', 'C', '2345')
insert into Employee (Id, Company, Salary) values ('14', 'C', '2645')
insert into Employee (Id, Company, Salary) values ('15', 'C', '2645')
insert into Employee (Id, Company, Salary) values ('16', 'C', '2652')
insert into Employee (Id, Company, Salary) values ('17', 'C', '65')
*/

/*
569. Median Employee Salary
Hard
The Employee table holds all employees. The employee table has three columns: Employee Id, Company Name, and Salary.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|1    | A          | 2341   |
|2    | A          | 341    |
|3    | A          | 15     |
|4    | A          | 15314  |
|5    | A          | 451    |
|6    | A          | 513    |
|7    | B          | 15     |
|8    | B          | 13     |
|9    | B          | 1154   |
|10   | B          | 1345   |
|11   | B          | 1221   |
|12   | B          | 234    |
|13   | C          | 2345   |
|14   | C          | 2645   |
|15   | C          | 2645   |
|16   | C          | 2652   |
|17   | C          | 65     |
+-----+------------+--------+

Write a SQL query to find the median salary of each company. Bonus points if you can solve it without using any built-in SQL functions.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|5    | A          | 451    |
|6    | A          | 513    |
|12   | B          | 234    |
|9    | B          | 1154   |
|14   | C          | 2645   |
+-----+------------+--------+
*/


/*
Solution:
Solution 1:

Inspired by @yauheni
https://leetcode.com/problems/find-median-given-frequency-of-numbers/discuss/102710/Easy-peasy

SELECT
  id,
  Company,
  Salary
FROM Employee e
WHERE 1 >= ABS((SELECT COUNT(*) FROM Employee e1 WHERE e.company = e1.company AND e.Salary >= e1.Salary) -
           (SELECT COUNT(*) FROM Employee e2 WHERE e.company = e2.company AND e.Salary <= e2.Salary))
GROUP BY Company, Salary

SOLUTION 2:

Sort + @rank column and then SELECT the median

SELECT
  sub.Id,
  sub.Company,
  sub.Salary
FROM (
    SELECT
        @rank := IF(@lastCompany = e.Company, @rank + 1, 1) as Rank,
        e.id,
        e.company,
        e.salary,
        fre.tot,
        @lastCompany := e.company
    FROM (SELECT @rank := 0, @lastCompany := 'A') SQLvars, Employee e
    LEFT JOIN ( SELECT e1.company, count(*) as tot FROM Employee e1 GROUP BY e1.company ) fre ON fre.company = e.company
    ORDER BY e.Company, e.Salary
) sub
WHERE sub.rank = sub.tot DIV 2 + 1 OR (sub.tot % 2 = 0 AND sub.rank = sub.tot DIV 2)
*/

/*
SELECT Id, Company, Salary
FROM (
SELECT *, ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary ASC, Id ASC) AS RN_ASC,
ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary DESC, Id DESC) AS RN_DESC
FROM Employee) AS temp
WHERE RN_ASC BETWEEN RN_DESC - 1 AND RN_DESC + 1
ORDER BY Company, Salary;
*/

/*
Leetcode Solution:
Approach #1: Using the definition of median [Accepted]

Intuition

By the definition of median, the count of the bigger numbers than itself should be equal to the count of the smaller ones in an odd array.

Algorithm

Take array [1,3,2] for example, is the first number 1 the median? No, because this array only have 3 elements but there are 2 of them (3, 2) are greater than 1. To continue, we know 3 is not the median as well since there are 2 elements smaller. But for the last element 2, there are equal amount of bigger and smaller numbers. So it is the median in this array!

What if an array has even amount of distinct values, the median is the average of the middle two elements next to each other after sorting this array. It is not hard to understand that for either of these two elements, the difference (absolute value) of its bigger and smaller number than itself in this array is 1, which is the exactly frequency of a element in the distinct array.

So in general, the median's frequency should be equal or grater than the absolute difference of its bigger elements and small ones in an array no matter whether it has odd or even amount of numbers and whether they are distinct. This rule is the key, and it is represented as the following code.

SUM(CASE
    WHEN Employee.Salary = alias.Salary THEN 1
    ELSE 0
END) >= ABS(SUM(SIGN(Employee.Salary - alias.Salary)))

Thus, this approach is as following in MySQL code.

MySQL

SELECT
    Employee.Id, Employee.Company, Employee.Salary
FROM
    Employee,
    Employee alias
WHERE
    Employee.Company = alias.Company
GROUP BY Employee.Company , Employee.Salary
HAVING SUM(CASE
    WHEN Employee.Salary = alias.Salary THEN 1
    ELSE 0
END) >= ABS(SUM(SIGN(Employee.Salary - alias.Salary)))
ORDER BY Employee.Id
;

    Note: In MySQL 5.6, this code runs fine, but if you are using MySQL 5.7+, please use ANY_VALUE(Employee.Id) instead of Employee.Id in the SELECT statement. Otherwise, you may encouter the following error message: Error Code: 1055. Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'Employee.Id' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by. For more details on how to user ANY_VALUE(arg), please refer to this link.

Approach #2: Sort and then select the median [Accepted]

Intuition

In general, we can just pick the middle one(s) to get the median if the records are ranked by salary. But how can we get them sorted particularly MySQL does not have the build-in rank function, and these are several companies in this case.

Algorithm

By adding a virtual column to simulate the ranking, we can sort these records by salary and pick up the middle one(s). Here we need to use the session variable to achieve this goal.

This approach is more efficient than the first one since it does not calculate all the salary one by one in the table.

SELECT
    Id, Company, Salary
FROM
    (SELECT
        e.Id,
            e.Salary,
            e.Company,
            IF(@prev = e.Company, @Rank:=@Rank + 1, @Rank:=1) AS rank,
            @prev:=e.Company
    FROM
        Employee e, (SELECT @Rank:=0, @prev:=0) AS temp
    ORDER BY e.Company , e.Salary , e.Id) Ranking
        INNER JOIN
    (SELECT
        COUNT(*) AS totalcount, Company AS name
    FROM
        Employee e2
    GROUP BY e2.Company) companycount ON companycount.name = Ranking.Company
WHERE
    Rank = FLOOR((totalcount + 1) / 2)
        OR Rank = FLOOR((totalcount + 2) / 2)
;
*/
