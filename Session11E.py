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


from Session11A import customer
from Session10C import vehicle
from Session10D import Driver


class Ride:
    def __init__(self, customer=None, date="20th June,2024", time="12:00", from_location="Home", to_location="Work", distance=4, fare=200, driver=None):
        self.customer = customer
        self.date = date
        self.time = time
        self.from_location = from_location
        self.to_location = to_location
        self.distance = distance
        self.fare = fare
        self.driver = driver

    def add_ride_details(self):
        print("ENTER RIDE DETAILS")
        self.from_location = input("Enter From Location")
        self.to_location = input("Enter To Location")

    def link_customer(self, customer):
        self.customer = customer

    def link_driver(self, driver):
        self.driver = driver

    def show(self):

        self.customer.show()


        print("~~~~~~~~~~~~~~RIDE~~~~~~~~~~~~~~~~~~~")


        print("FROM: {} | TO: {}".format(self.from_location, self.to_location))
        print("DISTANCE: {} | FARE: {}".format(self.distance, self.fare))
        print("DATE: {} | TIME: {}".format(self.date, self.time))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        self.driver.show()




