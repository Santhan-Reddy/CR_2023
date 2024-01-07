import numpy as np

an_array = np.array([[11,12,13],[21,22,23],[31,32,33],[41,42,43]])
print(an_array)


col_indices = np.array([0, 1, 2, 0])
row_indices = np.arange(4)

print(col_indices)
print(row_indices)


for i, j in zip(row_indices, col_indices):
    print(i, ' ', j)


print('values in the array at those indices: ', an_array[row_indices, col_indices])


an_array[row_indices, col_indices] = 10000

print("\n changed array")
print(an_array)



