# Australian Weather Data (using bom.gov.au)
Access to the Australian [Bureau of Meteorology](https://bom.gov.au/) weather data.

[![Actions Status](https://github.com/tonyallan/weather-au/workflows/build/badge.svg)](https://github.com/tonyallan/weather-au/actions)
![PyPI](https://img.shields.io/pypi/v/weather-au)

Currently a work in progress subject to breaking changes!



## Purpose

The purpose of these modules is to fetch weather data from various Australian Bureau of Meteorology websites.



## Weather API

Fetches data from the API's at `api.weather.bom.gov.au` (e.g. [Parkville hourly forecast](https://api.weather.bom.gov.au/v1/locations/r1r143/forecasts/hourly)).

This information has been reverse engineered from the [beta website](https://weather.bom.gov.au/) with no information about future access arrangements, content or availability.


### Example using `WeatherApi`
```python3
import sys
from weather_au import api

loc = '3052'
w = api.WeatherApi(search=loc, debug=0)

location = w.location()

# check if the search produced a result (other methods will also return None if the search fails).
if location is None:
    sys.exit('Search failed for location ' + loc)

print(f"\nLocation: {location['name']} {location['state']}, timezone:{location['timezone']}\n")

for warn in w.warnings():
    print(f"Warning short title:  {warn['short_title']}")

    warning = w.warning(id=warn['id'])
    print(f"Warning title:        {warning['title']}")

observations = w.observations()
print(f"\nObservations (temp): {observations['temp']:2}")

forecast_rain = w.forecast_rain()
print(f"Forecast Rain:       amount:{forecast_rain['amount']}, chance:{forecast_rain['chance']}")

```


### Example using `Summary`
```python3
from weather_au import summary

print(summary.Summary(search='parkville').summary_text())
```



## XML and Scraping

Modules:

- `observations` - fetch XML formatted data from the BOM FTP server.
- `uv_index` - fetch the UV data from the XML encoded state based IDZ00107-IDZ00113 products.
- `place` - scrape data from location based [pages](http://www.bom.gov.au/places/vic/parkville/).

Where possible WeatherApi, should be used as it uses an API rather than scraping the web page.


## Disclaimer

This project is not related to or endorsed by the Australian Bureau of Meteorology (BOM). 

From the BOM [copyright notice](http://reg.bom.gov.au/other/copyright.shtml): Where no terms of use are associated with a set of material, then you may download, use and copy that material for personal use, or use within your organisation but you may not supply that material to any other person or use it for any commercial purpose.



## Usage

Additional examples are in the `examples` folder.



## URL's

- Base for anon FTP data `ftp://ftp.bom.gov.au/anon/gen/`
- Capital City Observations - VIC - Melbourne (Olympic Park) `http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json`
  - where `IDV60901` is the product, and
  - `95936` is the weather station id.
- Weather Observations - VIC - Melbourne (Olympic Park) `http://www.bom.gov.au/fwo/IDV60910/IDV60910.95936.json`
- `http://www.bom.gov.au/places/vic/parkville/`



## Resources

1. [New weather page](https://weather.bom.gov.au/)
1. [FTP public products](http://www.bom.gov.au/catalogue/anon-ftp.shtml)
1. [Weather Data Services](http://www.bom.gov.au/catalogue/data-feeds.shtml)
1. [How to use BOM API for weather, tide and swell](https://stackoverflow.com/questions/39534018/how-to-use-bom-api-for-weather-tide-and-swell)
1. [Github has a number of projects using bom.gov.au data](https://github.com/search?q=bom.gov.au)
1. [256 km Melbourne Radar Loop](http://www.bom.gov.au/products/IDR022.loop.shtml)
1. [Catalogue of RSS Feeds](http://www.bom.gov.au/rss/)

