import requests
import json
import time



api_requests_hourly = 60
api_url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = ''


cities = [
    'London',
    'Seattle',
    'Denver'
            ]

##
# The syntax of the requests param is translated:
# From: {'KEY1': YOUR_VAR, 'KEY2': 'STRING'}
# Into: ?KEY1=<YOUR_VAR>&KEY2=STRING
#
# An example is like this: https://api.endpoint.com/interesting/url?KEY1=<YOUR_VAR>&KEY2=STRING
# Like this:  requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=<api_key>')


def get_weather_metrics(city):
    print("Processing get_weather_metrics for city:", city)

    response = requests.get(
        api_url,
        params={'q': city, 'appid': api_key, 'units': 'imperial'} )

    response_json = response.json()

        # Print human readable json response
        # print(json.dumps(response_json, indent=4))

    city_temp = response_json["main"]["temp"]

    print("Temperature in", city, "=", city_temp)


request_freq = (api_requests_hourly / len(cities) * 60)
print("Updating every", request_freq, "seconds.")

while True:
    for city in cities:
        get_weather_metrics(city)

    time.sleep(request_freq)
