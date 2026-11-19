import os
from dotenv import load_dotenv

load_dotenv()


class conf:
    db_host = os.getenv("DB_HOST", "localhost")
    db_name = os.getenv("DB_NAME", "sandwich_maker_api")
    db_port = int(os.getenv("DB_PORT", "3306"))
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    app_host = "localhost"
    app_port = 8000