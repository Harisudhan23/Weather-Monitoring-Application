# Weather-Monitoring-Application

   This project monitors real-time weather data using the OpenWeatherMap API and processes the data to generate daily weather summaries for selected cities. It also provides threshold-based alerts for extreme weather conditions like high temperatures. The application stores and aggregates weather data, such as average temperature, max/min temperature, and dominant weather conditions.

## Table of Contents
   Description
   Setup Instructions
   Usage
   API Key Setup
   Examples
   Test Cases
   Limitations
   License

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/Harisudhan23/weather-monitoring.git

   ```bash
   cd weather-monitoring
   
3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   
3.Run and Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   python weather_monitoring.py
   ```
## API Key Setup

   This application requires an API key from OpenWeatherMap to fetch real-time weather data.
   Sign up at (https://openweathermap.org/) and get your API key.
   ```bash
   API_KEY = 'your_openweathermap_api_key' /f7bcfb10dc468db88dd48901adaca928
   ```
## Usage

   Monitor real-time weather data:
   The program fetches weather data for multiple cities (e.g., Delhi, Mumbai, Chennai, etc.) every 5 minutes and stores it.
   Temperature is converted from Kelvin to Celsius.

   Daily summaries:
   It computes daily summaries, including the average, max, and min temperatures, and the dominant weather condition.
   
   Threshold Alerts:
   Alerts are generated if the temperature in any city crosses a defined threshold (default: 35°C).
   ```
## Examples

   Fetch Weather Data:
   ```bash
   city_id = 1273294  # Delhi
   data = get_weather_data(city_id)
   print(data)
   
   Output:
   ```bash
   {'main': 'Clear', 'temp': 27.0, 'feels_like': 30.0, 'dt': 1609459200}

   Check Temperature Thresholds:
   ```bash
   check_thresholds('Delhi', {'temp': 36.0}, threshold_temp=35)

   Output:
   ```bash
   Alert! Delhi has crossed the temperature threshold: 36.0°C

   Record Weather Data:
   ```bash
   record_weather('Delhi', {'temp': 27.0, 'feels_like': 30.0, 'main': 'Clear', 'dt': 1609459200})
   
   Calculate Daily Summaries:
   ```bash
   summary = calculate_daily_summary('Delhi')
   print(summary)
   
   Output:
    ```bash
   {
    'average_temp': 28.33,
    'max_temp': 30.0,
    'min_temp': 27.0,
    'dominant_condition': 'Clear'
   }
   ```
## Test Cases

   Unit tests are included to ensure the correct functionality of the weather monitoring system. To run the tests:
   ```bash
   python -m unittest test_weather_monitoring.py
   ```
## Licence

This project is licensed under the MIT License - see the LICENSE file for details.






