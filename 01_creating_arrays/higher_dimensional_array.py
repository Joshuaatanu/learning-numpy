import numpy  as np
# you can define the numberof dimensions of an array by using th endim argument 
arr  = np.array([1, 2, 3, 4] ,ndmin=5)

print(arr)
print('number of dimensions', arr.ndim)
# In this array the innermost dimension (5th dim) has 4 elements, 
# the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, 
# the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array