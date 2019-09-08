from weather import place

# Parse http://www.bom.gov.au/places/vic/parkville
obsp = place.Place('vic', 'parkville')

air_temperature = obsp.air_temperature()
station_id = obsp.station_id()

print(f'Station ID: {station_id}\nAir Temperature: {air_temperature}')
