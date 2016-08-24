# add a weekday and week column
data['weekday'] = data.index.weekday
data['week'] = data.index.week
data.head()