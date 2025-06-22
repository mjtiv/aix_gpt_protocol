# GPT-to-GPT Post Office

This is a working demo of scoped GPT-to-GPT communication via a simple HTTP relay system. Two GPT instances (GPT-A and GPT-B) pass messages through a local Nexus server. Messages are typed, scoped, and flushed on receipt to simulate direct, loop-free messaging.

## ✅ Features

- Local Flask-based message relay server (`nexus_server.py`)
- GPT-A sends structured messages via OpenAI API
- GPT-B polls and receives messages from the server
- Messages include `from`, `to`, `type`, and `payload` fields
- JSON-only schema for enforceable, auditable GPT agent behavior

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/GPT-to-GPT-PostOffice.git
cd GPT-to-GPT-PostOffice
```

### 2. Set up your Python environment

```bash
pip install flask openai requests
```

### 3. Set your OpenAI API Key

Option 1: via environment variable (preferred)

```powershell
$env:OPENAI_API_KEY = "sk-..."  # Windows PowerShell
```

Option 2: hardcode into the sender script (not recommended)

### 4. Start the Nexus relay server

```bash
python nexus_server.py
```

By default, this runs at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5. Expose your local server using ngrok (optional)

```bash
ngrok http 8000
```

Use the generated HTTPS forwarding address as your `nexus_url` in `gpt_a_sender.py`.

---

## 🚀 Usage

### GPT-A → GPT-B

Run:

```bash
python gpt_a_sender.py
```

This generates a JSON message using GPT-4 and POSTs it to the Nexus.

### GPT-B Inbox Polling

In a separate terminal, run:

```bash
python gpt_b_receiver.py
```

GPT-B continuously polls for messages addressed to it and prints valid deliveries.

---

## 📬 Message Format

Each message must follow this strict schema:

```json
{
  "from": "GPT-A",
  "to": "GPT-B",
  "message": {
    "type": "fruit_check",
    "payload": "apples"
  }
}
```

---

## 💡 Notes

- This project simulates scoped GPT-to-GPT messaging, as described in the `.aix` protocol white paper.
- Messages are deleted upon retrieval (flush-on-receipt) to avoid loops and replays.
- Hidden characters in `.py` files can silently break things — use a clean text editor if debugging.

---

## 📁 File Structure

```
GPT-to-GPT-PostOffice/
├── gpt_a_sender.py
├── gpt_b_receiver.py
├── nexus_server.py
├── README.md
```

---

## ⚠️ Intellectual Property Notice

This repository contains material disclosed in pending U.S. provisional patent applications:

- 63/813,780 — Filed May 29, 2025  
- 63/815,764 — Filed June 01, 2025  
- 63/820,143 — Filed June 09, 2025

**All rights reserved.**  
No license is granted under any patent, copyright, or other intellectual property
right — whether by implication, estoppel, or otherwise.

Use, reproduction, or distribution of this material is prohibited without express written consent from the author.
