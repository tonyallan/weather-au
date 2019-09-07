from weather import observations, place

# Read and parse the XML file ftp://ftp.bom.gov.au/anon/gen/fwo/IDV60920.xml
obs = observations.Observations('Vic')

# Print the product ID associated with this XML file
# product -> amoc -> identifier = IDV60920
print(f'Product ID: {obs.identifier}\n')

# <observations>
for station in obs.stations():

    # <station wmo-id="95936" ... description="Melbourne (Olympic Park)">
    wmo_id = station['wmo-id']                                  
    description = station['description']

    # <element units="Celsius" type="air_temperature">9.8</element>
    air_temperature = obs.air_temperature(station['wmo-id'])
    if air_temperature is None:
        print(f'{wmo_id} {description}')
    else:
        print(f'{wmo_id} {description}   ({air_temperature})')


# http://www.bom.gov.au/places/vic/parkville
obsp = place.Place('vic', 'parkville')

air_temperature = obsp.air_temperature()
station_id = obsp.station_id()

print(f'\n{station_id} {air_temperature}')
