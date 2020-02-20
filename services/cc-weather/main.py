import requests

#response = requests.get(
#    'https://api.github.com/search/repositories',
#    params={'q': 'requests+language:python'}, )

#response = requests.get(
#    'https://api.openweathermap.org/data/2.5/weather',
#    params={'q': 'London&appid=45943213061eaf57c7c9c497369686c5'}, )

api_url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = ''
city = 'London'

response = requests.get(
    api_url,
    params={'q': city, 'appid': api_key, 'units': 'imperial'} )

json_response = response.json()


#print(response.headers)
print(response.json())


## This request worked when executes w/cli
# requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=45943213061eaf57c7c9c497369686c5')don&appid=45943213061eaf57c7c9c497369686c5')