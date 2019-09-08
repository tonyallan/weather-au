from weather import uv_alert

obs_uv = uv_alert.UvAlert('Vic')
print(obs_uv.acknowedgment, '\n')

aac_list = obs_uv.aac_list()

for description in aac_list:
    print(f'{aac_list[description]} {description}')


location_name = 'Melbourne'
uv_alert = obs_uv.uv_alert(obs_uv.get_aac(location_name))

print('\nUV Alert for', location_name, uv_alert)
