import unittest
from src.main import to_float, read_weather_data, process_humidity, process_sunshine, process_temperature

test_data_summary_year = [
    {
        'a_temp': 65.5,
        'a_min_temp': 40.0,
        'a_max_temp': 90.0,
        'a_rainfall': 2.3,
        'a_wind': 10.5,
        'a_humidity': 70.0,
        'a_pressure': 29.92,
        'p_hot': 0.2,
        'p_rain': 0.3,
        'p_sunshine': 0.6
    },
    {
        'a_temp': 72.0,
        'a_min_temp': 50.0,
        'a_max_temp': 95.0,
        'a_rainfall': 1.1,
        'a_wind': 8.4,
        'a_humidity': 65.3,
        'a_pressure': 30.01,
        'p_hot': 0.35,
        'p_rain': 0.15,
        'p_sunshine': 0.75
    },
    {
        'a_temp': 55.2,
        'a_min_temp': 32.0,
        'a_max_temp': 78.0,
        'a_rainfall': 3.5,
        'a_wind': 12.3,
        'a_humidity': 80.2,
        'a_pressure': 29.88,
        'p_hot': 0.1,
        'p_rain': 0.4,
        'p_sunshine': 0.5
    }
]

def init_global_variables():
    weather_years = ["2020", "2021", "2022"]
    return weather_years, len(weather_years)

class TestWeatherFunctions(unittest.TestCase):

    def test_to_float(self):
        self.assertEqual(to_float('14.0'), 14.0)
        self.assertEqual(to_float('blank'), 0.0)
        self.assertEqual(to_float(''), 0.0)

    def test_read_weather_data(self):
        test_data = "./archive/test.csv"
        summary = read_weather_data(test_data)
        
        self.assertIsInstance(summary, dict)
        self.assertIn('a_temp', summary)
        self.assertIn('a_min_temp', summary)
        self.assertIn('a_max_temp', summary)
        self.assertIn('a_rainfall', summary)
        self.assertIn('a_wind', summary)
        self.assertIn('a_humidity', summary)
        self.assertIn('a_pressure', summary)
        self.assertIn('p_hot', summary)
        self.assertIn('p_rain', summary)
        self.assertIn('p_sunshine', summary)

        self.assertTrue(0 <= summary['p_hot'] <= 1)
        self.assertTrue(0 <= summary['p_rain'] <= 1)
        self.assertTrue(0 <= summary['p_sunshine'] <= 1)
        self.assertTrue(summary['a_min_temp'] <= summary['a_temp'] <= summary['a_max_temp'])

    def test_process_humidity(self):
        from src import main
        main.WEATHER_YEARS, main.YEAR_LENGTH = init_global_variables()
        
        humidity_year = process_humidity(test_data_summary_year)

        self.assertIsInstance(humidity_year, dict)
        self.assertEqual(set(humidity_year.keys()), set(main.WEATHER_YEARS))

        expected_humidities = {main.WEATHER_YEARS[i]: test_data_summary_year[i]['a_humidity'] for i in range(main.YEAR_LENGTH)}
        self.assertEqual(humidity_year, expected_humidities)

    def test_process_sunshine(self):
        smallest_sunshine_ratio, largest_sunshine_ratio = process_sunshine(test_data_summary_year)

        self.assertTrue(smallest_sunshine_ratio < largest_sunshine_ratio)
        self.assertTrue(smallest_sunshine_ratio, 0.5)
        self.assertTrue(largest_sunshine_ratio, 0.75)

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

if __name__ == '__main__':
    unittest.main()
