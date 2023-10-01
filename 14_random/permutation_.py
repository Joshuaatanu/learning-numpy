from numpy import random
import numpy as np


#randomly shuffles the array
# arr = np.array([1, 2, 3, 4, 5])

# random.shuffle(arr)

# print(arr)
#  generating permutations of arrays

# this leaves the original array unchanged
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))