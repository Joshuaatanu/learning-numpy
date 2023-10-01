from numpy import random

# x = random.randint(100) # generates arandom number between 1 and 100

# x =random.rand() # generates arandom number between 0 and 1
# print(x)

# generating a random array

# In NumPy we work with arrays, and you can use the two methods
# from the above examples to make random arrays.
# # Integers
# The randint() method takes a size parameter where you can specify the shape of an array.


# x =  random.randint(100 , size=(5)) this generates a 1-D array
# x = random.randint(100, size =(3,5)) this generates a 2-D array

# the rand() method allows you to specify the shape of the array

# x = random.rand(5,3,3)
# print(x)

#  generate a random number from an array

x = random.choice([3, 5, 7, 9] , size=(5,3,3)) #we can specify the size of the array
print(x)