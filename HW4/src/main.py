#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from bs4 import BeautifulSoup
from flask import Flask
from re import sub
from requests import get
 
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
        current_temp = to_int(clean_text(temp_element.get_text(strip=True))) if temp_element else None

        feels_like_element = self.soup.find("a", class_="summaryFeelLikeContainerCompact-E1_1")
        feels_like_temp = to_int(
            clean_text(
                feels_like_element.find_all("div")[-1].get_text(strip=True)
            )
        ) if feels_like_element else None

        return current_temp, feels_like_temp

    def get_airq(self):
        """Scrapes and returns the current air quality."""
        airq_value_element = self.soup.find("a", class_="aqiDetailItemGroupCompact-E1_1")
        return to_int(
            airq_value_element.find_all("div", {"aria-hidden":"true"})[-1].get_text(strip=True)
        ) if airq_value_element else None

    def get_wind(self):
        """Scrapes and returns the current wind speed."""
        wind_speed_element = self.soup.find("a", class_="detailItemGroup-E1_1")
        return to_int(
            clean_text(
                wind_speed_element.find("div", id="CurrentDetailLineWindValue").get_text(strip=True)
            )
        ) if wind_speed_element else None

    def get_humidity(self):
        """Scrapes and returns the current humidity rate."""
        humidity_rate_element = self.soup.find_all("a", class_="detailItemGroup-E1_1")[1]
        return to_int(
            clean_text(
                humidity_rate_element.find("div", id="CurrentDetailLineHumidityValue").get_text(strip=True)
            )
        ) if humidity_rate_element else None
    
class Proxy:

    def __init__(self, name):
        """Initializes the Flask app and registers API routes."""
        self.app = Flask(name)
        self.app.add_url_rule("/temp", "temp", self.dispatch_temp_req)
        self.app.add_url_rule("/airq", "airq", self.dispatch_airq_req)
        self.app.add_url_rule("/wind", "wind", self.dispatch_wind_req)
        self.app.add_url_rule("/humidity", "humidity", self.dispatch_get_humidity_req)
        self.url = "https://www.msn.com/en-us/weather/forecast"
        self.scraper = Webscrapper(self.url)

    def dispatch_temp_req(self):
        """Handles requests for temperature data."""
        current_temperature, feels_like_temperature = self.scraper.get_temp()
        return {'current': current_temperature, 'feels like': feels_like_temperature}
    
    def dispatch_airq_req(self):
        """Handles reqests for air quality data."""
        air_quality = self.scraper.get_airq()
        return {'air quality': air_quality}
    
    def dispatch_wind_req(self):
        """Handles reqests for wind speed data."""
        wind_speed = self.scraper.get_wind()
        return {'wind': wind_speed}
    
    def dispatch_get_humidity_req(self):
        """Handles reqests for humidity data."""
        humidity_rate = self.scraper.get_humidity()
        return {'humidity': humidity_rate}

    def run(self):
        """Starts the Flask web server to serve API requests."""
        self.app.run()

if __name__ == "__main__":
    p = Proxy(__name__)
    p.run()
