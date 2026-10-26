from groq import Groq
import json
import os
from dotenv import load_dotenv

# -----------------------------
# Create Groq Client
# -----------------------------


# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# -----------------------------
# Student Marks Data
# -----------------------------
students = [
    {
        "name": "Rahul",
        "python": 92,
        "java": 84,
        "dbms": 88
    },
    {
        "name": "Priya",
        "python": 76,
        "java": 95,
        "dbms": 91
    },
    {
        "name": "Arjun",
        "python": 65,
        "java": 70,
        "dbms": 68
    }
]

# Convert JSON to String
student_data = json.dumps(students, indent=2)

# -----------------------------
# Prompt
# -----------------------------
prompt = f"""
You are an academic performance analyst.

Analyze the following student marks.

{student_data}

Provide:

1. Overall class performance
2. Best performing student
3. Weakest student
4. Subject-wise observations
5. Suggestions for improvement
6. Write the report in professional English.
"""

# -----------------------------
# Send to Groq
# -----------------------------
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)