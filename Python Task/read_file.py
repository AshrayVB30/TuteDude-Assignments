# 4. Read from a File
# We used open in read mode and file.read to read and print to display.

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
