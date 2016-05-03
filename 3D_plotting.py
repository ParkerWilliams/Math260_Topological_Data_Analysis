import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = np.load('1_torus.npy')
xs = []
ys = []
zs = []
for i in range(0,len(data)):
    xs.append(list(data[i])[0])
    ys.append(list(data[i])[1])
    zs.append(list(data[i])[2])
ax.scatter(xs, ys, zs, c='c')
plt.show()