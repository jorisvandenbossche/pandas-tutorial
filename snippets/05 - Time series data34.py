data.resample('A').mean().plot()
data.mean(axis=1).resample('A').mean().plot(color='k', linestyle='--', linewidth=4)