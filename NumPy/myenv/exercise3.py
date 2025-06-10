# import numpy as np

# # Create two 1D arrays x = [0, 1, 2] and y = [10, 20, 30].
# # Using broadcasting, create a 2D array where each element is x + yᵀ.

# x = np.array([0, 1, 2])
# y = np.array([10, 20, 30])

# result = x + y[:, np.newaxis]   # This turns y into a column vector → shape becomes (3, 1)
# print(result)


# # Given a 2D NumPy array, normalize each row so that the sum of each row is 1.

# z = np.array([[1, 2, 3], [4, 5, 6]])
# row_sums = z.sum(axis=1, keepdims=True)    # keepdims=True keeps the dimensions — result becomes 2D
# print(z.sum(axis = 1))  # z.sum(axis=1) gives [6, 15] — sum of each row
# print(row_sums)
# normalized = z / row_sums
# print(normalized)


# # Given two 1D arrays a = np.array([1, 2, 3]) and b = np.array([10, 20, 30]), use broadcasting to calculate their outer product (not dot product).

# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])

# outer = a[:, np.newaxis] * b
# print(outer)

# # In a 2D array, replace the maximum element in each row with 0.

# arr = np.array([[1, 3, 12],
#               [3, 8, 6]])

# # Find index of max in each row
# max_indices = arr.argmax(axis=1)
# print(max_indices)
# # Replace max with 0 using row indices
# for i, idx in enumerate(max_indices):
#     arr[i, idx] = 0

# print(arr)
        

import numpy as np

a = np.arange(5, 16)
a[a % 2 == 1] = -1
print(a)


arr = np.arange(1, 10).reshape(3, 3)
arr_reversed = arr[:, ::-1]
print(arr_reversed)


arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
# Use np.diagonal() or slicing

b = np.diagonal(arr1)
print(b)

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
result = y[:, np.newaxis]
print(x+result)


arr2 = np.arange(1, 17).reshape(4, 4)
# Replace max of each row with 0

max_indices = arr2.argmax(axis=1)
# print(max_indices)
for i, id in enumerate(max_indices):
    arr2[i, id] = 1

print(arr2)


x1 = np.array([10, 25, 35, 60, 45, 5])
# Output should be [25, 35, 45]
x1 = x1 [20 < x1]
x1 = x1 [x1 < 50]
print(x1)