target = input("Enter target: ")
port = int(input("Enter port: "))
protocol = input("Enter protocol: ").lower()

if port > 0 and port <= 65535 and protocol == "tcp":
    print(f"Target   : {target}")
    print(f"Port     : {port}")
    print(f"Protocol : {protocol}")

    print("Target is valid")

else:
    print("Invalid Target.")