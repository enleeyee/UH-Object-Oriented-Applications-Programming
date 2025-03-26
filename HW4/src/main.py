from flask import Flask
import requests
from bs4 import BeautifulSoup

def to_int(value, default = 0):
    """Converts valid values into int or default value 0."""
    try:
        return int(value)
    except ValueError:
        return default

class Webscrapper:
    
    def get_soup(self, url):
        """Fetches the webpage content and returns a BeautifulSoup object."""
        response = requests.get(url)
        html_content = response.content
        return BeautifulSoup(html_content, "html.parser")
    
    def get_temp(self, url):
        """Scrapes and returns the current temperature and 'feels like' temperature."""
        soup = self.get_soup(url)

        temp_element = soup.find("a", class_="summaryTemperatureCompact-E1_1")
        current_temp = to_int(
            temp_element.get_text(strip=True)
            .replace("°F", "")
        ) if temp_element else None

        feels_like_element = soup.find("a", class_="summaryFeelLikeContainerCompact-E1_1")
        feels_like_temp = to_int(
            feels_like_element.find_all("div")[-1].get_text(strip=True)
            .replace("°", "")
            .replace("\u200e", "")
        ) if feels_like_element else None

        return current_temp, feels_like_temp
    
    def get_airq(self, url):
        """Scrapes and returns the current air quality."""
        soup = self.get_soup(url)

        airq_value_element = soup.find("a", class_="aqiDetailItemGroupCompact-E1_1")
        return to_int(airq_value_element.find_all("div", {"aria-hidden":"true"})[-1].get_text(strip=True)) if airq_value_element else None

class Proxy:

    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.app.add_url_rule("/temp", "temp", self.dispatch_temp_req)
        self.app.add_url_rule("/airq", "airq", self.dispatch_airq_req)
        self.url = "https://www.msn.com/en-us/weather/forecast"

    def dispatch_temp_req(self):
        currect_temperature, feels_like_temperature = Webscrapper().get_temp(self.url)
        return {'current': currect_temperature, 'feels like': feels_like_temperature}
    
    def dispatch_airq_req(self):
        air_quality = Webscrapper().get_airq(self.url)
        return {'air quality': air_quality}
    
    def run(self):
        self.app.run()

if __name__ == "__main__":
    p = Proxy(__name__)
    print(p.dispatch_temp_req())
    print(p.dispatch_airq_req())
    # p.run()
        