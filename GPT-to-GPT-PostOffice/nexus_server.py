from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)
inboxes = defaultdict(list)

@app.route("/nexus/send", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data or "to" not in data:
        return jsonify({"error": "Invalid payload"}), 400
    recipient = data["to"]
    inboxes[recipient].append(data)
    print(f"Message sent to {recipient}: {data}")
    return jsonify({"status": "delivered"}), 200

@app.route("/nexus/inbox", methods=["GET"])
def get_messages():
    recipient = request.args.get("recipient")
    if not recipient:
        return jsonify({"error": "Recipient not specified"}), 400
    messages = inboxes[recipient]
    inboxes[recipient] = []  # clear inbox after delivery
    print(f"{len(messages)} message(s) retrieved for {recipient}")
    return jsonify(messages), 200

if __name__ == "__main__":
    print("Nexus server running on http://127.0.0.1:8000")
    app.run(port=8000)