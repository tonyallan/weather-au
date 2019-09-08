import weather

# https://lxml.de/elementsoup.html

# <forecast>
#   ...
#   <area aac="VIC_PT001" description="Aireys Inlet" type="location">
#     <forecast-period index="0" start-time-local="2019-09-08T01:00:00+10:00" ...
#        <text type="uv_alert">
#          Sun protection recommended from 10:40 am to 2:00 pm, UV Index predicted to reach 4 [Moderate]

class UvIndex:

    def __init__(self, state=None):

        self.state = state
        self.soup = weather.fetch_xml(weather.UV_INDEX_PRODUCT_URL[state])
        self.identifier = self.soup.identifier.contents[0]
    

    def area(self):

        area_list =[]

        for area in self.soup.find_all('area', {'type': 'location'}):
            area_list.append(area.attrs)

        return area_list


    def uv_alert(self, aac=None):

        area = self.soup.find('area', {'type': 'location', 'aac': aac})

        if area is not None:
            forecast_period = area.find('forecast-period', {'index': '0'})
            #start_time = forecast_period['start-time-local']

            if forecast_period is not None:
                text = forecast_period.find('text', {'type': 'uv_alert'})

                if text is not None:
                    return text.contents[0]

        return None


    def __str__(self):
        return str(self.soup)