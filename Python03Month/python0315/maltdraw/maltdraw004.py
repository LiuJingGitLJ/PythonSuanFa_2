import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
import numpy  as np
fig = plt.figure()
ax = Axes3D(fig)
rv = stats.multivariate_normal([0, 0], cov=1)

x, y = np.mgrid[-2:1:.11, -2:1:.11]
ax.plot_surface(x, y, rv.pdf(np.dstack((x, y))), rstride=1, cstride=1)
ax.set_zlim(0, 0.2)

# savefig('../figures/plot3d_ex.png',dpi=48)
plt.show()