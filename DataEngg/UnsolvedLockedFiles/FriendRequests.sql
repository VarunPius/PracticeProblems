/*
Schema:
Create table If Not Exists friend_request ( sender_id INT NOT NULL, send_to_id INT NULL, request_date DATE NULL)
Create table If Not Exists request_accepted ( requester_id INT NOT NULL, accepter_id INT NULL, accept_date DATE NULL)
Truncate table friend_request
insert into friend_request (sender_id, send_to_id, request_date) values ('1', '2', '2016/06/01')
insert into friend_request (sender_id, send_to_id, request_date) values ('1', '3', '2016/06/01')
insert into friend_request (sender_id, send_to_id, request_date) values ('1', '4', '2016/06/01')
insert into friend_request (sender_id, send_to_id, request_date) values ('2', '3', '2016/06/02')
insert into friend_request (sender_id, send_to_id, request_date) values ('3', '4', '2016/06/09')
Truncate table request_accepted
insert into request_accepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03')
insert into request_accepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08')
insert into request_accepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08')
insert into request_accepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09')
insert into request_accepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/10')
*/

/*
597. Friend Requests I: Overall Acceptance Rate
Easy

In social network like Facebook or Twitter, people send friend requests and accept others’ requests as well. Now given two tables as below:


Table: friend_request

| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016_06-01 |
| 1         | 3          | 2016_06-01 |
| 1         | 4          | 2016_06-01 |
| 2         | 3          | 2016_06-02 |
| 3         | 4          | 2016-06-09 |


Table: request_accepted

| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |


Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.


For the sample data above, your query should return the following result.



|accept_rate|
|-----------|
|       0.80|

Note:
    The accepted requests are not necessarily from the table friend_request. In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
    It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances are only counted once.
    If there is no requests at all, you should return 0.00 as the accept_rate.

Explanation: There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.

Follow-up:
    Can you write a query to return the accept rate but for every month?
    How about the cumulative accept rate for every day?
*/

/*
Solution:

Approach: Using round and ifnull [Accepted]

Intuition

Count the accepted requests and then divides it by the number of all requests.

Algorithm

To get the distinct number of accepted requests, we can query from the request_accepted table.

select count(*) from (select distinct requester_id, accepter_id from request_accepted;

With the same technique, we can have the total number of requests from the friend_request table:

select count(*) from (select distinct sender_id, send_to_id from friend_request;

At last, divide these two numbers and round it to a scale of 2 decimal places to get the required acceptance rate.

Wait! The divisor (total number of requests) could be '0' if the table friend_request is empty. So, we have to utilize ifnull to deal with this special case.

MySQL

select
round(
    ifnull(
    (select count(*) from (select distinct requester_id, accepter_id from request_accepted) as A)
    /
    (select count(*) from (select distinct sender_id, send_to_id from friend_request) as B),
    0)
, 2) as accept_rate;
*/

/*
602. Friend Requests II: Who Has the Most Friends
Medium

In social network like Facebook or Twitter, people send friend requests and accept others' requests as well.



Table request_accepted

+--------------+-------------+------------+
| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
+--------------+-------------+------------+
This table holds the data of friend acceptance, while requester_id and accepter_id both are the id of a person.

Write a query to find the the people who has most friends and the most friends number under the following rules:

    It is guaranteed there is only 1 people having the most friends.
    The friend request could only been accepted once, which mean there is no multiple records with the same requester_id and accepter_id value.

For the sample data above, the result is:

Result table:
+------+------+
| id   | num  |
|------|------|
| 3    | 3    |
+------+------+
The person with id '3' is a friend of people '1', '2' and '4', so he has 3 friends in total, which is the most number than any others.

Follow-up:
In the real world, multiple people could have the same most number of friends, can you find all these people in this case?
*/

/*
Solution:

Approach: Union requester_id and accepter_id [Accepted]

Algorithm

Being friends is bidirectional, so if one person accepts a request from another person, both of them will have one more friend.

Thus, we can union column requester_id and accepter_id, and then count the number of the occurrence of each person.

select requester_id as ids from request_accepted
union all
select accepter_id from request_accepted;

    Note: Here we should use union all instead of union because union all will keep all the records even the 'duplicated' one.

Taking the sample as an example, the output is:
ids
1
1
2
3
2
3
3
4

Then it will be fairly easy to get the 'ids' with most occurrence using the same technique as mentioned in problem 580. Customer Placing the Largest Number of Orders.

MySQL

select ids as id, cnt as num
from
(
select ids, count(*) as cnt
   from
   (
        select requester_id as ids from request_accepted
        union all
        select accepter_id from request_accepted
    ) as tbl1
   group by ids
   ) as tbl2
order by cnt desc
limit 1
;
*/