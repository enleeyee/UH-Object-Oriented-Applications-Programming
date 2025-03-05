test_file = "./archive/test.csv"

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

test_data_summary_season_year = [
    {
        "warm": {
            "a_temp": 78.0,
            "a_min_temp": 57.0,
            "a_max_temp": 79.0,
            "a_rainfall": 0.0,
            "a_wind": 9.5,
            "a_humidity": 54.5,
            "a_pressure": 29.90,
            "p_hot": 0.8,
            "p_rain": 0.0,
            "p_sunshine": 1.0
        },
        "cold": {
            "a_temp": 49.0,
            "a_min_temp": 43.0,
            "a_max_temp": 55.0,
            "a_rainfall": 0.0,
            "a_wind": 15.0,
            "a_humidity": 58.0,
            "a_pressure": 30.35,
            "p_hot": 0.2,
            "p_rain": 0.0,
            "p_sunshine": 0.5
        }
    },
    {
        "warm": {
            "a_temp": 72.0,
            "a_min_temp": 53.0,
            "a_max_temp": 77.0,
            "a_rainfall": 0.0,
            "a_wind": 10.5,
            "a_humidity": 50.0,
            "a_pressure": 30.12,
            "p_hot": 0.7,
            "p_rain": 0.1,
            "p_sunshine": 0.8
        },
        "cold": {
            "a_temp": 60.0,
            "a_min_temp": 50.0,
            "a_max_temp": 70.0,
            "a_rainfall": 0.2,
            "a_wind": 12.0,
            "a_humidity": 65.0,
            "a_pressure": 30.00,
            "p_hot": 0.3,
            "p_rain": 0.2,
            "p_sunshine": 0.6
        }
    },
    {
        "warm": {
            "a_temp": 77.0,
            "a_min_temp": 56.0,
            "a_max_temp": 79.0,
            "a_rainfall": 0.1,
            "a_wind": 11.0,
            "a_humidity": 55.0,
            "a_pressure": 30.20,
            "p_hot": 0.75,
            "p_rain": 0.05,
            "p_sunshine": 0.9
        },
        "cold": {
            "a_temp": 55.0,
            "a_min_temp": 48.0,
            "a_max_temp": 60.0,
            "a_rainfall": 0.2,
            "a_wind": 13.0,
            "a_humidity": 62.0,
            "a_pressure": 30.15,
            "p_hot": 0.25,
            "p_rain": 0.15,
            "p_sunshine": 0.55
        }
    }
]

def init_global_variables():
    weather_years = ["2010", "2006", "2008"]
    return weather_years, len(weather_years)
