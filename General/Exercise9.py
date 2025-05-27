# 🧪 Exercise 1: Greet a User
# Task: Write a function greet_user(name) that prints "Hello, <name>!"

def greet_user(name):
    print(f"Hello {name}")

print("Enter your name: ")
name = input()

greet_user(name)


# 🧪 Exercise 2: Square of a Number
# Task: Write a function square(num) that returns the square of a number.

def square(num):
    return num * num

print("Enter a number:")
n = int(input())
print(square(n))


# 🧪 Exercise 3: Add Two Numbers
# Task: Write a function add(a, b) that returns the sum of two numbers.

def add(x, y):
    return x+y
print(add(1,2))

# 🧪 Exercise 4: Check Even or Odd
# Task: Write a function is_even(num) that returns True if a number is even, else False.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print("Enter a number")
x = int(input())
print(f"Is the number {x} even? {is_even(x)}")

# 🧪 Exercise 5: Count Vowels
# Task: Write a function count_vowels(text) that returns the number of vowels in a string.

def count_vowels(str):
    count = 0
    for char in str:
        if char.lower() in "aeiou":
            count += 1
    return count

print("Enter a string: ")
str1 = input()
print(f"The total vowels in the string {str1} is {count_vowels(str1)}")