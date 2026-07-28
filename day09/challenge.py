name = input("Enter your name: ")

with open("users.txt", "a") as file:
    file.write("\n" + name)

print("Name saved successfully!")

with open("users.txt", "r") as file:
    print("\nSaved Users:")
    print(file.read())