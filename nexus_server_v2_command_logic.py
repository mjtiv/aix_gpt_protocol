from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    data = request.get_json()

    sender_pid = data.get("sender_PID", "")
    zone_signature = data.get("zone_signature", "")

    if sender_pid.startswith("NodeGPT_B"):
        reply = {
            "command": "UpdateProtocol_v2.1",
            "status": "approved"
        }
    elif zone_signature == "Alpha_Zone_456":
        reply = {
            "command": "RetaskNode",
            "status": "reassignment_pending"
        }
    else:
        reply = {
            "command": "HoldPosition",
            "status": "review"
        }

    return jsonify({
        "received": data,
        "response": reply
    })

if __name__ == '__main__':
    app.run(port=5000)