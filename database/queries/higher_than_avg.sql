WITH hirings_2021 AS (
    SELECT
        department.id as id,
        department.department as department,
        COUNT(employee.id) as hired
    FROM
        employee
        LEFT JOIN department ON department.id = department_id
    WHERE
        EXTRACT (
            year
            FROM
                employee.datetime
        ) = 2021
    GROUP BY
        department.id
    ORDER BY
        hired DESC
)
SELECT
    id,
    department,
    hired
FROM
    hirings_2021
WHERE
    hired > (
        SELECT
            AVG(hired)
        FROM
            hirings_2021
    )