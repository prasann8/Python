class Flightbooking:

    # Default Constructor in Python
    # Self is reference variable, which will held the hashcode of object

    def __init__(self):
        print("Self:", self)
        self.from_location = "New Delhi"
        self.to_location = "Bengaluru"
        self.travel_date = "18th June, 2024"
        self.number_of_traveller = 1
        self.travel_class = "Economy"

    # Parameterized Constructor
    def __init__(self, from_location, to_location, travel_date, number_of_travellers, travel_class):
        # print("Self:", self)
        self.from_location = from_location
        self.to_location = to_location
        self.travel_date = travel_date
        self.number_of_traveller = number_of_travellers
        self.travel_class = travel_class

    def show(self):
        print("~~~~~~~~~~~~~~~~~~")
        print("Booking Data:")
        print("FROM:", self.from_location, "TO:", self.to_location)
        print("~~~~~~~~~~~~~~~~~~\n")

booking1 = Flightbooking("New Delhi", "Chandigarh", "18th June, 2024", 2, "Economy")
print("booking1:", booking1)
print("booking1 data:")
# print(vars(booking1))
booking1.show()

booking2 = Flightbooking("Chennai", "Bengaluru", "18th June, 2024", 1, "Premium")
print("booking2:", booking2)
print("booking2 data:")
# print(vars(booking2))
booking2.show()

# Throw Error
booking3 = Flightbooking()
booking3.show()
print("1")
print(vars(booking3))



