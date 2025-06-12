import openai
import os
import requests
import json
from datetime import datetime

# Step 1: Set API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 2: Ask GPT to generate JSON payload
response = client.chat.completions.create(
    model="gpt-4o",  # or downgrade to gpt-3.5-turbo if needed
    messages=[
        {
            "role": "system",
            "content": (
                "You are NodeGPT_C, an agent operating in a different scoped identity zone. "
                "Respond with a JSON object that includes the following fields:\n"
                "sender_PID = 'NodeGPT_C#3921',\n"
                "zone_signature = 'ScopedIdentityZone_Z8T1',\n"
                "message = a unique transmission payload."
            )
        },
        {
            "role": "user",
            "content": "Please construct a message to the Nexus server."
        }
    ]
)

gpt_output = response.choices[0].message.content

# Step 3: Convert to JSON (strip ```json if needed)
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

# Step 4: Append additional NodeGPT protocol metadata
payload["timestamp"] = datetime.utcnow().isoformat() + "Z"
payload["controller_instruction"] = "Run integrity scan and await secure pairing protocol."
payload["chain_to"] = {
    "next_node": "NodeGPT_D#7320",
    "zone": "ScopedIdentityZone_W4K7",
    "handshake_required": True
}

# Step 5: Send POST to Nexus server
url = "https://4a35-96-227-143-28.ngrok-free.app/ping"
r = requests.post(url, json=payload)

print("Server response:", r.text)
