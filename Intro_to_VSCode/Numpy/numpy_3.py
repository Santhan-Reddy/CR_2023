import numpy as np


x_values = np.arange(0, 1005, 5)
print(x_values)

y_values = np.linspace(0, 1000, 1001)
print(y_values)


print(np.nan)
print(np.inf)


print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.array([10]) / 0))

print(np.sqrt(-1))
print(np.array([10]) / 0)

arr_eye = np.eye(6,6)
print(arr_eye)