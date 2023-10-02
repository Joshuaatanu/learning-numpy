# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
# It has two parameter:
# a - shape parameter.
# size - The shape of the returned array.

from numpy import random

# x = random.pareto(a=2, size=(2, 3))

# print(x)


# Visualization of Pareto Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()