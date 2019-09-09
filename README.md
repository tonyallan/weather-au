# Australian Weather Data (using bom.gov.au)
Access to the Australian [Bureau of Meteorology](https://bom.gov.au/) weather data.

[![Actions Status](https://github.com/tonyallan/weather-au/workflows/build/badge.svg)](https://github.com/tonyallan/weather-au/actions)
![PyPI](https://img.shields.io/pypi/v/weather-au)

Currently a work in progress subject to frequent breaking changes!

## Purpose

The purpose of these modules is to fetch weather data from various Australian Bureau of Meteorology websites.

### `weather_au_api` Beta JSON API

Fetch data from the beta API's at `api.weather.bom.gov.au` (e.g. [Parkville 3-hourly forecast](https://api.weather.bom.gov.au/v1/locations/r1r143/forecasts/3-hourly)).

This information has been reverse engineered from the [beta website](https://weather.bom.gov.au/) with no information about future access arrangements, content or availability.

### `weather_au` XML and Scraping

Modules:

- `observations` - fetch XML formatted data from the BOM FTP server.
- `uv_index` - fetch the UV data from the XML encoded state based IDZ00107-IDZ00113 products.
- `place` - scrape data from location based [pages](http://www.bom.gov.au/places/vic/parkville/).


## Disclaimer

This project is not related to or endorsed by the Australian Bureau of Meteorology (BOM). 

From the BOM [copyright notice](http://reg.bom.gov.au/other/copyright.shtml): Where no terms of use are associated with a set of material, then you may download, use and copy that material for personal use, or use within your organisation but you may not supply that material to any other person or use it for any commercial purpose.

## Usage

Additional examples are in the `examples` folder.

### Sample for Parkville in Melbourne Vic Australia

```python3
from weather import place, observations, uv_index

# Parse http://www.bom.gov.au/places/vic/parkville
place_data = place.Place('vic', 'parkville')
print(place_data.acknowedgment)

station_id = place_data.station_id()
print('Station ID',station_id)

air_temperature = place_data.air_temperature()
print('Air Temperature', air_temperature)

forecast = place_data.forecast()
print('Forecast', forecast)


uv_data = uv_index.UvIndex('Vic')
print('\n' + uv_data.acknowedgment)

location_name = 'Melbourne'
uv_message = uv_data.uv_message(uv_data.get_aac(location_name))

print('UV Message for', location_name, uv_message)
```

Produces output:
```
Data courtesy of Bureau of Meteorology (http://www.bom.gov.au/places/vic/parkville)
Station ID 95936
Air Temperature 8.6
Forecast {'issued': '4:20 pm AEST on Sunday 8 September 2019', 'date': 'Rest of Monday', 'min': '8', 'max': '13', 'precis': 'Showers easing. Wind easing.'}

Data courtesy of Bureau of Meteorology (ftp://ftp.bom.gov.au/anon/gen/fwo/IDZ00112.xml)
UV Message for Melbourne Sun protection recommended from 10:30 am to  2:00 pm, UV Index predicted to reach 4 [Moderate]
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

