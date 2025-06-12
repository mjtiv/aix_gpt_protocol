# .aix GPT Protocol

**Scoped GPT Messaging Architecture for Trusted Multi-Agent Communication**  
Patent-Pending | Version 1.0 | June 2025  
[Whitepaper PDF](./Scoped_GPT_Messaging_aix_WhitePaper_v1.0.pdf)  
[Author: M. Joseph Tomlinson IV]([https://www.linkedin.com/in/mjtiv](https://www.linkedin.com/in/m-joseph-tomlinson-iv-ph-d-14373b78/))

---

## 🧬 What is `.aix`?

`.aix` is a protocol and architecture for enabling secure, identity-governed communication between GPT agents.  
Each agent message includes:

- A **Persistent Identity Tag (PID)**
- A **Scoped Zone Signature**
- An **Invocation Audit Record (IAR)**

The system enforces trust boundaries, detects drift, and logs all communication for rollback, quarantine, and audit use.

This repo includes:

- 🔐 Live-tested Python server (`nexus_server_v1_trustcheck.py`)
- 🛰️ Simulated scoped Node GPTs (`gpt_node_ping_A.py` to `I.py`)
- 🧾 Whitepaper (PDF)
- 🧪 Reproducible results with rejection tests, zone validation, and agent quarantine logic

## ⚠️ Intellectual Property Notice

This repository contains material covered by **pending U.S. patent applications**:

- 63/813,780 (Filed May 29, 2025)  
- 63/815,764 (Filed May 01, 2025)  
- 63/820,143 (Filed June 09, 2025)  

All rights reserved. No license or rights are granted under any patent, copyright, or other intellectual property by implication, estoppel, or otherwise.

Use, reproduction, or distribution of this material without express written permission from the author is prohibited.
