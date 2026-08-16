# Day 15 - Tuples and Sets

# Tuple
services = ("FTP", "SSH", "HTTP")

print("Tuple:")
print(services)

print("Second service:")
print(services[1])


# Set
ports = {21, 22, 80, 80, 443, 22}

print("\nSet:")
print(ports)

print("Number of unique ports:")
print(len(ports))


# Add
ports.add(53)

print("\nAfter add:")
print(ports)


# Remove
ports.remove(22)

print("\nAfter remove:")
print(ports)


# Set operations
ports1 = {21, 22, 80}
ports2 = {22, 80, 443}

print("\nIntersection:")
print(ports1 & ports2)

print("\nUnion:")
print(ports1 | ports2)

print("\nDifference:")
print(ports1 - ports2)