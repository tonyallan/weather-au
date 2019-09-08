import os, sys
sys.path.append(os.path.abspath('.'))
import pytest
import urllib


from weather import uv_alert

def test_invalid_state():
    with pytest.raises(KeyError, match='zzz'):
        obs = uv_alert.UvAlert('zzz')

obs = uv_alert.UvAlert('Vic')

def test_obs():
    assert obs is not None

def test_acknowedgment_url():
    assert len(obs.url) > 0
    assert len(obs.acknowedgment) > 0

def test_identifier():
    assert obs.identifier == 'IDZ00112'

def test_aac_list():
    aac_list = obs.aac_list()
    assert len(aac_list) > 10

    for description in aac_list:
        assert description is not None
        assert aac_list[description] is not None

def test_get_aac():
    assert obs.get_aac('Melbourne') == 'VIC_PT042'

def test_uv_alert():
    uv = obs.uv_alert('VIC_PT042')
    assert uv is not None
    assert 'UV Index' in uv
