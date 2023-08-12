import database_config
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

url_object = URL.create(
    drivername=database_config.db_driver,
    username=database_config.db_username,
    password=database_config.db_password,
    host=database_config.db_host,
    port=database_config.db_port,
    database=database_config.db_database,
)

engine = create_engine(url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
