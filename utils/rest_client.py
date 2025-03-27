import requests
import sys
import os
from requests.generate_content_request import *

def gemini_request(body: dict, model: str, method: str, api_key: str) -> dict:
    url = f"""https://generativelanguage.googleapis.com/v1beta/models/{model}:{method}?key={api_key}"""

    response = requests.post(url = url, json = body)
    
    if response.status_code != 200:
        # Write down in db?
        ...

    return response.text

if __name__ == "__main__":
    method = "generateContent"
    model = "gemini-2.0-flash"
    api_key = os.getenv("API_KEY")

    
    

