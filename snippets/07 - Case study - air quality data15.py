# Drop the origal date and hour columns
data_stacked = data_stacked.drop(['date', 'level_1'], axis=1)
data_stacked.head()