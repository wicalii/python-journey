# Day 08 - Dictionaries

# Create Dictionary
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    53: "DNS"
}

# Access values
print(services[22])
print(services.get(80))
print(services.get(25, "Unknown Service"))

print("----------------")

# Keys
print(services.keys())

print("----------------")

# Values
print(services.values())

print("----------------")

# Items
print(services.items())

print("----------------")

# Loop through keys
for port in services:
    print(port)

print("----------------")

# Loop through key and value
for port, service in services.items():
    print(f"{port} -> {service}")