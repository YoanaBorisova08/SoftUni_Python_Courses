//1
SELECT
    CONCAT(a.address, ' ', a.address_2) AS apartment_address,
    b.booked_for AS nights
FROM
    apartments AS a
JOIN
    bookings AS b
USING
    (booking_id)
ORDER BY
    a.apartment_id

//2
SELECT
    a.name,
    a.country,
    b.booked_at::DATE
FROM
    apartments AS a
LEFT JOIN
    bookings AS b
USING
    (booking_id)
LIMIT 10;

//3
SELECT
    b.booking_id,
    b.starts_at::DATE,
    b.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM bookings as b
RIGHT JOIN customers as c
USING (customer_id)
ORDER BY
    customer_name
LIMIT 10;

//4
SELECT
    b.booking_id,
    a.name as apartment_owner,
    a.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) as customer_name
FROM bookings as b
FULL JOIN apartments as a
USING (booking_id)
    FULL JOIN customers as c
    USING (customer_id)
ORDER BY
    booking_id, apartment_owner, customer_name;

//5
SELECT
    b.booking_id,
    c.first_name as customer_name
FROM bookings as b CROSS JOIN customers as c
ORDER BY
    customer_name;

//6
SELECT
    b.booking_id,
    b.apartment_id,
    c.companion_full_name
FROM bookings as b JOIN customers as c USING (customer_id)
WHERE
    apartment_id IS NULL;

//7
SELECT
    apartment_id,
    booked_for,
    first_name,
    country
FROM bookings as b JOIN  customers as c USING (customer_id)
WHERE c.job_type = 'Lead'

//8
SELECT
    count(*)
FROM bookings as b JOIN customers as c USING (customer_id)
WHERE c.last_name = 'Hahn'

//9
SELECT
    a.name,
    sum(b.booked_for)
FROM
    apartments as a JOIN bookings as b USING (apartment_id)
GROUP BY
    a.name
ORDER BY
    a.name;

//10
SELECT
    a.country,
    count(*) as booking_count
FROM
    bookings as b
JOIN apartments as a USING (apartment_id)
WHERE
    b.booked_at > '2021-05-18 07:52:09.904+03' and b.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY
    a.country
ORDER BY
    booking_count DESC;

//11
SELECT
    country_code,
    mountain_range,
    peak_name,
    elevation
FROM
    peaks as p JOIN mountains_countries as mc USING (mountain_id)
JOIN mountains as m ON m.id = p.mountain_id
WHERE elevation > 2835 AND country_code = 'BG'
ORDER BY
    elevation DESC

//12
SELECT
    country_code,
    count(*) as "mountain_range_count"
FROM
    mountains_countries as mc
JOIN mountains as m ON m.id = mc.mountain_id
WHERE country_code IN ('US','RU', 'BG')
GROUP BY country_code
ORDER BY
    mountain_range_count DESC;

//13
SELECT
    country_name,
    river_name
FROM
    countries as c FULL JOIN countries_rivers as cr USING (country_code)
FULL JOIN rivers as r ON r.id = cr.river_id
WHERE c.continent_code = (SELECT continent_code FROM continents WHERE continent_name = 'Africa')
ORDER BY country_name
LIMIT 5;


//14
SELECT
    MIN(area) AS min_average_area
FROM (SELECT
          AVG(area_in_sq_km) AS area
      FROM countries
      GROUP BY continent_code)
    AS average_area
;

//15
SELECT
    count(*)
FROM
    countries
LEFT JOIN mountains_countries as mc USING (country_code)
WHERE
    mc.mountain_id IS NULL;

//16
CREATE TABLE monasteries(
    id INT GENERATED ALWAYS AS IDENTITY  PRIMARY KEY,
    monastery_name VARCHAR(255),
    country_code CHAR(2)
)
;
INSERT INTO monasteries(monastery_name, country_code)
VALUES   ('Rila Monastery "St. Ivan of Rila"', 'BG'),
         ('Bachkovo Monastery "Virgin Mary"', 'BG'),
         ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
         ('Kopan Monastery', 'NP'),
         ('Thrangu Tashi Yangtse Monastery', 'NP'),
         ('Shechen Tennyi Dargyeling Monastery', 'NP'),
         ('Benchen Monastery', 'NP'),
         ('Southern Shaolin Monastery', 'CN'),
         ('Dabei Monastery', 'CN'),
         ('Wa Sau Toi', 'CN'),
         ('Lhunshigyia Monastery', 'CN'),
         ('Rakya Monastery', 'CN'),
         ('Monasteries of Meteora', 'GR'),
         ('The Holy Monastery of Stavronikita', 'GR'),
         ('Taung Kalat Monastery', 'MM'),
         ('Pa-Auk Forest Monastery', 'MM'),
         ('Taktsang Palphug Monastery', 'BT'),
         ('Sümela Monastery', 'TR');
;

ALTER TABLE countries
ADD COLUMN three_rivers BOOLEAN DEFAULT FALSE;


UPDATE
    countries
SET three_rivers = (
    SELECT
        COUNT(*) > 3
    FROM
        countries_rivers as cr
    WHERE
        cr.country_code = countries.country_code)
;


SELECT
    monastery_name as monastery,
    country_name as country
FROM
    monasteries m
JOIN countries AS c
USING (country_code)
WHERE NOT c.three_rivers
ORDER BY
    monastery_name;

//17
UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO
    monasteries (monastery_name, country_code)
VALUES ('Hanga Abbey', (SELECT country_code FROM countries WHERE country_name = 'Tanzania')),
       ('Myin-Tin-Daik', (SELECT country_code FROM countries WHERE country_name ='Myanmar'))
;

SELECT
    con.continent_name,
    cou.country_name,
    count(m.country_code) AS monasteries_count

FROM countries as cou
    JOIN continents as con USING(continent_code)
    LEFT JOIN monasteries AS m
    USING(country_code)
WHERE
    NOT cou.three_rivers
GROUP BY cou.country_name,
         con.continent_name
ORDER BY
    monasteries_count DESC,
    country_name;




//18
SELECT
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE
    schemaname = 'public'
ORDER BY
    tablename,
    indexname

//19
CREATE VIEW
    continent_currency_usage
AS
SELECT
    ranked.continent_code,
    ranked.currency_code,
    ranked.currency_usage
FROM
(
SELECT ct.continent_code,
        ct.currency_code,
        ct.currency_usage,
        DENSE_RANK() OVER (PARTITION BY ct.continent_code ORDER BY ct.currency_usage DESC) AS ranked_by_usage
 FROM (SELECT continent_code,
              currency_code,
              COUNT(currency_code) AS currency_usage
       FROM countries
       GROUP BY continent_code,
                currency_code
       HAVING COUNT(currency_code) > 1) AS ct
 ) AS ranked
WHERE
    ranked_by_usage = 1
ORDER BY
    ranked.currency_usage DESC;

//20

WITH
    "row_number"
AS
(
SELECT c.country_name,
                COALESCE(p.peak_name, '(no highest peak)')                                AS highest_peak_name,
                COALESCE(p.elevation, 0)                                                  AS highest_peak_elevation,
                COALESCE(m.mountain_range, '(no mountain)')                               AS mountain,
                ROW_NUMBER() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS row_num
         FROM countries as c
                  LEFT JOIN mountains_countries AS mc
                            USING (country_code)
                  LEFT JOIN peaks AS P
                            USING (mountain_id)
                  LEFT JOIN mountains as m
                            ON
                                m.id = p.mountain_id
)

SELECT
    country_name,
    highest_peak_name,
    highest_peak_elevation,
    mountain
FROM
    row_number
WHERE row_num = 1
ORDER BY
    country_name,
    highest_peak_elevation DESC
;