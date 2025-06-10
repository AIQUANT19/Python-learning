import pandas as pd

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Salary': [50000, 52000, 60000, 58000, 61000, 45000, 47000],
    'Experience': [2, 3, 4, 5, 3, 2, 3]
}

df = pd.DataFrame(data)
print(df)

grouped = df.groupby('Department')
print(grouped)

print(grouped['Salary'].min())

print(grouped['Experience'].sum())

result = df.groupby('Department').agg({
    'Salary': 'mean',
    'Experience': 'max'
})
print(result)


result1 = df.groupby('Department').agg({
    'Salary': ['min','mean', 'max'],
    'Experience': ['min', 'sum']
})
print(result1)