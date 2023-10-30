import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
# Data for plotting

fig, ax = plt.subplots()
x = []
y = []
for t in range(0, 200):
    x.append(t)
    start = time.time()
    for i in range(0, t):
        for j in range(0, t):
            print(t)
    y.append(time.time() - start)
ax.plot(x, y)


# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
ax.grid()

# fig.savefig("test.png")
plt.show()