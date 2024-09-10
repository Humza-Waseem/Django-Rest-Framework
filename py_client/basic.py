import requests

endpoint = 'http://127.0.0.1:8000/'

response = requests.get(endpoint, json={'name': 'Hamza', 'age': 20})
print(response.status_code)
print(response.text)

try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON")
    data = None
