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
        fd_curr = self.forecasts_daily[0]
        fd_next = self.forecasts_daily[1]

        return dict(
            location            = f"{self.location['name']}, {self.location['state']}",
            current_temp        = self.observations['temp'],
            precis              = fd_curr['short_text'],
            max_temp            = fd_curr['temp_max'],
            overnight_min_temp  = fd_next['temp_min'],
            temp_feels_like     = self.observations['temp_feels_like'],
            chance_of_rain      = self.forecasts_daily[0]['rain']['chance']
            )


    def __str__(self):
        s = self.summary()

        return '\n'.join((
            "Summary",
            f"Location           {s['location']}",
            f"Current Temp       {s['current_temp']}°",
            f"Precis             {s['precis']}",
            f"Max                {s['max_temp']}°",
            f"Overnight Min      {s['overnight_min_temp']}°",
            f"Feels Like         {s['temp_feels_like']}°",
            f"Chance of any Rain {s['chance_of_rain']}%",
            "",
            self.api.acknowedgment))
