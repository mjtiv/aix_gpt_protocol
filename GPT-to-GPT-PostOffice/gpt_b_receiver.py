import time
import requests

recipient = "GPT-B"
nexus_url = "https://8ea3-96-227-143-28.ngrok-free.app"

while True:
    try:
        response = requests.get(f"{nexus_url}/nexus/inbox", params={"recipient": recipient})
        messages = response.json()
        
        if messages:
            print(f"\n{len(messages)} new message(s) received by {recipient}:")
            for msg in messages:
                print(msg)
        else:
            print("No new messages...")

    except Exception as e:
        print("Error fetching:", e)

    time.sleep(5)