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
        INSERT INTO deleted_employees
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

