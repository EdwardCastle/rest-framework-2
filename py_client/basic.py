import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query": "hello world"})
print(get_response.json())
