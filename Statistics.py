import pandas as pd
from Dowload_csv import get_csv_path #import of the function from Dowload_csv.py

df = pd.read_csv(get_csv_path()) # setting the datafrase using the function
print(df.head()) #checking the dataframe loading 

# --- DATA CLEANING --- : cleaning and exploring data

print(df.columns)

# Column descriptions:
# Dataset columns:
# Unnamed         -> Row index from the original dataset
# date            -> Match date
# time            -> Match kickoff time
# comp            -> Competition name
# round           -> Matchday or round number
# day             -> Day of the week
# venue           -> Home or away match
# result          -> Match result (W = Win, D = Draw, L = Loss)
# gf              -> Goals scored by the team
# ga              -> Goals conceded by the team
# opponent        -> Opposing team
# xg              -> Expected goals for the team
# xga             -> Expected goals against the team
# poss            -> Ball possession percentage
# attendance      -> Number of spectators
# captain         -> Team captain
# formation       -> Team formation used
# opp formation   -> Opponent's formation
# referee         -> Match referee
# match report    -> Link/reference to the match report
# notes           -> Additional match notes
# sh              -> Total shots
# sot             -> Shots on target
# dist            -> Average shooting distance
# fk              -> Free-kick shots
# pk              -> Penalty kicks scored
# pkatt           -> Penalty kick attempts
# season          -> Season year
# team            -> Team name

print(df.isna().sum()[df.isna().sum() > 0])

#xg               2
#xga              2
#attendance     688 this variable could be usefull, so we can impute the NAN values
#notes         3898 this variable is not relevant and can be dropped
#dist             4
#fk               2







