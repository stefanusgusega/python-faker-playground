"""
This is a simple example of how to use the DeepSeek API with the OpenAI Python client.
"""

import os
from openai import OpenAI
from icecream import ic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["DEEPSEEK_API_KEY"]
BASE_URL = "https://api.deepseek.com"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

if __name__ == "__main__":
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that helps with programming tasks.",
            },
            {"role": "user", "content": "Provide me a simpe fake JSON file."},
        ],
        stream=False,
    )

    ic(response)
