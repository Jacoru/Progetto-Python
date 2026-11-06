# Serie A Match Analysis (2020-2025)

## Overview

This project analyzes Serie A football matches from the 2020-2025 seasons using Python and Pandas.

The objective is to perform data exploration, cleaning, statistical analysis, and visualization of match-related metrics such as:

- Match results
- Goals scored and conceded
- Expected Goals (xG)
- Expected Goals Against (xGA)
- Ball possession
- Shots and shots on target
- Team performance across seasons

The project uses the Kaggle API through the `kagglehub` package to automatically download the dataset.

---

## Dataset

The dataset contains detailed information about Serie A matches from 2020 to 2025.

### Source

[Kaggle - Serie A Matches Dataset (2020-2025)](https://www.kaggle.com/datasets/marcelbiezunski/serie-a-matches-dataset-2020-2025)

---

## Dataset Features

The dataset includes the following information:
## Dataset Features

| Column | Description |
|----------|----------|
| Unnamed:0 | Original row index (ID)|
| date | Match date |
| time | Match kickoff time |
| comp | Competition name |
| round | Matchday or round number |
| day | Day of the week |
| venue | Home or away match |
| result | Match result (W = Win, D = Draw, L = Loss) |
| gf | Goals scored by the team |
| ga | Goals conceded by the team |
| opponent | Opposing team |
| xg | Expected goals for the team |
| xga | Expected goals against the team |
| poss | Ball possession percentage |
| attendance | Number of spectators |
| captain | Team captain |
| formation | Team formation used |
| opp formation | Opponent's formation |
| referee | Match referee |
| match report | Link/reference to the match report |
| notes | Additional match notes |
| sh | Total shots |
| sot | Shots on target |
| dist | Average shooting distance |
| fk | Free-kick shots |
| pk | Penalty kicks scored |
| pkatt | Penalty kick attempts |
| season | Season year |
| team | Team name |

---

## Requirements

There will be a requirements file to define entirely the list of Library.

---

## Running the Project

The dataset is automatically downloaded through KaggleHub:

```python
import kagglehub

folder = kagglehub.dataset_download(
    "marcelbiezunski/serie-a-matches-dataset-2020-2025"
)
```

Then the CSV file can be loaded with:

```python
import pandas as pd
import os

csv_file = os.path.join(folder, "matches_seriea.csv")

df = pd.read_csv(csv_file)
```

---

## Analysis
The analysis are runned in the statistics' file.
The project can be extended to compute some descriptive analysis like:

- Total points by team
- Home vs Away performance
- Win/Draw/Loss distribution
- Offensive and defensive efficiency
- Goal distribution analysis
- Correlation between xG and actual goals
exc..
Following this part, there will be a description part with some graphs and a short part of modelling:
(Haven't done yet)
---

## Author
Russo Jacopo - Statale University

Developed in Python using:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- KaggleHub
