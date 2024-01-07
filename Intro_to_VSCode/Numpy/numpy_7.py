# joining and plitting array

import numpy as np

a1 = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

a2 = np.array([[11,12,13,14,15],
              [16,17,18,19,20]])


a = np.concatenate((a1, a2), axis=0)
print(a)

a = np.concatenate((a1, a2), axis=1)
print(a)

a = np.stack((a1, a2))
print(a)

# split

a = np.array([[1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [13,14,15,16,17,18],
              [19,20,21,22,23,24]])


print(np.split(a, 2, axis= 0))
print(np.split(a, 2, axis= 1))

print(a.min())
print(a.max())
print(a.mean())
print(a.std())
print(np.median(a))






