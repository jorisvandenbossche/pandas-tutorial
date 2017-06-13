fig, ax = plt.subplots()
data.loc['2011':'2012', 'L06_347'].resample('M').mean().plot(ax=ax)
data.loc['2011':'2012', 'L06_347'].resample('M').median().plot(ax=ax)
ax.legend(["mean", "median"])