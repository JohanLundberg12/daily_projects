import random

import matplotlib.pyplot as plt
import numpy as np

# x from -10 to 10
x = np.linspace(-10, 10, 10000000)

# generate y as a random walk

y = [0]
for i in range(1, len(x)):
    y.append(y[i - 1] + random.uniform(-1, 1))


ax = plt.axes()
ax.plot(x, y)

axin = ax.inset_axes([0.5, 0.5, 0.3, 0.3])
axin.plot(x, y)
axin.set_xlim(-1, 1)

ax.indicate_inset_zoom(axin)
plt.show()
