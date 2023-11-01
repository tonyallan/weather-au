import sys
from weather_au import api

loc = '3802'
w = api.WeatherApi(search=loc, debug=0)

print(repr(w))
print(w.acknowedgment)


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
print(f"Observations (temp): {observations['temp']:2}")


forecast_rain = w.forecast_rain()
print(f"Forecast Rain:       amount:{forecast_rain['amount']}, chance:{forecast_rain['chance']}")


print('\nDaily:')
for f in w.forecasts_daily():
    if f['temp_min'] is None:
        temp_min = '--'
    else:
        temp_min = f"{f['temp_min']:2}"

    if f['temp_max'] is None:
        temp_max = '--'
    else:
        temp_max = f"{f['temp_max']:2}"

    print(f"{f['date']} temp_min:{temp_min}, temp_max:{temp_max}, {f['short_text']}")


print('\nHourly:')
for f in w.forecasts_hourly():
    print(f"{f['time']} temp:{f['temp']:2}, {f['icon_descriptor']}")
