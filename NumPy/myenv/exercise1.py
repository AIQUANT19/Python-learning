# Create a NumPy array from 0 to 9.
# Replace all even numbers with -1 and print the result.

import numpy as np

x = np.arange(0,10,1)
for i in range(0, len(x)):
    if x[i] % 2 == 0:
        x[i] = -1
print(x)


# Create and print a 3x3 identity matrix using NumPy.
# An identity matrix has 1s on the diagonal and 0s elsewhere.

y = np.zeros([3,3])
for i in range(0,3):
    for j in range(0,3):
        if i == j:
            y[i][j] = 1
print(y)

z = np.eye(3)
print(f"The another identity element is\n {z}")