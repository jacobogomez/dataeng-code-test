import database_config
from sqlalchemy import URL, Column, DateTime, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

url_object = URL.create(
    drivername=database_config.db_driver,
    username=database_config.db_username,
    password=database_config.db_password,
    host=database_config.db_host,
    port=database_config.db_port,
    database=database_config.db_database,
)

engine = create_engine(url_object)
Base = declarative_base()

connection = engine.connect()


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    department = Column(String)


class Job(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True)
    job = Column(String)


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey("department.id"))
    job_id = Column(Integer, ForeignKey("job.id"))


Department.__table__.create(bind=engine, checkfirst=True)
Job.__table__.create(bind=engine, checkfirst=True)
Employee.__table__.create(bind=engine, checkfirst=True)
