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


print(df.head())  # Get the 5 rows

print(df.columns)   # Get the column names

print(df.shape)  # return the dimensions(rows, columns)

print(df.describe())   # Get statistics of numeric columns

print(df["Math"])

print(df.Name)

print(df.iloc[1])   # Second row

print(df.loc[1])

print(df[1:3]) # second row & third row