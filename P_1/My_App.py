# imports
import matplotlib.pyplot as plt
import numpy as np
import json


time_values = list()
distance_values = list()
with open("DATA_MyApp.json", "r") as rf:
    data = json.load(rf)
    for km, time in data["distanceRecoreds_1km_time"].items():
        time_new = time[1].split(':')
        time_values.append(int(time_new[0]) + int(time_new[1]) / 60)
        distance_values.append(km)

y_pos = np.arange(len(time_values))
plt.bar(y_pos, time_values)
plt.xticks(y_pos, distance_values)
plt.show()
