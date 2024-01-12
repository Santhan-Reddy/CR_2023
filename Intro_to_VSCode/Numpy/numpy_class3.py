import numpy as np

arr = np.random.randn(10)
print(arr)

# arr.sort()

arr1 = np.sort(arr)
print(arr1)


s1 = np.array(['desk', 'chair', 'bulb'])
s2 = np.array(['lamp', 'chair', 'bulb'])

print(np.intersect1d(s1, s2)) # comman values in s1 and s2

print(np.setdiff1d(s1, s2)) # item that is in s1 bit not in s2

print(np.union1d(s1, s2)) # combine and give unique array

print(np.in1d(s1, s2)) # bollean out put if teh item in s1 is present in s2 than true else false

# broadcasting

start = np.zeros((4,3))
print(start)

add_rows = np.array([1, 2, 3])
print(add_rows)

y = start + add_rows
print(y)




x = np.array([23.23, 24.44])
np.save('an_arr', x)
np.load('an_arr.npy')

add1_rows = np.array([[1, 2, 3]])
add_col = add1_rows.T
print(add_col)

np.savetxt('n_arr.txt', X=x, delimiter=',')
np.loadtxt('n_arr.txt', delimiter=',')
