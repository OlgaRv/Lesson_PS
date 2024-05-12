import requests
import pprint

param = {
    'q': 'python',
}

response = requests.get('https://api.github.com/search/repositories', params=param)

response_json = response.json()
pprint.pprint(response_json)

print(f"количество репозиториев: {response_json['total_count']}")
