# Day 12 - Try Except

try:
    number = int(input("Enter number: "))

    print(f"Your number is: {number}")

except ValueError:
    print("Invalid number!")

print("Program Finished")