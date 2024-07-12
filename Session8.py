# OOPS : Object oriented programming language

"""
Principle of OOPS :
1. Think of an object
2. Create its class
3. Using class create real object
"""

"""

Principle of OOPS:
1. Think of object

Adhaar: download, update, verify, generate VID
"""

# 2. Create class of object
# Below class represents the object. It is discription of object
class FlightBooking:
    pass

# 3. Create the real object from class in memory
# Below is : Object Construction Statement

booking1 = FlightBooking()

# Booking1 is a reference variable . FlightBooking() represents object creation

print(booking1)
print(vars(booking1))

print(id(booking1))
print(hex(id(booking1)))

booking2 = FlightBooking()

# reference copy operation
booking3 = booking1

# Operations on object
# 1. Write Operation

booking1.from_location = "New Delhi"
booking1.to_location = "Goa"
booking1.travel_date = "15th July, 2024"
booking1.number_of_travellers = 3
booking1.travel_class = "Economy"

booking2.from_location = "Chennai"
booking2.to_location = "Bangalore"
booking2.travel_date = "25th July, 2024"
booking2.number_of_travellers = 1
booking2.travel_class = "Premium"
booking2.booked_at = "12:50 17th June, 2024"

# 2. Update Operation
booking3.number_of_travellers = 2
booking3.from_location = "Chandigarh"

# 3. Read Operation
print("Booking1 data:")
print(vars(booking1))
print("FROM:", booking1.from_location, "TO:", booking1.to_location)

print("Booking2 data:")
print(vars(booking2))
print("FROM:", booking2.from_location, "TO:", booking2.to_location)

# 4. Delete Operation
del booking1.travel_class
print("Booking1 data after delete:")
print(vars(booking1))

del booking1

print("Booking3 data:")
print(vars(booking3))
print("FROM:", booking3.from_location, "TO:", booking3.to_location)

















