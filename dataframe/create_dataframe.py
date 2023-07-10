import os
import pandas as pd

folder = '/home/kev/code/DerKevster/climate_discovery/raw_data/'

# Limit the data to the last 10 years and combine them into one pandas dataframe

dfs = []
error_files = []

for file in os.listdir(folder):
    if os.path.isfile(folder+file) and os.path.getsize(folder+file) > 0:
        try:
            df = pd.read_csv(folder+file)
            df['DATE'] = pd.to_datetime(df['DATE'])
            df = df[df['DATE'] >= '2013-07']
            dfs.append(df)
        except pd.errors.ParserError:
            error_files.append(file)

print(f'Error files: {error_files}')

df = pd.concat(dfs)

# Limit to columns I need

df = df[['STATION', 'DATE', 'LATITUDE', 'LONGITUDE', 'TMAX', 'TMIN']]

# Drop all rows that have NaNs

df.dropna(inplace=True)

# Average the data by STATION and MONTH

df['DATE'] = pd.to_datetime(df['DATE'])
df['MONTH'] = df['DATE'].dt.month
df_monthly_avg = df.groupby(['STATION', 'MONTH']).mean(numeric_only=True)
df_monthly_avg = df_monthly_avg.reset_index()

df_monthly_avg.to_csv('output.csv', index=False)
