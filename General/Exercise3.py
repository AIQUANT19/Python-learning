# 1. Multiplication Table
# Ask the user for a number, and print its multiplication table up to 10.

print("Enter a number for multiplication table")
output = int(input())

x = 1
while x <= 10:
    # print(output, "*", x, "=", output * x)
    print(f"{output} * {x} = {output * x}")

    x = x + 1


# 2. Factorial Calculator
# Ask the user for a number n, and print the factorial of that number using a while loop.

print("Enter a number")
num = int(input())
mul = 1
numb = num
while numb > 0:
    mul = mul * numb
    numb = numb - 1
print(f"The factorial value of {num} is {mul}")

# 3. Reverse a Number
# Ask the user to enter a number. Reverse the digits using math — don’t convert to string.

print("Enter a number to reverse")
num1 = int(input())

num2 = 0
while num1 > 0:
    num2 = (num2*10) + (num1 % 10)
    num1 = num1 // 10
print(f"The reverse number is {num2}")