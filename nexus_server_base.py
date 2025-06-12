from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    data = request.json
    print("Received Ping:", data)
    return jsonify({"status": "pong", "received": data}), 200

if __name__ == '__main__':
    app.run(port=5000)