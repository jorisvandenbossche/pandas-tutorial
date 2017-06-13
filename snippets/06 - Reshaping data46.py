grouped = cast.groupby(['year', 'type']).size()
table = grouped.unstack('type')
table.plot()