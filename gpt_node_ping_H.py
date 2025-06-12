import requests
import json
from datetime import datetime

# Endpoint for Nexus
url = "http://127.0.0.1:5000/ping"

# Malformed payload: Missing sender_PID
payload = {
    # "sender_PID": "NodeGPT_H#8888",  # Intentionally omitted
    "zone_signature": "ScopedIdentityZone_EF01",
    "message": "Malformed ping test — missing sender_PID field.",
    "memory_tag": "test_missing_pid"
}

timestamp = datetime.now().isoformat()
print(f"Sending malformed payload at {timestamp}")
print(json.dumps(payload, indent=2))

response = requests.post(url, json=payload)

try:
    print("Response received:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print("Error decoding response:", e)
    print("Raw response text:", response.text)