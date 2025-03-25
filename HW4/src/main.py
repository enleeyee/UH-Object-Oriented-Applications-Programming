from flask import Flask

class Webscrapper:
    
    def get_temp(url):
        # process the url: connect to url, retrieve page, filter the data
        # return the temperature
        pass

class Proxy:

    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.app.add_url_rule("/temp", "temp", self.dispatch_temp_req)
        self.app.add_url_rule("/airq", "airq", self.dispatch_airq_req)

    def dispatch_temp_req(self):
        print("handle the /temp request")

        url = "https://www.msn.com/en-us/weather/forecast"
        data = Webscrapper.get_temp(url)

        return {'current': 62, 'feels like': 66}
    
    def dispatch_airq_req(self):
        print("handle the /airq request")
        return {'air quality': 49}
    
    def run(self):
        self.app.run()

if __name__ == "__main__":
    p = Proxy(__name__)
    p.run()
        