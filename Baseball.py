import pandas as pd

batting = pd.read_csv('Batting.csv')

active_players = batting[batting['AB'] > 0]
active_players.describe()

batting.groupby('playerID')['HR'].sum().sort_values(ascending=False)

babe_ruth = batting[batting['playerID'] == 'ruthba01']

start_year = babe_ruth['yearID'].min()
start_year = babe_ruth['yearID'].max()

ruth_years = batting[(batting['yearID'] >= start_year) & (batting['yearID'] <= end_year)]
ruth_years.groupby('playerID')['HR'].sum().sort_values(ascending=False)