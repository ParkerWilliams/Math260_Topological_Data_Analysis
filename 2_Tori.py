import numpy as np

n = 50

u = np.random.uniform(0,2*np.pi,n)
v = np.random.uniform(0,2*np.pi,n)

a = 4
b = 1

results = []
for i in range(0,n):
    x = (a+b*np.cos(v[i]))*np.cos(u[i])
    y = (a+b*np.cos(v[i]))*np.sin(u[i])
    z = b*np.sin(v[i])

    results.append([x,y,z])


for i in range(0,n):
    x = 5+(a+b*np.cos(v[i]))*np.cos(u[i])
    y = 5+(a+b*np.cos(v[i]))*np.sin(u[i])
    z = 5+b*np.sin(v[i])

    results.append([x,y,z])

np.save('2_tori.npy',results)

