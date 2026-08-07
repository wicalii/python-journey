# Day 14 Challenges

services = ["FTP", "SSH", "DNS", "HTTP", "HTTPS"]

# Add new service
services.append("SMTP")

print("After adding SMTP:")
print(services)


# Remove service
services.remove("DNS")

print("\nAfter removing DNS:")
print(services)


# Insert service
services.insert(1, "Telnet")

print("\nAfter inserting Telnet:")
print(services)


# Show last service
print("\nLast service:")
print(services[-1])


# Show part of list
print("\nSlicing:")
print(services[1:4])