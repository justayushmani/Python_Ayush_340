#creating a new file
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is a sample file created using Python.\n")
file.close()

#reading a file
file = open("example.txt", "r")
content = file.read()
print(file) #this will print the file object info
print(content)

#reading  file using with statement
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#to get the file name
with open("example.txt", "r") as file:
    print("File Name:", file.name)

#to check whether file is closed or not
with open("example.txt", "r") as file:
    print("Is file closed?", file.closed)

#to get the mode of file
with open("example.txt", "r") as file:
    print("File Mode:", file.mode)

#reading files (read, readline, readlines)
with open("example.txt", "r") as file:
    content = file.read()
    print("Using read():\n", content)
    file.seek(0)  # Reset file pointer to the beginning
    line = file.readline()
    print("Using readline():\n", line)
    file.seek(0)  # Reset file pointer to the beginning
    lines = file.readlines()
    print("Using readlines():\n", lines)

#writing to a file (write, writelines)
with open("example.txt", "w") as file:
    file.write("First line using write().\n")
    file.writelines(["Second line using writelines().\n", "Third line using writelines().\n"])
