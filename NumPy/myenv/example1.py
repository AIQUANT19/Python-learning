# NumPy (Numerical Python) is a Python library used for:

# 1) Working with large arrays and matrices.

# 2) Performing mathematical operations efficiently.

# It's a core library for data science and machine learning.



import numpy as np

# Create a 1D array
a = np.array([1, 2, 3])
print("1D Array:", a)

# Create a 2D array
b = np.array([[1, 2], [3, 4]])
print("2D Array:\n", b)

# Array with all zeros
# 2 elements with 3 zeros
z = np.zeros((2, 3))
print("Zeros:\n", z)

# Array with all ones
# with 3 elements with 2 ones 
o = np.ones((3, 2))
print("Ones:\n", o)

# Array with a range of numbers
# From 0 to 10 with 2 value gap (Integer)
r = np.arange(0, 10, 2)
print("Range array:", r)

# Linearly spaced numbers
# From 0 to 1 with 4 values
l = np.linspace(0, 1, 4)
print("Linspace:", l)


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Addition:", x + y)
print("Multiplication:", x * y)
print("Dot Product:", np.dot(x, y))

print("Sum:", np.sum(x))
print("Mean:", np.mean(x))
print("Max:", np.max(x))
print("Reshape:\n", np.reshape(x, (3, 1)))



x = np.arange(5,16,1)
print(x)

y = np.ones((2,4))
print(y)