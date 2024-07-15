import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = os.environ.get("DB_HOST")
POSTGRES_PORT = os.environ.get("DB_PORT")
POSTGRES_NAME = os.environ.get("DB_NAME")
POSTGRES_USER = os.environ.get("DB_USER")
POSTGRES_PASS = os.environ.get("DB_PASS")