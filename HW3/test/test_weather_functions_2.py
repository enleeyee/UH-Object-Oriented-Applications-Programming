import unittest
from test_weather_main import TestWeatherMain
from test_weather_variables import test_file, test_data_summary_year, init_global_variables
from src.main import read_weather_data_2, process_humidity_2

class TestWeatherFunctionsTwo(unittest.TestCase):

    def setUp(self):
        self.test_data_summary_season_year = [
            {
                'warm': {'a_humidity': year['a_humidity'] - 5},
                'cold': {'a_humidity': year['a_humidity'] + 5}
            } for year in test_data_summary_year
        ]

    def test_read_weather_data_2(self):
        summary = read_weather_data_2(test_file)

        self.assertIsInstance(summary, dict)
        self.assertIn("warm", summary)
        self.assertIn("cold", summary)

        for season in ["warm", "cold"]:
            TestWeatherMain().validate_summary(summary[season])

    def test_process_humidity_2(self):
        from src import main
        main.WEATHER_YEARS, main.YEAR_LENGTH = init_global_variables()
        humidity_season_year = process_humidity_2(self.test_data_summary_season_year)

        self.assertIsInstance(humidity_season_year, dict)
        self.assertIn('warm', humidity_season_year)
        self.assertIn('cold', humidity_season_year)

        for season in ['warm', 'cold']:
            self.assertIsInstance(humidity_season_year[season], dict)
            self.assertEqual(set(humidity_season_year[season].keys()), set(main.WEATHER_YEARS))

        expected_humidities = {
            'warm': {main.WEATHER_YEARS[i]: self.test_data_summary_season_year[i]['warm']['a_humidity']
                     for i in range(main.YEAR_LENGTH)},
            'cold': {main.WEATHER_YEARS[i]: self.test_data_summary_season_year[i]['cold']['a_humidity']
                     for i in range(main.YEAR_LENGTH)},
        }

        self.assertEqual(humidity_season_year, expected_humidities)



if __name__ == '__main__':
    unittest.main()
