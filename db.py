import logging
from pymongo import MongoClient

import config

def save_snapshot (snapshot):
    logging.debug("Connecting to database on " + config.DB_CONNECTION_STRING)
    client = MongoClient(config.DB_CONNECTION_STRING)
    db = client.get_default_database()
    db.snapshots.insert_one(snapshot)
    logging.debug("Snapshot persisted in database.")
