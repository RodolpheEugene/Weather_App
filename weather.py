import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float

# create function to get latitude and longitude
def get_lat_lon(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json() # converts to json Object

    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

# Function to get current weather
def get_current_weather(lat, lon, API_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json() # converts to json Object
    data = WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=response.get('main').get('temp')
    )   

    return data


if __name__ == "__main__":
    lat, lon = get_lat_lon('Wauchula', 'FL', 'United States', api_key)
    print(get_current_weather(lat, lon, api_key))