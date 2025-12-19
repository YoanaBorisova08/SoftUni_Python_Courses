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

CALL sp_animals_with_owners_or_not('Hippo', '')