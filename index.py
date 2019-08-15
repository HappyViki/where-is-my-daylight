import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('data.csv')
df.columns = ['cities', 'longitude', 'utc_offset']

# Variables
x_long = df['longitude']
y_offset = df['utc_offset']
c = []

# Setup Plot
fig, ax = plt.subplots(figsize=(10, 5))
plt.grid()

for long,offset in zip(np.absolute(x_long),np.absolute(y_offset)):
    center = 15*offset
    if (long < center-15) or (long > center+15):
        c.append('r')
    elif (long < center-5) or (long > center+5):
        c.append('y')
    else:
        c.append('g')

# Set Plot
ax.scatter(x_long, y_offset, color=c)

# Set Labels
ax.set_title('Timezone Trend')
ax.set_xlabel('Longitude')
ax.set_ylabel('Offset From UTC')

# Display Plot
plt.show()