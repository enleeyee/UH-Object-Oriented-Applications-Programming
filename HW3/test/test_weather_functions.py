import unittest
from test_weather_main import TestWeatherMain
from test_weather_variables import test_file, test_data_summary_year, init_global_variables
from src.main import read_weather_data, process_humidity, process_sunshine, process_temperature

class TestWeatherFunctions(unittest.TestCase):

    def test_read_weather_data(self):
        summary = read_weather_data(test_file)
        TestWeatherMain().validate_summary(summary)

    def test_process_humidity(self):
        from src import main
        main.WEATHER_YEARS, main.YEAR_LENGTH = init_global_variables()
        humidity_year = process_humidity(test_data_summary_year)

        self.assertIsInstance(humidity_year, dict)
        self.assertEqual(set(humidity_year.keys()), set(main.WEATHER_YEARS))

        expected_humidities = {
            main.WEATHER_YEARS[i]: test_data_summary_year[i]['a_humidity'] for i in range(main.YEAR_LENGTH)
        }
        self.assertEqual(humidity_year, expected_humidities)

    def test_process_sunshine(self):
        smallest_sunshine_ratio, largest_sunshine_ratio = process_sunshine(test_data_summary_year)

        self.assertTrue(smallest_sunshine_ratio <= largest_sunshine_ratio)

    def test_process_temperature(self):
        from src import main
        main.WEATHER_YEARS, main.YEAR_LENGTH = init_global_variables()
        avg_temps, min_temps, max_temps, hot_ratios = process_temperature(test_data_summary_year)

        self.assertEqual(len(avg_temps), main.YEAR_LENGTH)
        self.assertEqual(len(min_temps), main.YEAR_LENGTH)
        self.assertEqual(len(max_temps), main.YEAR_LENGTH)
        self.assertEqual(len(hot_ratios), main.YEAR_LENGTH)

        self.assertEqual(avg_temps, [65.5, 72.0, 55.2])
        self.assertEqual(min_temps, [40.0, 50.0, 32.0])
        self.assertEqual(max_temps, [90.0, 95.0, 78.0])
        self.assertEqual(hot_ratios, [0.2, 0.35, 0.1])
