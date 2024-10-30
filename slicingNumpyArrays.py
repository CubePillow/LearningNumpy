import numpy as np

# Slicing Numpy Arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

#returm 2,3,4,5
print(np1[1:5]) #not including 5. element

#return from something till the end of array
print(np1[2:])

#return negative Slices
print(np1[-3:-1]) #7,8

#Steps
print(np1[1:5:2]) #2,4 2-5 with steps 2
#Steps on the entire array
print(np1[::2])

#Slice a 2-d array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#pull out a single item
print(np2[1,3]) #9
#slice a 2d array
print(np2[0:1,1:3]) # [[2,3]]
print(np2[0:2,1:3]) # [[2,3],[7,8]]