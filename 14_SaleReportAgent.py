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
# Monthly Sales Data
# -----------------------------
sales = [
    {"month":"January","sales":125000},
    {"month":"February","sales":118000},
    {"month":"March","sales":145000},
    {"month":"April","sales":162000},
    {"month":"May","sales":151000},
    {"month":"June","sales":175000}
]

sales_data = json.dumps(sales, indent=2)

prompt = f"""
You are a senior business analyst.

Analyze the following monthly sales data.

{sales_data}

Generate:

1. Executive Summary
2. Highest Sales Month
3. Lowest Sales Month
4. Sales Trend
5. Business Insights
6. Recommendations
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

print(response.choices[0].message.content)