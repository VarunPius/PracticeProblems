/*
Schema:
CREATE TABLE IF NOT EXISTS insurance (PID INTEGER(11), TIV_2015 NUMERIC(15,2), TIV_2016 NUMERIC(15,2), LAT NUMERIC(5,2), LON NUMERIC(5,2) )
Truncate table insurance
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('1', '10', '5', '10', '10')
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('2', '20', '20', '20', '20')
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('3', '10', '30', '20', '20')
insert into insurance (PID, TIV_2015, TIV_2016, LAT, LON) values ('4', '10', '40', '40', '40')
*/

/*
585. Investments in 2016
Medium

Write a query to print the sum of all total investment values in 2016 (TIV_2016), to a scale of 2 decimal places, for all policy holders who meet the following criteria:

    Have the same TIV_2015 value as one or more other policyholders.
    Are not located in the same city as any other policyholder (i.e.: the (latitude, longitude) attribute pairs must be unique).

Input Format:
The insurance table is described as follows:

| Column Name | Type          |
|-------------|---------------|
| PID         | INTEGER(11)   |
| TIV_2015    | NUMERIC(15,2) |
| TIV_2016    | NUMERIC(15,2) |
| LAT         | NUMERIC(5,2)  |
| LON         | NUMERIC(5,2)  |

where PID is the policyholder's policy ID, TIV_2015 is the total investment value in 2015, TIV_2016 is the total investment value in 2016, LAT is the latitude of the policy holder's city, and LON is the longitude of the policy holder's city.

Sample Input

| PID | TIV_2015 | TIV_2016 | LAT | LON |
|-----|----------|----------|-----|-----|
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |

Sample Output

| TIV_2016 |
|----------|
| 45.00    |

Explanation

The first record in the table, like the last record, meets both of the two criteria.
The TIV_2015 value '10' is as the same as the third and forth record, and its location unique.

The second record does not meet any of the two criteria. Its TIV_2015 is not like any other policyholders.

And its location is the same with the third record, which makes the third record fail, too.

So, the result is the sum of TIV_2016 of the first and last record, which is 45.
*/

/*
Solution:
Approach: Using GROUP BY and COUNT [Accepted]

Intuition

To decide whether a value in a column is unique or not, we can use GROUP BY and COUNT.

Algorithm

Check whether the value of a record's TIV_2015 is unique, if it is not unique, and at the same time, its location (LAT, LON) pair is unique, then this record meeting the criteria. So it should be counted in the sum.

MySQL

SELECT
    SUM(insurance.TIV_2016) AS TIV_2016
FROM
    insurance
WHERE
    insurance.TIV_2015 IN
    (
      SELECT
        TIV_2015
      FROM
        insurance
      GROUP BY TIV_2015
      HAVING COUNT(*) > 1
    )
    AND CONCAT(LAT, LON) IN
    (
      SELECT
        CONCAT(LAT, LON)
      FROM
        insurance
      GROUP BY LAT , LON
      HAVING COUNT(*) = 1
    )
;

    Tips: Concat the LAT and LON as a whole to represent the location information.

Note: These two criteria should be met without an order, so if you attempt to filter data using criteria #1 first and then criteria #2, you will get a wrong result.

Taking the sample input as an example, the data set will be as following after taking the first criteria.
PID 	TIV_2015 	TIV_2016 	LAT 	LON
1 	10 	5 	10 	10
3 	10 	30 	20 	20
4 	10 	40 	40 	40

Then, the second criteria cannot filter any records on this data set. So the result is 75(5+30+40), which is obviously wrong since the location of record with PID '3' is actually the same with the record having been filtered by the first criteria.
PID 	TIV_2015 	TIV_2016 	LAT 	LON
2 	20 	20 	20 	20
3 	10 	30 	20 	20
*/