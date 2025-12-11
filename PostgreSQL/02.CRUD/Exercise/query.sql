//1
SELECT * FROM cities
order by id;

//2
SELECT
    concat(name, ' ', state) AS "cities_information",
    area AS "area_km2"
FROM
    cities

//3
SELECT DISTINCT ON (name)
    name,
    area as area_km2
FROM
    cities
ORDER BY
    name DESC;

//4
SELECT
    id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    job_title
FROM
    employees
ORDER BY
    first_name
LIMIT 50
;

//5
SELECT
    id,
    CONCAT_WS(' ', first_name, middle_name, last_name) AS full_name,
    hire_date
FROM
    employees
ORDER BY
    hire_date
OFFSET 9

//6
SELECT
    id,
    CONCAT(number, ' ', street) AS adress,
    city_id
FROM
    addresses
WHERE id>=20
;

//7
SELECT
    CONCAT(number, ' ', street) AS address,
    city_id
FROM
    addresses
WHERE
    city_id > 0
        AND
    city_id % 2 = 0
ORDER BY
    city_id
;

//8
SELECT
    name,
    start_date,
    end_date
FROM
    projects
WHERE
    start_date >= '2016-06-01 07:00:00'
            AND
    end_date < '2023-06-04 00:00:00'
ORDER BY
    start_date

//9
SELECT
    number,
    street
FROM
    addresses
WHERE
    id BETWEEN 50 AND 100
        OR
    number < 1000
;

//10
SELECT
    employee_id,
    project_id
FROM
    employees_projects
WHERE
    employee_id IN (200, 250)
            AND
    project_id NOT IN (50, 100)

//11
SELECT
    name,
    start_date
FROM
    projects
WHERE
    name IN ('Mountain', 'Road', 'Touring')
LIMIT 20;

//12
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    job_title,
    salary
FROM
    employees
WHERE
    salary in (12500, 14000, 23600, 25000)
ORDER BY
    salary DESC;

//13
SELECT
    id,
    employees.first_name,
    employees.last_name
FROM
    employees
WHERE
    middle_name is NULL
LIMIT 3;

//14
INSERT INTO departments(department, manager_id)
VALUES
    ('Finance', 3),
    ('Information Services', 42),
    ('Document Control', 90),
    ('Quality Assurance', 274),
    ('Facilities and Maintenance', 218),
    ('Shipping and Receiving', 85),
    ('Executive', 109);

//15

CREATE TABLE company_chart
AS
SELECT
    CONCAT(employees.first_name, ' ', employees.last_name) AS full_name,
    employees.job_title,
    employees.department_id,
    employees.manager_id
FROM
    employees;

//16
UPDATE
    projects
SET
    end_date = start_date + INTERVAL '5 months'
WHERE
    end_date is NULL
;

//17
UPDATE
    employees
SET
    salary = salary + 1500,
    job_title = 'Senior' || ' ' || job_title
WHERE
    hire_date BETWEEN '1998-01-01' AND '2000-01-05'
RETURNING  *;

//18
DELETE FROM
           addresses
WHERE
    city_id IN (5, 17, 20, 30);

//19
CREATE VIEW
    view_company_chart
AS
SELECT
    full_name,
    job_title
FROM
    company_chart
WHERE
    manager_id = 184;

//20
CREATE VIEW
    view_addresses
AS
SELECT
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    e.department_id,
    CONCAT(a.number, ' ', a.street) AS address
FROM
    employees AS e
JOIN
    addresses AS a
ON
    a.id = e.address_id
ORDER BY
    address
;

//21
ALTER VIEW
    view_addresses
RENAME TO
    view_employee_addresses_info;

//22
DELETE VIEW view_company_chart;

//23
UPDATE
    projects
SET
    name = UPPER(name)
RETURNING *;

//24
CREATE VIEW
    view_initials
AS
SELECT
    LEFT(first_name, 2) AS initial,
    last_name
FROM
    employees
ORDER BY
    last_name;

//25
