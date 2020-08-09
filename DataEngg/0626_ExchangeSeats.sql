/*
Schema:
Create table If Not Exists seat(id int, student varchar(255))
Truncate table seat
insert into seat (id, student) values ('1', 'Abbot')
insert into seat (id, student) values ('2', 'Doris')
insert into seat (id, student) values ('3', 'Emerson')
insert into seat (id, student) values ('4', 'Green')
insert into seat (id, student) values ('5', 'Jeames')
*/

/*
Question

Medium

Mary is a teacher in a middle school and she has a table seat storing students’ names and their corresponding seat ids. The column id is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+

For the sample input, the output is:

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

Note: If the number of students is odd, there is no need to change the last one’s seat.
*/

-- Solution:
SELECT
    CASE
        WHEN s.id % 2 <> 0 AND s.id = (SELECT COUNT(*) FROM seat) THEN s.id
        WHEN s.id % 2 = 0 THEN s.id - 1
        ELSE s.id + 1
    END AS id,
    s.student
FROM
    seat s
ORDER BY id DESC;

/*
SELECT
    a.id id,
    COALESCE(b.student, a.student) student
FROM
    seat a LEFT JOIN seat b
    ON b.id = (CASE
               WHEN a.id%2=1 THEN a.id+1
               ELSE a.id-1
               END)
ORDER BY a.id
*/
