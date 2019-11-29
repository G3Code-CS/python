import requests

api_url = "http://shibe.online/api/shibes?count=1"
params = {"count": 5}
response = requests.get(api_url, params)

print(f"Status code is {response.status_code}")
print(response.json())
