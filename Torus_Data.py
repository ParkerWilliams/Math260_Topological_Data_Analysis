import numpy as np

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

np.save('clean_results.csv',results)

u = np.random.uniform(0,2*np.pi,n) + np.random.normal(0,1)
v = np.random.uniform(0,2*np.pi,n) + np.random.normal(0,1)

results = []
for i in range(0,n):
    x = (a+b*np.cos(v[i]))*np.cos(u[i])
    y = (a+b*np.cos(v[i]))*np.sin(u[i])
    z = b*np.sin(v[i])

    results.append([x,y,z])

np.save('noisy_results.csv',results)