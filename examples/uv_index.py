from weather_au import uv_index

uv_data = uv_index.UvIndex('Vic')
print(uv_data.acknowedgment, '\n')

aac_list = uv_data.aac_list()

for description in aac_list:
    print(f'{aac_list[description]} {description}')


location_name = 'Melbourne'
uv_message = uv_data.uv_message(uv_data.get_aac(location_name))

print('\nUV Message for', location_name, uv_message)
