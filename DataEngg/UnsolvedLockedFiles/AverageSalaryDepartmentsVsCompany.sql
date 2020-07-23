/*
Schema:
Create table If Not Exists salary (id int, employee_id int, amount int, pay_date date)
Create table If Not Exists employee (employee_id int, department_id int)
Truncate table salary
insert into salary (id, employee_id, amount, pay_date) values ('1', '1', '9000', '2017/03/31')
insert into salary (id, employee_id, amount, pay_date) values ('2', '2', '6000', '2017/03/31')
insert into salary (id, employee_id, amount, pay_date) values ('3', '3', '10000', '2017/03/31')
insert into salary (id, employee_id, amount, pay_date) values ('4', '1', '7000', '2017/02/28')
insert into salary (id, employee_id, amount, pay_date) values ('5', '2', '6000', '2017/02/28')
insert into salary (id, employee_id, amount, pay_date) values ('6', '3', '8000', '2017/02/28')
Truncate table employee
insert into employee (employee_id, department_id) values ('1', '1')
insert into employee (employee_id, department_id) values ('2', '2')
insert into employee (employee_id, department_id) values ('3', '2')
*/

/*
615. Average Salary: Departments VS Company
Hard

Given two tables as below, write a query to display the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.


Table: salary

| id | employee_id | amount | pay_date   |
|----|-------------|--------|------------|
| 1  | 1           | 9000   | 2017-03-31 |
| 2  | 2           | 6000   | 2017-03-31 |
| 3  | 3           | 10000  | 2017-03-31 |
| 4  | 1           | 7000   | 2017-02-28 |
| 5  | 2           | 6000   | 2017-02-28 |
| 6  | 3           | 8000   | 2017-02-28 |


The employee_id column refers to the employee_id in the following table employee.



| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |


So for the sample data above, the result is:



| pay_month | department_id | comparison  |
|-----------|---------------|-------------|
| 2017-03   | 1             | higher      |
| 2017-03   | 2             | lower       |
| 2017-02   | 1             | same        |
| 2017-02   | 2             | same        |


Explanation


In March, the company's average salary is (9000+6000+10000)/3 = 8333.33...


The average salary for department '1' is 9000, which is the salary of employee_id '1' since there is only one employee in this department. So the comparison result is 'higher' since 9000 > 8333.33 obviously.


The average salary of department '2' is (6000 + 10000)/2 = 8000, which is the average of employee_id '2' and '3'. So the comparison result is 'lower' since 8000 < 8333.33.


With he same formula for the average salary comparison in February, the result is 'same' since both the department '1' and '2' have the same average salary with the company, which is 7000.
*/

/*
Solution:

Approach: Using avg() and case...when... [Accepted]

Intuition

Solve this problem by 3 steps as below.

Algorithm

1.Calculate the company's average salary in every month MySQL has the built-in function avg() to get the average of a list of numbers. Also, we need to format the pay_date column for future use.

select avg(amount) as company_avg,  date_format(pay_date, '%Y-%m') as pay_month
from salary
group by date_format(pay_date, '%Y-%m')
;

company_avg 	pay_month
7000.0000 	2017-02
8333.3333 	2017-03

2.Calculate the each department's average salary in every month To do this, we need to join the salary table with the employee table using condition salary.employee_id = employee.id.

select department_id, avg(amount) as department_avg, date_format(pay_date, '%Y-%m') as pay_month
from salary
join employee on salary.employee_id = employee.employee_id
group by department_id, pay_month
;

department_id 	department_avg 	pay_month
1 	7000.0000 	2017-02
1 	9000.0000 	2017-03
2 	7000.0000 	2017-02
2 	8000.0000 	2017-03

3.Compare the previous numbers and display the result This step might be the hardest if you have no idea on how to use MySQL flow control statement case...when....

MySQL, like other programming languages, also has its flow control. Click this link to learn it: https://dev.mysql.com/doc/refman/5.7/en/flow-control-statements.html

At last, combine the above two query and join them on department_salary.pay_month = company_salary.pay_month.

MySQL

select department_salary.pay_month, department_id,
case
  when department_avg>company_avg then 'higher'
  when department_avg<company_avg then 'lower'
  else 'same'
end as comparison
from
(
  select department_id, avg(amount) as department_avg, date_format(pay_date, '%Y-%m') as pay_month
  from salary join employee on salary.employee_id = employee.employee_id
  group by department_id, pay_month
) as department_salary
join
(
  select avg(amount) as company_avg,  date_format(pay_date, '%Y-%m') as pay_month from salary group by date_format(pay_date, '%Y-%m')
) as company_salary
on department_salary.pay_month = company_salary.pay_month
;
*/