hamlet = titles[titles['title'] == 'Hamlet']
hamlet.groupby(hamlet.year // 10 * 10).size().plot(kind='bar')