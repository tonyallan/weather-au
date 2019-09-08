from weather import place, observations, uv_alert

# Parse http://www.bom.gov.au/places/vic/parkville
obs_place = place.Place('vic', 'parkville')
print(obs_place.acknowedgment)

station_id = obs_place.station_id()
print('Station ID',station_id)

air_temperature = obs_place.air_temperature()
print('Air Temperature', air_temperature)

forecast = obs_place.forecast()
print('Forecast', forecast)


obs_uv = uv_alert.UvAlert('Vic')
print('\n' + obs_uv.acknowedgment)

location_name = 'Melbourne'
uv_alert = obs_uv.uv_alert(obs_uv.get_aac(location_name))

print('UV Alert for', location_name, uv_alert)
