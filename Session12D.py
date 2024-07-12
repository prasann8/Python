class Customer:
    def __init__(self, name, phone, email, address, gender, age):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.gender = gender
        self.age = age

    def add_customer_details(self):
        print("ENTER CUSTOMER DETAILS")
        self.name = input("Enter Customer name:")
        self.phone = input("Enter Customer phone:")
        self.email = input("Enter Customer email:")
        self.address = input("Enter Customer address:")
        self.gender = input("Enter Customer gender:")
        self.age = int(input("Enter Customer age:"))

    def show(self):
        print("~~~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~~~~~~~")
        print("CUSTOMER NAME: {} | PHONE: {}".format(self.name,self.phone))
        print("EMAIL: {} | ADDRESS: {}".format(self.email, self.address))
        print("GENDER: {} | AGE: {}".format(self.gender, self.age))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")