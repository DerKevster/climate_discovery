import pandas as pd

data = pd.read_csv('Weather_Stations.csv', delimiter=';')
size_list = data['Column3'].tolist()

for i in range(len(size_list)):
    size_list[i] = float(size_list[i][:-1])

print(f'{sum(size_list) / 1048576} GB')
