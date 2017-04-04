import re
import pandas as pd 
import os
movie_data = pd.read_csv(os.path.join("data",'movies_awards.csv'))
lenght_movies = movie_data['Title'].count()
dummy=[0 for i in xrange(lenght_movies)]

d={}
columns = ['Awards_won','Awards_nominated','Primetime_awards_won','Primetime_awards_nominated',
           'Oscar_awards_won','Oscar_awards_nominated','Golden_Globe_awards_won','Golden_Globe_awards_nominated',
          'BAFTA_awards_won','BAFTA_awards_nominated','Another_nominated','Another_won']
cols = {'Movies':movie_data['Title'],'Awards':movie_data['Awards']}
cols1 = d.fromkeys(columns,dummy)
cols.update(cols1)
req_data = pd.DataFrame(cols)
req_data['Awards'].fillna("",inplace=True)
req_data['Awards'] = [i.lower() for i in req_data['Awards'].values]
nominated = 'nominated for [0-9]+'
for i in req_data.index:
    awards  = req_data['Awards'].ix[i]
    if awards:
        if 'nominated for' in awards:
            oscar = re.findall('{0} oscar'.format(nominated),awards)
            goldenglobe = re.findall('{0} golden globe'.format(nominated),awards)
            primetime = re.findall('{0} primetime'.format(nominated),awards)
            bafta = re.findall('{0} BAFTA'.format(nominated),awards)
            another = re.findall('{0} another'.format(nominated),awards) 
            if oscar:
                req_data['Oscar_awards_nominated'].ix[i] = oscar[0].split()[-2]
            if goldenglobe:
                req_data['Golden_Globe_awards_nominated'].ix[i] = goldenglobe[0].split()[-3]
            if primetime:
                req_data['Primetime_awards_nominated'].ix[i] = primetime[0].split()[-2]
            if bafta:
                req_data['BAFTA_awards_nominated'].ix[i] = bafta[0].split()[-2]
            if another:
                req_data['Another_nominated'].ix[i] = another[0].split()[-2]
        if 'won' in awards or "win" in awards:
            oscar_wins = re.findall('won [0-9]+ oscar',awards)
            primetime_wins = re.findall('won [0-9]+ primetime',awards)
            bafta_wins = re.findall('won [0-9]+ bafta',awards)
            another_wins = re.findall('another [0-9]+ win',awards)
            goldenglobe_wins = re.findall('won [0-9]+ goldenglobe',awards)
            if oscar_wins:
                req_data['Oscar_awards_won'].ix[i] = oscar_wins[0].split()[-2]
            if goldenglobe_wins:
                req_data['Golden_Globe_awards_won'].ix[i] = goldenglobe_wins[0].split()[-3]
            if primetime_wins:
                req_data['Primetime_awards_won'].ix[i] = primetime_wins[0].split()[-2]
            if bafta_wins:
                req_data['BAFTA_awards_won'].ix[i] = bafta_wins[0].split()[-2]
            if another_wins:
                req_data['Another_won'].ix[i] = another_wins[0].split()[-2]

        if re.search('another [0-9]+ nominat',awards):
            anot = re.findall('another [0-9]+ nominat',awards)
            if anot:
                req_data['Another_nominated'].ix[i] = anot[0].split()[-2]
                
        if 'win' in awards:
            wins = re.findall('[0-9 ]+win[s]*',awards)
            if wins:
                req_data['Awards_won'].ix[i]= wins[0].split()[0]
        if 'nominat' in awards:
            nomi = re.findall('[0-9 ]+nominat*',awards)
            if nomi:
                req_data['Awards_nominated'].ix[i] = nomi[0].split()[0]
print req_data.head(2)
req_data.to_csv('Q4_PART_1.csv')
            
            
