# Create a NumPy array with values from 10 to 19.
# Extract a slice that includes the middle 5 values.

import numpy as np

a = np.arange(10,20,1)
print(a[2:7])

# Create a NumPy array with values from 0 to 9 and reverse it using slicing.

b = np.arange(10)
print(b)
c = b[::-1]
print(c)


arr = np.zeros((3,3))
count = 1
for i in range(0,3):
    for j in range(0,3):
        arr[i][j] = count
        count += 1

print(arr)
# Extract the second column as a 1D array.

arr_second = arr[:, 1]
print(arr_second)


# From the array [10, 15, 20, 25, 30, 35], use boolean indexing to extract only the even numbers.

x = np.array([10,15,20,25,30,35])
print(x[x % 2 == 0])