import unittest
from parameterized import param, parameterized
from src.main import to_float

class TestWeatherMain(unittest.TestCase):

    @parameterized.expand([
        ('14.0', 14.0),
        ('blank', 0.0),
        ('', 0.0),
    ])
    def test_to_float(self, value, expected_result):
        self.assertEqual(to_float(value), expected_result)

    def validate_summary(self, summary):
        self._check_required_keys(summary)
        self._validate_probability_fields(summary)
        self._validate_temperature_range(summary)

    def _check_required_keys(self, summary):
        required_keys = {
            'a_temp', 'a_min_temp', 'a_max_temp', 'a_rainfall',
            'a_wind', 'a_humidity', 'a_pressure',
            'p_hot', 'p_rain', 'p_sunshine'
        }
        self.assertTrue(required_keys.issubset(summary.keys()))

    def _validate_probability_fields(self, summary):
        for key in ['p_hot', 'p_rain', 'p_sunshine']:
            self.assertTrue(0 <= summary[key] <= 1)

    def _validate_temperature_range(self, summary):
        self.assertTrue(summary['a_min_temp'] <= summary['a_temp'] <= summary['a_max_temp'])
        