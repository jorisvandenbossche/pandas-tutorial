c = cast
c = c[c.year // 10 == 200]
c = c[c.n == 1]
c.type.value_counts()