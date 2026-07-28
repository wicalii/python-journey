# Day 09 - File Handling

# Write to a file
with open("hello.txt", "w") as file:
    file.write("Hello Python")

# Read from a file
with open("hello.txt", "r") as file:
    print(file.read())

# Append to a file
with open("hello.txt", "a") as file:
    file.write("\nLearning Python")

# Read again
with open("hello.txt", "r") as file:
    print(file.read())