import numpy as np
import csv

n = 1000

u = np.random.uniform(0,2*np.pi,n)
v = np.random.uniform(0,2*np.pi,n)

a = 1
b = 1

results = []
for i in range(0,n):
    x = (a+b*np.cos(v[i]))*np.cos(u[i])
    y = (a+b*np.cos(v[i]))*np.sin(u[i])
    z = b*np.sin(v[i])

    results.append([x,y,z])


with open('clean_results.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in results:
        spamwriter.writerow(row)

u = np.random.uniform(0,2*np.pi,n) + np.random.normal(0,1)
v = np.random.uniform(0,2*np.pi,n) + np.random.normal(0,1)

results = []
for i in range(0,n):
    x = (a+b*np.cos(v[i]))*np.cos(u[i])
    y = (a+b*np.cos(v[i]))*np.sin(u[i])
    z = b*np.sin(v[i])

    results.append([x,y,z])

with open('noisy_results.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in results:
        spamwriter.writerow(row)