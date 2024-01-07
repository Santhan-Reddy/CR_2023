import numpy as np

num = np.random.randint(100)

print(num)

# import random as ran
# num1 = ran.randint(1, 300)
# print(num1)

num1 = np.random.randint(50, 100, size=(2,3,4))
print(num1)

num2 = np.random.choice([11,22,44,55,66,77,88], size = (2, 3, 5))
print(num2)