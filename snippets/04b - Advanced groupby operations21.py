cast['n_total'] = cast.groupby('title')['n'].transform('max')
cast.head()