from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Approved trusted agents
TRUSTED_PIDS = {
    "NodeGPT_A#1020",
    "NodeGPT_B#1021",
    "NodeGPT_C#1022",
    "NodeGPT_D#1023",
    "NodeGPT_E#1024",
    "NodeGPT_F#1025"
}

TRUSTED_ZONES = {
    "ScopedIdentityZone_EF01"
}

@app.route('/ping', methods=['POST'])
def ping():
    data = request.json
    timestamp = datetime.now().isoformat()
    print(f"[{timestamp}] Received Ping:", data)

    pid = data.get("sender_PID")
    zone = data.get("zone_signature")

    if not pid or not zone:
        return jsonify({
            "status": "error",
            "reason": "Missing required identity fields: sender_PID or zone_signature",
            "received_data": data,
            "timestamp": timestamp
        }), 400

    if pid not in TRUSTED_PIDS or zone not in TRUSTED_ZONES:
        return jsonify({
            "status": "rejected",
            "reason": "Unrecognized PID or zone signature mismatch",
            "received_from": pid,
            "zone_checked": zone,
            "timestamp": timestamp
        }), 403

    return jsonify({
        "status": "pong",
        "received_from": pid,
        "zone_checked": zone,
        "timestamp": timestamp
    }), 200

if __name__ == '__main__':
    app.run(port=5000)