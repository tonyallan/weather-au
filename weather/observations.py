import weather

# https://docs.python.org/3/library/xml.dom.html#module-xml.dom

class Observations:

    def __init__(self, state=None):

        self.state = state
        self.soup = weather.fetch_xml(weather.OBSERVATION_PRODUCT_URL[state])
        self.identifier = self.soup.find('identifier').contents[0]
    

    def stations(self):

        station_list =[]

        for station in self.soup.find_all('station'):
            station_list.append(station.attrs)

        return station_list


    def elements(self, wmo_id=None):

        return self.soup.find('station', {'wmo-id': wmo_id})


    def air_temperature(self, wmo_id=None):
        """ Don't assume that any elements exist or an element with type air_temperature
        """

        elements = self.soup.find('station', {'wmo-id': wmo_id})

        if elements is not None:
            air_temperature_el = elements.find('element', {'type': 'air_temperature'})

            if air_temperature_el is not None:
                return air_temperature_el.contents[0]

        return None


    def __str__(self):
        return str(self.soup)