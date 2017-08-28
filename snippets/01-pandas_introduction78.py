df25 = df[df['Age'] <= 25]
df25['Survived'].sum() / len(df25['Survived'])