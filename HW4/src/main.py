#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from bs4 import BeautifulSoup
from flask import Flask, Response as FlaskResponse
from re import sub
from requests import get
from json import dumps
 
def to_int(value, default = 0):
    """Converts valid values into int or default value 0."""
    try:
        return int(value)
    except ValueError:
        return default

def clean_text(value):
    """Removes unwanted symbols like degrees, mph, or hidden unicode characters."""
    return sub(r"[°Fmph%]", "", value).replace("\u200e", "")

class Webscrapper:
    
    def __init__(self, url):
        """Initialize and fetch page content once to avoid redundant requests."""
        self.soup = self.get_soup(url)

    def get_soup(self, url):
        """Fetches the webpage content and returns a BeautifulSoup object."""
        response = get(url)
        html_content = response.content
        return BeautifulSoup(html_content, "html.parser")

    def get_temp(self):
        """Scrapes and returns the current temperature and 'feels like' temperature."""
        temp_element = self.soup.find("a", class_="summaryTemperatureCompact-E1_1")
        current_temperature = to_int(clean_text(temp_element.get_text(strip=True))) if temp_element else None

        feels_like_element = self.soup.find("a", class_="summaryFeelLikeContainerCompact-E1_1")
        feels_like_temperature = to_int(
            clean_text(
                feels_like_element.find_all("div")[-1].get_text(strip=True)
            )
        ) if feels_like_element else None
        return {'current': current_temperature, 'feels like': feels_like_temperature}

    def get_airq(self):
        """Scrapes and returns the current air quality."""
        airq_value_element = self.soup.find("a", class_="aqiDetailItemGroupCompact-E1_1")
        airq_value_data = to_int(
            airq_value_element.find_all("div", {"aria-hidden":"true"})[-1].get_text(strip=True)
        ) if airq_value_element else None
        return {'air quality': airq_value_data}

    def get_wind(self):
        """Scrapes and returns the current wind speed."""
        wind_speed_element = self.soup.find("a", class_="detailItemGroup-E1_1")
        wind_speed_data = to_int(
            clean_text(
                wind_speed_element.find("div", id="CurrentDetailLineWindValue").get_text(strip=True)
            )
        ) if wind_speed_element else None
        return {'wind': wind_speed_data}

    def get_humidity(self):
        """Scrapes and returns the current humidity rate."""
        humidity_rate_element = self.soup.find_all("a", class_="detailItemGroup-E1_1")[1]
        humidity_rate_data = to_int(
            clean_text(
                humidity_rate_element.find("div", id="CurrentDetailLineHumidityValue").get_text(strip=True)
            )
        ) if humidity_rate_element else None
        return {'humidity': humidity_rate_data}
    
class Proxy:

    def __init__(self, name):
        """Initializes the Flask app and registers API routes."""
        self.flask_app = Flask(name)
        self.flask_app.add_url_rule("/", "home", self.dispatch_home_req)
        self.flask_app.add_url_rule("/temp", "temp", self.dispatch_temp_req)
        self.flask_app.add_url_rule("/airq", "airq", self.dispatch_airq_req)
        self.flask_app.add_url_rule("/wind", "wind", self.dispatch_wind_req)
        self.flask_app.add_url_rule("/humidity", "humidity", self.dispatch_get_humidity_req)
        self.url = "https://www.msn.com/en-us/weather/forecast"
        self.scraper = Webscrapper(self.url)

    def dispatch_home_req(self):
        """Handles requests when the initial link is opened and displays a home page."""
        html_content = """
        <html>
            <head>
                <title>Weather API Home</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }
                    h1 { color: #333; }
                    ul { list-style-type: none; padding: 0; }
                    li { margin: 10px 0; }
                    a { text-decoration: none; color: #0066cc; font-size: 18px; }
                    a:hover { text-decoration: underline; }
                </style>
            </head>
            <body>
                <h1>Welcome to the Weather API</h1>
                <p>Click a link below to view current weather data:</p>
                <ul>
                    <li><a href="/temp">Temperature</a></li>
                    <li><a href="/airq">Air Quality</a></li>
                    <li><a href="/wind">Wind Speed</a></li>
                    <li><a href="/humidity">Humidity</a></li>
                </ul>
            </body>
        </html>
        """
        return FlaskResponse(html_content, status=200, content_type = "text/html")

    def dispatch_temp_req(self):
        """Handles requests for temperature data."""
        temperature_data = self.scraper.get_temp()
        return FlaskResponse(dumps(temperature_data), status = 200, content_type = "application/json")
    
    def dispatch_airq_req(self):
        """Handles requests for air quality data."""
        air_quality_data = self.scraper.get_airq()
        return FlaskResponse(dumps(air_quality_data), status = 200, content_type = "application/json")
    
    def dispatch_wind_req(self):
        """Handles requests for wind speed data."""
        wind_speed_data = self.scraper.get_wind()
        return FlaskResponse(dumps(wind_speed_data), status = 200, content_type = "application/json")
    
    def dispatch_get_humidity_req(self):
        """Handles requests for humidity data."""
        humidity_rate_data = self.scraper.get_humidity()
        return FlaskResponse(dumps(humidity_rate_data), status = 200, content_type = "application/json")

    def run(self):
        """Starts the Flask web server to serve API requests."""
        if self.flask_app is None:
            return
        self.flask_app.run()

if __name__ == "__main__":
    p = Proxy(__name__)
    p.run()
