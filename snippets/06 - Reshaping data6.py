colnames = ['date'] + [item for pair in zip(hours, ['flag']*24) for item in pair]

data = pd.read_csv("data/BETR8010000800100hour.1-1-1990.31-12-2012",
                   sep='\t', header=None, na_values=[-999, -9999], names=colnames)