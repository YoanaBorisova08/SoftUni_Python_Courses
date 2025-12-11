//1
SELECT
    title
FROM
    books
WHERE SUBSTRING(title, 1, 3) = 'The'
ORDER BY id;

//2
SELECT
    REPLACE(title, 'The', '***')
FROM
    books
WHERE LEFT(title, 3) = 'The'
ORDER BY id;

//3
SELECT
    id,
    side * height / 2 as area
FROM
    triangles
ORDER BY id;

//4
SELECT
    title,
    TRUNC(cost, 3) AS modified_price
FROM
    books
ORDER BY id;

//5
SELECT
    first_name,
    last_name,
    date_part('year', born) AS year
FROM
    authors

//7
SELECT
    title
FROM
    books
WHERE title like '%Harry Potter%'
ORDER BY id;