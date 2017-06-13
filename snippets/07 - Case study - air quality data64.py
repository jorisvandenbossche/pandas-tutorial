df2011 = data['2011'].dropna()
df2011.groupby(df2011.index.week)[['BETN029', 'BETR801']].quantile(0.95).plot()