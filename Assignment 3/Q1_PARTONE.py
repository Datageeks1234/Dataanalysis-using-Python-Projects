import pandas as pd
import os
data = pd.read_csv(os.path.join('data','vehicle_collisions.csv'), parse_dates = [1])
data['DATE'] = [i.to_datetime() for i in data['DATE']]
data['year']=[i.year for i in data['DATE']]
data['year-month']=["{0}-{1}".format(i.year,i.month) for i in data['DATE']]
data_2016 = data[data['year']==2016]
data_required = pd.DataFrame({'MONTH':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','spe','Oct','Nov','Dec'],
'MANHATTAN':range(12),'NYC':range(12),'PERCENTAGE':range(12)
	})
data_required = pd.DataFrame({'MONTH':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','spe','Oct','Nov','Dec'],
'MANHATTAN':range(12),'NYC':range(12),'PERCENTAGE':range(12)
	})
data_required['MANHATTAN']=data_2016[data['BOROUGH']=="MANHATTAN"].groupby('year-month').count()['BOROUGH'].values
data_required['NYC']=data_2016.groupby('year-month').count()['BOROUGH'].values
data_required['PERCENTAGE'] = (data_required['MANHATTAN']/data_required['NYC'])*100
data_required.to_csv('Q1_PARTONE.csv')