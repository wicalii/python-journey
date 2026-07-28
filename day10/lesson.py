# Day 10 - Port Service Lookup Tool

services = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

while True:
    port = int(input("Enter port (0 to exit): "))

    if port == 0:
        print("Goodbye!")
        break

    service = services.get(port, "Unknown Service")

    print(f"{port} -> {service}")

    with open("history.txt", "a") as file:
        file.write(f"{port} -> {service}\n")

print("\nHistory:")

with open("history.txt", "r") as file:
    print(file.read())