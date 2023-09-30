import numpy as np 

#iterating each scalar element

# arr = np.array([1,2,3,4,5,6,7,8])

# newarr = arr.reshape(2,2,2)

# for x in np.nditer(newarr):
#     print(x)

#  iterating arraay with differnte data types

# arr = np.array([1,2,3])
# for x in np.nditer(arr, flags =['buffered'], op_dtypes=['S']):
#     print(x)    

# iterating with a different step size

# arr = np.array([1,2,3,4,5,6,7,8])
# newarr = arr.reshape(2,4)
# for x in np.nditer(newarr[:,::2]):
#     print(x)

# enumerated iteration using ndenumarate()

# arr = np.array([1,2,3])
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

for idx , x in np.ndenumerate(arr):
    print(idx,x)
