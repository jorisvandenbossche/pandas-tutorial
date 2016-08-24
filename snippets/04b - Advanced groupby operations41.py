c = cast
c = c[c.year // 10 == 195]
c = c[c.n == 1]
c.type.value_counts()