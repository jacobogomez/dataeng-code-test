from sqlalchemy import Column, DateTime, Integer, String, Table

from .database import metadata_obj

department = Table(
    "department",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("department", String),
)

job = Table(
    "job",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("job", String),
)

employee = Table(
    "employee",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("datetime", DateTime),
    Column("department_id", Integer),
    Column("job_id", Integer),
)
