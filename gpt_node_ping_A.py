import openai
import os
import requests
import json

# Step 1: Set API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 2: Ask GPT to generate JSON payload
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a NodeGPT agent in a scoped identity zone. Respond with a JSON object that contains: sender_PID, zone_signature, and a brief message."},
        {"role": "user", "content": "Please construct a message to the Nexus server."}
    ]
)

gpt_output = response.choices[0].message.content

# Step 3: Convert to JSON
try:
    # Strip markdown-style ```json blocks if present
    if gpt_output.startswith("```"):
        gpt_output = gpt_output.strip("`").strip()
        if gpt_output.lower().startswith("json"):
            gpt_output = gpt_output[4:].strip()
    payload = json.loads(gpt_output)
except json.JSONDecodeError:
    print("GPT output was not valid JSON:")
    print(gpt_output)
    exit()

# Step 4: Send POST to Nexus
url = "https://4a35-96-227-143-28.ngrok-free.app/ping"
r = requests.post(url, json=payload)

print("Server response:", r.text)