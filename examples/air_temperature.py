from weather import observations, place


obs = observations.Observations('Vic')

print(f'Product ID: {obs.identifier}\n')

for station in obs.stations():
    wmo_id = station['wmo-id']
    description = station['description']
    air_temperature = obs.air_temperature(station['wmo-id'])
    if air_temperature is None:
        print(f'{wmo_id} {description}')
    else:
        print(f'{wmo_id} {description}   ({air_temperature})')


obsp = place.Place('vic', 'parkville')

air_temperature = obsp.air_temperature()
station_id = obsp.station_id()

print(f'\n{station_id} {air_temperature}')
