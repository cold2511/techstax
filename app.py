from flask import Flask, render_template, jsonify
from routes.webhook import webhook_bp
from config.db import events_collection
from bson.json_util import dumps

app = Flask(__name__)

app.register_blueprint(webhook_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def get_events():
    events = list(events_collection.find().sort("timestamp", -1).limit(10))
    return dumps(events)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
