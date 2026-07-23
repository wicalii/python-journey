def add(a, b):
    return a + b


result = add(20, 30)
print(result)


def check_port(port):
    if 1 <= port <= 65535:
        return True
    return False


print(check_port(53))
print(check_port(70000))