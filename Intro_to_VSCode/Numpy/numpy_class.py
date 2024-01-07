import numpy as np

an_array = np.array([[11, 12, 13, 14],[21, 22,23, 24],[31, 32, 33, 34]])

print(an_array)


print(an_array.shape)
print(an_array.size)

row_rank1 = an_array[1, :]
print(row_rank1)

row_rank2 = an_array[1:2, :]
print(row_rank2)


col_rank1 = an_array[:, 1]
print(col_rank1)

col_rank2 = an_array[:, 1:2]
print(col_rank2)
print(col_rank1.shape)
print(col_rank1.size)
print(col_rank2.shape)
print(col_rank2.size)




