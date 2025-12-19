--1
CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR(50), last_name VARCHAR(50))
RETURNS VARCHAR(101)
AS
$$
    DECLARE
        full_name VARCHAR(101);
    BEGIN
        full_name := CONCAT(INITCAP(LOWER(first_name)), ' ', INITCAP(LOWER(last_name)));
        RETURN full_name;
    END
$$
LANGUAGE plpgsql;

--2
CREATE FUNCTION fn_calculate_future_value(initial_sum DECIMAL, yearly_interest_rate DECIMAL, number_of_years INT)
RETURNS DECIMAL
AS
$$
    BEGIN
        RETURN TRUNC(initial_sum*POWER(1+yearly_interest_rate, number_of_years), 4);
    END
$$
LANGUAGE plpgsql;

--3
CREATE OR REPLACE FUNCTION fn_is_word_comprised (set_of_letters VARCHAR(50), word VARCHAR(50))
RETURNS BOOLEAN
AS
$$
    DECLARE
        i INT;
        letter CHAR(1);
    BEGIN
        for i IN 1..LENGTH(word) LOOP
            letter := SUBSTRING(LOWER(word), i, 1);
            IF POSITION(letter IN LOWER(set_of_letters)) = 0 THEN
                RETURN FALSE;
            END IF;
        END LOOP;
        RETURN TRUE;
    END
$$
LANGUAGE plpgsql;



--3.2
CREATE OR REPLACE FUNCTION fn_is_word_comprised (set_of_letters VARCHAR(50), word VARCHAR(50))
RETURNS BOOLEAN
AS
$$
    BEGIN
        RETURN TRIM(LOWER(word), LOWER(set_of_letters)) = '';
    END
$$
LANGUAGE plpgsql;

//4
CREATE OR REPLACE FUNCTION fn_is_game_over(is_game_over BOOLEAN)
RETURNs TABLE(
    name VARCHAR(50),
    game_type_id INT,
    is_finished BOOLEAN)
AS
$$
    BEGIN
        RETURN QUERY SELECT
                          g.name,
                          g.game_type_id,
                          g.is_finished
                      FROM games as g
                      WHERE g.is_finished = is_game_over;
    END
$$
LANGUAGE plpgsql
;


--5
CREATE OR REPLACE FUNCTION fn_difficulty_level(level INT)
RETURNS VARCHAR
AS
$$
    DECLARE
        difficulty_level VARCHAR(20);
    BEGIN
        CASE
            WHEN level <= 40 THEN difficulty_level := 'Normal Difficulty';
            WHEN level <=60 THEN difficulty_level := 'Nightmare Difficulty';
            ELSE difficulty_level := 'Hell Difficulty';
        END CASE;
        RETURN difficulty_level;
    END
$$
LANGUAGE plpgsql;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level) AS difficulty_level
FROM users_games
ORDER BY
    user_id;

--6
CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
    game_name VARCHAR(50)
)
RETURNS table(total_cash DECIMAL)
AS
$$
    BEGIN
        RETURN QUERY
            WITH ranked_games
            AS
            (
            SELECT cash,
                ROW_NUMBER() OVER (ORDER BY cash DESC ) AS row_num
            FROM games as g
            JOIN users_games as ug
            ON ug.game_id = g.id
            WHERE g.name = game_name
            )
            SELECT (ROUND(SUM(cash), 2)) AS total_cash
            FROM ranked_games
            WHERE row_num%2<>0;
    END
$$
LANGUAGE plpgsql;


--7
CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS
$$
    DECLARE
        holder_info RECORD;
    BEGIN
        FOR holder_info IN
            SELECT
                CONCAT(ac.first_name, ' ', ac.last_name) AS full_name,
                SUM(balance) AS total_balance
            FROM accounts AS a
            JOIN account_holders AS ac
            ON ac.id = a.account_holder_id
            GROUP BY full_name
            HAVING SUM(balance) > searched_balance
            ORDER BY full_name
        LOOP
            RAISE NOTICE '% - %', holder_info.full_name, holder_info.total_balance;
        END LOOP;

    END;
$$
LANGUAGE plpgsql;

--8
CREATE OR REPLACE PROCEDURE sp_deposit_money(account_id INT, money_amount NUMERIC(10, 4))
AS
$$
    BEGIN
        UPDATE accounts
        SET balance = balance + money_amount
        WHERE id = account_id;
    END
$$
LANGUAGE plpgsql;

--9
CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INT, money_amount NUMERIC(10, 4))
AS
$$
    DECLARE
        curr_balance NUMERIC;
    BEGIN
        curr_balance := (SELECT balance FROM accounts WHERE id = account_id);
        IF curr_balance>=money_amount THEN
            UPDATE accounts
            SET balance = curr_balance - money_amount
            WHERE  id = account_id;
        ELSE
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
        end if;

    END
$$
LANGUAGE plpgsql;

--10
CREATE OR REPLACE PROCEDURE sp_transfer_money(sender_id INT, receiver_id INT, amount NUMERIC)
AS
$$
    DECLARE
        curr_balance NUMERIC;
    BEGIN
        SELECT balance INTO curr_balance FROM accounts WHERE id=sender_id;
        IF(curr_balance>=amount) THEN
            CALL sp_withdraw_money(sender_id, amount);
            CALL sp_deposit_money(receiver_id, amount);
        END IF;
    END
$$
LANGUAGE plpgsql;


--11
DROP PROCEDURE sp_retrieving_holders_with_balance_higher_than

--12
CREATE TABLE IF NOT EXISTS logs(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    account_id INT,
    old_sum NUMERIC,
    new_sum NUMERIC
)

CREATE OR REPLACE FUNCTION
    trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER AS
$$
    BEGIN
        INSERT INTO logs(account_id, old_sum, new_sum)
            VALUES
        (OLD.id, OLD.balance, NEW.balance);
        RETURN NEW;
    END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_account_balance_change
AFTER UPDATE OF balance ON accounts
FOR EACH ROW
WHEN (NEW.balance <> OLD.balance) EXECUTE FUNCTION trigger_fn_insert_new_entry_into_logs();


//13
CREATE TABLE IF NOT EXISTS notification_emails(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    recipient_id INT,
    subject TEXT,
    body TEXT
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER AS
$$
    DECLARE
        subject TEXT;
        body TEXT;
    BEGIN
        subject := format('Balance change for account: %s', NEW.account_id);
        body := format('On %s your balance was changed from %s to %s.', CURRENT_DATE, new.old_sum, new.new_sum);
        INSERT INTO notification_emails(recipient_id, subject, body)
        VALUES (new.account_id, subject, body );
        RETURN NEW;
    END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs
FOR EACH ROW EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();
