import sys
import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    args = sys.argv[1:]
    if not args:
        print("no prompt supplied")
        sys.exit(1)
    user_prompt = " ".join(args)
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=user_prompt
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
    print(f"Response: {response.text}")
    

if __name__ == "__main__":
    main()
