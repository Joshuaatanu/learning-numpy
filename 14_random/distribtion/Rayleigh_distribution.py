# Rayleigh distribution is used in signal processing.
# It has two parameters:
# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.


from numpy import random
# x = random.rayleigh(scale=2, size=(2, 3))


# print(x)


# Visualization of Rayleigh Distribution


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()