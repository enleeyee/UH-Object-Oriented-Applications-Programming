import unittest
from test_weather_main import TestWeatherMain
from test_weather_variables import test_file, test_data_summary_season_year, init_global_variables
from src.main import read_weather_data_2, process_humidity_2, process_sunshine_2, process_temperature_2

class TestWeatherFunctionsTwo(unittest.TestCase):

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
        main.YEAR_LENGTH = len(test_data_summary_season_year)
        humidity_season_year = process_humidity_2(test_data_summary_season_year)

        self.assertIsInstance(humidity_season_year, dict)
        self.assertIn('warm', humidity_season_year)
        self.assertIn('cold', humidity_season_year)

        for season in ['warm', 'cold']:
            self.assertIsInstance(humidity_season_year[season], dict)
            self.assertEqual(set(humidity_season_year[season].keys()), set(main.WEATHER_YEARS))

        expected_humidities = {
            'warm': {main.WEATHER_YEARS[i]: test_data_summary_season_year[i]['warm']['a_humidity']
                     for i in range(main.YEAR_LENGTH)},
            'cold': {main.WEATHER_YEARS[i]: test_data_summary_season_year[i]['cold']['a_humidity']
                     for i in range(main.YEAR_LENGTH)},
        }

        self.assertEqual(humidity_season_year, expected_humidities)

    def test_process_sunshine_2(self):
        season_sunshine_ratios = process_sunshine_2(test_data_summary_season_year)
        
        for season in ['warm', 'cold']:
            smallest_sunshine_ratio, largest_sunshine_ratio = season_sunshine_ratios[season]
            self.assertTrue(smallest_sunshine_ratio <= largest_sunshine_ratio)

    def test_process_temperature_2(self):
        from src import main
        main.WEATHER_YEARS, main.YEAR_LENGTH = init_global_variables()
        season_temperature_lists = process_temperature_2(test_data_summary_season_year)

        for season in ['warm', 'cold']:
            avg_temps, min_temps, max_temps, hot_ratios = season_temperature_lists[season]
            self.assertEqual(len(avg_temps), main.YEAR_LENGTH)
            self.assertEqual(len(min_temps), main.YEAR_LENGTH)
            self.assertEqual(len(max_temps), main.YEAR_LENGTH)
            self.assertEqual(len(hot_ratios), main.YEAR_LENGTH)
