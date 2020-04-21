## Notes to Self


### Manual build and upload

```
cd ~/GitHub/weather-au
pytest
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

`twine` will ask for the PyPi username and password.


### Test on repl.it

[https://repl.it/@tony_allan/weather-au](https://repl.it/@tony_allan/weather-au)


### BOM UV Info

UV Index previously called UV Alert.

[Ultraviolet (UV) Index Data Services](http://reg.bom.gov.au/uv/data.shtml)
[About UV and sun protection times](http://reg.bom.gov.au/uv/)
[Average solar ultraviolet (UV) Index](http://reg.bom.gov.au/jsp/ncc/climate_averages/uv-index/index.jsp)


### Testing

The following code is added to example to ease local testing:

```
import os, sys
sys.path.append(os.path.abspath('.'))
```

To run the tests, cd to the weater-au folder and run:

```
pytest
```

### Weather Radar

There are two versions of the weather radar, one associated with the [old website](http://www.bom.gov.au/products/IDR024.loop.shtml), which for each location, is a [background](http://www.bom.gov.au/products/radar_transparencies/IDR024.background.png), [location](http://www.bom.gov.au/products/radar_transparencies/IDR024.locations.png) and [range](http://www.bom.gov.au/products/radar_transparencies/IDR024.range.png) image and six timestamped [overlay](http://www.bom.gov.au/radar/IDR024.T.202004210548.png) images with the data.

With a bit of effort a composite image could be created.

The new website uses an arcgis tile server with [background](https://tiles.arcgis.com/tiles/eJi5Ccfp64bqr5ym/arcgis/rest/services/proton_labels_std/MapServer/tile/9/312/459) and [overlay](https://api.weather.bom.gov.au/v1/rainradar/tiles/202004210500/8/229/156.png) tiles.

This format is more complex with no obvious data source to marry the tiles together. If you change the radar on the webpage then additional images are fetched but no new data which implies that the needed tiles are calculated by the javascript on the page.
