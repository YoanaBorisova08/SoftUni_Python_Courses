--HOW TO CREATE FUNCTION
--1
CREATE OR REPLACE FUNCTION fn_get_initials(varchar, varchar)
RETURNS  varchar(5)
AS
$$
    BEGIN
        RETURN concat(left($1, 1), '.', left($2, 1), '.');
    END
$$
LANGUAGE plpgsql;

--2
CREATE OR REPLACE FUNCTION fn_get_initials(varchar, varchar)
RETURNS  varchar(5)
AS
$$
    DECLARE
        first_name ALIAS FOR $1;
        last_name ALIAS FOR $2;
    BEGIN
        RETURN concat(left(first_name, 1), '.', left(last_name, 1), '.');
    END
$$
LANGUAGE plpgsql;

--3
CREATE OR REPLACE FUNCTION fn_get_initials(first_name varchar, last_name varchar)
RETURNS  varchar(5)
AS
$$
    BEGIN
        RETURN concat(left(first_name, 1), '.', left(last_name, 1), '.');
    END
$$
LANGUAGE plpgsql;

SELECT fn_get_initials('Yoana', 'Borisova');


-- Bank transaction
CREATE OR REPLACE PROCEDURE sp_transfer_money(
    IN sender_id INT,
    IN receiver_id int,
    IN transfer_amount INT,
    OUT status varchar(50)
) AS
$$
    DECLARE
        sender_amount int;
        receiver_amount int;
        temp_value int;
    BEGIN
        SELECT bgn FROM bank WHERE id = sender_id INTO sender_amount;
        IF sender_amount < transfer_amount THEN
            status:= 'The sender does not have enough money';
            RETURN;
        END IF;
        SELECT bgn FROM BANK WHERE id= receiver_id INTO receiver_amount;
        UPDATE bank SET bgn = bgn + transfer_amount WHERE id = receiver_id;
        UPDATE bank SET bgn = bgn - transfer_amount WHERE id = sender_id;
        SELECT bgn FROM bank WHERE id = sender_id INTO temp_value;
        IF sender_amount - transfer_amount <> temp_value THEN
            status := 'Error when transfer from sender';
            ROLLBACK;
            RETURN;
        END IF;
        SELECT bgn FROM bank WHERE id = receiver_id INTO temp_value;
        IF receiver_amount + transfer_amount <> temp_value THEN
            status := 'Error when transfer to receiver';
            ROLLBACK;
            RETURN;
        END IF;
        status := 'Success';
        COMMIT;
    END
$$
LANGUAGE plpgsql;


