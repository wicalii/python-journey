# Day 17 - Port Analyzer


def validate_port(port):
    return 1 <= port <= 65535


def get_service(port):
    services = {
        21: "FTP",
        22: "SSH",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS"
    }

    return services.get(port, "Unknown Service")


def analyze_port(port):
    if not validate_port(port):
        return "Invalid Port"

    return get_service(port)


port = int(input("Enter port: "))

result = analyze_port(port)

print(f"{port} -> {result}")