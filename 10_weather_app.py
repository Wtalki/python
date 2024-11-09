import requests
import json

# Function to get weather data
def get_weather(city):
    api_key = "0e750e1b90f30195afc5177f822461c6"

    base_url = "https://api.openweathermap.org/data/2.5/weather"  # Use Current Weather API for city name

    # Parameters for the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # To get temperature in Celsius; use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url,params=params)
        print(response)
        response.raise_for_status()

        weather_data = response.json()
        print(weather_data)

        city_name = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description.capitalize()}")

    except requests.exceptions.HTTPError as http_error:
        print(f"http error occured: {http_error.message}")

def main():
    print("welcome to the weather app")
    city = input("enter the name of the city")
    get_weather(city)

main()