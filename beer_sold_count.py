__author__ = 'ygong10'

import csv, pandas as pd, array
#with open('mercury.csv','rb') as csvfile:
df = pd.read_csv('volumec.csv')
saved_volume = df.volume
saved_time = df.time

print saved_volume
print saved_time
oz_to_liter = 0.354882
volume1 = []
volume_count = saved_volume.sum(axis=0)
glass_count = volume_count/oz_to_liter
print volume_count
print str(glass_count) + " Liters"



# glass_count  = 0
# for i in range(len(saved_volume)):
#     volume_count += saved_volume.index(i)
#
# print volume_count

