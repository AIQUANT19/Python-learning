import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, None, 30, 22],
    'City': ['Delhi', 'Mumbai', None, 'Chennai']
}

df = pd.DataFrame(data)
print(df.isnull())   # This returns a DataFrame of the same shape as df, with True where values are missing (NaN), and False elsewhere.
print("\nCount of missing values:\n", df.isnull().sum())
# Print rows with any missing values
print("Rows with NaNs:\n", df[df.isnull().any(axis=1)])

df_cleaned = df.dropna()   # Removes rows (by default) that contain any missing values.
print(df_cleaned)

# Fill with a constant
df_filled = df.fillna("Don't know")

# Fill age column with average age
df_filled['Age'] = df['Age'].fillna(df['Age'].mean())

print(df_filled)

# Replace "Mumbai" with "Bombay"
df['City'] = df['City'].replace('Mumbai', "Bombay")

print(df)


df['Age'] = df['Age'].fillna(0)
df['Age'] = df['Age'].astype(int)
print(df.dtypes)

# Drop rows with missing values
print("After dropping:\n", df.dropna())