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
# Rockies vs the League

team_hr_per_year = (
  batting
  .groupby(['yearID', 'teamID'])['HR']
  .sum()
  .reset_index()
)

rockies_hr = (
  team_hr_per_year
  [team_hr_per_year['teamID'] == 'COL']
  .set_index('yearID')['HR']
)

league_avg_hr = (
  team_hr_per_year
  .groupby('yearID')['HR']
  .mean()
)

league_avg_hr = league_avg_hr[league_avg_hr.index >= 1993]

plt.figure(figsize=(10, 6))

# starting to plot league average
plt.plot(league_avg_hr.index,
  league_avg_hr.values,
  label='League Average',
  color='orange',
  linestyle='--'
)

#Plotting Rockies
plt.plot(
  rockies_hr.index,
  rockies_hr.values
  label = 'Colorado Rockies',
  color = '#33006F'
)

#comparing the league average and Rockies and nameing graph
plt.title('Colorado Rockies Home Runs vs. League Average')
plt.xlabel('Year')
plt.ylable('Home Runs')
plt.legend()

plt.grid(True)
plt.show


#calculating OBP 
batting[['BB', 'HBP', 'Sf']] = batting[['BB', 'HBP', 'SF']].fillna(0)

#making OBP column
batting['OBP'] = (
  (batting['H'] + batting['BB'] + batting['HBP']) /
  (batting['AB'] + batting['BB'] + batting['HBP'] + batting['SF'])
)

#No plate appearances then fill 0
batting['OBP'] = batting['OBP'].fillna(0)

#loading and getting salary data
salaries = pd.read_csv('Salaries.csv')

batting_with_salary = batting.merge(
  salaries
  on = ['playerID', 'hearID', 'teamID']
  how = 'left'
)

batting_with_salary.head()

#Eliminate players that we are not interested in
value_df = batting_with_salary[
  (batting_with_salary['salary'] > 0) &
  (batting_with_salary['OBP'] > 0) &
  (batting_with_salary['AB'] >= 200)
].copy()

#calculate OBP per dollar 
value_DF['OBP_per_dollar'] = value_df['OBP]'] / value_df['salary']


#function to offically sort this data 
value_df_sorted = value_df.sort_values(
  by = 'OBP_per dollar',
  ascending = False
)