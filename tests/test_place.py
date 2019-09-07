import pytest
import urllib

import weather
from weather import place

obs = place.Place('vic', 'parkville')

air_temperature = obs.air_temperature()
assert air_temperature is not None
assert air_temperature > -30.0
assert air_temperature < 60.0

station_id = obs.station_id()
assert station_id is not None
assert len(station_id) == 5

with pytest.raises(urllib.error.HTTPError, match='HTTP Error 404: Not Found'):
    obs = place.Place('vic', 'zzz')
