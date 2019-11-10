import sys
import urllib.request

from bs4 import BeautifulSoup

import weather_au


class PlaceException(Exception):
    pass

class Place:
    """
    If the structure of the page changes, a PlaceException is raised.

    If the content is not present then None is returned except for forecast()
    where the data is omitted from the result.
    """

    def __init__(self,state=None, location=None):
        # See http://www.bom.gov.au/places/ to search for valid locations.
        # Will raise urllib.error.HTTPError if state or place not found

        self.url = weather_au.PLACES_URL.format(state=state, location=location)
        self.acknowedgment = f'Data courtesy of Bureau of Meteorology ({self.url})'

        req = urllib.request.Request(self.url, data=None, headers={'User-Agent': weather_au.PLACES_USER_AGENT})
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

        if len(temp_node.contents) > 0:
            return float(temp_node.contents[0][:-3])
        else:
            return None


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
            if len(a_node.contents) > 0:
                result['date'] = a_node.contents[0].strip()

        # min is not always present
        min_node = forecast_summary.find('dd', 'min')
        if min_node is not None:
            if len(min_node.contents) > 0:      
                result['min'] = min_node.contents[0][:-3]

        # max is not always present
        max_node = forecast_summary.find('dd', 'max')
        if max_node is not None:
            if len(max_node.contents) > 0:
                result['max'] = max_node.contents[0][:-3]

        precis_node = forecast_summary.find('dd', 'summary')
        if precis_node is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=dd class=summary)") 
        
        if len(precis_node.contents) > 0:
            result['precis'] = precis_node.contents[0]

        return result


    def station_id(self):
        # <p class="station-id">ID: 95936</p>

        station_p = self.soup.find('p', 'station-id')
        if station_p is None:
            raise PlaceException(f"Could not parse HTML ({self.url}, tag=p class=station_id)")

        if len(station_p.contents) > 0:
            return station_p.contents[0][4:]
        else:
            return None
