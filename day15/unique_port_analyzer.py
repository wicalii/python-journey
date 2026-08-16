ports = [21, 22, 80, 22, 443, 80, 53, 21]

unique_ports = set(ports)

services = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

for port in sorted(unique_ports):

    service = services.get(port, "Unknown Service")

    print(f"{port} -> {service}")

    with open("scan_history.txt", "a") as file:
        file.write(f"{port} -> {service}\n")