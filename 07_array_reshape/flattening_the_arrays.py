import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
newarr = arr.reshape(-1)
print(newarr)