from Sun import Sun

coords = {'longitude' : 23.10, 'latitude' : 53.13 }

sun = Sun()

print('Wschod - {}:{}'.format(sun.getSunriseTime( coords )['hr'],sun.getSunriseTime( coords )['min']))
print('Zachód - {}:{}'.format(sun.getSunsetTime( coords )['hr'],sun.getSunsetTime( coords )['min']))