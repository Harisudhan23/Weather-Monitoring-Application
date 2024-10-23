import requests
import time
from collections import defaultdict
import datetime

# OpenWeatherMap API key
API_KEY = 'f7bcfb10dc468db88dd48901adaca928'

# Dictionary to store weather data for each city
weather_summary = defaultdict(list)

# Get weather data from OpenWeatherMap API
def get_weather_data(city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        data = response.json()
        return {
            'main': data['weather'][0]['main'],  # Main weather condition (Rain, Clear, etc.)
            'temp': data['main']['temp'] - 273.15,  # Convert Kelvin to Celsius
            'feels_like': data['main']['feels_like'] - 273.15,  # Convert Kelvin to Celsius
            'dt': data['dt']  # Time of the data update (Unix timestamp)
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Record weather data for a city
def record_weather(city, data):
    # Convert Unix timestamp to date
    date = datetime.datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d')
    weather_summary[city].append(data)

# Calculate daily summary for a city
def calculate_daily_summary(city):
    daily_data = weather_summary[city]
    if not daily_data:
        return None
    temps = [entry['temp'] for entry in daily_data]
    summary = {
        'average_temp': sum(temps) / len(temps),
        'max_temp': max(temps),
        'min_temp': min(temps),
        'dominant_condition': max(set([entry['main'] for entry in daily_data]), key=[entry['main'] for entry in daily_data].count)
    }
    return summary

# Check for temperature thresholds
def check_thresholds(city, data, threshold_temp=35):
    if data['temp'] > threshold_temp:
        print(f"Alert! {city} has crossed the temperature threshold: {data['temp']}°C")

# City IDs for monitoring weather in key cities
CITY_IDS = {'Delhi': 1273294, 'Mumbai': 1275339, 'Chennai': 1264527, 'Bangalore': 1277333, 'Kolkata': 1275004, 'Hyderabad': 1269843}

# Main loop to fetch and process weather data every 5 minutes
while True:
    for city, city_id in CITY_IDS.items():
        weather_data = get_weather_data(city_id)
        if weather_data:  # Check if valid data was returned
            record_weather(city, weather_data)
            check_thresholds(city, weather_data)
            
            # Print weather data for the city
            print(f"\nCurrent Weather Data for {city}:")
            print(f"Main: {weather_data['main']}")
            print(f"Temperature: {weather_data['temp']:.2f}°C")
            print(f"Feels like: {weather_data['feels_like']:.2f}°C")
            print(f"Timestamp: {datetime.datetime.fromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
            
        else:
            print(f"Failed to get data for {city}")
    
    # Wait for 5 minutes before fetching data again
    time.sleep(300)
