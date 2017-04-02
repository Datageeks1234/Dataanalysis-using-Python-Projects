import pandas as pd
import os
data = pd.read_csv(os.path.join('data','vehicle_collisions.csv'), parse_dates = [1])
data['DATE'] = [i.to_datetime() for i in data['DATE']]
data['year']=[i.year for i in data['DATE']]
data_gt_2015 = data[data['year']>=2015]
boroughs= data_gt_2015['BOROUGH'].unique()
data_required = pd.DataFrame({'BOROUGH':boroughs,'ONE_VEHICLE_INVOLVED':range(len(boroughs)),
                             'TWO_VEHICLE_INVOLVED':range(len(boroughs)),
                              'THREE_VEHICLE_INVOLVED':range(len(boroughs)),
                              'MORE_VEHICLE_INVOLVED':range(len(boroughs))
                             })
data_required.index = boroughs
cols  = data_required.columns.values.tolist()
cols.remove('BOROUGH')
MORE_VEHICLE_INVOLVED_count = {}
ONE_VEHICLE_INVOLVED_count = {}
TWO_VEHICLE_INVOLVED_count = {}
THREE_VEHICLE_INVOLVED_count = {}
for borough in boroughs:
    for col in cols:
        if col == "MORE_VEHICLE_INVOLVED":
            data_borough = data_gt_2015[data['BOROUGH']==borough]
            MORE_VEHICLE_INVOLVED_count.update({borough:len( [i for i,j in
                    zip(pd.isnull(data_borough['VEHICLE 4 TYPE']),pd.isnull(data_borough['VEHICLE 4 TYPE']))
                   if i or j
                   ])})
        elif col == "ONE_VEHICLE_INVOLVED":
            data_borough = data_gt_2015[data['BOROUGH']==borough]
            ONE_VEHICLE_INVOLVED_count.update({borough:len( [i for i in
                    pd.isnull(data_borough['VEHICLE 1 TYPE']) if i
                   ])})
        elif col == "TWO_VEHICLE_INVOLVED":
            data_borough = data_gt_2015[data['BOROUGH']==borough]
            TWO_VEHICLE_INVOLVED_count.update({borough:len( [i for i in
                    pd.isnull(data_borough['VEHICLE 2 TYPE']) if i
                   ])})
        elif col == "THREE_VEHICLE_INVOLVED":
            data_borough = data_gt_2015[data['BOROUGH']==borough]
            THREE_VEHICLE_INVOLVED_count.update({borough:len( [i for i in
                    pd.isnull(data_borough['VEHICLE 3 TYPE']) if i
                   ])})
data_required = pd.DataFrame({'ONE_VEHICLE_INVOLVED':ONE_VEHICLE_INVOLVED_count,
                             'TWO_VEHICLE_INVOLVED':TWO_VEHICLE_INVOLVED_count,
                              'THREE_VEHICLE_INVOLVED':THREE_VEHICLE_INVOLVED_count,
                              'MORE_VEHICLE_INVOLVED':MORE_VEHICLE_INVOLVED_count
                             })
data_required.to_csv("Q1_PARTTWO.csv")