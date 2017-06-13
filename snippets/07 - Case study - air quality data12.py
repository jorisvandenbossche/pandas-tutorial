# we use stack to reshape the data to move the hours (the column labels) into a column.
# But we don't want to move the 'date' column label, therefore we first set this as the index.
# You can check the difference with "data.stack()"
data2 = data.set_index('date')
data_stacked = data2.stack()
data_stacked.head()