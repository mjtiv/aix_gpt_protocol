from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def receive_ping():
    data = request.get_json()
    response = {
        "status": "pong",
        "timestamp": datetime.utcnow().isoformat(),
        "received_from": data.get("sender_PID"),
        "zone_checked": data.get("zone_signature"),
        "instruction": "Peer acknowledged. No further action required."
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5003)
