from model import Department, Employee, Job

from database import engine

Department.__table__.create(bind=engine, checkfirst=True)
Job.__table__.create(bind=engine, checkfirst=True)
Employee.__table__.create(bind=engine, checkfirst=True)
