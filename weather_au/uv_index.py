import weather_au

# https://lxml.de/elementsoup.html

# <forecast>
#   ...
#   <area aac="VIC_PT001" description="Aireys Inlet" type="location">
#     <forecast-period index="0" start-time-local="2019-09-08T01:00:00+10:00" ...
#        <text type="uv">
#          Sun protection recommended from 10:40 am to 2:00 pm, UV Index predicted to reach 4 [Moderate]

class UvIndex:

    def __init__(self, state=None):

        self.state = state
        self.url = weather_au.uv_PRODUCT_URL[state]
        self.soup = weather_au.fetch_xml(self.url)
        self.identifier = self.soup.identifier.contents[0]
        self.acknowedgment = f'Data courtesy of Bureau of Meteorology ({self.url})'
    

    def aac_list(self):
        # Return a dict of aac with a key of description

        aacs = {}

        for area in self.soup.find_all('area', {'type': 'location'}):
            aacs[area.attrs['description']] = area.attrs['aac']

        return aacs


    def get_aac(self, description=None):
        # Get an aac given the description

        aacs = self.aac_list()

        if description in aacs:
            return aacs[description]
        else:
            return None


    def uv_message(self, aac=None):

        area = self.soup.find('area', {'type': 'location', 'aac': aac})

        if area is not None:
            forecast_period = area.find('forecast-period', {'index': '0'})
            #start_time = forecast_period['start-time-local']

            if forecast_period is not None:
                text = forecast_period.find('text', {'type': 'uv_alert'})

                if text is not None and len(text.contents) > 0:
                    return text.contents[0]

        return None


    def uv_solar_noon_index(self):
        return weather_au.UV_INDEX_URL


    def __str__(self):
        return str(self.soup)