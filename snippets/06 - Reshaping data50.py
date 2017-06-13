grouped = cast.groupby(['year', 'type']).size()
table = grouped.unstack('type')
(table['actor'] / (table['actor'] + table['actress'])).plot(ylim=[0,1])