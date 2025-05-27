#  Exercise 1: Tuple Basics
# Create a tuple with 5 elements and:

# Print the first and last elements.

# Count how many times a certain value appears.

# Find the index of a value.

# print("Enter some numbers with one space")

# s = input()

# items = s.split()

# nums = tuple(int(x) for x in items)

# print(nums)

# print(f"The first and last elements of the tuple {nums} are {nums[0]} and {nums[len(nums)-1]}")
# print(f"The counts of the tuple {nums} is {nums.count(20)}")


# new_tuple = (1,2,4)

# x,y,z=new_tuple

# print(x,y,z)

# nested = (1, 2, (3, 4, 5))
# print(nested[2])
# print(len(nested))
# for i in range(1, len(nested)+1):
#     print(f"The {i}th element is {nested[i-1]} ")


# book = {
#     "title": "1984",
#     "author": "George Orwell",
#     "year": 1949
# }

# print(book["author"])
# print(book["title"])
# print(book["year"])

# book["genre"] = "sjkdk"
# book.pop("year")


# print(book)

# for key,value in book.items():
#     print(f"{key} : {value}")


# words = input("Enter 5 words separated by spaces: ").split()

# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)


student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# 1. Print the student's name
# 2. Add a new key "major" with value "Computer Science"
# 3. Update the age to 21
# 4. Remove the "grade"
# 5. Print all keys and values

# print(student["name"])
# student["major"] = "Computer Science"
# student["age"] = 21
# student.pop("grade")

# for key,value in student.items():
#     print(f"{key}: {value}")

# new_update = {}
# for i in range(0, 3):
#     print("Enter name:")
#     s = input()
#     print("Enter number")
#     t = input()
#     new_update[s] = t
# print(new_update)


# print("Enter a sentence:")

# sen = input().split()

# print(sen)

# word_count = {}

# for word in sen:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)

# str = "I am in India"

# str1 = str.split()

# print(str1[0])
# str2 = []
# for i in range(0,len(str1)):
#     str2.append(str1[len(str1)-1-i])

# print(str2)