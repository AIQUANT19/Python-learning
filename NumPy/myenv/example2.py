# Indexing and Slicing in NumPy

import numpy as np

a = np.array([1,2,3,4,5])

print(a[0])
print(a[-1])

print(a[0:2])

# This is different
print(a[::2])


b = np.array([[1, 2, 3], [4, 5, 6]])

print(b[0, 0])   # Element at row 0, col 0 → 1
print(b[1, 2])   # Element at row 1, col 2 → 6


print(b[:, 1])   # All rows, column 1 → [2 5]
print(b[0, :])   # Row 0, all columns → [1 2 3]
print(b[:, ::2]) # All rows, every 2nd column → [[1 3], [4 6]]


x = np.array([5, 10, 15, 20, 25])
print(x[x > 10])   # → [20 25]
