# Task:
# Write a program that asks the user for a filename.
# Try to open and read the file. If the file doesn't exist, print an error message.

# try:
#     with open("log.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File does not exist.")



# Task:
# Append "Hello from Python\n" to a file called log.txt.
# Use a try–except block to catch any error and print a message if writing fails.

# try:
#     with open("log1.txt","a") as f:
#         f.write("Hello from Python\n")
# except PermissionError:
#     print("Writing failure!!")


#     Task:

# Open a file called numbers.txt which contains one number per line.

# Read all lines.

# Try to convert each line to an integer.

# If any line has invalid data (e.g. a letter), catch it and print "Invalid line: <line>".

with open("numbers.txt","r") as f:
    for num in f:
        line = num.strip()
        try:
            value = int(line)
            print(f"Read numbers: {value}")
        except ValueError:
            print(f"Invalid number: {num}")