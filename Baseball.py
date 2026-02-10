import pandas as pd
import matplotlib.pyplot as plt

batting = pd.read_csv('Batting.csv')

active_players = batting[batting['AB'] > 0]
active_players.describe()

batting.groupby('playerID')['HR'].sum().sort_values(ascending=False)

babe_ruth = batting[batting['playerID'] == 'ruthba01']

start_year = babe_ruth['yearID'].min()
start_year = babe_ruth['yearID'].max()

ruth_years = batting[(batting['yearID'] >= start_year) & (batting['yearID'] <= end_year)]
ruth_years.groupby('playerID')['HR'].sum().sort_values(ascending=False)


total_hr_by_year = batting.groupby('yearID')['HR'].sum()
plt.figure(figsize=(10, 6))
plt.plot(total_hr_by_year.index, total_hr_by_year.values)

plt.title('Total Home Runs Over Time')
plt.xlabel('Year')
plt.ylabel('Total Home Runs')

plt.grid(True)
plt.show()