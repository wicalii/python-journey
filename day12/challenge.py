services = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}


while True:

    try:
        port = int(input("Enter port (0 to exit): "))

        if port == 0:
            print("Goodbye!")
            break

        service = services.get(port, "Unknown Service")

        print(f"{port} -> {service}")

    except ValueError:
        print("Invalid port!")