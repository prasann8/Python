"""
    customer = name, phone, email, address, gender, age
"""


class Customer:

    def __init__(self, name="", phone="", email="", address="", gender="", age=15):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
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
        print("CUSTOMER NAME: {} | PHONE: {}".format(self.name, self.phone))
        print("EMAIL: {} | ADDRESS: {}".format(self.email, self.address))
        print("GENDER: {} | AGE: {}".format(self.gender, self.age))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def to_csv(self):
        data = "{}, {}, {}, {}, {}, {}\n".format(self.name, self.phone, self.email, self.address, self.gender, self.age)
        return data