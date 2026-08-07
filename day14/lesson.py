# Day 14 - Lists Practice

# List
ports = [21, 22, 80, 443]

print("Original List:")
print(ports)


# append()
ports.append(53)

print("\nAfter append:")
print(ports)


# remove()
ports.remove(80)

print("\nAfter remove:")
print(ports)


# pop()
removed_port = ports.pop(1)

print("\nRemoved port:")
print(removed_port)

print("After pop:")
print(ports)


# insert()
ports.insert(1, 22)

print("\nAfter insert:")
print(ports)


# len()
print("\nNumber of ports:")
print(len(ports))


# Negative Index
print("\nLast port:")
print(ports[-1])


# Slicing
print("\nFirst two ports:")
print(ports[:2])

print("\nFrom index 1:")
print(ports[1:])