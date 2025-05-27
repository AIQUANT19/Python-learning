# swapping without Temp
# Swap the values of two variables x and y without using a third variable.

var1 = 5
var2 = 10
var1 = var1+var2
var2 = var1-var2
var1 = var1-var2
print("var1 =", var1)
print("var2 =", var2)




#Digits of a Number
#Create a variable num = 749.
#Print the sum of its digits using variables only — not strings.


num = 835
hundreds = num // 100
tens = (num % 100) // 10
ones = (num % 100) % 10

print (hundreds+tens+ones)



# Compound Calculation
x = 5
y = 3
z = 2

print(((x+y)*z)//(x-z))


# Age in Months and Days
# Create a variable age_years for your age.
# Calculate and print your:

# Age in months

# Age in days (use 365 days per year)

Age = 26

Age_in_Months = Age * 12
Age_in_Days = Age_in_Months * 30

print (Age_in_Months)
print (Age_in_Days)


print(type(5 + 3.0))

print(type("10" + "5"))

print(type(10 > 3))

print(type(5 / 2))

print(type(True + False))

print(False + False)
print(True+True)

print(5/2)
print(type(5.0//2))


a,b = 2,1

a,b = b, a

print("a =", a)
print("b =",b)