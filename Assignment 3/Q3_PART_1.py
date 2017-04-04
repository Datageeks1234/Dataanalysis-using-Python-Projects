import pandas as pd 
import os
cricket_data = pd.read_csv(os.path.join("data",'cricket_matches.csv'))
def get_score(i):
    if cricket_data['home'].ix[i] == cricket_data['innings1'].ix[i]:
        return cricket_data['innings1_runs'].ix[i]
    return cricket_data['innings2_runs'].ix[i]
cricket_data['home_score']= map(get_score, cricket_data.index)
cricket_data['home_score'] = map(float,cricket_data['home_score'].values )
host_win_data = cricket_data[cricket_data['home'] == cricket_data['winner']]
mean_data = host_win_data.groupby('home').mean()
print mean_data['home_score'].head(2)
mean_data['home_score'].to_csv('Q3_PARTONE.csv')