# Import the required libraries
import os                     # Read environment variables
from dotenv import load_dotenv  # Load variables from .env
from groq import Groq           # Groq client

# Load .env file
load_dotenv()   # Calling the Function

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Check API key
if not api_key:
    raise ValueError("API KEY NOT FOUND")

# Create Groq client
client = Groq(api_key=api_key)

# Model
model = "llama-3.3-70b-versatile"

# System prompt
sysPrompt=input("System Abot TO Behave.")

# User prompt
prompt = input("Enter your prompt: ") # Take Input From User

# Messages
messages = [
    {
        "role": "system",
        "content": sysPrompt
    },
    {
        "role": "user",
        "content": prompt
    }
]

# Parameters


temperature = float(input("Enter temperature (0-2): "))

max_tokens = int(input("Enter max completion tokens: "))

# API Call
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
    max_completion_tokens=max_tokens
)

# Print AI Response
print("\nAI Response:\n")
print(response.choices[0].message.content)

# Print Token Usage
print("\nToken Usage")
print("Prompt Tokens:", response.usage.prompt_tokens)
print("Completion Tokens:", response.usage.completion_tokens)
print("Total Tokens:", response.usage.total_tokens)