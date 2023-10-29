"""
An analysis for Detroit Lions
"""


import pandas as pd
import matplotlib.pyplot as plt

cities_df = pd.read_csv('cities.csv')
mlb_teams = pd.read_csv('mlb_teams.csv')
nfl_stadiums = pd.read_csv('nfl_stadiums.csv')
nfl_teams = pd.read_csv('nfl_teams.csv')
nhl_teams = pd.read_csv('nhl_teams.csv')

df_list = [cities_df, mlb_teams, nfl_stadiums, nfl_teams, nhl_teams]

#print head for each one
for df in df_list:
    print(df.head())