## Notes to myself

### Manual build and upload

```
cd ~/Documents/GitHub/weather-au
pytest
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

### Test on repl.it

[https://repl.it/@tony_allan/weather-au](https://repl.it/@tony_allan/weather-au)


### BOM UV Info

UV Index previously called UV Alert.

[Ultraviolet (UV) Index Data Services](http://reg.bom.gov.au/uv/data.shtml)
[About UV and sun protection times](http://reg.bom.gov.au/uv/)
[Average solar ultraviolet (UV) Index](http://reg.bom.gov.au/jsp/ncc/climate_averages/uv-index/index.jsp)