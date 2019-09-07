import sys
import urllib.request

from bs4 import BeautifulSoup


class PlaceException(Exception):
    pass

class Place:

    URL = 'http://www.bom.gov.au/places/{state}/{location}'

    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'


    def __init__(self,state=None, location=None):
        # See http://www.bom.gov.au/places/ to search for valid locations.
        # Will raise urllib.error.HTTPError if state or place not found

        self.url = self.URL.format(state=state, location=location)

        req = urllib.request.Request(self.url, data=None, headers={'User-Agent': self.USER_AGENT})

        f = urllib.request.urlopen(req)
        page_html =  f.read().decode('utf-8') # assume utf-8
        self.soup = BeautifulSoup(page_html, 'html.parser')


    def air_temperature(self):
        # Return current temperature in °C as a float

        summary_node = self.soup.find(id='summary-1')
        if summary_node is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, id=summary-1)")

        temp_node = summary_node.find('li', 'airT')
        if temp_node is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=li class=airT)")

        temp_text = temp_node.contents[0]
        return float(temp_text[:-3])


    def station_id(self):
        # <p class="station-id">ID: 95936</p>

        station_p = self.soup.find('p', 'station-id')
        if station_p is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=p class=station_id)")

        return station_p.contents[0][4:]
