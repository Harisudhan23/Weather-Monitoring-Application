import unittest
from unittest.mock import patch
from Weather_monitoring import get_weather_data, record_weather, calculate_daily_summary, check_thresholds

class TestWeatherMonitoring(unittest.TestCase):

    @patch('weather_monitoring.requests.get')
    def test_get_weather_data(self, mock_get):
        # Mock API response
        mock_response = {
            'weather': [{'main': 'Clear'}],
            'main': {'temp': 300.15, 'feels_like': 303.15},
            'dt': 1609459200  # Timestamp for 2021-01-01
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        city_id = 1273294  # Example city ID for Delhi
        data = get_weather_data(city_id)

        self.assertIsNotNone(data)
        self.assertEqual(data['main'], 'Clear')
        self.assertAlmostEqual(data['temp'], 27.0, delta=0.1)  # Kelvin to Celsius
        self.assertAlmostEqual(data['feels_like'], 30.0, delta=0.1)

    def test_record_weather(self):
        city = 'Delhi'
        weather_data = {
            'main': 'Clear',
            'temp': 27.0,
            'feels_like': 30.0,
            'dt': 1609459200
        }
        weather_summary = {}
        record_weather(city, weather_data)

        self.assertIn(city, weather_summary)
        self.assertEqual(len(weather_summary[city]), 1)
        self.assertEqual(weather_summary[city][0]['temp'], 27.0)

    def test_calculate_daily_summary(self):
        city = 'Delhi'
        weather_summary = {
            'Delhi': [
                {'temp': 27.0, 'main': 'Clear'},
                {'temp': 30.0, 'main': 'Clouds'},
                {'temp': 28.0, 'main': 'Clear'}
            ]
        }
        summary = calculate_daily_summary(city)

        self.assertIsNotNone(summary)
        self.assertAlmostEqual(summary['average_temp'], 28.33, delta=0.1)
        self.assertEqual(summary['max_temp'], 30.0)
        self.assertEqual(summary['min_temp'], 27.0)
        self.assertEqual(summary['dominant_condition'], 'Clear')

    def test_check_thresholds(self):
        city = 'Delhi'
        weather_data = {'temp': 36.0}
        with self.assertLogs(level='INFO') as log:
            check_thresholds(city, weather_data, threshold_temp=35)
            self.assertIn(f"Alert! {city} has crossed the temperature threshold", log.output[0])


if __name__ == '__main__':
    unittest.main()
