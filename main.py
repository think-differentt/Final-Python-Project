# <Author> Justin Lewis Carter
# <Date> 11OCT20
# Program - This is a program that is used to get weather information from openweathermap
# and display it to the user.
#
# Some printing information taken from https://www.youtube.com/watch?v=PWZKTWJ9bJE REQ 1 - Asks the user for their
# zip code or city. REQ 2 - Use the zip code or city name in order to obtain weather forecast data from:
# http://openweathermap.org/ REQ 3 - Display the weather forecast in a readable format to the user. REQ 4 - Use
# comments within the application where appropriate in order to document what the program is doing. REQ 5 - Use
# functions including a main function. REQ 6 - Allow the user to run the program multiple times. REQ 7 - Use the
# Requests library in order to request data from the webservice. REQ 8 - Use Python 3. REQ 9 - Use try blocks when
# establishing connections to the webservice. You must print a message to the user indicating whether or not the
# connection was successful.

import requests
import json
from pprint import pprint

print("------------------Welcome to my weather application---------------------")


def weather_query():
    # Asks the user for their zip code or city
    city_name = input("Please enter your the city name:")
    # Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=b15c469fd15ac99f42fd131c12433903&units=imperial' % city_name
    current_weather = requests.get(url)
    # DISPLAY THE WEATHER FORECAST-
    data = current_weather.json()

    # Display the weather forecast in a readable format to the user.
    # Use try blocks when establishing connections.
    try:
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']

        latitude = data['coord']['lat']
        longitude = data['coord']['lon']

        description = data['weather'][0]['description']

        print('Temperature : {} degree F'.format(temp))
        print('Wind Speed : {} m/s'.format(wind_speed))
        print('Latitude : {}'.format(latitude))
        print('Longitude : {}'.format(longitude))
        print('Description : {}'.format(description))

    except KeyError:
        print("Invalid Entry, try again.")

    # Allow the user to run the program multiple times.
    x = input('Press a letter or number then ENTER to exit, otherwise press ENTER to continue:')
    if x:
        exit(0)
    else:
        weather_query()


# Use functions including a main function.
def main():
    weather_query()


main()
