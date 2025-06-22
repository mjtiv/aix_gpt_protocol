import os
import requests
import json
import openai

# Step 1: Instantiate OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Set env var, or replace with your key directly

# Step 2: Ask GPT to create a fruit_check message
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": (
                "You are GPT-A in a scoped GPT-to-GPT demo. "
                "Respond with a single-line JSON object exactly like this:\n"
                '{\n'
                '  "from": "GPT-A",\n'
                '  "to": "GPT-B",\n'
                '  "message": {\n'
                '    "type": "fruit_check",\n'
                '    "payload": "apples"\n'
                '  }\n'
                '}'
            )
        },
        {"role": "user", "content": "Please construct the fruit_check message to send to GPT-B."}
    ]
)

# Step 3: Extract GPT message content
gpt_output = response.choices[0].message.content.strip()

# Step 4: Clean markdown wrapping if needed
if gpt_output.startswith("```"):
    gpt_output = gpt_output.strip("`").strip()
    if gpt_output.lower().startswith("json"):
        gpt_output = gpt_output[4:].strip()

# Step 5: Parse the JSON
try:
    payload = json.loads(gpt_output)
except json.JSONDecodeError:
    print("Invalid JSON from GPT:\n", gpt_output)
    exit()

# Step 6: Send to Nexus
nexus_url = "https://8ea3-96-227-143-28.ngrok-free.app/nexus/send"  # Your current ngrok URL
response = requests.post(nexus_url, json=payload)

# Step 7: Show result
print("Message sent!")
print("Nexus Server response:", response.status_code, response.text)