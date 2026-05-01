import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def parse_order(text: str):
    prompt = f"""
    Extract order info as JSON:

    Input: "{text}"

    Output format:
    {{
      "dish": string,
      "no_onion": boolean,
      "spicy_level": "none" | "low" | "medium" | "high"
    }}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output[0].content[0].text