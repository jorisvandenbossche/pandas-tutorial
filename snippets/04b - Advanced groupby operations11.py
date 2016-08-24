cast1990 = cast[cast['year'] >= 1990]
cast1990 = cast1990[cast1990.n == 1]
cast1990.groupby('name').size().nlargest(10)