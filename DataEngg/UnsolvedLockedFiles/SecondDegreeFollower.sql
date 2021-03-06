/*
Schema:
Create table If Not Exists follow (followee varchar(255), follower varchar(255))
Truncate table follow
insert into follow (followee, follower) values ('A', 'B')
insert into follow (followee, follower) values ('B', 'C')
insert into follow (followee, follower) values ('B', 'D')
insert into follow (followee, follower) values ('D', 'E')
*/

/*
614. Second Degree Follower
Medium

In facebook, there is a follow table with two columns: followee, follower.

Please write a sql query to get the amount of each follower’s follower if he/she has one.

For example:

+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+

should output:

+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+

Explaination:
Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is E. A does not exist in follower list.

Note:
Followee would not follow himself/herself in all cases.
Please display the result in follower's alphabet order.
*/

/*
Solution:

The table and OJ code use upper and lower case, such as 'B' and 'b' interchangeably. But it requires specific upper or lower case in the output, to be consistent with follower column only!

Here is my answer to apply this approach.

select distinct follower, num
from follow,
(select followee, count(distinct follower) as num from follow
group by followee) as t
where follower = t.followee
order by follower;
*/