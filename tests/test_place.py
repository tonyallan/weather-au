import os, sys
sys.path.append(os.path.abspath('.'))

import pytest
import urllib


from weather_au import place

def test_404():
    with pytest.raises(urllib.error.HTTPError, match='HTTP Error 404: Not Found'):
        place_data = place.Place('vic', 'zzz')

place_data = place.Place('vic', 'parkville')

def test_obs():
    assert place_data is not None

def test_acknowedgment_url():
    assert len(place_data.url) > 0
    assert len(place_data.acknowedgment) > 0

def test_station_id():
    station_id = place_data.station_id()
    assert station_id is not None
    assert len(station_id) == 5

def test_forecast():
    forecast = place_data.forecast()
    assert 'issued' in forecast
    assert 'date' in forecast
    assert 'precis' in forecast

def test_air_temperature():
    air_temperature = place_data.air_temperature()
    assert air_temperature is not None
    assert air_temperature > -30.0
    assert air_temperature < 60.0
