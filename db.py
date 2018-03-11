import logging
from pymongo import MongoClient

def save_snapshot (snapshot):
    client = MongoClient("mongodb://localhost")
    db=client.ass_track
    db.snapshots.insert_one(snapshot)
    logging.info("Snapshot persisted in database.")
