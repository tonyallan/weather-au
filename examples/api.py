from weather_au import api

w = api.WeatherApi(search='parkville+vic', debug=0)

print(repr(w))
print(w.acknowedgment)


location = w.location()
print(f"\nLocation: {location['name']} {location['state']}, timezone:{location['timezone']}\n")


for warn in w.warnings():
    print(f"Warning short title:  {warn['short_title']}")

    warning = w.warning(id=warn['id'])
    print(f"Warning title:        {warning['title']}")


observations = w.observations()
print(f"\nObservations (temp): {observations['temp']:2}")


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


print('\n3 Hourly:')
for f in w.forecasts_3hourly():
    print(f"{f['time']} temp:{f['temp']:2}, {f['icon_descriptor']}")
