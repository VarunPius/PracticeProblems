/*
Schema:
CREATE TABLE IF NOT EXISTS student (student_id INT,student_name VARCHAR(45), gender VARCHAR(6), dept_id INT)
CREATE TABLE IF NOT EXISTS department (dept_id INT, dept_name VARCHAR(255))
Truncate table student
insert into student (student_id, student_name, gender, dept_id) values ('1', 'Jack', 'M', '1')
insert into student (student_id, student_name, gender, dept_id) values ('2', 'Jane', 'F', '1')
insert into student (student_id, student_name, gender, dept_id) values ('3', 'Mark', 'M', '2')
Truncate table department
insert into department (dept_id, dept_name) values ('1', 'Engineering')
insert into department (dept_id, dept_name) values ('2', 'Science')
insert into department (dept_id, dept_name) values ('3', 'Law')
*/

/*
580. Count Student Number in Departments
Medium

A university uses 2 data tables, student and department, to store data about its students and the departments associated with each major.

Write a query to print the respective department name and number of students majoring in each department for all departments in the department table (even ones with no current students).

Sort your results by descending number of students; if two or more departments have the same number of students, then sort those departments alphabetically by department name.

The student is described as follow:

| Column Name  | Type      |
|--------------|-----------|
| student_id   | Integer   |
| student_name | String    |
| gender       | Character |
| dept_id      | Integer   |

where student_id is the student's ID number, student_name is the student's name, gender is their gender, and dept_id is the department ID associated with their declared major.

And the department table is described as below:

| Column Name | Type    |
|-------------|---------|
| dept_id     | Integer |
| dept_name   | String  |

where dept_id is the department's ID number and dept_name is the department name.

Here is an example input:
student table:

| student_id | student_name | gender | dept_id |
|------------|--------------|--------|---------|
| 1          | Jack         | M      | 1       |
| 2          | Jane         | F      | 1       |
| 3          | Mark         | M      | 2       |

department table:

| dept_id | dept_name   |
|---------|-------------|
| 1       | Engineering |
| 2       | Science     |
| 3       | Law         |

The Output should be:

| dept_name   | student_number |
|-------------|----------------|
| Engineering | 2              |
| Science     | 1              |
| Law         | 0              |
*/

/*
Solution:

Approach: Using OUTER JOIN and COUNT(expression) [Accepted]

Intuition

Use GROUP BY function can measure student number in a department, and then use COUNT function to count the number of records of each department.

Algorithm

We can use OUTER JOIN to query all departments. The problem is to display '0' for departments without no current students. Some people will write the following query using COUNT(*).

SELECT
    dept_name, COUNT(*) AS student_number
FROM
    department
        LEFT OUTER JOIN
    student ON department.dept_id = student.dept_id
GROUP BY department.dept_name
ORDER BY student_number DESC , department.dept_name
;

Unfortunately, it wrongly displays '1' for departments like 'Law' without current students for the sample input.

| dept_name   | student_number |
|-------------|----------------|
| Engineering | 2              |
| Law         | 1              |
| Science     | 1              |

Instead, COUNT(expression) could be used because it does not take account if expression is null. You can refer to the MySQL manual for the details.

Thus, here is a right solution after fixing the issue above.

MySQL

SELECT
    dept_name, COUNT(student_id) AS student_number
FROM
    department
        LEFT OUTER JOIN
    student ON department.dept_id = student.dept_id
GROUP BY department.dept_name
ORDER BY student_number DESC , department.dept_name
;
*/