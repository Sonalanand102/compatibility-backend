from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = client.models.list()

for model in models:
    print("Model name:", model.name)
    print("Description:", getattr(model, "description", "N/A"))
    print("Input token limit:", getattr(model, "input_token_limit", "N/A"))
    print("Output token limit:", getattr(model, "output_token_limit", "N/A"))
    print("-" * 50)
