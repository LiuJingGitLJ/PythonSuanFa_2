import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x = np.arange(0, 200)
y = np.arange(0, 100)
x, y = np.meshgrid(x, y)
z = np.random.randint(0, 200, size=(100, 200))%3
print(z.shape)

# ax.scatter(x, y, z, c='r', marker='.', s=50, label='')
ax.plot_surface(x, y, z,label='')
plt.show()