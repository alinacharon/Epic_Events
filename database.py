import logging

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from config import create_db_engine, DATABASE_NAME, DATABASE_USER
from models.entities.base import Base

# Logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_database(postgres_engine):
    """Creates the database if it does not exist."""
    try:
        with postgres_engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT")
            connection.execute(
                text(f"CREATE DATABASE {DATABASE_NAME} OWNER {DATABASE_USER}"))
            logger.info(f"Database '{DATABASE_NAME}' created successfully.")
    except SQLAlchemyError as e:
        if "database \"" + DATABASE_NAME + "\" already exists" in str(e):
            logger.info(
                f"Database '{DATABASE_NAME}' already exists. No new database created.")
        else:
            logger.error(f"Error creating database: {e}")
            raise


def create_tables(engine):
    """Creates all tables in the database."""
    try:
        Base.metadata.create_all(engine)
        logger.info("Tables created successfully.")
    except SQLAlchemyError as e:
        logger.error(f"Error creating tables: {e}")
        raise


def init_database():
    """Initializes the database and creates all necessary tables."""
    postgres_engine = None
    engine = None

    try:
        # Create a connection to the default 'postgres' database
        postgres_engine = create_db_engine('postgres')

        # Create the database
        create_database(postgres_engine)

        # Connect to the created or existing database
        engine = create_db_engine()

        # Create tables
        create_tables(engine)

    except SQLAlchemyError as e:
        logger.error(f"An error occurred during database initialization: {e}")
        raise

    finally:
        if postgres_engine:
            postgres_engine.dispose()
        if engine:
            engine.dispose()


def reset_database():
    """Delete all tables and recreate them."""
    engine = create_db_engine()
    try:
        Base.metadata.drop_all(engine)
        logger.info("All tables dropped successfully.")
        Base.metadata.create_all(engine)
        logger.info("All tables recreated successfully.")
    except SQLAlchemyError as e:
        logger.error(f"Error resetting database: {e}")
        raise
    finally:
        engine.dispose()


if __name__ == "__main__":
    init_database()
