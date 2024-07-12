"""
    Code 3 objects
    1. Dish : name , price ,rating
    2. Menu : name ,number_of_dishes, dishes
    3. Restaurant : name, phone, email, address, operating_hours, rating, menu
"""

# Class for the object dish
class Dish:

    # Parameterized Constructor, with default values of arguments passed into it
    def __init__(self, name="", price=0, rating=1.5):
        # print(">>Self is: {}".format(self))
        self.name = name  # Copy the contents of name(input to constructor) into self.name (Attribute of object )
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Dish: {}, {}, {}".format(self.name, self.price, self.rating))
        print("~~~~~~~~~~~~~~~~~~~~~~~\n")

"""

dish1 = dish()
print("Dish1:", hex(id(dish1)))

dish2 = dish("Dal Makhni", 250, 4.5)
print("Dish2:", hex(id(dish2)))

dish3 = dish("Paneer Masala", 350, 4.5)
print("Dish3:", hex(id(dish3)))

"""

"""
# List of Dishes
dishes = [Dish(),
          Dish("Dal Makhni", 250, 4.5),
          Dish("Paneer Masala", 350, 4.5)
          ]

for index in range(len(dishes)):
    dishes[index].show()

"""