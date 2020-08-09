/*
Schema:
Create table If Not Exists stadium (id int, visit_date DATE NULL, people int)
Truncate table stadium
insert into stadium (id, visit_date, people) values ('1', '2017-01-01', '10')
insert into stadium (id, visit_date, people) values ('2', '2017-01-02', '109')
insert into stadium (id, visit_date, people) values ('3', '2017-01-03', '150')
insert into stadium (id, visit_date, people) values ('4', '2017-01-04', '99')
insert into stadium (id, visit_date, people) values ('5', '2017-01-05', '145')
insert into stadium (id, visit_date, people) values ('6', '2017-01-06', '1455')
insert into stadium (id, visit_date, people) values ('7', '2017-01-07', '199')
insert into stadium (id, visit_date, people) values ('8', '2017-01-08', '188')
*/

/*
Question

Hard

X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, visit_date, people

Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

For example, the table stadium:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
For the sample data above, the output is:

+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
Note:
Each day only have one row record, and the dates are increasing with id increasing.

*/

-- Solutions:


/*
Possible Solutions:
with t as ( select t1.id , t1.visit_date , t1.people ,
            id - row_number() OVER(ORDER BY id) as grp
       from stadium t1
       where people >= 100
          )
select t.id, t.visit_date ,t.people
from t
where grp in ( select grp from t group by grp having count(*) >=3  )

select distinct t1.*
from stadium t1, stadium t2, stadium t3
where t1.people>=100 and t2.people>=100 and t3.people>=100 and
(
(t1.id-t2.id=1 and t1.id-t3.id=2 and t2.id-t3.id=1)
or
(t2.id-t1.id=1 and t2.id-t3.id=2 and t1.id-t3.id=1)
or
(t3.id-t2.id=1 and t2.id-t1.id=1 and t3.id-t1.id=2)
)
order by t1.id;

SELECT
    s0.*
FROM
    stadium s0 LEFT JOIN
    stadium s1 ON s1.id = s0.id + 1 LEFT JOIN
    stadium s2 ON s2.id = s0.id + 2 LEFT JOIN
    stadium s_1 ON s_1.id = s0.id - 1 LEFT JOIN
    stadium s_2 ON s_2.id = s0.id - 2
WHERE
    (s0.people > 99 AND s1.people > 99 AND s2.people > 99) OR
    (s_1.people > 99 AND s0.people > 99 AND s1.people > 99) OR
    (s_2.people > 99 AND s_1.people > 99 AND s0.people > 99)
ORDER BY s0.id
*/
