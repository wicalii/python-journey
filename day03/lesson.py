# ============================
# Day 03 - elif
# ============================

# if / elif / else

port = 22

if port == 22:
    print("SSH Service")

elif port == 80:
    print("HTTP Service")

elif port == 443:
    print("HTTPS Service")

elif port == 53:
    print("DNS Service")

else:
    print("Unknown Service")


# Another Example

score = 85

if score >= 90:
    print("Grade A")

elif score >= 80:
    print("Grade B")

elif score >= 70:
    print("Grade C")

else:
    print("Failed")