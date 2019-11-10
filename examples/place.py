from weather_au import place

# Parse http://www.bom.gov.au/places/vic/parkville
place_data = place.Place('vic', 'endeavour-hills')
print(place_data.acknowedgment, '\n')

station_id = place_data.station_id()
air_temperature = place_data.air_temperature()

print(f'Station ID: {station_id}\nAir Temperature: {air_temperature}°C')

forecast = place_data.forecast()
print('\nForecast', forecast)

# mising data in forecast is omitted
if 'precis' in forecast:
    print('Precis', forecast['precis'])
else:
    print('No precis available')
