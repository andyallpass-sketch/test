import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

XAI_API_KEY = os.getenv("GROK_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

try:
    models = client.models.list()
    print("Available models:")
    for m in models.data:
        print(f"- {m.id}")
except Exception as e:
    print("Error listing models:", str(e))
