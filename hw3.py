import requests
import pprint

data_to_send = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data_to_send)

response_json = response.json()
print(f"Статус запроса: {response.status_code}")
pprint.pprint(response_json)
