import requests
import json
from datetime import datetime

# Configuration
target_url = "http://127.0.0.1:5003/ping"

# JSON Payload
payload = {
    "sender_PID": "NodeGPT_E#1023",
    "zone_signature": "ScopedIdentityZone_EF01",
    "message": "Ping from NodeGPT_E to NodeGPT_F. Initiating peer test.",
    "memory_tag": "chain_test_001"
}

# Logging timestamp
timestamp = datetime.utcnow().isoformat()
print(f"Sending payload at {timestamp}")
print(json.dumps(payload, indent=4))

# POST request
response = requests.post(target_url, json=payload)
print("Response received:")
print(json.dumps(response.json(), indent=4))
