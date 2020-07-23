/*
Question:

Medium

Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/

# Solution:
-- Using Function:

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N-1;
  RETURN (
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET N
  );
END


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
    # Write your MySQL query statement below.
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT N,1 );
    -- LIMIT offset, row_count : offset removes first x rows and rowcount selects y rows after that;
    -- here remove N rows and select 1 row
END

-- MySQL:
SELECT Salary FROM Employee
ORDER BY Salary DESC LIMIT n-1,1

--Oracle:
SELECT * FROM (
    SELECT Emp.*,
        ROW_NUMBER() OVER (ORDER BY Salary DESC) rownumb
    FROM Employee Emp
    )
where rownumb = n;  /*n is nth highest salary*/

SELECT * FROM (
    SELECT EmployeeID, Salary
        ,RANK() OVER (ORDER BY Salary DESC) ranking
    FROM Employee
    )
WHERE ranking = N;


-- This SQL to find the Nth highest salary should work in SQL Server, MySQL, DB2, Oracle, Teradata, and almost any other RDBMS:
-- (note: low performance because of subquery)
SELECT *                    /*This is the outer query part */
FROM Employee Emp1
WHERE (N-1) = (             /* Subquery starts here */
    SELECT COUNT(DISTINCT(Emp2.Salary))
    FROM Employee Emp2
    WHERE Emp2.Salary > Emp1.Salary);

-- The most important thing to understand in the query above is that the subquery is evaluated each and every time a row is processed by the outer query.
-- In other words, the inner query can not be processed independently of the outer query since the inner query uses the Emp1 value as well.
-- In order to find the Nth highest salary, we just find the salary that has exactly N-1 salaries greater than itself.


/* SQL Server TOP solution
SELECT TOP 1 Salary
FROM (
      SELECT DISTINCT TOP N Salary
      FROM Employee
      ORDER BY Salary DESC
      ) AS Emp
ORDER BY Salary

//2nd highest salary example
SELECT Id, Salary
FROM Employee e
WHERE 2=(SELECT COUNT(DISTINCT Salary) FROM Employee p
WHERE e.Salary<=p.Salary);
*/

/*SQL Server without TOP Keyword
SELECT Salary FROM Employee
ORDER BY Salary DESC OFFSET N-1 ROW(S)
FETCH FIRST ROW ONLY
*/


