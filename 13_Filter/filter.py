import numpy as np

# arr = np.array([41,42,43,44])

# x = [True, False, True, False]
# newarr= arr[x]
# print(newarr)


#  creating a filter array

# arr = np.array([41,42,43,44])
# #   create an emtpty list
# filter_arr =[]

# #  go through each element in the arr
# for element in arr:
#     #  if the element is higher than 42 , set the value to true, else set the value to false
#     if element > 42 :
#         filter_arr.append(True)
#     else :
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(newarr)


# creating a filter array that displays only even numbers

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# filter_arr =[]
# for element in arr :
#     if element %2 ==0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

#  creating a filter directly from an array


# arr = np.array([41,42,43,44])

# filter_arr = arr> 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6,7])
filter_arr = arr % 2 == 1
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
