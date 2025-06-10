# Create a 1D array with values from 5 to 15

import numpy as np

a = np.arange(5,16,1)
print(a)

# Create a 3x3 array of all 9s

b = np.full((3,3),9)

print(b)

# Create two arrays and perform addition, multiplication

x = np.array([1,2,3])
y = np.array([4,5,6])

print(f"The sum will be {x+y}")
print(f"The multipliation will be {x*y}")

# Find mean and max of a 2D array

z = np.array([1,2,3])

print(np.mean(z))
print(np.max(z))


# Create a 3x3 array from 1 to 9

arr = np.zeros((3,3))
total = 1
for i in range(0,3):
    for j in range(0,3):
        arr[i][j] = total
        total += 1
print(arr)
# Slice the second column
print(f"The second column will be {arr[:,1]}")

# Reverse each row
print(f"The array whose reverse row will be: {arr[::-1]}")


# Create an array from 0 to 19.

arr2 = np.arange(0,20)
print(arr2)

# Replace all numbers divisible by 3 with -3.
arr2[arr2 % 3 == 0] = -3
print(arr2)
# Extract all numbers greater than 10 and less than 18.

print(arr2[(arr2 > 10) & (arr2 < 18)])


# Create two 2D arrays:
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]

# 1. Stack them vertically
# 2. Stack them horizontally
# 3. Concatenate them along axis=0 and axis=1

p = np.array([[1,2],[3,4]])
q = np.array([[5,6],[7,8]])

result = np.vstack((p,q))
print(result)

result1 = np.hstack((p,q))
print(result1)

con1 = np.concatenate((p,q),axis = 0)
print(con1)

con2 = np.concatenate((p,q),axis = 1)
print(con2)