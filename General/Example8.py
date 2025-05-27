# List Comprehensions


# numbers = []
# for i in range(10):
#     numbers.append(i*2)
# print(numbers)

numbers = [i*2 for i in range(10)]
print(numbers)


oddNum = [i for i in range(10) if i % 2 != 0]

print(oddNum)

words = ["Hello", "Atosi"]
lower_words = [word.lower() for word in words]

print(lower_words)