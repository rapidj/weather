import requests

headers = {'Accept-Language': 'ru-RU'}
params = {'lang': 'ru', 'n': '', 'T': '', 'q': '', 'M': ''}
cities = ['Лондон', 'Шереметьево', 'Череповец']
# url_template = 'http://wttr.in/{}?nTqmM&lang=ru'
url_template = 'http://wttr.in/{}'
for city in cities:
    url = url_template.format(city)
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    print(response.text)