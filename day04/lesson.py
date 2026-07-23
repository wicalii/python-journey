# ============================
# Day 04 - Functions
# ============================


# Basic Function

def show_banner():
    print("========================")
    print("Python Security Toolkit")
    print("========================")


show_banner()


# Function with Parameter

def show_service(service):
    print(f"Service: {service}")


show_service("SSH")
show_service("HTTP")
show_service("HTTPS")


# Function with Multiple Parameters

def show_target(target, port):
    print(f"Target: {target}")
    print(f"Port: {port}")


show_target("google.com", 443)
show_target("192.168.1.10", 22)


# Scope Example

name = "Ali"


def hello():
    name = "Python"
    print(name)


hello()

print(name)