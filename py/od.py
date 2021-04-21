import csv

import pandas as pd

tmp_lst = []
with open('OD.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tmp_lst.append(row)
df = pd.DataFrame(tmp_lst[1:], columns=tmp_lst[0])

OD_RESULT = df.groupby(['OTime', 'DName']).count()['userID'].reset_index()
OD_RESULT.columns = ['Source', 'Target', 'weight']
OD_RESULT = OD_RESULT[OD_RESULT['weight'] > 0].reset_index(drop=True)
OD_RESULT = OD_RESULT.sort_values(by='weight').reset_index(drop=True)
OD_RESULT.to_csv('Sta1_6.1.csv')
