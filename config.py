import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load from .env
load_dotenv()

DATABASE_USER = os.getenv('DB_USER')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PORT = os.getenv('DB_PORT')
DATABASE_NAME = os.getenv('DB_NAME')


# Engine creation


def create_db_engine(database_name=None):
    if database_name is None:
        database_name = DATABASE_NAME
    return create_engine(
        f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{database_name}')


engine = create_db_engine()
