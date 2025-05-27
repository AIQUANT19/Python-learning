# # #File Handleing

# # #Opening a file:
# f = open("example.txt", "r")

# # content = f.read() #Read whole files

# # print(content)

# line = f.readline()  # Read one line

# print(line)

# lines = f.readlines()  # Read all the rest lines as a list

# print(lines)

# # f.close()



# #If we use `with`, Python close the file after using automatically
# with open("example.txt", "r") as f:
#     data = f.read()
#     print(data)

# #Writing a file
# # If a file exists, the file is overwritten
# #If the file does not exist, the file will be created and then written.

# with open("example.txt", "w") as f:
#     f.write("Hello, file!\n")
#     f.write("Another line.")


# # for append case:

# with open("example.txt", "a") as f:
#     f.write("Appended line.\n")




# 1) Why should I close a file?
# When you open a file using open(), Python keeps a connection (called a "file handler") to that file in your system's memory.

# If you don’t close it, it may cause:

# Memory leaks (especially when opening many files).

# File corruption or failure to save changes (especially in write mode).

# Problems accessing the file again later.


# with open("sample.txt", "w") as f:
#     f.write("This is a new line.\n")
#     f.write("This will overwrite the file.\n")


# with open("sample.txt", "a") as f:
#     f.write("This line will be added.\n")


lines = ["One\n", "Two\n", "Three\n"]

with open("numbers.txt", "w") as f:
    f.writelines(lines)
