from Session12B import Dish
from Session12C import Order
from Session12D import Customer

dish_menu = [
    Dish(name="Dal Makhni", origin="Indian", spicy="Normal", price=250, type="VEG"),
    Dish(name="Paneer Makhni", origin="Indian", spicy="Normal", price=400, type="VEG"),
    Dish(name="Butter Chiken", origin="Indian", spicy="Spicy", price=750, type="NON-VEG"),
    Dish(name="Burger", origin="American", spicy="Spicy", price=50, type="VEG"),
    Dish(name="Pizza", origin="Italian", spicy="Normal", price=700, type="NON-VEG")
        ]

customer1 = Customer(name="John", phone="9877889877", email="john@example.com", gender="Male", address="Ludhiana", age=21)
customer2 = Customer(name="Jia", phone="987786669877", email="jia@example.com", gender="Female", address="Pathankot", age=12)

# Hard Coding: We as developer are linking objects
# order1 = Order(oid=1, dishes=[dish_menu[0], dish_menu[2]], customer=customer1, total=dish_menu[0].price+dish_menu[2].price)
# order2 = Order(oid=2, dishes=[dish_menu[2], dish_menu[3], dish_menu[4]], customer=customer2, total=dish_menu[2].price+dish_menu[3].price+dish_menu[4].price)

order1 = Order(oid=1)
order1.link_customer(customer = customer1)
order1.link_dishes([dish_menu[0], dish_menu[2]])

order2 = Order(oid=2)
order2.link_customer(customer = customer2)
order2.link_dishes(dishes=[dish_menu[2], dish_menu[3], dish_menu[4]])

order1.show()
order2.show()