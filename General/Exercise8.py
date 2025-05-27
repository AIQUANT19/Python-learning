#  Exercise 1: Squares of Even Numbers
# Task: Create a list of squares for even numbers from 1 to 20.

numbers = [x ** 2 for x in range(1,21) if x % 2 == 0]
print(f"The quares of even numbers are {numbers}")


#  Exercise 2: Filter Words
# Task: Given a list of words, create a new list that contains only the words longer than 3 characters.

words = ["hi", "hello", "sun", "sky", "python", "go"]

new_list = [word for word in words if len(word) > 3]
print(f"The new list is {new_list}")

# Exercise 3: Numbers Not Divisible by 3
# Task: Create a list of numbers from 1 to 30 that are not divisible by 3.


not_divisible_by_3 = [num for num in range(1, 31) if num % 3 != 0]

print(f"The numbers whose are not divided by 3 is {not_divisible_by_3}")


# Exercise 4: Remove Vowels from a String
# Task: Given a string, use a list comprehension to remove all vowels and join it back into a string.

text = "List comprehensions are powerful"
new_text = "".join([char for char in text if char.lower() not in "aeiou"])
print(new_text)



# Exercise 5: Word Lengths
# Task: Given a sentence, return a list of the length of each word.

sentence = "Python is fun and fast"

length = [len(word) for word in sentence.split()]

print(length)