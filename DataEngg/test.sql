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

SELECT h.hacker_id, h.name, count(c.challenge_id) AS chall
FROM hackers h JOIN challenges c ON h.hacker_id=c.hacker_id
GROUP BY h.hacker_id
HAVING
    chall = (SELECT count(challenge_id) AS ch
             FROM challenges
             GROUP BY hacker_id
             ORDER BY ch DESC LIMIT 1)
    OR chall in (SELECT ch
                 FROM (SELECT count(challenge_id) AS ch
                       FROM challenges GROUP BY hacker_id) l
                 GROUP BY ch HAVING count(ch)=1)
ORDER BY chall DESC, h.hacker_id;


/*
Enter your query here.
*/
select c.hacker_id, h.name ,count(c.hacker_id) as c_count
/* this is the join we want to output them from */
from Hackers as h inner join Challenges as c on c.hacker_id = h.hacker_id
/* after they have been grouped by hacker */
group by c.hacker_id, h.name
/* but we want to be selective about which hackers we output */
/* having is required (instead of where) for filtering on groups */
having
    /* output anyone with a count that is equal to... */
    c_count =
        /* the max count that anyone has */
        (SELECT MAX(temp1.cnt)
        from (SELECT COUNT(hacker_id) as cnt
             from Challenges
             group by hacker_id
             order by hacker_id) temp1)

    /* or anyone who's count is in... */
    or c_count in
        /* the set of counts... */
        (select t.cnt
         from (select count(*) as cnt
               from challenges
               group by hacker_id) t
         /* who's group of counts... */
         group by t.cnt
         /* has only one element */
         having count(t.cnt) = 1)

/* finally, the order the rows should be output */
order by c_count DESC, c.hacker_id

/* ;) */
;

SELECT c.hacker_id, h.name, COUNT(c.challenge_id) c_cnt
FROM
hackers h JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY c.hacker_id, h.name
HAVING
    c_cnt = (SELECT MAX(ch)
             FROM (SELECT COUNT(challenge_id) ch FROM Challenges GROUP BY hacker_id) mid)
    OR c_cnt IN (SELECT ch
                 FROM (SELECT COUNT(challenge_id) ch FROM Challenges GROUP BY hacker_id) mid
                 GROUP BY ch
                 HAVING cd = 1);

SELECT f1.x, f1.y
FROM
	Functions f1 JOIN Functions f2 ON f1.x = f2.y AND f1.y = f2.x
WHERE
	f1.x <= f1.y
GROUP BY
	f1.x, f1.y
HAVING
	COUNT(*) > 1 OR (COUNT(*) = 1 AND f1.x != f1.y)
ORDER BY
	f1.x;
--
HAVING
    COUNT(*) > 1 OR (COUNT(*) = 1 AND f1.x != f1.y)


-----------------------------------

res = [i for i in range(len(test_str)) if test_str.startswith("http", i)]

import re

s = 'asdf=5;iwantthis123jasd'
result = re.search('asdf=5;(.*)123jasd', s)
print(result.group(1))

a = "https://delta.com is a test. we are testing for tohers too like https://apple.com"
re.search('https(.*)com')



SELECT vpa, by_tbl.amount, to_tbl.amount
FROM
    (SELECT paid_by, amount FROM transaction_log) by_tbl,
    (SELECT paid_to, amount FROM transaction_log) to_tbl,
    user_financial_detail usr
WHERE
    usr.vpa = by_tbl.paid_by
    AND usr.vpa = to_tbl.paid_to


SELECT vpa, by_tbl.amount, to_tbl.amount
FROM
    (SELECT paid_by, -1*amount FROM transaction_log) by_tbl,
    (SELECT paid_to, amount FROM transaction_log) to_tbl
WHERE
    to_tbl.paid_to = by_tbl.paid_by

SELECT out_tbl.paid_by,
    SUM(
        CASE WHEN out_tbl.status = 'OUT' THEN out_tbl.cash
             WHEN in_tbl.status = 'IN' THEN in_tbl.cash
        END
    ) as cash
FROM
    (SELECT 'OUT' AS status, paid_by, -1*SUM(amount) AS cash FROM transaction_log GROUP BY paid_by) out_tbl,
    (SELECT 'IN' AS status, paid_to, SUM(amount) AS cash FROM transaction_log GROUP BY paid_to) in_tbl
WHERE
    out_tbl.paid_by = in_tbl.paid_to
GROUP BY out_tbl.paid_by;


SELECT CONCAT(usr.first_name, ' ', usr.last_name) as name, usr.vpa, trns.cash,
    CASE WHEN trns.cash < -1 * usr.credit_limit THEN 'YES'
        ELSE 'NO' END AS credit_limit_breached
FROM
(SELECT out_tbl.paid_by,
    SUM(
        CASE WHEN out_tbl.status = 'OUT' THEN out_tbl.cash
             WHEN in_tbl.status = 'IN' THEN in_tbl.cash
        END
    ) as cash
FROM
    (SELECT 'OUT' AS status, paid_by, -1*SUM(amount) AS cash FROM transaction_log GROUP BY paid_by) out_tbl,
    (SELECT 'IN' AS status, paid_to, SUM(amount) AS cash FROM transaction_log GROUP BY paid_to) in_tbl
WHERE
    out_tbl.paid_by = in_tbl.paid_to
GROUP BY out_tbl.paid_by) trns,
user_financial_detail usr
where
trns.paid_by = usr.vpa
;

----

SELECT CONCAT(usr.first_name, ' ', usr.last_name) as name, usr.vpa, trns.cash,
    CASE WHEN trns.cash < -1 * usr.credit_limit THEN 'YES'
        ELSE 'NO' END AS credit_limit_breached
FROM
    (
    SELECT usr_vpa, SUM(cash) as cash FROM
    (
    SELECT paid_by as usr_vpa, -1*SUM(amount) AS cash FROM transaction_log GROUP BY paid_by
    UNION
    SELECT paid_to as usr_vpa, SUM(amount) AS cash FROM transaction_log GROUP BY paid_to
    ) unn
    GROUP BY usr_vpa
    )trns,
    user_financial_detail usr
WHERE
    trns.usr_vpa = usr.vpa
;





