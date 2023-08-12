import os

db_driver = os.getenv("DB_DRIVER", "")
db_username = os.getenv("DB_USERNAME", "")
db_password = os.getenv("DB_PASSWORD", "")
db_host = os.getenv("DB_HOST", "")
db_port = int(os.getenv("DB_PORT", ""))
db_database = os.getenv("DB_DATABASE", "")
