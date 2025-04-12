country_code = {'India' : '0091',
                'Australia' : '0025',
                'Indonesia' : '0062'}

#search dictionary for country code of india 
print("country code of Indonesia -")
print(country_code.get('Indonesia', 'Not found'))

print()

#search dictionary for country code of japan 
print("country code of japan -")
print(country_code.get('japan', 'Not found'))
