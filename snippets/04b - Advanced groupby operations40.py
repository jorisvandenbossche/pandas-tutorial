c = cast
c[c.title.str.startswith('The Life')].title.value_counts().head(10)