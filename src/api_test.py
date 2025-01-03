import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the OpenAI API key from the .env file
openai_api_key = os.getenv("OPEN_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key is missing. Check your .env file or environment variables.")

# Set the OpenAI API key
openai.api_key = openai_api_key

# Simple test to check the model
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can test with "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )
    print("Test response:", response)
except Exception as e:
    print("Error with OpenAI API:", e)
