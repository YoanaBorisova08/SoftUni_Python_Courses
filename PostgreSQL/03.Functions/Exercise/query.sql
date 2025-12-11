//1
CREATE VIEW
    view_river_info
AS
SELECT
    CONCAT_WS(
            ' ',
            'The river',
            river_name,
            'flows into the',
            outflow,
            'and is',
            "length",
            'kilometers long.') AS "River Information"
FROM
    rivers
ORDER BY
    river_name
;

//2
CREATE VIEW
    view_continents_countries_currencies_details
AS
SELECT
    CONCAT_WS(': ',
            con.continent_name,
            con.continent_code) AS continent_details,
    CONCAT_WS(' - ',
            cou.country_name,
            cou.capital,
            cou.area_in_sq_km,
           'km2') AS country_information,
    CONCAT(cu.description, ' (', cu.currency_code, ')')
        AS currencies
FROM
    continents AS con,
    countries AS cou,
    currencies AS cu
WHERE
    con.continent_code = cou.continent_code
        AND
    cou.currency_code = cu.currency_code
ORDER BY
    country_information,
    currencies
;

//3
ALTER TABLE countries
ADD COLUMN
    capital_code CHAR(2)
;

UPDATE
    countries
SET
    capital_code = SUBSTRING(capital, 1, 2)
RETURNING *;

//4
SELECT
    RIGHT(description, -4) AS substring
FROM
    currencies;

//5
SELECT
    SUBSTRING("River Information", '([0-9]{1,4})' ) AS river_length
FROM
    view_river_info;

//6
SELECT
     REPLACE(mountain_range, 'a', '@') AS "replace_a",
     REPLACE(mountain_range, 'A', '$') AS "replace_A"
FROM
    mountains

//7
SELECT
    capital,
    TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM
    countries;

//8
SELECT
    continent_name,
    TRIM(LEADING FROM continent_name) AS "trim"
FROM
    continents;

//9
SELECT
    continent_name,
    TRIM(TRAILING FROM continent_name) AS "trim"
FROM
    continents;

//10
SELECT
    LTRIM(peak_name, 'M') AS left_trim,
    RTRIM(peak_name, 'm') AS right_trim
FROM
    peaks;

//11
SELECT
    CONCAT(m.mountain_range, ' ', p.peak_name) as mountain_information,
    CHAR_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS characters_length,
    BIT_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS bits_of_a_tring
FROM
    mountains as m,
    peaks as p
WHERE
    m.id = p.mountain_id
;

//12
SELECT
    population,
    LENGTH(CAST(population AS VARCHAR)) AS length
FROM
    countries

//13
SELECT
    peaks.peak_name,
    LEFT(peak_name, 4) AS positive_left,
    LEFT(peak_name, -4) AS negative_left
FROM
    peaks;

//14
SELECT
    peaks.peak_name,
    RIGHT(peak_name, 4) AS positive_right,
    RIGHT(peak_name, -4) AS negative_right
FROM
    peaks;

//15
UPDATE
    countries
SET
    iso_code = UPPER(LEFT(country_name, 3))
WHERE
    iso_code IS NULL;

//16
UPDATE countries
SET country_code = LOWER(REVERSE(country_code))

//17
SELECT
    CONCAT_WS(' ', elevation,
           CONCAT(REPEAT('-', 3), REPEAT('>', 2)),
           peak_name) AS "Elevation --->> Peak Name"
FROM peaks
WHERE
    elevation >= 4884

//18
CREATE TABLE
    bookings_calculation
AS
SELECT
    booked_for
FROM bookings
WHERE apartment_id = 93
;

ALTER TABLE
    bookings_calculation
ADD COLUMN
    "multiplication" numeric,
ADD COLUMN
    "modulo" numeric
;

UPDATE
    bookings_calculation
SET
    multiplication = 50*booked_for,
    modulo = booked_for % 50
;

//19
SELECT
    latitude,
    ROUND(latitude, 2) AS round,
    TRUNC(latitude, 2) AS trunc
FROM
    apartments;

//20
 SELECT
    longitude,
    @ longitude AS abs
FROM
    apartments;


//21
ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPTZ
    DEFAULT CURRENT_TIMESTAMP;


SELECT
    TO_CHAR(billing_day, 'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS') AS "Biling Day"
FROM bookings;

//22
SELECT
    EXTRACT(YEAR FROM booked_at) AS YEAR,
    EXTRACT(MONTH FROM booked_at) AS MONTH,
    EXTRACT(DAY FROM booked_at) AS DAY,
    EXTRACT(HOUR FROM booked_at) AS HOUR,
    EXTRACT(MINUTE FROM booked_at) AS MINUTE,
    CEIL(EXTRACT(SECOND FROM booked_at) ) AS SECOND
FROM
    bookings;

//23
SELECT
    user_id,
    AGE(starts_at, booked_at) "Early Birds"
FROM
    bookings
WHERE
        AGE(starts_at, booked_at) >= INTERVAL '10 months';

//24
SELECT
    companion_full_name,
    email
FROM
    users
WHERE
    companion_full_name ILIKE '%aNd%'
    AND
    email NOT LIKE '%@gmail'
;

//25
SELECT
    LEFT(first_name, 2) AS initials,
    COUNT('initials') AS user_count
FROM
    users
GROUP BY
    initials
ORDER BY
    user_count DESC,
    initials ASC;

//26
SELECT
    SUM(booked_for) AS total_value
FROM
    bookings
WHERE
    apartment_id = 90;

//27
SELECT
    AVG(multiplication) AS average_value
FROM
    bookings_calculation;