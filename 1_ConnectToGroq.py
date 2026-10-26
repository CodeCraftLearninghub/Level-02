# pip3 install groq

from groq import Groq
client = Groq(api_key="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")


response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models in 50 words"
        }
    ]
)

print(response)
#print(response.choices[0].message.content)