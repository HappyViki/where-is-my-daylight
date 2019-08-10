import numpy as np
import matplotlib.pyplot as plt

cities = [
	# example element
	# {'city':'Narnia',
	# 'longitude': 3.14,
	# 'time': 11:11},
	{'city':'Salt Lake City, UT, USA',
	'longitude':'-111.8910',
	'time':'06:00'},
	{'city':'Mountain View, CA, USA',
	'longitude':'-122.0839',
	'time':'05:00'}
]

#test print
print(cities[1]['city'])
print(cities[1]['longitude'])
print(cities[1]['time'])

# plot arguments
x = cities['longitude'] #likely to fail, fix syntax or reformat cities object
y = cities['time']
colors = (0,0,0) # optional
area = 9 # optional

# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Correlation between Longitude and Local Time')
plt.xlabel('Longitude')
plt.ylabel('Local Time')
plt.show()
