import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline


def logistic(r, x):
    return r * x * (1 - x)


x = np.linspace(0, 4)
# print(x)
for i in x:
    print(logistic(0.6, i))
# fig, ax = plt.subplots(1, 1)
# ax.plot(x, logistic(2, x), 'k')
