# Day 16 - Service Reporter

services = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}


print("===== Service Reporter =====")

print("\nAvailable Services:")

for port, service in services.items():
    print(f"{port} -> {service}")


port = int(input("\nEnter port: "))

service = services.get(port, "Unknown Service")

print(f"{port} -> {service}")


if port in services:
    print("Port Found")
else:
    print("Port Not Found")