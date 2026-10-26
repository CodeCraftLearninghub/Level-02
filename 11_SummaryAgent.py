
import os
from groq import Groq
from dotenv import load_dotenv
import json

# Load the API key from .env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_topic_summary(topic):
    prompt = f"""
    Create a student-friendly summary about: {topic}

    Return the response in the following JSON format:
    {{
        "title": "Topic title",
        "description": "Simple explanation of the topic",
        "advantages": ["Advantage 1", "Advantage 2"],
        "disadvantages": ["Disadvantage 1", "Disadvantage 2"],
        "references": [
            "Official documentation URL",
            "Reliable learning resource URL"
        ]
    }}

    Instructions:
    - Use simple English suitable for engineering students.
    - Keep the description concise and informative.
    - Provide at least 3 advantages and disadvantages.
    - Include relevant reference URLs.
    - Return only valid JSON.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are an educational content assistant. Return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"},
        temperature=0.3
    )

   
    return json.loads(response.choices[0].message.content)


def display_summary(data):
    print("\n" + "=" * 60)
    print(f"TOPIC TITLE: {data['title']}")
    print("=" * 60)

    print("\nDESCRIPTION")
    print("-" * 40)
    print(data["description"])

    print("\nADVANTAGES")
    print("-" * 40)
    for item in data["advantages"]:
        print(f"  + {item}")

    print("\nDISADVANTAGES")
    print("-" * 40)
    for item in data["disadvantages"]:
        print(f"  - {item}")

    print("\nREFERENCE RESOURCES")
    print("-" * 40)
    for url in data["references"]:
        print(f"  • {url}")

    print("\n" + "=" * 60)


def main():
    topic = input("Enter a topic to summarize: ").strip()
    try:
        print("\nGenerating summary...")
        summary = generate_topic_summary(topic)
        display_summary(summary)

    except Exception as error:
        print(f"Error generating summary: {error}")

if __name__ == "__main__":
    main()
