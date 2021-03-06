/*
Schema:
CREATE TABLE If Not Exists point_2d (x INT NOT NULL, y INT NOT NULL)
Truncate table point_2d
insert into point_2d (x, y) values ('-1', '-1')
insert into point_2d (x, y) values ('0', '0')
insert into point_2d (x, y) values ('-1', '-2')
*/

/*
612. Shortest Distance in a Plane
Medium

Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.

Write a query to find the shortest distance between these points rounded to 2 decimals.

| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |


The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:

| shortest |
|----------|
| 1.00     |

Note: The longest distance among all the points are less than 10000.
*/

/*
Solution:
Approach 1: Using SQRT, POW() functions and math knowledge [Accepted]

Intuition

Calculate the distances between each two points and then display the smallest one.

Algorithm

The euclidean distance between two points P1(x1,y1) and P2(x2, y2) in two dimensions is defined as sqrt{(x1-x2)^2+(y1-y2)^2}

​. So in order to get the distances, we can join this table with itself, and then utilize the built-in function POW() and SQRT() like below.

SELECT
    p1.x,
    p1.y,
    p2.x,
    p2.y,
    SQRT((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2))) AS distance
FROM
    point_2d p1
        JOIN
    point_2d p2 ON p1.x != p2.x OR p1.y != p2.y
;

    Note:

        The condition 'p1.x != p2.x OR p2.y != p2.y' is to avoid calculating the distance of a point with itself. Otherwise, the minimum distance will be always zero.
        The columns p1.x, p1.y, p2.x and p2.y are for demonstrating. They are not necessary for the final solution.

So the output would be as below after running this code on the sample data.

| x  | y  | x  | y  | distance           |
|----|----|----|----|--------------------|
| 0  | 0  | -1 | -1 | 1.4142135623730951 |
| -1 | -2 | -1 | -1 | 1                  |
| -1 | -1 | 0  | 0  | 1.4142135623730951 |
| -1 | -2 | 0  | 0  | 2.23606797749979   |
| -1 | -1 | -1 | -2 | 1                  |
| 0  | 0  | -1 | -2 | 2.23606797749979   |

At last, choose the minimum distance and round it to 2 decimals as required.

MySQL

SELECT
    ROUND(SQRT(MIN((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)))), 2) AS shortest
FROM
    point_2d p1
        JOIN
    point_2d p2 ON p1.x != p2.x OR p1.y != p2.y
;

    Note: To put the MIN() inside of SQRT() will slightly improve the performance.

Approach 2: Optimize to avoid reduplicate calculations [Accepted]

Intuition

It is unnecessary to calculate the distance between all points to all other points since some of them may already be done. So how to avoid the reduplicate calculations?

Algorithm

When join the table with itself, we can claim to only calculate the distance between one point to another point in a certain rule such ponts with bigger x value. By following this rule, we can avoid quite a lot of reduplicate calculations.

SELECT
    t1.x,
    t1.y,
    t2.x,
    t2.y,
    SQRT((POW(t1.x - t2.x, 2) + POW(t1.y - t2.y, 2))) AS distance
FROM
    point_2d t1
        JOIN
    point_2d t2 ON (t1.x <= t2.x AND t1.y < t2.y)
        OR (t1.x <= t2.x AND t1.y > t2.y)
        OR (t1.x < t2.x AND t1.y = t2.y)
;

The output is as below for the sample data. You may notice that there are only 4 records, 1/3 less than the previous solution.

| x  | y  | x  | y  | distance           |
|----|----|----|----|--------------------|
| -1 | -2 | -1 | -1 | 1                  |
| -1 | -1 | 0  | 0  | 1.4142135623730951 |
| -1 | -2 | 0  | 0  | 2.23606797749979   |
| -1 | -1 | -1 | -2 | 1                  |

    Note: The best case is to compare n*(n-1)/2 times, but practically it is not always true considering two points may have same x value or y value. In this case, you may notice the distance between (-1, -2) and (-1, -1) appearing twice in the first and last line in the output.

Here comes the solution to select the shortest distance and round to two decimals.

MySQL

SELECT
    ROUND(SQRT(MIN((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)))),2) AS shortest
FROM
    point_2d p1
        JOIN
    point_2d p2 ON (p1.x <= p2.x AND p1.y < p2.y)
        OR (p1.x <= p2.x AND p1.y > p2.y)
        OR (p1.x < p2.x AND p1.y = p2.y)
;


*/