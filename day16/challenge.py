# Day 16 - Challenges

users = {
    "Ali": 19,
    "Reza": 20,
    "Amir": 18
}


# Show users and ages
for name, age in users.items():
    print(f"{name} -> {age}")


# Change age
users["Ali"] = 20

print("\nAfter changing Ali's age:")
print(users)


# Add new user
users["Sara"] = 19

print("\nAfter adding Sara:")
print(users)


# Check user
if "Ali" in users:
    print("\nAli exists")

if "John" not in users:
    print("John not found")


# Get user
print("\nGet user:")
print(users.get("Reza", "User not found"))
print(users.get("John", "User not found"))