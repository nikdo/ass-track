import logging
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)

IS_PRODUCTION = os.environ.get("PYTHON_ENV") == "production"
DB_CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING")

logging.getLogger().setLevel(logging.INFO if IS_PRODUCTION else logging.DEBUG)
