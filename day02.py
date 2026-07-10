import os
from dotenv import load_dotenv
from groq import Groq

# Load API Key
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found!")

# Create Groq Client
client = Groq(api_key=my_api_key)

# User Input
temperature = float(input("Enter temperature (0-2): "))

# Model
model = "llama-3.3-70b-versatile"

# Messages
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI tutor. Keep every answer within 10 words."
    },
    {
        "role": "user",
        "content": "Explain Machine Learning."
    }
]

# API Call
response = client.chat.completions.create(
    model=model,
    temperature=temperature,
    messages=messages
)

print(response.choices[0].message.content)