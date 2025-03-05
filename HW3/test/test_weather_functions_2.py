import unittest
from test_weather_main import TestWeatherMain
from test_weather_variables import test_file
from src.main import read_weather_data_2

class TestWeatherFunctionTwo(unittest.TestCase):

    def test_read_weather_data_2(self):
        summary = read_weather_data_2(test_file)

        self.assertIsInstance(summary, dict)
        self.assertIn("warm", summary)
        self.assertIn("cold", summary)

        for season in ["warm", "cold"]:
            TestWeatherMain().validate_summary(summary[season])

if __name__ == '__main__':
    unittest.main()
