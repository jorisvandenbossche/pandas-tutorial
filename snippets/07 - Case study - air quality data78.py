data_weekend = data.groupby(['weekend', data.index.hour]).mean()
data_weekend.head()