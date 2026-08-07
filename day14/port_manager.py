ports = [21, 22, 80]


while True:

    print("\n===== Port List Manager =====")
    print("1. Show Ports")
    print("2. Add Port")
    print("3. Remove Port")
    print("4. Exit")


    choice = input("Choose: ")


    if choice == "1":

        print("Current Ports:")
        print(ports)


    elif choice == "2":

        new_port = int(input("Enter new port: "))

        ports.append(new_port)

        print("Port added!")
        print(ports)


    elif choice == "3":

        remove_port = int(input("Enter port to remove: "))

        if remove_port in ports:

            ports.remove(remove_port)

            print("Port removed!")
            print(ports)

        else:

            print("Port not found")


    elif choice == "4":

        print("Goodbye!")

        break


    else:

        print("Invalid option")