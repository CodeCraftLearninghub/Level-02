import os
from groq import Groq

# ==========================================
# BLOCK 1: Connecting to Groq
# ==========================================
# The client reads the GROQ_API_KEY environment variable automatically
client = Groq(api_key="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")

# ==========================================
# BLOCK 2: Sample Health Parameters (Patient Data)
# ==========================================
# Simple key health indicators that a typical health report would show
patient_report = {
    "patient_name": "Spider Man (Peter Parker)",
    "age": 45,
    "blood_pressure": "145/95 mmHg",  # High (Stage 2 Hypertension)
    "fasting_blood_sugar": "135 mg/dL", # High (Diabetic range)
    "cholesterol_total": "240 mg/dL",   # High (Borderline high/high)
    "daily_activity_level": "Sedentary (Office worker)"
}

# ==========================================
# BLOCK 3: Formatting Prompt & Generating Guidance
# ==========================================
# Instruct the AI on its role and format requirements
instruction = (
    "You are an empathetic and professional AI Health Agent. Analyze the following patient health parameters "
    "and provide a meaningful, easy-to-read health summary. "
    "Format your response clearly into the following four distinct sections:\n"
    "1. 🩺 Patient Health Summary (Explain what their numbers mean in simple terms)\n"
    "2. 🚫 Top 3 Foods to Avoid (And briefly why)\n"
    "3. ✅ Top 3 Foods to Include (And briefly why)\n"
    "4. ⚠️ Key Lifestyle Precautions (Actionable daily habits)\n\n"
    "Disclaimer: Keep it factual, practical, and add a brief disclaimer that this is AI guidance and not a medical prescription.\n\n"
)

# Convert the health report dictionary into a readable text format for the AI
data_string = f"Patient Health Metrics:\n{patient_report}"

try:
    # Send the request to Groq using a fast, high-reasoning model
    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": instruction + data_string
            }
        ],
        temperature=0.2, # Very low temperature ensures highly accurate, clinical, and safe responses
    )

    # ==========================================
    # BLOCK 4: Response Display
    # ==========================================
    print("\n==========================================")
    print("👨‍⚕️ AI HEALTH AGENT REPORT")
    print("==========================================")
    print(completion.choices[0].message.content)
    print("==========================================\n")

except Exception as e:
    print(f"❌ An error occurred: {e}")
