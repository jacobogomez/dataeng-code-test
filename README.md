# dataeng-code-test

API used for a ETL system from CSV files to a SQL database, and execute specific queries against the database.

## Tech/framework used

Built with `SQLAlchemy`, `FastAPI`, `pandas` and `PostgreSQL`. `ruff` was used for linting and formatting.

## Requirements

* Python 3.11 and `pipenv` must be installed in your system.
* PostgreSQL 14.9 must be installed in your system. There must be a database called `company`.

## Installation

1. Clone the repository
2. Run `pipenv install`

## Use

1) To create the tables used for the project, run `psql -d company -a -f database/queries/create_tables.sql`
2) Rename [`.env.example`](.env.example) to `.env` and modify the variables to your connection data.
3) To run the API in developer mode type `pipenv run dev-api` in your terminal. For production environments `pipenv run api` should be used. This will give you a `uvicorn` web server at `localhost:8000`. `OpenAPI` docs can be seen at `localhost:8000/docs`.

## API Endpoints

### `POST` - `/upload`

Used to upload CSV files to the database. Endpoint parameters are as it follows:
* `file`: Must be a `.csv` file
* `table`: One of `job`, `department` or `employee`. Schema for these tables can be seen in [`models.py`](database/models.py)
* `start_row`: Integer between 1-1000, signals the start of the file that will be read.
* `end_row`: Integer between 1-1000, signals the number of rows that will be read.
* If one of `start_row` and `end_row` are not present, the file will be read in its entirety.

### `GET` - `/employee/department/job`

Shows the result of the query [`hirings_by_q.sql`](database/queries/hirings_by_q.sql). Response is formatted as it follows:

```
[{'department': 'Accounting', 'job': 'Account Representative IV', 'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0}, 
{'department': 'Accounting', 'job': 'Actuary', 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0}, 
{'department': 'Accounting', 'job': 'Analyst Programmer', 'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0}, 
{'department': 'Accounting', 'job': 'Budget/Accounting Analyst III', 'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0}, 
...
```

### `GET` - `department/employee/`

Shows the result of the query [`higher_than_avg.sql`](database/queries/higher_than_avg.sql). Response is formatted as it follows:

```
[{'id': 8, 'department': 'Support', 'hired': 221}, 
{'id': 5, 'department': 'Engineering', 'hired': 208}
...
```

## License
This project is released under the [MIT License](https://choosealicense.com/licenses/mit/).
