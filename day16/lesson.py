# Day 16 - Dictionary Practice

services = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}


# keys()
print("Keys:")
for port in services.keys():
    print(port)


# values()
print("\nValues:")
for service in services.values():
    print(service)


# items()
print("\nItems:")
for port, service in services.items():
    print(f"{port} -> {service}")


# Change value
services[80] = "HTTPS"

print("\nAfter changing port 80:")
print(services)


# Add new key
services[8080] = "HTTP-ALT"

print("\nAfter adding port 8080:")
print(services)


# get()
print("\nUsing get():")
print(services.get(22, "Unknown Service"))
print(services.get(9999, "Unknown Service"))


# in
print("\nChecking ports:")

if 22 in services:
    print("Port 22 exists")

if 9999 not in services:
    print("Port 9999 does not exist")