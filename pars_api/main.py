import requests


from pprint import pprint

def request_url(url):
    return requests.get(url)

def get_residents(response: requests.Response):
    return response.json().get('residents')

def form_list(data: list):
    for id, resident in enumerate(data):
        if id == 0: symbol = ' ╔'
        elif id > 0 and id < 9: symbol = ' ╠'
        elif id == 9: symbol = ' ╚'
        
        yield f' {symbol} {id+1} {resident}'

def main():
    url_planets = 'https://swapi.py4e.com/api/planets/1/'
    url_search = 'https://swapi.py4e.com/api/people/?search={q}'
    response_planets = request_url(url_planets)
    
    
    if response_planets.status_code == 200:

        residents = get_residents(response_planets)
        if residents:
            print(f"Персонажи:")
            for step in form_list(residents):
                print(step)
        else: 
            return 'Не нашел персонажей'
        
        response_search = request_url(url_search.format(q='Luke'))
        
        print('\n')

        if response_search.status_code == 200:
            print(f'Запрос по {response_search.url}')
            pprint(response_search.json())
            print('\n')
            response_planet = request_url(response_search.json()['results'][0]['homeworld'])
            print(f"Диаметр планеты {response_planets.json()['name']} = {response_planet.json()['diameter']}")

        return 'finish'

    else:
        return f'ERROR {response_planets.status_code}'


if __name__ == '__main__':
    print(main())