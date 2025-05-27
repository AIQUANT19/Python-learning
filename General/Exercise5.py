#  Exercise 1: Count Elements
# Ask the user to enter 5 numbers. Store them in a list.
# Print how many numbers were entered using len().

print("Enter numbers separated by spaces:")
a = input().split()               # split into list of strings
a = [int(x) for x in a]           # convert strings to integers

print(f"The length of the user's list is {len(a)}")

a.sort()
print(f"The sorted list is: {a}")


#  Exercise 2: Find Maximum
# Ask the user to enter numbers separated by spaces.
# Store them in a list, and print the largest number.

print("Enter numbers separted by spaces")
arr1 = input().split()
arr1 = [int(x) for x in arr1]
max = arr1[0]
for i in range(1,len(arr1)):
    if max < arr1[i]:
        max = arr1[i]
print(f"The largest number in the list {arr1} is {max}")

# Exercise 3: Count Even Numbers
# Create a list of numbers.
# Print how many of them are even.

print("Enter numbers by spaces")
arr = input().split()

arr = [int(x) for x in arr]

total_even_numbers = 0
for i in range(0,len(arr)):
    if arr[i] % 2 == 0:
        total_even_numbers += 1
print(f"The total even numbers in {arr} is {total_even_numbers}")

#  Exercise 4: Merge Two Lists
# Ask the user to enter two lists of 3 items each.
# Merge them into one using extend() and print the result.

print("Enter 3 numbers by spaces")
arr = input().split()
arr = [int(x) for x in arr]
print("Enter another 3 numbers by spaces")
arr1 = input().split()
arr1 = [int(x) for x in arr1]
arr.extend(arr1)
print(arr)


#  Exercise 5: Remove Item
# Create a list of colors: ["red", "green", "blue", "yellow"]
# Ask the user to enter a color to remove.
# Remove it from the list using remove() and print the new list.

colors = ["red", "green", "blue", "yellow"]
print(f"Enter a number between 0 to {len(colors)-1}")
#print("Enter a color")
val = int(input())
colors.pop(val)

print(f"After removing the elements, the new list is {colors}")

# Exercise 6: Reverse a List
# Create a list of any 5 numbers.
# Reverse the list without using .reverse() — do it using slicing or a loop.

print("Enter 5 numbers by spaces")
arr = input().split()
arr = [int(x) for x in arr]

arr1 = []

for i in range(0, len(arr)):
    arr1.append(arr[len(arr)-i-1])

print(f"The new list is {arr1}")