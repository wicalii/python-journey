import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

characters = uppercase + lowercase + numbers + symbols

while True:

    length = int(input("Password length (0 to exit): "))

    if length == 0:
        print("Goodbye!")
        break

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print(f"Generated Password: {password}")