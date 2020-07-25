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

-----------------------------------------------------------------

SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop=53

SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON a.company=b.company
    JOIN stops s ON a.stop = s.id and b.
WHERE a.stop=53

SELECT x.company, x.num, x.name, y.name
FROM
(SELECT a.company, a.num, a.stop, s.name
FROM route a JOIN stops s ON a.stop = s.id) x,
(SELECT b.company, b,num, b.stop, s.name
FROM route b JOIN stops s ON b.stop = s.id) y
where
x.name = 'Craiglockhart'
and y.name = 'London Road';

SELECT x.company, x.num, x.name, y.name
FROM
(SELECT a.company, a.num, a.stop, s.name
FROM route a JOIN stops s ON a.stop = s.id) x,
(SELECT b.company, b.num, b.stop, s.name
FROM route b JOIN stops s ON b.stop = s.id) y
where
x.company = y.company
and x.num = y.num
and x.name = 'Craiglockhart'
and y.name = 'London Road';

SELECT r1.company, r1.num, s1.name, s2.name
FROM
route r1 JOIN stops s1 ON s1.id = r1.stop
JOIN route r2 ON r1.company = r2.company and r1.num = r2.num
JOIN stops s2 ON s2.id = r2.stop
and s1.name = 'Craiglockhart'
and s2.name = 'London Road';

SELECT r1.company, r1.num , r1.stop, r2.stop
FROM
route r1 JOIN route r2 ON r1.company = r2.company and r1.num = r2.num
AND r1.stop = 115 and r2.stop = 137

SELECT r1.company, r1.num
FROM
route r1 JOIN route r2 ON r1.company = r2.company and r1.num = r2.num
AND r1.stop = 115 and r2.stop = 137


SELECT DISTINCT(CITY) FROM STATION WHERE CITY REGEXP '^[aeiou]'
SELECT
    n,
    CASE
        WHEN p IS NULL then 'Root'
        WHEN n in (SELECT p fROM BST where p not null) then 'Inner'
        ELSE 'Leaf'
    END
FROM BST
ORDER BY n;

