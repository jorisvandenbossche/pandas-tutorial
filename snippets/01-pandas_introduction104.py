data_weekend = no2.groupby(['weekend', no2.index.hour]).mean()
data_weekend.head()