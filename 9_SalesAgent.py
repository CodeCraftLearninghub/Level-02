import os
from groq import Groq

# ==========================================
# BLOCK 1: Connecting to Groq
# ==========================================
# The client automatically looks for the GROQ_API_KEY environment variable

client = Groq(api_key="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")


# ==========================================
# BLOCK 2: Mock Sales Data (5 Records)
# ==========================================
# Simple list of dictionaries representing recent sales transactions
sales_data = [
    {"date": "2026-10-21", "product": "Wireless Mouse", "quantity": 15, "revenue": 450, "region": "North"},
    {"date": "2026-10-22", "product": "Mechanical Keyboard", "quantity": 5, "revenue": 600, "region": "South"},
    {"date": "2026-10-23", "product": "4K Monitor", "quantity": 2, "revenue": 800, "region": "East"},
    {"date": "2026-10-24", "product": "Wireless Mouse", "quantity": 10, "revenue": 300, "region": "North"},
    {"date": "2026-10-25", "product": "USB-C Hub", "quantity": 20, "revenue": 500, "region": "West"}
]

# ==========================================
# BLOCK 3: Formatting Prompt & Generating Summary
# ==========================================
# Instruct the AI on its role and pass the structured sales data into the prompt
instruction = (
    "You are a helpful AI Sales Agent. Analyse the following raw sales data "
    "and provide a short, executive summary. Include the total revenue, "
    "the top-performing product, and one clear business insight.\n\n Generate the response line by line."
)

# Convert the sales data list into a readable string block for the AI
data_string = f"Sales Data:\n{sales_data}"

try:
    # Send the combined prompt to Groq's fast Llama model
    response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": instruction + data_string
            }
        ],
        temperature=0.3, # Low temperature keeps the summary factual and accurate
    )

    # ==========================================
    # BLOCK 4: Response Display
    # ==========================================
    print("\n==========================================")
    print("📈 AI SALES AGENT SUMMARY")
    print("==========================================")
    print(response.choices[0].message.content)
    print("==========================================\n")

except Exception as e:
    print(f"❌ An error occurred: {e}")
