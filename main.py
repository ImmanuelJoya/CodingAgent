import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key =api_key)

# print (f"API Key: {api_key}")

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "name a few sifi-movies of all times, based on users reviews",
)

print(response.text)