# Australian Weather Data (using bom.gov.au)
Access to the Australian [Bureau of Meteorology](https://bom.gov.au/) weather data.

[![Actions Status](https://github.com/tonyallan/weather-au/workflows/build/badge.svg)](https://github.com/tonyallan/weather-au/actions)
![PyPI](https://img.shields.io/pypi/v/weather-au)

Currently a work in progress!

## Disclaimer

This project is not related to or endorsed by the Australian Bureau of Meteorology (BOM). 

From the BOM [copyright notice](http://reg.bom.gov.au/other/copyright.shtml): Where no terms of use are associated with a set of material, then you may download, use and copy that material for personal use, or use within your organisation but you may not supply that material to any other person or use it for any commercial purpose.

## Usage

Additional examples are in the `examples` folder.

### Sample for Parkville in Melbourne Vic Australia

```python3
from weather import place, observations, uv

# Parse http://www.bom.gov.au/places/vic/parkville
obs_place = place.Place('vic', 'parkville')
print(obs_place.acknowedgment)

station_id = obs_place.station_id()
print('Station ID',station_id)

air_temperature = obs_place.air_temperature()
print('Air Temperature', air_temperature)

forecast = obs_place.forecast()
print('Forecast', forecast)


obs_uv = uv.Uv('Vic')
print('\n' + obs_uv.acknowedgment)

location_name = 'Melbourne'
uv = obs_uv.uv(obs_uv.get_aac(location_name))

print('UV Alert for', location_name, uv)
```

Produces output:
```
Data courtesy of Bureau of Meteorology (http://www.bom.gov.au/places/vic/parkville)
Station ID 95936
Air Temperature 9.3
Forecast {'issued': '4:20 pm AEST on Sunday 8 September 2019', 'date': 'Rest of Sunday', 'precis': 'Showers easing. Windy.'}

Data courtesy of Bureau of Meteorology (ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00112.xml)
UV Alert for Melbourne Sun protection recommended from 10:30 am to  2:00 pm, UV Index predicted to reach 4 [Moderate]
```

*The Forecast dict may also include min and max, depending on the time of day.*

## URL's

- Base for anon FTP data `ftp://ftp.bom.gov.au/anon/gen/`
- Capital City Observations - VIC - Melbourne (Olympic Park) `http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json`
  - where `IDV60901` is the product, and
  - `95936` is the weather station id.
- Weather Observations - VIC - Melbourne (Olympic Park) `http://www.bom.gov.au/fwo/IDV60910/IDV60910.95936.json`
- `http://www.bom.gov.au/places/vic/parkville/`

## Resources

1. [FTP public products](http://www.bom.gov.au/catalogue/anon-ftp.shtml)
1. [Weather Data Services](http://www.bom.gov.au/catalogue/data-feeds.shtml)
1. [How to use BOM API for weather, tide and swell](https://stackoverflow.com/questions/39534018/how-to-use-bom-api-for-weather-tide-and-swell)
1. [Github has a number of projects using bom.gov.au data](https://github.com/search?q=bom.gov.au)
1. [256 km Melbourne Radar Loop](http://www.bom.gov.au/products/IDR022.loop.shtml)
1. [Catalogue of RSS Feeds](http://www.bom.gov.au/rss/)

