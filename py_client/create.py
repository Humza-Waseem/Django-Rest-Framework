import requests


endpoint = 'http://127.0.0.1:8000/products/Create'



data = { 'title': 'Nail Polish', 'description': 'Nail Polish description', 'price': 10.00}

response = requests.post(endpoint, json=data)


print(response.status_code)
# print(response.text)

try:
    data = response.json()
    json_data = data
    print(json_data)
    
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON")
  
    data = None