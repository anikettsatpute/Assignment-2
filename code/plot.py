#CS21BTECH11056

import matplotlib.pyplot as plt

import numpy as np
x = np.linspace(0,10,100)
y = 2.25*x - 5.5

y1 = 0*x + 14

plt.plot( x, y, label = "line 1")
plt.plot( x, y1, label = "line 2")


plt.legend()
plt.show()
