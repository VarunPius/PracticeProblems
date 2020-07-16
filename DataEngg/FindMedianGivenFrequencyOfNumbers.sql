/*
Create table If Not Exists Numbers (Number int, Frequency int)
Truncate table Numbers
insert into Numbers (Number, Frequency) values ('0', '7')
insert into Numbers (Number, Frequency) values ('1', '1')
insert into Numbers (Number, Frequency) values ('2', '3')
insert into Numbers (Number, Frequency) values ('3', '1')
*/
/*
571. Find Median Given Frequency of Numbers
Hard
The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+

In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

+--------+
| median |
+--------|
| 0.0000 |
+--------+

Write a query to find the median of all numbers and name the result as median.

*/

/*
My solution, I think, is super simple.

select  avg(n.Number) median
from Numbers n
where n.Frequency >= abs((select sum(Frequency) from Numbers where Number<=n.Number) -
                         (select sum(Frequency) from Numbers where Number>=n.Number))

Explanation:
Let's take all numbers from left including current number and then do same for right.
(select sum(Frequency) from Numbers where Number<=n.Number) as left
(select sum(Frequency) from Numbers where Number<=n.Number) as right
Now if difference between Left and Right less or equal to Frequency of the current number that means this number is median.
Ok, what if we get two numbers satisfied this condition? Easy peasy - take AVG(). Ta-da!
*/
