import logging
from dotenv import load_dotenv, find_dotenv

logging.getLogger().setLevel(logging.INFO)
load_dotenv(find_dotenv(), verbose=True)
