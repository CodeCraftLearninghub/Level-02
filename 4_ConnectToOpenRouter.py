import os

from openai import OpenAI


api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("Set the OPENROUTER_API_KEY environment variable before running this script.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

completion = client.chat.completions.create(
    model="google/gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": " write something about AI in 50 words.",
        }
    ],
)

print(completion.choices[0].message.content)
