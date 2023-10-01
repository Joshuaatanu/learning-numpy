from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=1, scale=2,size=1000), hist=False)

#  The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curv
plt.show()