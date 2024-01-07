import numpy as np

# an_array = np.array([[11,12],[21,22],[31,32]])
# print(an_array)

# filter = (an_array > 15)
# print(filter)

# print(an_array[filter])

# print('\n', an_array[an_array > 15])


x = np.array([[111, 112],[121, 122]], dtype=np.int32)
y = np.array([[211, 212],[221, 222]], dtype=np.float64)

print(x, '\n')
print(y)

print( x + y)
print(np.add(x, y))

print()
print( x * y)
print(np.multiply(x, 10))

# arr1 = 10 * np.random.randn(2, 5)
arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr1)

print(arr1.mean())
print(np.median(arr1, axis=0))
print(np.median(arr1, axis=1))