CREATE DATABASE test_db;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    gender VARCHAR(50),
    age INT

);

SELECT
    first_name AS "FirstName",
    last_name AS "LastName"
FROM employees AS e


SELECT
    concat(first_name, ' ', last_name) AS "Full Name",
    age
FROM employees AS e
;


//1
SELECT
    id,
    concat(first_name, ' ', last_name) AS "Full name",
    job_title AS "Job Title"
    from employees

//2
    SELECT
    id,
    concat(first_name, ' ', last_name) AS full_name,
    job_title AS "Job Title",
    salary
    FROM employees
    WHERE salary>=1000
ORDER BY id;

//3
SELECT
    id,
    first_name,
    last_name,
    job_title,
    department_id,
    salary
FROM employees
WHERE department_id = 4 AND salary >=1000
ORDER BY id;

//4
INSERT INTO employees(first_name, last_name, job_title,	department_id, salary)
VALUES
    ('Samantha', 'Young', 'Housekeeping', 4, 900),
    ('Roger', 'Palmer', 'Waiter', 3, 928.33)
;

SELECT * FROM employees;

//5
UPDATE employees
SET salary = salary + 100
WHERE job_title = 'Manager'
;
SELECT * FROM employees
WHERE job_title = 'Manager'
;

//6
DELETE FROM employees
WHERE department_id IN (1, 2)
;
SELECT * FROM employees
ORDER BY id
;

//7
