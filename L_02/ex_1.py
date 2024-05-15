# Получение данных.
# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON


import requests
import pprint

param = {
    'q': 'html',
}

response = requests.get('https://api.github.com/search/repositories', params=param)

response_json = response.json()
pprint.pprint(response_json)
