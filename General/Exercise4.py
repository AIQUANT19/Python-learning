# # Exercise 1: Squares of Numbers
# # Print the square of numbers from 1 to 10.

# for i in range(1, 11):
#     print(f"{i} squared is {i*i}")

# #  Exercise 2: Triangle Pattern (Stars)
# # Print this pattern using a loop:
# # *
# # **
# # ***
# # ****
# # *****

# for i in range(1, 6):
#     print("*" * i)

# #  Exercise 3: Sum of First N Numbers
# # Ask the user for a number n and print the sum of the first n natural numbers.

# print("Enter a number")
# x = int(input())

# print(f"The sume of first {x} numbers is {(x*(x+1))//2}")

# #  Exercise 4: Countdown
# # Print numbers from 10 to 1 using a for loop.

# for i in range(0,10):
#     print(10-i)



for i in range(1, 6):
    print(" " * (6-i) + "*" * i)

for i in range(1, 10):
    if( i % 2 == 1):
        print(" " * ((10-i)//2) + "*" * i + " " * ((10-i)//2))

for i in range(1,6):
    print("*" * (6-i))


for i in range(1, 6):
    print(" " * (i-1) + "*" * (6-i))


rows = 3  # Half the diamond (top height)

# 🔺 Top half
for i in range(1, rows + 1):  # i = 1 to 3
    spaces = rows - i         # spaces: 2, 1, 0
    stars = 2 * i - 1         # stars: 1, 3, 5
    print(" " * spaces + "*" * stars)

# 🔻 Bottom half
for i in range(rows - 1, 0, -1):  # i = 2 to 1
    spaces = rows - i            # spaces: 1, 2
    stars = 2 * i - 1            # stars: 3, 1
    print(" " * spaces + "*" * stars)
