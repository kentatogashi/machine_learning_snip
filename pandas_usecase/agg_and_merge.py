import io
import requests as r
import pandas as pd

print('get test data')
url = 'https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv'
res = r.get(url).content
df = pd.read_csv(io.StringIO(res.decode('UTF-8')))
print('compute mean cnt by state')
agg_df = df.groupby('state').agg(dict(cnt=['mean', 'sum']))
agg_df.reset_index(inplace=True)
agg_df.columns = ['state', 'cnt_mean', 'cnt_sum']
print('append mean cnt to original data.')
result = pd.merge(df, agg_df)
print(result.to_csv())
