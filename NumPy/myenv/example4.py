import numpy as np

arr = np.arange(1,5)
print(arr)

result = np.where(arr > 2, -1, 0)
print(result)

print(np.any(arr > 3))

print(np.all(arr > 2))

# Given an array, replace all values less than 10 with 0, and keep others as-is.

arr2 = np.array([3, 10, 7, 12, 5, 20])
# Use np.where

result1 = np.where(arr2 < 10, 0, arr2)
print(result1)