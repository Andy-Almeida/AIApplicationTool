# Hello
import openai 
from openai import OpenAI

def Test_API_Key(api_key):
  try:
    # Test by making a request to list available engines
    ChatGPT = OpenAI(api_key=api_key)
    ChatGPT.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "user", "content": "Hello World"}
      ]
    )
    print("API key is valid!")
    return True
  except openai.APIConnectionError as e:
    print(f"Failed to connect to OpenAI API: {e}")
    pass
  except openai.AuthenticationError as e:
    print("Incorrect API key provided.\nYou can find your API key at https://platform.openai.com/account/api-keys.")
    pass
  except Exception as e:
    print(e)
    return False
    
# Prompt for the API key
key = input("Enter your ChatGPT API key: ")
if Test_API_Key(key):
  print("API key is valid!")