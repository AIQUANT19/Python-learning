import pandas as pd

data = {
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, None, 30, 22],
    'City': ['Delhi', 'Mumbai', None, 'Chennai']
}

df = pd.DataFrame(data)

# 👉 Task: Print a boolean DataFrame showing which values are missing (True = NaN)
print(df.isnull())


# 👉 Task: Drop all rows that have any missing values
# and store the result in `df_cleaned`

print(df.dropna())

# 👉 Task: Fill missing Name/City with "Unknown" and Age with the average age
df_filled = df.fillna("Unknown")
df_filled['Age'] = df['Age'].fillna(df['Age'].mean())
print(df_filled)

