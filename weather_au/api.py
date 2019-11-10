import json
import urllib.request

class WeatherApi:
    """ Australian Weather Data API

    These API's have been reverse engineered from their usage in the web page
    https://weather.bom.gov.au/

    There are two sets to use this API. Thie first is to find and set a location 
    and the second is to call the API which returns JSON data.

    With a Suburb and state or a post code, the first results is almost always 
    the correct one.

    The website seems to be refreshing data every 10 minutes.

    Each API returns a two-element dictionary - metadata and data. Data is returned.

    Data is in metric units unless otherwise indicated.

    forecasts/3-hourly checks for a six character geohash. Search return 7 characters.

    # click on warning
    # https://api.weather.bom.gov.au/v1/warnings/IDV36310?cbts=1568014740

    """

    API_BASE = 'https://api.weather.bom.gov.au/v1'
    API_FORECAST_RAIN = API_BASE + 'forecast/rain'
    API_WARNINGS = API_BASE + 'warnings'
    API_FORECAST_DAILY = 'forecasts/daily'
    API_FORECAST_3HOURLY = 'forecasts/3-hourly'
    API_OBSERVATIONS = 'observations'
    SEARCH = 'locations?search='
    ACKNOWLEDGEMENT = 'Data courtesy of the Australian Bureau of Meteorology (https://api.weather.bom.gov.au)'


    def __init__(self, geohash=None, search=None, debug=0):

        self._location = None
        self.geohash = geohash

        self.response_timestamp = None

        self.acknowedgment = self.ACKNOWLEDGEMENT
        self.debug = debug

        # set self.geohash and self.location
        if search is not None:
            self.search(search=search)


    def _fetch_json(self, url):

        if self.debug >= 1:
            print('Fetching:', url)

        req = urllib.request.Request(url)

        json_text = urllib.request.urlopen(req).read().decode('utf-8')
        result =  json.loads(json_text)

        self.response_timestamp = result['metadata']['response_timestamp']

        return result


    def search(self, search='', select=0):
        """
        Returns search result list or [] if no matches or if the search string was ''.

        Example https://api.weather.bom.gov.au/v1/locations?search=3130
                https://api.weather.bom.gov.au/v1/locations?search=Parkville+VIC

        Multiple matching records are returned. If suburb and state are specified then
        selecting the first element should be sufficient.

        If no match is found an empty list is returned and self.gohash is None.
        
        data:[{geohash, id, name, postcode, state},]

        geohash     e.g. 'r1r143n'
        id          e.g. 'Parkville (Vic.)-r1r143n'
        name        e.g. 'Parkville'
        state       e.g. 'VIC'

        Location is returned as a 6 character precision geohash such as '1r143n'.
        (https://en.wikipedia.org/wiki/Geohash)
        """
        self._location = None
        self.geohash = None

        if search == '':
            return []

        # The search API doesn't like the dash character.
        search = search.replace('-', '+')

        data = self._fetch_json(f'{self.API_BASE}/{self.SEARCH}{search}')

        if len(data['data']) > select:
            self._location = data['data'][select]

            if 'geohash' in self._location:
                self.geohash = self._location['geohash'][:6]

        return data['data']


    def api(self, api=None, type='locations'):
        # type is locations (with geohash) or warnings (without)
        if type == 'locations':

            if self.geohash is None:
                return None

            result = self._fetch_json('/'.join(filter(None, [self.API_BASE, type, self.geohash, api])))

        else:
            result = self._fetch_json('/'.join(filter(None, [self.API_BASE, type, api])))

        if 'data' in result:
            return result['data']

        return None


    def location(self):
        """
        Example https://api.weather.bom.gov.au/v1/locations/r1r143n

        {geohash, id, name, state, latitude, longitude, timezone}
        or None
        
        id          e.g. 'Parkville (Vic.)-r1r143n'
        name        e.g. 'Parkville'
        state       e.g. 'VIC'
        latitude    e.g. -37.78678894042969
        longitude   e.g. 144.95155334472656
        timezone    e.g. 'Australia/Melbourne'
        """
        return self.api()


    def warnings(self):
        """
        Example https://api.weather.bom.gov.au/v1/locations/r1r143/warnings

        [{id, state, expiry_time, issue_time, type, short_title, warning_group_type, phase}]
        or None
        
        id is a product ID, e.g. 'IDV29000'
        type                e.g. 'sheep_graziers_warning'
        short_title         e.g. 'Sheep Graziers Warning'
        warning_group_type  e.g. 'minor'
        phase               e.g. 'cancelled'
        """
        return self.api('warnings')


    def warning(self, id=None):
        """
        Example https://api.weather.bom.gov.au/v1/warnings/IDV29000

        [{id, state, expiry_time, issue_time, type, short_title, warning_group_type, phase}]
        {id, title, state, expiry_time, issue_time, type, short_title, message, phase}}
        or None
        
        id is a product ID, e.g. 'IDV29000'
        title               e.g. 'Sheep Graziers Warning for North Central forecast district'
        type                e.g. 'sheep_graziers_warning'
        short_title         e.g. 'Sheep Graziers Warning'
        message             e.g. '<div class="product">\n<p class="p-id">IDV29000</p> ... \n</div>\n'
        phase               e.g. 'cancelled'
        """
        return self.api(id, type='warnings')


    def observations(self):
        """
        Example https://api.weather.bom.gov.au/v1/locations/r1r143/observations

        {temp, 
              temp_feels_like, 
              wind:{speed_kilometre, speed_knot, direction},
              rain_since_9am,
              humidity,
              station:{bom_id, name, distance}
            }
        or None
        
        station bom_id      e.g. '086338'
                name        e.g. 'Melbourne (Olympic Park)'
                distance    e.g. 5401    [metre]
        """
        return self.api('observations')


    def forecast_rain(self):
        """
        Example https://api.weather.bom.gov.au/v1/locations/r1r143/forecast/rain

        {amount, chance, start_time, period}
        or None

        The definition of period is not clear, e.g. 'PT1H'
        """
        return self.api('forecast/rain')


    def forecasts_daily(self):
        """
        Example https://api.weather.bom.gov.au/v1/locations/r1r143/forecasts/daily

        [{rain:{amount:{max, min, units}, chance},
               uv:{category, end_time, max_index, start_time},
               astronomical:{sunrise_time, sunset_time},
               date,
               temp_max,
               temp_min,
               extended_text,
               icon_descriptor,
               short_text,
               fire_danger,
               now:{is_night, now_label, later_label, temp_now, temp_later}
            },]
        or None

        now_label   e.g. 'Overnight Min'
        later_label e.g. 'Tomorrow's Max'

        Observed 8 elements in the list. Might be 7 elements in the list sometimes?
        """
        return self.api('forecasts/daily')


    def forecasts_3hourly(self):
        """
        Example https://api.weather.bom.gov.au/v1/locations/r1r143/forecasts/3-hourly

        [{rain:{amount:{min, max, units}, chance},
               temp,
               wind:{speed_knot, speed_kilometre, direction},
               icon_descriptor,
               time,
               is_night,
               next_forecast_period
            },]
        or None

        wind direction  .e.g 'WSW'

        Observed 16 elements in the list.

        A six character geohash is expected.
        """
        return self.api('forecasts/3-hourly')


    def __repr__(self):

        if self._location is None:
            loc = ''
        else:
            loc = f"{self._location['name']} {self._location['state']}"

        if self.geohash is None:
            geohash = 'None'
        else:
            geohash = "'" + self.geohash + "'"

        return f"WeatherApi(geohash={geohash}, search='{loc}', debug={self.debug}), " + \
            f"timestamp={self.response_timestamp}"

