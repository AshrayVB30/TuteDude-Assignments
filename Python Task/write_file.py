# 3. Write to a File
# Write a program to create a text file and write some content to it.
# Using file functions like write and open.

with open("sample.txt", "w") as file:
    file.write("This is a sample text written to the file.\n")
    file.write("Python file handling is easy!\n")

print("Content written to sample.txt")