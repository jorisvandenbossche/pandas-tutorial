cast1950 = cast[cast.year // 10 == 195]
cast1950 = cast1950[cast1950.n == 1]
cast1950.groupby(['year', 'type']).size()