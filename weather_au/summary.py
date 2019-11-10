import collections
from weather_au import api

class Summary:
    """
    Use the API to bring together a summary of the current weather and forecast
    that is similar to https://weather.bom.gov.au/

    TODO: validate the text and values for max_temp, overnight_min_temp, 
          chance_of_rain based on when the website switches from one form to anoth.
    """

    def __init__(self, geohash=None, search=None, debug=0):
        self.api = api.WeatherApi(geohash=geohash, search=search, debug=debug)
        self.refresh()


    def refresh(self):
        self.location            = self.api.location()
        self.warnings            = self.api.warnings()
        self.observations        = self.api.observations()
        self.forecast_rain       = self.api.forecast_rain()
        self.forecasts_daily     = self.api.forecasts_daily()
        self.forecasts_3hourly   = self.api.forecasts_3hourly()


    def summary(self):
        Item = collections.namedtuple('Item', ['label', 'value', 'unit'])

        fd_curr = self.forecasts_daily[0]
        fd_next = self.forecasts_daily[1]

        now = fd_curr['now']

        if self.location is None:
            location = '--'
        else:
            location = f"{self.location['name']}, {self.location['state']}"

        result = collections.OrderedDict(
            location        = Item('Location',                    location,                                  ''),
            current_temp    = Item('Current Temp',                self.observations['temp'],                 '°'),
            precis          = Item('Precis',                      fd_curr['short_text'],                     ''),
            temp_now        = Item(fd_curr['now']['now_label'],   fd_curr['now']['temp_now'],                '°'),
            temp_later      = Item(fd_curr['now']['later_label'], fd_curr['now']['temp_later'],              '°'),
            temp_feels_like = Item('Feels Like',                  self.observations['temp_feels_like'],      '°'),
            chance_of_rain  = Item('Chance of any Rain',          self.forecasts_daily[0]['rain']['chance'], '%')
            )

        # TODO: at 11:30pm I say 0-2mm, 20% and website says 20% which is the next three hourly value???
        rain_amount = fd_curr['rain']['amount']
        
        if rain_amount['max'] is not None and rain_amount['max'] > 0:
            result['possible_rainfall'] = Item('Possible Rainfall', f"{rain_amount['min']}-{rain_amount['max']}", rain_amount['units'])

        return result


    def summary_text(self):
        result = ''

        for item in self.summary().values():
            result += f"{item.label:20s}{item.value}{item.unit}\n"
        
        result += '\n' + self.api.acknowedgment

        return result


    def today(self):
        fd_curr = self.forecasts_daily[0]

        result = dict(
            extended_text       = fd_curr['extended_text']
            )


