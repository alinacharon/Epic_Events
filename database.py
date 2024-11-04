import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Создание базового класса для декларативных моделей
Base = declarative_base()

# Получение данных подключения из переменных окружения
DATABASE_USER = os.getenv('DB_USER', 'admin')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD', 'mypassword')
DATABASE_HOST = os.getenv('DB_HOST', 'localhost')
DATABASE_PORT = os.getenv('DB_PORT', '5432')
DATABASE_NAME = os.getenv('DB_NAME', 'database')


# Функция для создания движка базы данных
def create_db_engine(database_name=None):
    if database_name is None:
        database_name = DATABASE_NAME
    return create_engine(
        f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{database_name}')


# Создание движка для основной базы данных
engine = create_db_engine()
