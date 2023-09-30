import numpy as np

# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.

# arr = np.array([1,2,3,4,5,4,4])

# x = np.where(arr == 4)

# print(x)
# print(arr[3])
# print(arr[5])
# print(arr[6])

#  in the ext example we are trying to find the indexes of the  values tha t are even

# arr  =np.array([1,2,3,4,5,6,7,8])
# x = np.where(arr%2 ==0)

# print(x)

#  in the next example we are trying to find the value of the indexes that are odd

# arr =  np.array([1,2,3,4,5,6,7,8])

# x = np.where(arr%2 ==1)
# print(x)

#  using the searchsorted()  method


# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 6) # show the index of the value input
# x = np.searchsorted(arr, 7, side='left') # Find the indexes where the value 7 should be inserted, starting from the right:

# print(x)


#  multiple values 

arr= np.array([1,3,5,7])
x = np.searchsorted(arr,[2,4,6])
print(x)
