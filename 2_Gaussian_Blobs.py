import numpy as np

n = 100

results = []
for i in range(0,n):
    x = np.random.normal(0,1)
    y = np.random.normal(0,1)
    z = np.random.normal(0,1)

    results.append([x, y, z])

for i in range(0, n):
    x = 5 + np.random.normal(0, 1)
    y = 5 + np.random.normal(0, 1)
    z = 5 + np.random.normal(0, 1)

    results.append([x, y, z])

np.save('2_Gaussian_blobs_very_far_apart.npy',results)