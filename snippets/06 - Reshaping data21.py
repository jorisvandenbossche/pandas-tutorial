fig, ax1 = plt.subplots()
df.pivot_table(index='Pclass', columns='Sex', 
               values='Survived', aggfunc='mean').plot(kind='bar', 
                                                       rot=0, 
                                                       ax=ax1)
ax1.set_ylabel('Survival ratio')