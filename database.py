import logging
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from config import create_db_engine, DATABASE_NAME, DATABASE_USER
from models.entities.base import Base
# Импортируем все модели, которые наследуются от Base
from models import User, Client, Event, Contract

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_database(postgres_engine):
    """Создает базу данных, если она не существует."""
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
    """Создает все таблицы в базе данных."""
    try:
        Base.metadata.create_all(engine)
        logger.info("Tables created successfully.")
    except SQLAlchemyError as e:
        logger.error(f"Error creating tables: {e}")
        raise


def init_database():
    """Инициализирует базу данных и создает все необходимые таблицы."""
    postgres_engine = None
    engine = None

    try:
        # Создание подключения к базе данных по умолчанию 'postgres'
        postgres_engine = create_db_engine('postgres')

        # Создание базы данных
        create_database(postgres_engine)

        # Подключение к созданной или существующей базе данных
        engine = create_db_engine()

        # Создание таблиц
        create_tables(engine)

    except SQLAlchemyError as e:
        logger.error(f"An error occurred during database initialization: {e}")
        raise

    finally:
        # Закрытие соединений
        if postgres_engine:
            postgres_engine.dispose()
        if engine:
            engine.dispose()


def reset_database():
    """Удаляет и пересоздает все таблицы (полезно для тестирования)."""
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
