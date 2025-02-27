import unittest
from src.main import mean, read_weather_data

class TestWeatherFunctions(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(mean([10, 20, 30]), 20)
        self.assertEqual(mean([]), 0)
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5]), 2.5)

    def test_read_weather_data(self):
        test_data = "./archive/test.csv"
        summary = read_weather_data(test_data)
        
        self.assertIsInstance(summary, dict)
        self.assertIn('avg_temp', summary)
        self.assertIn('min_temp', summary)
        self.assertIn('max_temp', summary)
        self.assertIn('avg_rainfall', summary)
        self.assertIn('avg_wind_speed', summary)
        self.assertIn('avg_humidity', summary)
        self.assertIn('avg_pressure', summary)

        self.assertTrue(summary['min_temp'] <= summary['avg_temp'] <= summary['max_temp'])

if __name__ == '__main__':
    unittest.main()
