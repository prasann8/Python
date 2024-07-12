from Session11 import Customer

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO CUSTOMER MANAGEMENT SYSTEM")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:

    print("1 Add Customer")
    print("2 View Customer")
    print("0 Quit")

    choice = int(input("Enter your choice:"))
    print("You selected", choice)

    if choice == 1:
        file = open("Customer.csv", "a")
        customer = Customer()
        customer.add_customer_details()
        customer.show()

        data = customer.to_csv()
        file.write(data)
        print("Data Written:", data)

    elif choice == 2:
        file = open("Customer.csv", "r")
        lines = file.readlines()
        for line in lines:
            print(line)

    elif choice == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Thank you for using Customer Management")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        file.close()
        break

