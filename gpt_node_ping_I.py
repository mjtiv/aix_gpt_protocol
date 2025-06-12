import requests
from datetime import datetime

url = "http://127.0.0.1:5000/ping"
timestamp = datetime.now().isoformat()

print(f"Sending raw invalid payload at {timestamp}")

# Send a raw string instead of a JSON object
invalid_data = "This is not a JSON payload."

headers = {
    "Content-Type": "text/plain"  # Purposely wrong content-type
}

response = requests.post(url, data=invalid_data, headers=headers)

print("Response received:")
print("Status Code:", response.status_code)
print("Raw Text:", response.text)