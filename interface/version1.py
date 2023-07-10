import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/kev/code/DerKevster/climate_discovery/dataframe/output.csv')

# Enter search parameters

month = input("Number of month: ")
min = input("Minimum temperature: ")
max = input("Maximum temperature: ")

# Reduce data to right month

df = df[df['MONTH'] == int(month)]
print(df)

# Print out world map

x_values = df['LONGITUDE']
y_values = df['LATITUDE']

colors = [
    'green' if tmin > float(min) and tmax < float(max) else
    'red' for date, tmin, tmax in zip(df['MONTH'], df['TMIN'], df['TMAX'])
]

plt.scatter(x_values, y_values, c=colors, s=2)
plt.xlabel('LONGITUDE')
plt.ylabel('LATITUDE')
plt.title('Locations in the World')
plt.show()
