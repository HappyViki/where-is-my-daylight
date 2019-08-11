import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('timezone_trend.csv')
df.columns = ['ID', 'Long', 'Local Time']

def scatterplot(df, x_dim, y_dim):
    
    # Variables
    x = df[x_dim]
    y = df[y_dim]
    c = []
    
    # Setup Plot
    fig, ax = plt.subplots(figsize=(10, 5))

    for i in x:
        if i < 0:
            c.append('r')
        else:
            c.append('g')
    
    # Set Plot
    ax.scatter(x, y, color=c)
    
    # Set Labels
    ax.set_title('Timezone Trend')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Local Time')
    
    # Display Plot
    plt.show()
    
scatterplot(df, 'Long', 'Local Time')