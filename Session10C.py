"""
    Driver has a vehicle
    Customer can book ride(s)

    Identify objects with attributes

    vehicle = registration number , color, make, model
    driver = name, phone, email, license_number, rating, gender, age, vehicle[1 to 1]

    1 driver has one vehicle

    customer = name, phone, email, address, gender, age

    ride = customer[1 to 1], date, time, from_location, to_location, distance, fare, driver[1 to 1]
    1 ride has 1 customer
    1 ride has 1 driver

"""

class vehicle:

    def __init__(self, reg_number="NA", brand="NA", model="NA", color="white"):
        self.reg_number = reg_number
        self.brand = brand
        self.model = model
        self.color = color

    def add_vehicle_details(self):
        print("ENTER VEHICLE DETAILS")
        self.reg_number = input("Enter Vehicle registration number:")
        self.brand = input("Enter Vehicle Brand:")
        self.model = input("Enter Vehicle model:")
        self.color = input("Enter Vehicle Color")

    def show(self):
        print("-------------------VEHICLE------------------------")
        print("REGISTERED NUMBER: {} | BRAND: {}".format(self.reg_number, self.brand))
        print("MODEL: {} | COLOR: {}".format(self.model, self.color))
        print("--------------------------------------------------")

# vehicle = Vehicle(reg_number = "PB10AB1234",)