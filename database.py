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
    try:
        # Connexion à la base de données 'postgres' par défaut
        with create_db_engine('postgres') as postgres_engine:
            # Crée la base de données
            create_database(postgres_engine)

        # Connexion à la base de données créée ou existante
        with create_db_engine() as engine:
            # Crée les tables
            create_tables(engine)

    except SQLAlchemyError as e:
        logger.error(
            f"Une erreur est survenue lors de l'initialisation de la base de données : {e}")
        raise


if __name__ == "__main__":
    init_database()
