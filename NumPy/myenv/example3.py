# Topic: NumPy Broadcasting

# What is Broadcasting?
# Broadcasting lets NumPy perform arithmetic operations on arrays of different shapes without writing loops.

# It automatically expands smaller arrays so that arithmetic operations work.

import numpy as np

# a = np.array([1,2,3])
# b = a + 5
# print(b)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b = np.array([10, 20, 30]) 
# result = a + b
# print(result)


# a1 = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b1 = np.array([[10],
#               [20]])  # shape (2, 1)
# result1 = a1 + b1
# print(result1)

# Create an array of numbers from 0 to 4. Add 10 to each element using broadcasting.
# a = np.arange(0,5)
# b = a + 10
# print(b)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# b = [10, 20, 30]
# print(a+b)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# b = [[100],[200]]

# print(a+b)