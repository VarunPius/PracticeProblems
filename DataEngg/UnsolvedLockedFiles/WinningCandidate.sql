/*
Create table If Not Exists Candidate (id int, Name varchar(255))
Create table If Not Exists Vote (id int, CandidateId int)
Truncate table Candidate
insert into Candidate (id, Name) values ('1', 'A')
insert into Candidate (id, Name) values ('2', 'B')
insert into Candidate (id, Name) values ('3', 'C')
insert into Candidate (id, Name) values ('4', 'D')
insert into Candidate (id, Name) values ('5', 'E')
Truncate table Vote
insert into Vote (id, CandidateId) values ('1', '2')
insert into Vote (id, CandidateId) values ('2', '4')
insert into Vote (id, CandidateId) values ('3', '3')
insert into Vote (id, CandidateId) values ('4', '2')
insert into Vote (id, CandidateId) values ('5', '5')
*/

/*
574. Winning Candidate
Medium
Table: Candidate

+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+

Table: Vote

+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id is the auto-increment primary key,
CandidateId is the id appeared in Candidate table.

Write a sql to find the name of the winning candidate, the above example will return the winner B.

+------+
| Name |
+------+
| B    |
+------+

Notes:
    You may assume there is no tie, in other words there will be only one winning candidate.
*/

/*
Solution:
Approach: Using JOIN and a temporary table [Accepted]

Algorithm

Query in the Vote table to get the winner's id and then join it with the Candidate table to get the name.

MySQL

SELECT
    name AS 'Name'
FROM
    Candidate
        JOIN
    (SELECT
        Candidateid
    FROM
        Vote
    GROUP BY Candidateid
    ORDER BY COUNT(*) DESC
    LIMIT 1) AS winner
WHERE
    Candidate.id = winner.Candidateid
;
*/