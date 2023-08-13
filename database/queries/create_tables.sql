CREATE TABLE IF NOT EXISTS job (
    id INTEGER NOT NULL,
    job VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS department (
    id INTEGER NOT NULL,
    department VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS employee (
    id INTEGER NOT NULL,
    name VARCHAR,
    datetime TIMESTAMP,
    department_id INTEGER,
    job_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(department_id) REFERENCES department (id),
    FOREIGN KEY(job_id) REFERENCES job (id)
);