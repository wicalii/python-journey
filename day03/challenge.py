target = input("Enter target: ")
port = int(input("Enter port: "))

if port == 22:
    print(f"{target} -> SSH Service")

elif port == 80:
    print(f"{target} -> HTTP Service")

elif port == 443:
    print(f"{target} -> HTTPS Service")

elif port == 53:
    print(f"{target} -> DNS Service")

else:
    print(f"{target} -> Unknown Service")