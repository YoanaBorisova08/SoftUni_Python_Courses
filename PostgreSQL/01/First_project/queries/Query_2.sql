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


