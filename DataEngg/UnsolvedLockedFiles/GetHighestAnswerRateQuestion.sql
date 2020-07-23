/*
Create table If Not Exists survey_log (id int, action varchar(255), question_id int, answer_id int, q_num int, timestamp int)
Truncate table survey_log
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '285', 'None', '1', '123')
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'answer', '285', '124124', '1', '124')
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '369', 'None', '2', '125')
insert into survey_log (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'skip', '369', 'None', '2', '126')
*/

/*
578. Get Highest Answer Rate Question
Medium

Get the highest answer rate question from a table survey_log with these columns: id, action, question_id, answer_id, q_num, timestamp.

id means user id; action has these kind of values: "show", "answer", "skip"; answer_id is not null when action column is "answer", while is null for "show" and "skip"; q_num is the numeral order of the question in current session.

Write a sql query to identify the question which has the highest answer rate.

Example:

Input:
+------+-----------+--------------+------------+-----------+------------+
| id   | action    | question_id  | answer_id  | q_num     | timestamp  |
+------+-----------+--------------+------------+-----------+------------+
| 5    | show      | 285          | null       | 1         | 123        |
| 5    | answer    | 285          | 124124     | 1         | 124        |
| 5    | show      | 369          | null       | 2         | 125        |
| 5    | skip      | 369          | null       | 2         | 126        |
+------+-----------+--------------+------------+-----------+------------+
Output:
+-------------+
| survey_log  |
+-------------+
|    285      |
+-------------+
Explanation:
question 285 has answer rate 1/1, while question 369 has 0/1 answer rate, so output 285.

Note: The highest answer rate meaning is: answer number's ratio in show number in the same question.
*/

/*
Solution:

Approach I: Using sub-query and SUM() function [Accepted]

Intuition

Calculate the answered times / show times for each question.

Algorithm

First, we can use SUM() to get the total number of answered times as well as the show times for each question using a sub-query as below.

SELECT
    question_id,
    SUM(CASE
        WHEN action = 'answer' THEN 1
        ELSE 0
    END) AS num_answer,
    SUM(CASE
        WHEN action = 'show' THEN 1
        ELSE 0
    END) AS num_show
FROM
    survey_log
GROUP BY question_id
;

| question_id | num_answer | num_show |
|-------------|------------|----------|
| 285         | 1          | 1        |
| 369         | 0          | 1        |

Then we can calculate the answer rate by its definition.

MySQL

SELECT question_id as survey_log
FROM
(
	SELECT question_id,
         SUM(case when action="answer" THEN 1 ELSE 0 END) as num_answer,
        SUM(case when action="show" THEN 1 ELSE 0 END) as num_show,
	FROM survey_log
	GROUP BY question_id
) as tbl
ORDER BY (num_answer / num_show) DESC
LIMIT 1

Approach II: Using sub-query and COUNT(IF...) function [Accepted]

Algorithm

This solution is very straight forward: use the COUNT() function to sum the answer and show time combining with the IF() function.

MySQL

SELECT
    question_id AS 'survey_log'
FROM
    survey_log
GROUP BY question_id
ORDER BY COUNT(answer_id) / COUNT(IF(action = 'show', 1, 0)) DESC
LIMIT 1;

*/

/*
comments:
This COUNT(IF(action = 'show', 1, 0)) is so wrong. should be COUNT(IF(action = 'show', 1, null))

*/