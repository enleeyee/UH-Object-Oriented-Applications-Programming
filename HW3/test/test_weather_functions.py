import unittest
from test_weather_main import TestWeatherMain
from test_weather_variables import test_file, test_data_summary_year, init_global_variables
from src.main import read_weather_data, process_humidity

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

if __name__ == '__main__':
    unittest.main()
