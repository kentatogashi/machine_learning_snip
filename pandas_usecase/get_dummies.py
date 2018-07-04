import io
import requests as r
import pandas as pd

url = 'https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv'
res = r.get(url).content
df = pd.read_csv(io.StringIO(res.decode('UTF-8')))
dummies = pd.get_dummies(df['city'])
print(dummies.to_csv())
"""
Output
,Belmont,Menlo Park,Redwood City,San Francisco,San Mateo,South San Francisco,Sunnyvale
0,0,0,1,0,0,0,0
1,0,0,0,0,1,0,0
2,0,0,0,0,1,0,0
3,0,0,0,0,1,0,0
4,0,0,0,0,1,0,0
5,0,1,0,0,0,0,0
6,0,1,0,0,0,0,0
7,0,1,0,0,0,0,0
8,0,0,1,0,0,0,0
9,0,0,1,0,0,0,0
10,0,0,1,0,0,0,0
11,0,0,1,0,0,0,0
12,0,0,1,0,0,0,0
13,0,0,1,0,0,0,0
14,0,0,0,1,0,0,0
15,0,0,0,0,0,0,1
16,0,0,0,0,0,1,0
17,0,0,1,0,0,0,0
18,0,0,0,0,1,0,0
19,1,0,0,0,0,0,0
20,0,0,0,1,0,0,0
"""
