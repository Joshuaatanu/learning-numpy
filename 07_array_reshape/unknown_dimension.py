import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

newarr = arr.reshape(2,5,-1)
# Convert 1D array with 8 elements to 3D array with 2x2 elements:
print(newarr.ndim)