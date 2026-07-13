import os
import json
from dotenv import load_dotenv
from groq import Groq


# Load API Key
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Api Key Not Foune")


from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    email: str
    college: str


# Create A Client 
client=Groq(api_key=api_key)

# Select The Model
model="llama-3.3-70b-versatile"

# Take The Input 
text=input("Enter The Text:\n")

# Create the Prompt

prompt = f"""
Extract the information from the following text.

Return ONLY valid JSON.

Fields:
- name
- age
- email
- college

Text:

{text}
"""

# Create Messages

messages=[
    {
       "role":"system",
       "content":"You are an information extraction assistant. Always return only valid JSON."
        
    },
    {
        "role":"user",
        "content":prompt

        
    }
]

# Parametres
temperature=float(input("Enter The Temperatue:\n"))


#  API call
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature
)

print(response.choices[0].message.content)


# response_json = json.loads(response.choices[0].message.content)
content = response.choices[0].message.content

# Remove markdown
content = content.replace("```json", "")
content = content.replace("```", "")
content = content.strip()

response_json = json.loads(content)

student = Student.model_validate(response_json)

print(student.name)
print(student.age)
print(student.email)
print(student.college)