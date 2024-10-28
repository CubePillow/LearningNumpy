import numpy as np
print(np.__version__)

#List vs Numpy
list1 = [1,2,3,4,5]
print(list1)

#list can contain different type of dates => for massive amounts of data, slow
list2 = ["John Elder", 41, list, True]

#Numpy - Numeric Python
# ndarray => same data type for array
np1 = np.array([0,1,2,3,4,5])
print(np1)

#Functions
#len()
print(np1.shape)

#create a array
#Range
np2 = np.arange(6)
print(np2)
#Step
np3 = np.arange(0,10,2)
print(np3)
#Zeros
np4= np.zeros(5)
print(np4)
#Multidimensional zeros
np5 = np.zeros((3,3))
print(np5)
#Full
np6 = np.full(3, 10)
print(np6)
#Multidimentional Full
np7 = np.full((3,3), 10)
print(np7)
#Convert python list to numpy
my_list = [1,2,3,4,5,6,7,8,9]
np8 = np.array(my_list)
print(np8)