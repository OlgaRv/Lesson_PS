# представление содержимого запроса в виде словаря

import requests
import pprint

param = {
    'q': 'python',
}

response = requests.get('https://api.github.com/search/repositories', params=param)

response_json = response.json()
pprint.pprint(response_json)

print(f"количество репозиториев: {response_json['total_count']}")


#  сохранение изображения по ссылке в файл

img ="https://img.freepik.com/premium-photo/colorful-flower-wallpapers-hd-wallpapers_802639-6371.jpg?w=1380"

response = requests.get(img)
with open("test.jpg", "wb") as f:
    f.write(response.content)



import requests

# пример get-запроса
response = requests.get('https://google.com')

print(response.status_code)
print(response.headers)
print(response.text)

# пример post-запроса

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "тестовый post запрос",
    "body": "тестовый текст",
    "userid": 2
}
response = requests.post(url, data=data)
print(response.status_code)
print(f"ответ - {response.json()}")