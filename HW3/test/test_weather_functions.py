import unittest
from test_weather_main import TestWeatherMain
from test_weather_variables import test_file, test_data_summary_year, init_global_variables
from src.main import read_weather_data, process_humidity, process_sunshine

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

        self.assertTrue(smallest_sunshine_ratio < largest_sunshine_ratio)
        self.assertTrue(smallest_sunshine_ratio, 0.5)
        self.assertTrue(largest_sunshine_ratio, 0.75)

if __name__ == '__main__':
    unittest.main()
