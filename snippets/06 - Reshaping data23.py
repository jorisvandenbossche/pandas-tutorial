df.pivot_table(index='Underaged', columns='Sex', 
               values='Fare', aggfunc='mean')