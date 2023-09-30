# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through each element one by one.

import numpy as np

# arr =np.array([1,2,3])

# for x in arr: 
#     print(x)


#  iterating a 2-D array
# arr =np.array([[1,2,3,4],[5,6,7,8]])
# for x in arr :
#     print(x)
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,2,3)
# print(newarr)
# print(newarr.ndim)
# for x in newarr :
#     print(x.ndim)

# print(newarr)

# iterating a 3-D array

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for x in arr :
#     print("X presents the 2-d Array: ")
#     print(x)

#  iterating down to scalars
for x in arr :
    for y in x:
     for z in y:
        print(z)