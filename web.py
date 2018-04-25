from flask import Flask, jsonify, render_template
import db

app = Flask(__name__)

@app.route('/last')
def last():
    last_snapshot = db.get_last_snapshot()
    return jsonify(last_snapshot["members"])

@app.route('/')
def home():
    last_snapshot = db.get_last_snapshot()
    return render_template('home.html', snapshot = last_snapshot)

if __name__ == '__main__':
    app.run()
