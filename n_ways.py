import csv
import matplotlib.pyplot as plt
import numpy as np
from intersection import crashes_at_n_way_intersection
ns = []
rates = []
with open('intersections.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['num_ways,crashes,total_scenarios,hit_rate']) #header
    for n in range(2,200):
        ns.append(n)
        (num_hits,total_scenarios) = crashes_at_n_way_intersection(n)
        writer.writerow([n, num_hits, total_scenarios, num_hits/total_scenarios])
        rates.append(num_hits/total_scenarios)

plt.plot(ns,rates)
plt.xlabel("number of ways at stop sign")
plt.ylabel("crash rate")
plt.title("Crash rate vs. N")
plt.show() #makes it actually appear on screen