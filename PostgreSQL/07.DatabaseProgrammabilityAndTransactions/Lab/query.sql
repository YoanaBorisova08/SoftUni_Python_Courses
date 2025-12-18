//1
CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS
$$
    DECLARE id INT;
    BEGIN
        SELECT town_id FROM towns as t WHERE t.name = town_name INTO id;
        RETURN (SELECT count(*)
                FROM employees AS e
                         JOIN addresses AS a USING (address_id)
                         JOIN towns as t USING (town_id)
                WHERE t.town_id = id);
    END
$$
LANGUAGE  plpgsql;


//2

CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR(20))
AS
$$
    DECLARE
        id INT;
    BEGIN
        SELECT department_id FROM departments WHERE name = department_name INTO id;
        UPDATE employees
        SET salary = salary * 1.05
        WHERE department_id = id ;
    END
$$
LANGUAGE plpgsql

//3
CREATE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
    DECLARE
        employee INT;
    BEGIN
        IF (SELECT employee_id FROM employees WHERE employee_id = id) IS NULL
            THEN ROLLBACK ;
        END IF;
        UPDATE employees
        SET salary = salary * 1.05
        WHERE
            employee_id = id;
        COMMIT;

    END
$$
LANGUAGE plpgsql;

//4
CREATE TABLE deleted_employees(
employee_id SERIAL primary key,
first_name varchar(20),
last_name varchar(20),
middle_name varchar(20),
job_title varchar(50),
department_id int,
salary numeric(19,4)
);


CREATE OR REPLACE FUNCTION backup_fired_employees()
RETURNS TRIGGER
AS
$$
    BEGIN
        INSERT INTO deleted_employees(first_name, last_name, middle_name, job_title, department_id, salary)
        VALUES (
                   old.first_name,
                   old.last_name,
                   old.middle_name,
                   old.job_title,
                   old.department_id,
                   old.salary
        );
        RETURN old;
    END
$$
LANGUAGE plpgsql
;

CREATE OR REPLACE TRIGGER trigger_backup_fired_employees
AFTER DELETE ON employees
FOR EACH ROW EXECUTE PROCEDURE backup_fired_employees();