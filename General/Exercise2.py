# Exercise 1
# Add Two Numbers
# Ask the user to enter two numbers. Print their sum.

print("Enter a number")
num = int(input())
print("Enter another number")
num2 = int(input())

print("The sum of the two numbers is", num+num2)

# Exercise 2: Birth Year
# Ask the user for their age.
# Calculate and print the year they were born (Assume the current year is 2025).

print("Enter your age:")
age = int(input())

print("You born in", 2025-age)

# Exercise 3: Simple Interest
# Ask for: Principal amount, Rate of interest, Time in years
# Then calculate Simple Interest using the formula:

print("Enter the amount which you want to give as a principal amount")
p = int (input())
print("Enter the rate of interest")
r = int(input())
print("Enter the year")
t = int(input())

print("Calculating the interest:")
i=(p*r*t)/100

print("The interest is ", i)