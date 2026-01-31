import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import get_files_info

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key =api_key)

# print (f"API Key: {api_key}")
    # print ("Args", sys.argv)

    if len(sys.argv) <2:
        print ("Please provide a prompt as a command line argument.")
        sys.exit(1)
    
    verbose_flag = False
    if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
        print ("Verbose mode enabled.")
        verbose_flag = True    

    prompt = sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
    )
    print(response.text)
    if response is None or response.usage_metadata is None:
        print("No response or usage metadata available.")
        return
    
    if verbose_flag:
        
        print (f"User Prompt: {prompt}")
        print (f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print (f"Prompt tokens: {response.usage_metadata.prompt_token_count}")

# print (get_files_info("calculator", "pkg"))

main()
