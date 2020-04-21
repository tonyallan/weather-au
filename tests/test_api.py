import os, sys
sys.path.append(os.path.abspath('.'))

import pytest

from weather_au import api


w1 = api.WeatherApi(search='parkville+vic')

def test_search_single():
    assert w1.geohash == 'r1r143n'[:6]

def test_search_repr():
    assert "WeatherApi(geohash='r1r143', search='Parkville VIC'" in repr(w1)

def test_search_location():
    location = w1.location()

    assert location['name']     == 'Parkville'
    assert location['state']    == 'VIC'
    assert location['timezone'] == 'Australia/Melbourne'

"""
Not sure how to test this?
for warn in w.warnings():
    print(f"Warnings:            {warn['short_title']}")
"""

def test_observations():
    observations = w1.observations()

    assert float(observations['temp']) > -50

def test_forecast_rain():
    forecast_rain = w1.forecast_rain()

    assert 'amount' in forecast_rain
    assert 'chance' in forecast_rain

def test_forecasts_daily():
    fd = w1.forecasts_daily()

    assert len(fd) >= 7
    assert 'temp_min' in fd[0]
    assert 'temp_max' in fd[0]
    assert 'short_text' in fd[0]

def test_forecasts_3hourly():
    f3 = w1.forecasts_3hourly()

    assert len(f3) >= 16
    assert 'time' in f3[0]
    assert 'temp' in f3[0]
    assert 'icon_descriptor' in f3[0]


w1a = api.WeatherApi(search='some+unknown+place')

def test_search_single_unknown():
    assert w1a.geohash is None

def test_search_repr_unknown():
    assert "WeatherApi(geohash=None, search=''" in repr(w1a)

def test_search_location_unknown():
    assert w1a.location() is None

def test_observations_unknown():
    assert w1a.observations() is None

def test_forecast_rain_unknown():
    assert w1a.forecast_rain() is None

def test_forecasts_daily_unknown():
    assert w1a.forecasts_daily() is None

def test_forecasts_3hourly_unknown():
    assert w1a.forecasts_3hourly() is None


def test_geohash_blank():
    w1b = api.WeatherApi(geohash='')
    assert w1b.location() is None

def test_geohash_short():
    w1b = api.WeatherApi(geohash='zzz', debug=1)
    assert w1b.location() is None

def test_geohash_location_long():
    w1b = api.WeatherApi(geohash='zzzzzzzz')
    assert w1b.location() is None

def test_geohash_location_outsude_area():
    w1b = api.WeatherApi(geohash='zzzzzz')
    assert w1b.location() is None

def test_geohash_location_invalid():
    w1b = api.WeatherApi(geohash='******')
    assert w1b.location() is None


w2 = api.WeatherApi() 

def test_search_multiple():
    assert len(w2.search('vic')) > 10

def test_search_invalid():
    assert w2.search('zzz') == []

def test_search_invalid():
    assert len(w2.acknowedgment) > 0


w3 = api.WeatherApi(search='')

def test_search_nothing1():
    assert w3.geohash is None


w4 = api.WeatherApi(search='endeavour-hills+vic')

def test_search_single_endeavour_hills():
    assert w4.geohash == None


w5 = api.WeatherApi(search='endeavour+hills+vic')

def test_search_single_endeavour_hills():
    assert w5.geohash == 'r1prcrs'[:6]

def test_search_repr_endeavour_hills():
    # repr returns the six character geohash
    assert "WeatherApi(geohash='r1prcr', search='Endeavour Hills VIC'" in repr(w5)

def test_search_location_endeavour_hills():
    location = w5.location()

    assert location['name']     == 'Endeavour Hills'
    assert location['state']    == 'VIC'
    assert location['timezone'] == 'Australia/Melbourne'
