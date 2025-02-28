import unittest
from src.main import to_float, read_weather_data

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

if __name__ == '__main__':
    unittest.main()
