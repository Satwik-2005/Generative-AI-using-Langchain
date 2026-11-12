from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Fetch available models
models = client.models.list()

for model in models:
    print("Model Name:", model.name)
    print("Supported Actions:", model.supported_actions)
    print("-" * 50)