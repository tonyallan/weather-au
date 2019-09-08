import sys
import urllib.request

from bs4 import BeautifulSoup

import weather


class PlaceException(Exception):
    pass

class Place:

    def __init__(self,state=None, location=None):
        # See http://www.bom.gov.au/places/ to search for valid locations.
        # Will raise urllib.error.HTTPError if state or place not found

        self.url = weather.PLACES_URL.format(state=state, location=location)

        req = urllib.request.Request(self.url, data=None, headers={'User-Agent': weather.PLACES_USER_AGENT})
        page_html = urllib.request.urlopen(req).read()
        
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
