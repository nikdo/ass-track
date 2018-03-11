import logging
import os
from pymongo import MongoClient

def save_snapshot (snapshot):
    logging.info("Connecting to database on " + os.environ.get("DB_CONNECTION_STRING"))
    client = MongoClient(os.environ.get("DB_CONNECTION_STRING"))
    db=client.ass_track
    db.snapshots.insert_one(snapshot)
    logging.info("Snapshot persisted in database.")
