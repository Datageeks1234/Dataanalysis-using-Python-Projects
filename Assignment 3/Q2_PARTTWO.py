import pandas as pd 
import os
emp_data = pd.read_csv(os.path.join("data",'employee_compensation.csv'))
data_calender = emp_data[emp_data['Year Type']=='Calendar']
#find average for each of the  columns for every employee
emp_means  = data_calender.groupby('Job Family').mean()
data_calender['sal5per'] = (data_calender['Salaries']*5.0)/100
emp_data_ot_gt_5per = data_calender[data_calender['Overtime']>data_calender['sal5per']]
emp_data_ot_gt_5per_gpby_jobfamily = emp_data_ot_gt_5per.groupby('Job Family').mean()
emp_data_ot_gt_5per_gpby_jobfamily['Percent_Total_Benifit']= (emp_data_ot_gt_5per_gpby_jobfamily['Total Benefits']/emp_data_ot_gt_5per_gpby_jobfamily['Total Compensation'])*100
data_req  = emp_data_ot_gt_5per_gpby_jobfamily[['Total Benefits','Total Compensation','Percent_Total_Benifit']]
data_req.to_csv('Q2_PARTTWO.csv')
print data_req.head(5)