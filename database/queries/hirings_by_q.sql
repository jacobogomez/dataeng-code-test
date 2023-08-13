WITH quarterly_count AS (
    SELECT
        department.department AS department,
        job.job AS job,
        COUNT(employee.id) as count,
        EXTRACT(
            QUARTER
            FROM
                employee.datetime
        ) as q
    FROM
        employee
        LEFT JOIN department ON department.id = department_id
        LEFT JOIN job ON job.id = job_id
    WHERE
        EXTRACT (
            year
            FROM
                employee.datetime
        ) = 2021
    GROUP BY
        department,
        job,
        q
    ORDER BY
        department,
        job,
        q
)
SELECT
    department,
    job,
    MAX(
        CASE
            WHEN q = 1 THEN count
            ELSE 0
        END
    ) AS q1,
    MAX(
        CASE
            WHEN q = 2 THEN count
            ELSE 0
        END
    ) AS q2,
    MAX(
        CASE
            WHEN q = 3 THEN count
            ELSE 0
        END
    ) AS q3,
    MAX(
        CASE
            WHEN q = 4 THEN count
            ELSE 0
        END
    ) AS q4
FROM
    quarterly_count
GROUP BY
    department,
    job;