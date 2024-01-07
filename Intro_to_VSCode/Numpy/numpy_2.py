import numpy as np

a = np.array([[1,2,3,],
              [4,"Hello", 6],
              [7,8,9]])
print(a)
print(a.shape)
print(a.size)
print(a.diagonal())
print(a.dtype)
print(a[0,0].dtype) 

a = np.array([[1,2,3,],
              [4,"5", 6],
              [7,8,9]], dtype = np.float32)
print(a)

print()
a= np.full((2,3), 7)
y = np.ones((2,3))
y = np.zeros((2,3,4), dtype= np.float32)
             
print(a)
print(y)
y[1][1][1] = 9
print(y[1][1][1])
print(y)

z = np.empty((3,4))
print(z)

