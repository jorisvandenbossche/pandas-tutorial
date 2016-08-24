hamlets = titles[titles['title'].str.match('Hamlet')]
hamlets['title'].value_counts()