# Day 07 - For Loops

# Example 1
for number in range(1, 11):
    print(number)

print("----------------")

# Example 2
for number in range(10, 0, -2):
    print(number)

print("----------------")

# Example 3
for letter in "security":
    print(letter)

print("----------------")

# Example 4
services = ["SSH", "HTTP", "HTTPS", "DNS"]

for service in services:
    print(service)

print("----------------")

# Example 5
ports = [22, 80, 443, 53, 21]

for port in ports:
    if port > 100:
        print(port)