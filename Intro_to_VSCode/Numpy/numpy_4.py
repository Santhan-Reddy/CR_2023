#Mathematical operations in numpy

import numpy as np

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

a1 = np.array(l1)
a2 = np.array(l2)

# in list
print(l1 * 5) # list multiplied by 5 - print the vales of list 5 times

print(a1 * 5) # numpy array mutlipled by 5 - print the valies of array multiplied by 5

print( l1 + l2) # contactinates the list

print( a1 + a2) # adds the vales of the array and prints the array

#boradcasting

n1 = np.array([1, 2, 3])
n2 = np.array([[1],
              [2]])

print( n1 * n2)


print(np.sqrt(n2))
