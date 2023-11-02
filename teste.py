pythonCopy code
import requests

api_url = 'https://api.koboldai.com/v1/generate-text'
api_key = 'YC0Jwj1pNh43H2kU3cil2CA'

headers = {
    'Authorization': 'Bearer ' + api_key
}

data = {
    'prompt': 'Once upon a time',
    'max_tokens': 50
}

response = requests.post(api_url, headers=headers, json=data)

print(response.json())
