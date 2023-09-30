import numpy as np

# join a 1-D array

# arr1 = np.array([1,2,3,])
# arr2 =np.array([4,5 ,6])

# arr= np.concatenate((arr1, arr2))
# print(arr)


#  joining a 2-D array

# arr1 =np.array([[1,2],[3,4]])
# arr2 =np.array([[5,6],[7,8]])

# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr.ndim)


# join arrays using stack functions

# arr1 = np.array([1,2,3,])
# arr2 =np.array([4,5 ,6])
# arr = np.stack((arr1,arr2), axis=1)
# print(arr)

# stacking along the rows


arr1 = np.array([1,2,3,])
arr2 =np.array([4,5 ,6])

# arr = np.hstack((arr1, arr2))


# stacking along the columns
# arr = np.vstack((arr1, arr2))

# stacking along the height (depth)

arr = np.dstack((arr1, arr2))



print(arr)