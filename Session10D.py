"""

    driver = name, phone, email, license_number, rating, gender, age, vehicle[1 to 1]

"""

from Session10C import vehicle

class Driver:
    def __init__(self, name, phone, email, license_number, rating, gender, age, vehicle):
        self.name = name
        self.phone = phone
        self.email = email
        self.license_number = license_number
        self.rating = rating
        self.gender = gender
        self.age = age
        self.vehicle = vehicle

    def add_driver_details(self):
        print("ENTER DRIVER DETAILS")
        self.name = input("Enter Driver name:")
        self.phone = input("Enter Driver phone:")
        self.email = input("Enter Driver email:")
        self.license_number = input("Enter Driver licence number:")
        self.rating = float(input("Enter Driver rating:"))
        self.gender = input("Enter Driver gender:")
        self.age = int(input("Enter Driver age:"))

        # 1 to 1 Mapping
        self.vehicle = vehicle()  # Object Construction
        self.vehicle.add_vehicle_details()

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("DRIVER NAME: {} | PHONE: {}".format(self.name, self.phone))
        print("EMAIL: {} | LICENSE NUMBER: {}".format(self.email, self.license_number))
        print("RATING: {} | GENDER: {} | AGE: {}".format(self.rating, self.gender, self.age))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        self.vehicle.show()
