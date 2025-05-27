# ✅ Exercise 1: Sentence Joiner
# Ask the user to enter 3 words.

# Combine them into a sentence using " ".join(...).

# print("Enter 3 words with spaces")
# word1 = input().split()

# print(word1)

# result = " ".join(word1)

# print("The new word is", result)



# Exercise 2: First Occurrence
# Ask the user to enter a sentence.

# Ask for a word to search.

# Use find() to print the first index where the word occurs.

# print("Enter a sentence...")

# sen = input()

# print("Enter another word...")

# word = input()

# print(f"The first index of the word {word} in {sen} is {sen.find(word)}")


# Exercise 3: Word Frequency Counter
# Ask the user to enter a sentence.

# Ask for a word to count.

# Use count() to show how many times that word appears.

# print("Enter a sentence...")

# sen = input()

# print("Enter another word...")

# word = input()

# print(f"The total count of the word {word} in {sen} is {sen.count(word)}")


# Exercise 4: File Checker
# Ask the user to input a filename (e.g., index.html, script.py).

# Print whether it starts with "index" and whether it ends with ".py".

# print("Enter a file path...")

# path = input()

# print(path.startswith("index"))
# print(path.endwith("py"))


# Reverse Words
# Ask the user to enter a sentence.

# Print the sentence with the words reversed.
# Example: “I love Python” → “Python love I”

# print("Enter a sentence...")

# sen = input().split()
# print(sen)
# reverse = []
# for i in range(0,len(sen)):
#     reverse.append(sen[len(sen) - 1 - i])

# newSen = " ".join(reverse)
# print(newSen)


# Vowel Counter
# Ask the user to enter a sentence.

# Count the number of vowels in it.

print("Enter a sentence!!!")

x = input()

vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
count = 0
for key in x.lower():
    if key in vowels:
        vowels[key] += 1

print(f"The total count is {vowels}")
