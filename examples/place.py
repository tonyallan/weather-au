from weather import place

# Parse http://www.bom.gov.au/places/vic/parkville
obs_place = place.Place('vic', 'parkville')
print(obs.acknowedgment)

station_id = obs_place.station_id()
air_temperature = obs_place.air_temperature()

print(f'Station ID: {station_id}\nAir Temperature: {air_temperature}')

forecast = obs_place.forecast()
print('\nForecast', forecast)
