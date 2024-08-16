import requests
import pprint

params = {
    'userId': '1',
}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

response_json = response.json()
print(f"Статус запроса: {response.status_code}")
pprint.pprint(response_json)
