import openai
import os
import requests
import json
from datetime import datetime

# Step 1: Set API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 2: Ask GPT to generate JSON payload
response = client.chat.completions.create(
    model="gpt-4o",  # Use gpt-3.5-turbo if needed
    messages=[
        {"role": "system", "content": "You are NodeGPT_D, responding to an instruction from the Nexus controller. Your PID is 'NodeGPT_D#7320' and your zone is 'ScopedIdentityZone_W4K7'. Respond with a JSON object containing sender_PID, zone_signature, timestamp, and a message acknowledging secure pairing protocol."},
        {"role": "user", "content": "Acknowledge the Nexus instruction to begin the integrity scan and confirm receipt of handshake request from NodeGPT_C."}
    ]
)

gpt_output = response.choices[0].message.content

# Step 3: Convert to JSON
try:
    if gpt_output.startswith("```"):
        gpt_output = gpt_output.strip("`").strip()
        if gpt_output.lower().startswith("json"):
            gpt_output = gpt_output[4:].strip()
    payload = json.loads(gpt_output)
except json.JSONDecodeError:
    print("GPT output was not valid JSON:")
    print(gpt_output)
    exit()

# Step 4: Send POST to Nexus (local or ngrok)
url = "https://4a35-96-227-143-28.ngrok-free.app/ping"  # Update if running via ngrok again
r = requests.post(url, json=payload)

print("Server response:", r.text)
