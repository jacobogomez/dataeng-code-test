import os

from sqlalchemy import URL, MetaData, create_engine
from sqlalchemy.orm import sessionmaker

config_params = {
    "drivername": os.getenv("DB_DRIVER", ""),
    "username": os.getenv("DB_USERNAME", ""),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", ""),
    "port": int(os.getenv("DB_PORT", "")),
    "database": os.getenv("DB_DATABASE", ""),
}

url_object = URL.create(**config_params)

engine = create_engine(url_object)
metadata_obj = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
