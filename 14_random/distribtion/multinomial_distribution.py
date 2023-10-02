# Multinomial Distribution
# Multinomial distribution is a generalization of binomial distribution.
# It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two.
#  e.g. Blood type of a population, dice roll outcome.
# It has three parameters:
# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilities of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.


from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)
