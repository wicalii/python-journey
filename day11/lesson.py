import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

characters = uppercase + lowercase + numbers + symbols

password = ""

length = int(input("Enter password length: "))

for i in range(length):
    password += random.choice(characters)

print(f"Generated Password: {password}")