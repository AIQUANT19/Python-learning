def greet(name):
    print(f"Hello {name}")


print("Enter your name: ")
name = input()
greet(name)

def square(x):
    return x ** 2

result = square(5)
print(result)

def add(a, b):
    return a+b
print(add(2,3))

def greet1(name = "friend"):
    print(f"Hello {name}")

greet1()
greet1("Atosi")


def student_info(name, age, course):
    print(f"{name} is {age} years old and learning {course}.")

student_info("Atosi", 26, "Python")