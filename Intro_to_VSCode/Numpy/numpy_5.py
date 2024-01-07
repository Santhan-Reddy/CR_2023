# Array functions 

import numpy as np


a1 = np.array([1,2,3])

#add items to the array

a1 = np.append(a1, [7, 8, 9])

print(a1)

a1 = np.insert(a1, 3, [4, 5, 6])
print(a1)


a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.insert(a, 2, [7, 8, 9], 0))
print(np.insert(a, 3, values=[7, 8], axis=1))
print(np.insert(arr= a, obj= 3, values=[9, 10], axis=1))


# delete items
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.delete(a, 1, 1)) # column deletion as axis is 1
print(np.delete(a, 1, 0))
