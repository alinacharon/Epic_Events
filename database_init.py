import logging

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from database import create_db_engine, DATABASE_NAME, DATABASE_USER, Base

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_database():
    # Создание подключения к базе данных по умолчанию 'postgres'
    postgres_engine = create_db_engine('postgres')

    try:
        # Создание соединения и установка автокоммита
        with postgres_engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT")
            try:
                connection.execute(text(f"CREATE DATABASE {DATABASE_NAME} OWNER {DATABASE_USER}"))
                logger.info(f"Database '{DATABASE_NAME}' created successfully.")
            except SQLAlchemyError as e:
                if "database \"" + DATABASE_NAME + "\" already exists" in str(e):
                    logger.info(f"Database '{DATABASE_NAME}' already exists. No new database created.")
                else:
                    logger.error(f"Error creating database: {e}")
                    raise

        # Теперь подключаемся к созданной или существующей базе данных
        engine = create_db_engine()

        # Импорт моделей перед созданием таблиц
        from models.entities.user import User
        from models.entities.client import Client

        # Создание таблиц с использованием Base
        Base.metadata.create_all(engine)
        logger.info("Tables created successfully.")

    except SQLAlchemyError as e:
        logger.error(f"An error occurred: {e}")

    finally:
        postgres_engine.dispose()
        if 'engine' in locals():
            engine.dispose()


if __name__ == "__main__":
    init_database()
