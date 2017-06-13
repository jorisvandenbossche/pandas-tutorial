data.loc['2009':, 'FR04037'].resample('M').mean().plot()
data.loc['2009':, 'FR04037'].resample('M').median().plot()