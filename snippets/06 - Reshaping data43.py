# alternative: rename columns at the end
temp = pivoted.set_index('Sex').stack().reset_index()
temp.rename(columns={'level_1': 'Pclass', 0: 'Fare'})