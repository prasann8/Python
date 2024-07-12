"""
    Code 3 objects
    1. Dish : name , price ,rating
    2. Menu : name ,number_of_dishes, dishes
    3. Restaurant : name, phone, email, address, operating_hours, rating, menu
"""


from Session9 import Dish
from Session9A import Menu

class restaurant:

    def __init__(self,name="NA", phone="NA", email = "NA", address = "NA",operating_hours = "10:00 to 23:00", rating = 2.5, menu = "None"):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operating_hours = operating_hours
        self.rating = rating
        self.menu = menu


    def show(self):
        print("RESTAURANT")
        print("~~~~~~~~~~~~~~~~~~")
        print("RESTAURANT IS: {} | {} | {}".format(self.name, self.phone, self.email))
        print("ADDRESS IS: {} | {} | {}".format(self.address, self.operating_hours, self.rating))
        print("~~~~~~~~~~~~~~~~~~\n")

        self.menu.show()

dishes = [
    Dish(),
    Dish("Dal Makhni", 250, 4.5),
    Dish("Paneer Masala", 350,  4.5)
]

menu = Menu(
    name = "Indian Veggie Delight",
    number_of_dishes = len(dishes),
    menu_dishes = dishes
)

restaurant = restaurant(name = "Ludhiana Veggie Delight",
                        phone = "+91 91579-11112",
                        email = "veggie@abc.com",
                        address = "Krishna Nagar",
                        rating = 4.5,
                        menu = menu
                        )