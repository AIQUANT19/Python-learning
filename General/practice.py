# def get_even(numbers):
#     return [n for n in numbers if n % 2 == 0]

# print(get_even([1,2,3,4,5,6,7]))

# def reverse_str(str):
#     result = ""
#     for i in range(0, len(str)):
#         result += (str[len(str)-1-i])
#     return result

# c = "Hello"
# print(reverse_str(c))

# a = "banana"
# def total_vowels(str):
#     count = 0
#     for c in str:
#         if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
#             count += 1
#     return count
# print(total_vowels(a))

# arr = [5,9,2,8,1]
# def get_max(list):
#     max = list[0]
#     for i in range(len(list)):
#         if max < list[i]:
#             max = list[i]
#     return max
# print(f"The maximum value of the list {arr} is {get_max(arr)}")

# print("Enter a number")
# val = input().strip()

# def get_sum(value):
#     sum = 0
#     for n in value:
#         sum += int(n)
#     return sum

# print(get_sum(val))

# arr1 = [1, 2, 2, 3, 4, 4]

# def check_duplicate(list):
#     result = []
#     for i in range(len(list)):
#         if list[i] not in result:
#             result.append(list[i])
#     return result

# print(check_duplicate(arr1))


# Write a function to check if a given string is a palindrome (reads the same forward and backward).

def check_palindrome(val):
    for i in range(len(val) // 2):
        if val[i] != val[len(val)-1-i]:
            return False
    return True

print(check_palindrome("helleh"))

# Write a function to calculate the factorial of a given number n.
def factorial(value):
    result = 1
    if value == 1:
        result = value
    else:
        result = value * factorial(value - 1)
    return result
print(factorial(5))

# Print numbers from 1 to 20.

# For multiples of 3, print "Fizz"

# For multiples of 5, print "Buzz"

# For multiples of both 3 and 5, print "FizzBuzz"

def FizzBuzz_code(list):
    for i in list:
        if (i % 3 == 0) & (i % 5 == 0):
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif (i % 3 == 0):
            print("Fizz")
        else:
            print(i)

FizzBuzz_code([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

# Write a function to find the second largest number in a list.

def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

print(second_largest([10, 20, 5, 8, 70]))

def count_chars(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

print(count_chars("hello world"))