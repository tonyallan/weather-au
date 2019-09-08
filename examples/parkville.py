from weather import place, observations, uv_alert

# Parse http://www.bom.gov.au/places/vic/parkville
obs_place = place.Place('vic', 'parkville')

station_id = obs_place.station_id()
print('\nStation ID',station_id)

air_temperature = obs_place.air_temperature()
print('Air Temperature', air_temperature)

forecast = obs_place.forecast()
print('\nForecast', forecast)

obs_uv = uv_alert.UvAlert('Vic')

location_name = 'Melbourne'
uv_alert = obs_uv.uv_alert(obs_uv.get_aac(location_name))

print('\nUV Alert for', location_name, uv_alert)
