# import numpy as np

# accessing a 1-d array

# arr = np.array([1,2,3,4])

# print(arr[2] + arr[3])

# accesing a 2-D array

# import numpy as np

# arr =np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print("print the second element on the 1st dimension :",arr[1,4])


# accesing a 3-D array

# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[1,0,2])

# negative indexing
 
import numpy as np

arr = np.array([[1,2,3,4,5,],[6,7,8,9,10,]])
print('last element from the 2nd dim :' ,arr[1,-1])