from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True,kde=False )

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()