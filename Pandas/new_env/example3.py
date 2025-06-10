import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, None, 30, 22],
    'City': ['Delhi', 'Mumbai', None, 'Chennai']
}

df = pd.DataFrame(data)
print(df.isnull())   # This returns a DataFrame of the same shape as df, with True where values are missing (NaN), and False elsewhere.

# Print rows with any missing values
print("Rows with NaNs:\n", df[df.isnull().any(axis=1)])

df_cleaned = df.dropna()   # Removes rows (by default) that contain any missing values.
print(df_cleaned)

# Fill with a constant
df_filled = df.fillna("Unknown")

# Fill age column with average age
df['Age'] = df['Age'].fillna(df['Age'].max())

print(df)

# Drop rows with missing values
print("After dropping:\n", df.dropna())