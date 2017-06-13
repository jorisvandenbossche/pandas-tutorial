sel = cast[(cast.character == 'Superman') | (cast.character == 'Batman')]
sel = sel.groupby(['year', 'character']).size()
sel = sel.unstack()
sel = sel.fillna(0)
sel.head()