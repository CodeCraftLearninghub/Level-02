# pip install python-dotenv
# pip install google-genai

import os
from dotenv import load_dotenv
from google import genai
load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set the GEMINI_API_KEY environment variable before running this script.")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=" write something about AI in 50 words.",
)

print(response.text)
