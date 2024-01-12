import numpy as np


x2d = np.array([[2,3],[4,5]])
y2d = np.array([[2,3], [4,5]])

print(x2d)
print(y2d)

print(x2d.dot(y2d))



a1d = np.array([9, 9])
b1d = np.array([10, 10])

print(np.dot(a1d, b1d))


x1 = np.random.randn(8)
print(x1)
y1 = np.random.randn(8)
print(y1)

print(np.maximum(x1, y1))
print(np.max(x1))


arr = np.arange(30)
print(arr)

print(arr.reshape(6, 5))


x_1 = np.array([1,2,3,4,5])
x_2 = np.array([11,22,33,44,55])

filter = np.array([True, True, 0, 0, 0])

out = np.where(filter, x_1, x_2)
print(out)

x11 = np.random.rand(5, 5)
print(x11)

print(np.where(x11 > 0.5, 100, 10))