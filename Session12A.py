"""
    Customer : name, phone, email, address, gender, age
    Dish : Name, type, spicy, price, veg/non veg,
    Order : time, place, dishes, order_value, order_number,

    1 Customer can place many orders
    1 Order can have many dishes

"""

def bubble_sort(data):
    for i in range(len(data)-1):
        print("i is:", i)
        for j in range(len(data)-i-1):
            print(j, end=" ")

            if data[j].price > data[j+1].price:
                # print("swapping {} with {}".format(data[j], data[j+1]))
                data[j], data[j+1] = data[j+1], data[j]

        print()




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

# List of dishes

dish1 = Dish(name="Dal Makhni", origin="Indian", spicy="Normal", price=250, type="VEG")
dish2 = Dish(name="Paneer Makhni", origin="Indian", spicy="Normal", price=400, type="VEG")
dish3 = Dish(name="Butter Chiken", origin="Indian", spicy="Spicy", price=750, type="NON-VEG")
dish4 = Dish(name="Burger", origin="American", spicy="Spicy", price=50, type="VEG")
dish5 = Dish(name="Pizza", origin="Italian", spicy="Normal", price=700, type="NON-VEG")

dishes = [dish1, dish2, dish3, dish4, dish5]


print("DISHES")
for dish in dishes:
    dish.show()

bubble_sort(dishes)

print("SORTED DISHES:")
for dish in dishes:
    dish.show()
"""

class Order:
    def __init__(self, time, place, dishes, order_value, order_number):
        self.time = time
        self.place = place
        self.dishes = dishes
        self.order_value = order_value
        self.order_number = order_number

    def add_order_details(self):
        self.time = input("Enter time of order:")
        self.place = input("Enter place:")
 

"""