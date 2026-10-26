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
patient = {
    "name": "Rahul Kumar",
    "age": 35,
    "blood_pressure": "150/95 mmHg",
    "heart_rate": 96,
    "blood_sugar": 182,
    "cholesterol": 245,
    "bmi": 29.8
}

prompt = f"""
You are a professional medical report designer.

Using the following patient information:

{patient}

Generate a COMPLETE HTML document.

Requirements:

1. Include HTML, CSS and Body.
2. Use modern CSS.
3. Use professional colors.
4. Add cards with shadow.
5. Add icons using emojis.
6. Show patient details in a table.
7. Highlight abnormal values in RED.
8. Highlight normal values in GREEN.
9. Add an "Overall Health Score" card.
10. Add Recommendations section.
11. Add Doctor Recommendation section.
12. Use responsive layout.
13. Do not include markdown.
14. Return ONLY valid HTML.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)

html = response.choices[0].message.content

with open("patient_report.html","w",encoding="utf-8") as f:
    f.write(html)

print("HTML report generated successfully!")