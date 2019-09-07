import os, sys
sys.path.append(os.path.abspath('.'))
import pytest
import urllib


from weather import observations

with pytest.raises(KeyError, match='zzz'):
    obs = observations.Observations('zzz')

obs = observations.Observations('Vic')
assert obs is not None
assert obs.identifier == 'IDV60920'

# for station in obs.stations():
#     print(station['wmo-id'], station['description'])

stations = obs.stations()
assert len(stations) > 10

for station in stations:
    station_wmo_id = station['wmo-id']
    assert station_wmo_id is not None

    station_description = station['description']
    assert station_description is not None

    station_air_temperature = obs.air_temperature(station['wmo-id'])
    #assert station_air_temperature is not None
    

air_temperature_95936 = obs.air_temperature('95936')
assert air_temperature_95936 is not None
