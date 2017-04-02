import pandas as pd 
import os
emp_data = pd.read_csv(os.path.join("data",'employee_compensation.csv'))
data_req = emp_data.groupby(['Organization Group','Department']).mean()
data_req['Total Compensation'].to_csv('Q2_PARTONE.csv')
print data_req.head(2)