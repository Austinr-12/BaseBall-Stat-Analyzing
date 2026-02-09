import pandas as pd

batting = pd.read_csv('Batting.csv')

active_players = batting[batting['AB'] > 0]
active_players.describe()

batting.groupby('playerID')['HR'].sum().sort_values(ascending=False)