import requests


def main():
    params = {'lang': 'ru', 'n': '', 'T': '', 'q': '', 'M': ''}
    cities = ['Лондон', 'Шереметьево', 'Череповец']
    url_template = 'http://wttr.in/{}'
    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()


