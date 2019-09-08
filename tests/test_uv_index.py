import os, sys
sys.path.append(os.path.abspath('.'))
import pytest
import urllib


from weather import uv_index

def test_invalid_state():
    with pytest.raises(KeyError, match='zzz'):
        obs = uv_index.UvIndex('zzz')

obs = uv_index.UvIndex('Vic')

def test_obs():
    assert obs is not None

def test_identifier():
    assert obs.identifier == 'IDZ00112'

def test_area_list():
    forecast = obs.area()
    assert len(forecast) > 10

    for area in forecast:
        area_aac = area['aac']
        assert area_aac is not None

        area_description = area['description']
        assert area_description is not None
   
def test_uv_alert():
    uv = obs.uv_alert('VIC_PT042')
    assert uv is not None
    assert 'UV Index' in uv
