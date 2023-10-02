# # Zipf's Law: In a collection the nth common term is 1/n times of the most
#  common term. E.g. 5th common word in english has occurs nearly 1/5th
# times as of the most used word.

# It has two parameters:
# a - distribution parameter.
# size - The shape of the returned array.


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)

sns.distplot(x[x < 10], kde=False)
plt.show()

print(x)
