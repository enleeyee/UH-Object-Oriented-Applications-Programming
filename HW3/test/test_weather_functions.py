import unittest
from test_weather_main import TestWeatherMain
from test_weather_variables import test_file
from src.main import read_weather_data

class TestWeatherFunctions(unittest.TestCase):

    def test_read_weather_data(self):
        summary = read_weather_data(test_file)
        TestWeatherMain().validate_summary(summary)

if __name__ == '__main__':
    unittest.main()
