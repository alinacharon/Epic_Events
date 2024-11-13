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

import sentry_sdk

sentry_sdk.init(
    dsn="https://b43d7478fdd759df9d312e4bf2c091fa@o4508285593190400.ingest.de.sentry.io/4508285609377872",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    #debug=True
)

# Manually call start_profiler and stop_profiler
# to profile the code in between
sentry_sdk.profiler.start_profiler()
# this code will be profiled
#
# Calls to stop_profiler are optional - if you don't stop the profiler, it will keep profiling
# your application until the process exits or stop_profiler is called.
sentry_sdk.profiler.stop_profiler()

# Engine creation


def create_db_engine(database_name=None):
    if database_name is None:
        database_name = DATABASE_NAME
    return create_engine(
        f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{database_name}')


engine = create_db_engine()
