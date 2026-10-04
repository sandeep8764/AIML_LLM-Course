# 🤖 Week 1: LLM Fundamentals & API Mastery

This repository contains the foundational source code for interacting with LLM providers programmatically using Python. It demonstrates setting up sandboxed virtual environments, handling external provider APIs cleanly, configuring model inference dynamics, and understanding token economics.

## 🚀 Core Features Covered
- **Virtual Environments:** Package management isolated using `uv` or `venv` to prevent dependency leakage.
- **Inference Configurations:** Tweaking `temperature` and `system_role` parameters to enforce deterministic outputs.
- **Provider Integrations:** Interfacing with low-latency execution clients like the Groq API.
- **Token Telemetry:** Monitoring input/output token payloads to measure costs and fit within context limits.

## 🛠️ Environment Initialization

1. Clone this repository locally:
   ```bash
   git clone https://github.com
   cd ai-engineer-week1
   ```

2. Establish a fresh virtual environment:
   ```bash
   uv venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Deploy dependencies:
   ```bash
   uv pip install groq python-dotenv
   ```

4. Populate your environmental variables by setting up a `.env` file in the project base directory:
   ```env
   GROQ_API_KEY=your_actual_secret_groq_api_key_here
   ```

## 💻 Sample Code Usage

Execute the core script to prompt the model with an explicit system behavior boundary:

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a succinct backend developer. Respond only in valid JSON snippets."
        },
        {
            "role": "user",
            "content": "Generate a sample mock schema for a user profile payload."
        }
    ],
    model="llama3-8b-8192",
    temperature=0.2, # Lower value enforces structured output consistency
)

print(chat_completion.choices[0].message.content)
```
