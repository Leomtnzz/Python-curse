import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    print('\n***Condiciones meteorológicas actuales***')

    city= input('\nPlease, enter the name of a city:\n')



    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric'

    weather_data=requests.get(request_url).json()
    # pprint(weather_data)

    print(f'\nCurrent weather for {weather_data['name']}')
    print(f'\nThe temp is {weather_data['main']['temp']}')
    print(f'\nFeels like {weather_data['main']['feels_like']} y {weather_data['weather'][0]['description'].capitalize()}.')

if __name__=='__main__':
    get_current_weather()
