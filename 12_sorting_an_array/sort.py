# Sorting means putting elements in an ordered sequence.
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np 

# arr  = np.array([3,2,0,1])
# arr = np.array(['banana', 'cherry', 'apple'])
# arr = np.array([True, False, True])
# print(np.sort(arr))

#  sorting a 2-D array

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))