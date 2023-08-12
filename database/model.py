from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from database import Base


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
