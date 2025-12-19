--1.1
CREATE DATABASE zoo_db;

CREATE TABLE owners(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(50)
);

CREATE TABLE animal_types(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    animal_type VARCHAR(30) NOT NULL
);

CREATE TABLE cages(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    animal_type_id INT NOT NULL REFERENCES animal_types(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE animals(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    birthdate DATE NOT NULL,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE ON UPDATE CASCADE,
    animal_type_id INT NOT NULL REFERENCES animal_types(id) ON DELETE CASCADE ON UPDATE CASCADE
)
;

CREATE TABLE volunteers_departments(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_name VARCHAR(30) NOT NULL
);

CREATE TABLE volunteers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(50),
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE ON UPDATE CASCADE,
    department_id INT NOT NULL REFERENCES volunteers_departments(id) ON DELETE CASCADE ON UPDATE CASCADE
)
;

CREATE TABLE animals_cages(
    cage_id INT REFERENCES cages(id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL ,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL
)


--2.2
INSERT INTO volunteers(name, phone_number, address, animal_id, department_id)
VALUES ('Anita Kostova',	'0896365412',	'Sofia, 5 Rosa str.',	15,	1),
('Dimitur Stoev',	'0877564223',	NULL,	42,	4),
('Kalina Evtimova',	'0896321112',	'Silistra, 21 Breza str.',	9,	7),
('Stoyan Tomov',	'0898564100',	'Montana, 1 Bor str.',	18,	8),
('Boryana Mileva',	'0888112233',	NULL,	31,	5)
;

INSERT INTO animals(name, birthdate, owner_id, animal_type_id)
VALUES ('Giraffe',	'2018-09-21',	21,	1),
('Harpy Eagle',	'2015-04-17',	15,	3),
('Hamadryas Baboon',	'2017-11-02',	NULL,	1),
('Tuatara',	'2021-06-30',	2,	4);

--2.3
UPDATE animals
SET owner_id = (SELECT id FROM owners WHERE owners.name = 'Kaloqn Stoqnov')
WHERE owner_id IS NULL ;

--2.4
DELETE FROM volunteers_departments
WHERE department_name = 'Education program assistant';

--3.5
SELECT
    name,
    phone_number,
    address,
    animal_id,
    department_id
FROM volunteers
ORDER BY
    name, animal_id, department_id;

--3.6
SELECT
    name,
    (SELECT animal_type FROM animal_types WHERE id=animal_type_id) AS animal_type,
    TO_CHAR(birthdate, 'DD.MM.YYYY') AS birthdate
FROM animals
ORDER BY name;

--3.7
SELECT
    o.name,
    COUNT(*) AS count_of_animals
FROM owners AS o JOIN animals AS a ON o.id = a.owner_id
GROUP BY o.name
ORDER BY count_of_animals DESC ,
         o.name
LIMIT 5;

--3.8
SELECT
    CONCAT(o.name, ' - ', a.name) AS "owners-animals",
    o.phone_number,
    ac.cage_id
FROM
    animals AS a JOIN owners AS o ON o.id=a.owner_id
    JOIN animal_types AS at ON a.animal_type_id = at.id
    JOIN animals_cages AS ac ON ac.animal_id = a.id
WHERE at.animal_type = 'Mammals'
ORDER BY
    o.name,
    a.name DESC;

--3.9
SELECT
    v.name,
    v.phone_number,
    TRIM(v.address, 'Sofia, ') AS address
FROM volunteers AS v
JOIN volunteers_departments AS vd ON v.department_id = vd.id
WHERE vd.department_name = 'Education program assistant'
                    AND
        v.address LIKE'%Sofia%'
ORDER BY name;


--3.10
SELECT
    a.name AS animal,
    extract('YEAR' FROM a.birthdate) AS birth_year,
    at.animal_type
FROM animals AS a JOIN animal_types AS at ON a.animal_type_id=at.id
WHERE a.owner_id IS NULL
        AND
    at.animal_type <> 'Birds'
        AND
    AGE('01/01/2022', a.birthdate) < '5 year'
ORDER BY name;

--4.11
CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department
(searched_volunteers_department VARCHAR(30))
RETURNS INT AS
$$
    BEGIN
        RETURN (SELECT COUNT(*)
                FROM volunteers_departments as vd
                JOIN volunteers as v ON v.department_id = vd.id
                WHERE department_name=searched_volunteers_department);
    END
$$
LANGUAGE plpgsql;

--4.12
CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not
(IN animal_name VARCHAR(30),
OUT result VARCHAR)
AS
$$
    BEGIN
        SELECT
            COALESCE(o.name, 'For adoption'::VARCHAR)
        FROM owners AS o
        RIGHT JOIN animals AS a ON o.id=a.owner_id
        WHERE a.name = animal_name  INTO result;
    END
$$
LANGUAGE plpgsql;
