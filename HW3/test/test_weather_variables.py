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

def init_global_variables():
    weather_years = ["2020", "2021", "2022"]
    return weather_years, len(weather_years)
