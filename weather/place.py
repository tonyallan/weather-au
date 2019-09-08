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
        self.acknowedgment = f'Data courtesy of Bureau of Meteorology ({self.url})'

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


    def forecast(self):
        
        result = {}

        forecasts_top = self.soup.find('div', 'forecasts-top')
        if forecasts_top is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=div class=forecasts-top)")

        # <span>issued at 4:20 pm AEST on Saturday 7 September 2019.</span>
        issued_node = forecasts_top.find('span')
        if issued_node is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=span)")

        issued_text = issued_node.contents[0]
        if 'issued at' not in issued_text:
            raise PlaceException(f"Could not parse HTML ({self.url}, span missing 'issued at')")
        
        result['issued'] = issued_text[9:-1].strip()

        forecast_summary = self.soup.find('dl', 'forecast-summary')
        if forecast_summary is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=dl class=forecast-summary)")

        # date
        date_node = forecast_summary.find('dt', 'date')
        if date_node is not None:
            a_node = date_node.find('a')
            date_text = a_node.contents[0]
            result['date'] = date_text.strip()

        # min is not always present
        min_node = forecast_summary.find('dd', 'min')
        if min_node is not None:        
            min_text = min_node.contents[0]
            result['min'] = min_text[:-3]

        # max is not always present
        max_node = forecast_summary.find('dd', 'max')
        if max_node is not None:
            max_text = max_node.contents[0]
            result['max'] = max_text[:-3]

        precis_node = forecast_summary.find('dd', 'summary')
        if precis_node is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=dd class=summary)") 
        
        precis_text = precis_node.contents[0]
        result['precis'] = precis_text

        return result


    def station_id(self):
        # <p class="station-id">ID: 95936</p>

        station_p = self.soup.find('p', 'station-id')
        if station_p is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=p class=station_id)")

        return station_p.contents[0][4:]
