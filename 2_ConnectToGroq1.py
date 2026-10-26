

from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# Your prompt
prompt = "give me 3 tips to sell my product."

# Send request
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role":"system",
            "content":"Answer every question humorously."
        },
        {
            "role":"user",
            "content":prompt
        }
]
)

# Print response
print(response.choices[0].message.content)

