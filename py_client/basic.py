import requests

endpoint = 'http://127.0.0.1:8000/api'

response = requests.get(endpoint)
print(response.status_code)
print(response.text)

try:
    data = response.json()
    
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON")
  
    data = None
