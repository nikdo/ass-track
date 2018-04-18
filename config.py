import logging
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)

IS_PRODUCTION = os.environ.get("PYTHON_ENV") == "production"
DB_CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING")

if IS_PRODUCTION:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(format='%(levelname)s %(message)s')
    logging.getLogger().setLevel(logging.DEBUG)
