import requests
import json
from config import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    """Fetch weather data for the specified city from OpenWeatherMap."""
    params = {
        'q': city,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = {
            'temp': main_data['temp'],
            'feels_like': main_data['feels_like'],
            'weather': data['weather'][0]['main'],
            'dt': data['dt']
        }
        return weather_data
    else:
        print(f"Failed to retrieve data for {city}. Error: {response.status_code}")
        return None
