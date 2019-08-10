import numpy as np
import matplotlib.pyplot as plt

cities = [
	# example element
	# {'city':'Narnia',
	# 'longitude': 3.14,
	# 'time': 11:11},
	{'city':'Portland, ME, USA',
	'longitude':'-70.2568',
	'time':'08:00'},
	{'city':'Miami, FL, USA',
	'longitude':'-80.1918',
	'time':'08:00'},
	{'city':'Chicago, IL, USA',
	'longitude':'-87.6298',
	'time':'07:00'},
	{'city':'San Antonio, TX, USA',
	'longitude':'-98.4936',
	'time':'07:00'},
	{'city':'Salt Lake City, UT, USA',
	'longitude':'-111.8910',
	'time':'06:00'},
	{'city':'Elko, NV, USA',
	'longitude':'-115.7631',
	'time':'05:00'},
	{'city':'Mountain View, CA, USA',
	'longitude':'-122.0839',
	'time':'05:00'},
	{'city':'Juneau, AK, USA',
	'longitude':'-134.4197',
	'time':'04:00'},
	{'city':'Anchorage, AK, USA',
	'longitude':'-149.9003',
	'time':'04:00'},
	{'city':'Honolulu, HI, USA',
	'longitude':'-157.8583',
	'time':'02:00'}
]

#test print
print(cities[1]['city'])
print(cities[1]['longitude'])
print(cities[1]['time'])

# plot arguments
colors = (0,0,0) # optional for arg 'c', potential to use for coloring by time zone, etc.
area = 9 # optional for arg 's', change point size as needed
x = []
y = []
for sub_list in cities: # loop option for assembling plot data
	x.append(sub_list['longitude'])
	y.append(sub_list['time'])


# Plot
plt.scatter(x, y, alpha=.8) # high alpha is okay for now, might need to lower once more data is added) 
plt.title('Correlation between Longitude and Local Time')
plt.xlabel('Longitude')
plt.ylabel('Local Time')
plt.show()
