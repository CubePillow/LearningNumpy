import numpy as np

np1 = np.array([0,1,2,3,-4,5,6,7,8,9])
print("original: ", np1)

#universial functions
#square root of each element
print("square root: ", np.sqrt(np1))
#Absolute value
print("absolute value: ", np.absolute(np1))
#Exponents
print("exponents: ", np.exp(np1))
#Min/Max
print("Min: ", np.min(np1))
#Sign positive or negative
print("Sign: ", np.sign(np1))
#Trig sin cos log
print("sin: ", np.sin(np1))

#Copy vs View
#View: still connected to original
np2 = np1.view()
print(f'Original NP1: {np1}')
print(f'Original NP2: {np2}')
np1[0] = 41
print(f'Changed NP1: {np1}')
print(f'Original NP2: {np2}') # np2 also be changed, as long as we change the original, the copy also be changed
np2[3] = 31
print(f'Original NP1: {np1}') #change view, original array also be changed
print(f'Changed NP2: {np2}')

print("--------------------")

#Copy: copy is completely different array
np3 =np1.copy()
print(f'Original NP1: {np1}')
print(f'Original NP3: {np3}')
np1[0] = 34
print(f'Changed NP1: {np1}')
print(f'Original NP3: {np3}')
np3[1] = 22
print(f'Original NP1: {np1}')
print(f'Changed NP3: {np3}')

