# Day 15 - Challenges

ips = {
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.1",
    "192.168.1.3"
}

print("Unique IPs:")
print(ips)

print("Number of unique IPs:")
print(len(ips))


ports1 = {21, 22, 80}
ports2 = {22, 80, 443}

print("\nCommon ports:")
print(ports1 & ports2)

print("\nAll ports:")
print(ports1 | ports2)

print("\nPorts only in ports1:")
print(ports1 - ports2)