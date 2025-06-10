import pandas as pd

# fruits = ["Apple", "Orange", "Banana", "Watermelon"]
# prices = [250, 50, 60, 120]
# fruit_prices = pd.Series(prices, index=fruits)

# # Print the price of "Watermelon".

# print(f"The price of Watermelon is {fruit_prices["Watermelon"]}")

# # Print the prices of both "Apple" and "Banana".

# print(f"The prices of Apple and Banana are \n{fruit_prices[["Apple", "Banana"]]}")

# # Slice and print the first 3 fruits.

# print(f"The first three fruits and their prices are \n{fruit_prices[:3]}")

# # Print the last fruit and its price.

# print(fruit_prices[-1:])

# # Check whether "Mango" is in the Series.

# print("Mango" in fruit_prices)

# # Change the price of "Orange" to 80.

# fruit_prices["Orange"] = 80

# print(fruit_prices)

# # Add a new fruit "Mango" with a price of 150.

# fruit_prices["Mango"] = 150

# print(fruit_prices)

# # Filter and print all fruits that cost more than 100.

# print(f"The fruits whose cost is greater than 100 are {fruit_prices[fruit_prices > 100]}")

# # Sort the Series by prices in ascending order.

# print(fruit_prices.sort_values())

# # Sort the Series by fruit names alphabetically.

# print(fruit_prices.sort_index())

#  Create a Series from a dictionary of student names and their marks:
data = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}
# Create a Series and print it.

scores = pd.Series(data)
print(scores)

# 2. Find and print:
# The student(s) with the highest marks.
max_score = scores.max()
print(f"The student(s) with the highest marks is(are) \n{scores[scores == max_score]}")

# All students who scored above 85.

print(f"The students who scored greater than 85 are \n{scores[scores>85]}")

# 3. Add a new student "Frank" with score 81.

scores["Frank"] = 81

# Then increase all scores by 5 bonus points.
scores = scores + 5

print(scores)

# Drop the student "Charlie" from the Series.

scores = scores.drop("Charlie")

print(scores)

# Use this function:
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'C'


grades = scores.apply(get_grade)
print("\nFinal Grades:\n",grades)