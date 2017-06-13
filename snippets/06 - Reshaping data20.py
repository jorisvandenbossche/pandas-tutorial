df.pivot_table(index='Pclass', columns='Sex', 
               values='Survived', aggfunc='mean')