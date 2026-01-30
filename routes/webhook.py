from flask import Blueprint, request, jsonify
from datetime import datetime
from config.db import events_collection

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def github_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.json

    data = None

    
    if event_type == "push":
        data = {
            "request_id": payload.get("after"),
            "author": payload["pusher"]["name"],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": datetime.utcnow()
        }


    elif event_type == "pull_request":
        pr = payload["pull_request"]

        
        if pr.get("merged"):
            data = {
                "request_id": pr["id"],
                "author": pr["user"]["login"],
                "action": "MERGE",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": datetime.utcnow()
            }
        else:
            data = {
                "request_id": pr["id"],
                "author": pr["user"]["login"],
                "action": "PULL_REQUEST",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": datetime.utcnow()
            }

    if data:
        events_collection.insert_one(data)

    return jsonify({"status": "received"}), 200
