import numpy as np

n = 100

u = np.random.uniform(0,2*np.pi,n)
v = np.random.uniform(0,2*np.pi,n)

a = 4
b = .25

results = []
for i in range(0,n):
    x = (a+b*np.cos(v[i]))*np.cos(u[i])
    y = (a+b*np.cos(v[i]))*np.sin(u[i])
    z = b*np.sin(v[i])

    results.append([x,y,z])

np.save('1_torus.npy',results)
