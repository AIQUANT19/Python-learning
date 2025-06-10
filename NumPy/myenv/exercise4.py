import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# 👉 Use np.vstack to stack them row-wise

result = np.vstack((a,b))

print(result)

x = np.array([[1], [2]])
# 👉 Use np.hstack to repeat x three times
# Expected shape: (2, 3)

result1 = np.hstack((x,x,x))
print(result1)

p = np.array([[10, 20], [30, 40]])
q = np.array([[1, 2], [3, 4]])
# 👉 Combine p and q column-wise

print(np.concatenate((p,q), axis = 0))

arr = np.arange(10)
# 👉 Replace even values with -1 using np.where

result2 = np.where(arr % 2 == 0, -1 ,arr)

print(result2)

x1 = np.array([5, 12, 17, 9, 3, 25])
# 👉 Get values between 10 and 20 (inclusive)

print(x1[(x1 > 9) & (x1 < 21)])

a = np.array([2, 4, 6, 8, 10])
# 👉 Replace all elements greater than 5 with the mean of the array

mean = np.mean(a)
a[a > 5] = mean
print(a)
