import os
import sentry_sdk

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load from .env
load_dotenv()

# Sentry configuration
def init_sentry():
    """Sentry inisialization"""
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
    )


SENTRY_DSN = os.getenv('SENTRY_DSN')

# DB configuration
DATABASE_USER = os.getenv('DB_USER')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_HOST = os.getenv('DB_HOST')
DATABASE_PORT = os.getenv('DB_PORT')
DATABASE_NAME = os.getenv('DB_NAME')


def create_db_engine(database_name=None):
    """Create a SQLAlchemy engine for the specified database."""
    if database_name is None:
        database_name = DATABASE_NAME
    return create_engine(
        f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{database_name}')


# Create the database engine
engine = create_db_engine()
