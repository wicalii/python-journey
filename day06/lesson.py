# Day 06 - While Loops

# Example 1: Count from 1 to 10

count = 1

while count <= 10:
    print(count)
    count += 1


print("--------------------")


# Example 2: Count from 10 to 1

count = 10

while count >= 1:
    print(count)
    count -= 1

print("Done")

print("--------------------")


# Example 3: while True + break

count = 1

while True:
    print(count)

    if count == 5:
        break

    count += 1

print("Finished")