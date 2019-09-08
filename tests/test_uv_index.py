import os, sys
sys.path.append(os.path.abspath('.'))
import pytest
import urllib


from weather import uv_index

def test_invalid_state():
    with pytest.raises(KeyError, match='zzz'):
        uv_data = uv_index.UvIndex('zzz')

uv_data = uv_index.UvIndex('Vic')

def test_obs():
    assert uv_data is not None

def test_acknowedgment_url():
    assert len(uv_data.url) > 0
    assert len(uv_data.acknowedgment) > 0

def test_identifier():
    assert uv_data.identifier == 'IDZ00112'

def test_aac_list():
    aac_list = uv_data.aac_list()
    assert len(aac_list) > 10

    for description in aac_list:
        assert description is not None
        assert aac_list[description] is not None

def test_get_aac():
    assert uv_data.get_aac('Melbourne') == 'VIC_PT042'

def test_uv():
    uv_message = uv_data.uv_message('VIC_PT042')
    assert uv_message is not None
    
    # http://reg.bom.gov.au/uv/data.shtml
    assert 'Sun protection' in uv_message
