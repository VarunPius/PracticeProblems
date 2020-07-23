Create table If Not Exists Scores (Id int, Score DECIMAL(3,2));
Truncate table Scores;
insert into Scores (Id, Score) values ('1', '3.5');
insert into Scores (Id, Score) values ('2', '3.65');
insert into Scores (Id, Score) values ('3', '4.0');
insert into Scores (Id, Score) values ('4', '3.85');
insert into Scores (Id, Score) values ('5', '4.0');
insert into Scores (Id, Score) values ('6', '3.65');

SELECT
    s.Score,
    Count(t.Score) as rank
from
    (select distinct score from scores) t,
    scores s
where
    s.score <= t.score
group by s.id, s.score
order by rank;

SELECT
    score,
    (SELECT COUNT(*)
     FROM (SELECT DISTINCT score s FROM Scores) tmp where s>=score) as Rank
FROM scores
ORDER BY Rank;

Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, ManagerId int);
Truncate table Employee;
insert into Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3');
insert into Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4');
insert into Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', NULL);
insert into Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', NULL);

SELECT
    e1.Name as Employee
FROM
    Employee e1 LEFT JOIN Employee e2 ON e1.ManagerID = e2.ID
WHERE
    e1.Salary > e2.Salary;

SELECT
    *
FROM
    Employee e1 LEFT JOIN Employee e2 ON e1.ManagerID = e2.ID
WHERE
    e1.Salary > e2.Salary;

SELECT
    *
FROM
    Employee e1 JOIN Employee e2 ON e1.ManagerID = e2.ID


{"headers": {"courses": ["student", "class"]},
"rows": {"courses": [
["A", "Math"],
["B", "English"],
["C", "Math"],
["D", "Biology"],
["E", "Math"],
["F", "Math"],
["A", "Math"]]}}
