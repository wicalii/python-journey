target = input("enter target: ")
ip_address = input("ip address: ")
port = int(input("port: "))
protocol = input("protocol: ")

print("========== Target Information ==========")

print(f"target:{ target}")
print(f"ip_Address:{ ip_address}")
print(f"port:{ port}")
print(f"protocol:{ protocol}")

print("========================================")

answer = input("save your information y/n ?")

if answer == "y":
    print("success")
else:
    print("ok!")   