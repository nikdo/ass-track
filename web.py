from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import config

app = Flask(__name__)

@app.route('/last')
def last():
    client = MongoClient(config.DB_CONNECTION_STRING)
    db = client.get_default_database()
    last_snapshot = db.snapshots.find().sort("_id", -1).limit(1)[0]
    return jsonify(last_snapshot["members"])

if __name__ == '__main__':
    app.run()
