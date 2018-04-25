from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import config

app = Flask(__name__)

def get_last_snapshot():
    client = MongoClient(config.DB_CONNECTION_STRING)
    db = client.get_default_database()
    return db.snapshots.find().sort("_id", -1).limit(1)[0]

@app.route('/last')
def last():
    last_snapshot = get_last_snapshot()
    return jsonify(last_snapshot["members"])

@app.route('/')
def home():
    last_snapshot = get_last_snapshot()
    return render_template('home.html', snapshot = last_snapshot)

if __name__ == '__main__':
    app.run()
