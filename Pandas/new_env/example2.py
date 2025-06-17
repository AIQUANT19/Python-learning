import pandas as pd

# Creating a simple student DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "History" : [85,75,95,56],
    "Math": [85, 92, 78, 90],
    "Science": [88, 94, 82, 85],
    "Geography" : [96,89,79,88],
}

df = pd.DataFrame(data)
print(df)


print(df.head())  # Get first 5 rows
print(df.tail())  # get last 5 rows
print(df.columns)   # Get the column names
print(df[:2])
print(df.shape)  # return the dimensions(rows, columns)
print(f"The average marks in Maths is {df["Math"].sum(axis=0)/df.count()}")
print(df.describe())   # Get statistics of numeric columns, count, mean, std, min, 25%, 50%, 75%, max
print(df.info())  # Info about the data types
print(df["Math"])
print(f"The students whose marks in Maths are greater than 90 is {df[df["Math"]>90]}")
print(df.Name)

print(df.iloc[1])   # Second row  # Row with index 1

print(df.loc[1])   # Row at position 1

print(df[1:3]) # second row & third row
# new_df = df.drop(axis="Math")

print(df)


def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    else:
        return 'C'
    
df["Grade_Math"] = df["Math"].apply(get_grade)

print(df)

df = df.drop("Geography", axis= 1)
print(df)