import requests
import json
from datetime import datetime

url = "http://127.0.0.1:5000/ping"

payload = {
    "sender_PID": "NodeGPT_G#9999",  # spoofed/unrecognized ID
    "zone_signature": "UntrustedZone_FAKE01",  # invalid zone
    "message": "Test from untrusted node attempting handshake.",
    "memory_tag": "test_invalid_pid_rejection"
}

timestamp = datetime.now().isoformat()
print(f"Sending spoofed payload at {timestamp}")
print(json.dumps(payload, indent=2))

try:
    response = requests.post(url, json=payload)
    print("Response received:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print("Request failed:", str(e))