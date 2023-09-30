
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr =arr.reshape(4,3)

# reshape from 1-D to 3-D
newarr =arr.reshape(2,3,2)
# this is the out put which means  we want each dimension to have 2arrays that contain 3 arrays with 2 elements


# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

print(newarr)