hamlets = titles[titles['title'].str.contains('Hamlet')]
hamlets['title'].value_counts()