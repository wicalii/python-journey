def is_valid_port(port):

    return 0 < port <= 65535


def analyze_port(port):

    if not is_valid_port(port):
        return "Invalid Port"

    services = {
        21: "FTP",
        22: "SSH",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS"
    }

    return services.get(port, "Unknown Service")


port = int(input("Enter port: "))

print(f"{port} -> {analyze_port(port)}")