"""
    Customer : name, phone, email, address, gender, age
    Dish : Name, type, spicy, price, veg/non veg,
    Order : time, place, dishes, order_value, order_number,

    1 Customer can place many orders
    1 Order can have many dishes

"""


class Dish:
    def __init__(self, name="", origin="INDIAN", spicy="NORMAL", price=0, type="VEG"):
        self.name = name
        self.origin = origin
        self.spicy = spicy
        self.price = price
        self.type = type

    def show(self):
        print("~~~~~~~~~~~~~DISHES~~~~~~~~~~~~~~~~~~")
        print("{} | {} | {} | {} | {}".format(self.name, self.origin, self.spicy, self.price, self.type))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
