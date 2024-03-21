import random

import matplotlib.pyplot as plt
import numpy as np

# x from -10 to 10
x = np.linspace(-10, 10, 100)

# generate y as a random walk

y = [0]
for i in range(1, len(x)):
    y.append(y[i - 1] + random.uniform(-1, 1))


ax = plt.axes()
ax.plot(x, y)

# (x, y) =  position of the zoomed plot
# width, height = width and height of the zoomed plot as percentage of the original plot
axin = ax.inset_axes([0.8, 0.1, 0.3, 0.3])
axin.plot(x, y)

# no y_lim, as we want to ensure the line is visible
axin.set_xlim(-1, 1)  # focus on the region between -1 and 1 on x-axis

ax.indicate_inset_zoom(axin)
plt.show()
