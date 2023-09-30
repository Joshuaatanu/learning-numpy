import numpy as np
# split is the reverse of joins
# arr = np.array([1,2,3,4,5,6])

# newarr = np.array_split(arr,2)
# print(newarr)


#  the difference between split() and array_split() is that the array_split() will automatically adjust the elements of the array to fit your input while split won't

# split into arrays

# arr = np.array([1,2,3,4,5,6])

# newarr = np.array_split(arr,3)
# print(newarr)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# splittinf a 2-D array

# arr  = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(6,2)
# myarr =np.array_split( newarr,3)
# print(myarr)


# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
# myarr = arr.reshape(6,3)
# newarr = np.array_split(myarr,3, axis=1)
# print(newarr)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
myarr = arr.reshape(6,3)
newarr = np.dsplit(myarr,3)
print(newarr)