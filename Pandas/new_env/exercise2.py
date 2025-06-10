import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 90, 78, 92],
    "English": [88, 76, 95, 85],
    "Science": [91, 89, 84, 90],
    "Sports": [70, 75, 80, 85]
}

df = pd.DataFrame(data)
print(df)
# 1. Print the names of students who scored more than 90 in Science.

score = df["Science"] > 90
print(df[score]["Name"])

# 2. Print the Math and Science scores of students whose English score is greater than 80.

Eng = df["English"] > 80
print(df[Eng][["Math", "Science"]])

# 3. Add a new column called "Total" which is the sum of all subjects for each student.

df["Total"] = df[["Math", "English", "Science", "Sports"]].sum(axis=1)

print(df)

# 4. Print the row of the student with the highest Total score.

print(df[df["Total"] == df["Total"].max()])

# 5. Sort the DataFrame based on Math scores in descending order.

df_sorted = df.sort_values(by="Math", ascending=False)

print(df_sorted)