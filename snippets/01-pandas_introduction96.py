no2.resample('A').mean().plot()
no2.mean(axis=1).resample('A').mean().plot(color='k', linestyle='--', linewidth=4)