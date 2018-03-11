import logging
import os
from dotenv import load_dotenv, find_dotenv

logging.getLogger().setLevel(logging.INFO)
load_dotenv(find_dotenv(), verbose=True)

IS_PRODUCTION = os.environ.get("PYTHON_ENV") == "production"
