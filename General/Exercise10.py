# Create a text file named fruits.txt with the following content:

f = open("exercise.txt", "w")

f.write("Apple\nBananna\nCherry\nMango\nPineapple")

f.close()

# Write a Python script that:

# Opens the file

# Reads all the lines one by one

# Prints each fruit in uppercase

# with open("exercise.txt","r") as f:
#     data = f.read()
#     print(data.upper())

# with open("exercise.txt","r") as f:
#     for line in f:
#         print(line.strip().upper())


# Write a script that:

# Creates (or opens) a file named log.txt

# Appends the current message: "User logged in.\n"

# Run it multiple times and observe the file growing!
for i in range(10):
    with open("log.txt","a")as f:
        f.write("User logged in.\n")