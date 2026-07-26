services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    53: "DNS"
}

ports = [21, 22, 25, 80, 443, 9999]

for port in ports:
    print(f"{port} -> {services.get(port, 'Unknown Service')}")