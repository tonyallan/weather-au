from weather import uv_index

obs = uv_index.UvIndex('Vic')

print(f'Product ID: {obs.identifier}\n')

# <observations>
for area in obs.area():

    # <station wmo-id="95936" ... description="Melbourne (Olympic Park)">
    aac = area['aac']                                  
    description = area['description']
    print(f'{aac} {description}')


# VIC_PT042 Melbourne
print(obs.uv_alert('VIC_PT042'))
