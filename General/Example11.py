#Exception Handling with File Operations

#To prevent our program from crashing and to handle errors gracefully using try, except.

# try:
#     with open("numberss.txt", "r") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found. Please check the file name.")
# except Exception as e:
#     print(f"An error occurred: {e}")


try:
    with open("readonly.txt", "w") as f:
        f.write("Hello!")
except PermissionError:
    print("You do not have permission to write to this file.")
