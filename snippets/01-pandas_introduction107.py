no2['hour'] = no2.index.hour
no2.pivot_table(columns='weekend', index='hour', values='BASCH')