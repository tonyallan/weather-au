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
