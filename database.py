import sqlalchemy as db
from sqlalchemy import create_engine, text
from models.entities.entities import metadata 
from sqlalchemy.exc import ProgrammingError

# Set connection data
DATABASE_USER = 'admin'
DATABASE_PASSWORD = 'mypassword'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
DATABASE_NAME = 'database'

# Create a connection to the default 'postgres' database
engine = create_engine(f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/postgres')

# Create a connection and set autocommit to true
with engine.connect() as connection:
    connection.execution_options(isolation_level="AUTOCOMMIT")  # Enable autocommit mode
    # Try to create the database
    try:
        connection.execute(text(f"CREATE DATABASE {DATABASE_NAME} OWNER {DATABASE_USER}"))
        #print(f"Database '{DATABASE_NAME}' created successfully.")
    except ProgrammingError as e:
        # Check if the error is because the database already exists
        if "database \"" + DATABASE_NAME + "\" already exists" in str(e):
            pass
            print(f"Database '{DATABASE_NAME}' already exists. No new database created.")
        else:
            print(f"Error creating database: {e}")

# Now connect to the created or existing database
engine = create_engine(f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')

# Create tables 
metadata.create_all(engine) 
print("Tables created successfully.")
