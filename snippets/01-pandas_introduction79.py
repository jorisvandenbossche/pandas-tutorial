# df.groupby('Sex')[['Survived']].aggregate(lambda x: x.sum() / len(x))
df.groupby('Sex')[['Survived']].mean()