name = input("Enter customer name")
phone = input("Enter customer phone")
email = input("Enter customer email")

customer_details = "{},{},{}\n".format(name, phone, email)

file = open("Customer.csv", "a")
file.write(customer_details)
print("Customer Data Saved")
file.close()