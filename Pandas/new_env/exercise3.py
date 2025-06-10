import pandas as pd

data = {
    "Student": ["Anna", "Ben", "Chris", "Diana", "Ethan"],
    "Math": [78, 95, 62, 88, 90],
    "English": [85, 80, 75, 92, 89],
    "Science": [90, 85, 70, 95, 93],
    "Attendance (%)": [92, 88, 75, 98, 85]
}

df = pd.DataFrame(data)
print(df)

# Print names of students who scored more than 85 in English.

print(df[df["English"] > 85]["Student"])

# Print names of students who have attendance above 90%.

print(df[df["Attendance (%)"] > 90]["Student"])

# Add a column Average which stores the average of Math, English, and Science for each student.

df["Total"] = df[["Math", "English", "Science", "Attendance (%)"]].sum(axis=1)
df["Average"] = df["Total"] / 3
print(df)

# Who has the lowest average score? Print the student's name and their average.

print(df[df["Average"] == df["Average"].min()][["Student", "Average"]])

# Sort the DataFrame based on Average in descending order.

df_sorted = df.sort_values(by="Average", ascending=False)

print(df_sorted)

# Print the Student and Attendance (%) of those who scored more than 90 in Science.

print(df[df["Science"] > 90][["Student","Attendance (%)"]])