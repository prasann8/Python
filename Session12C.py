class Order:
    def __init__(self, oid=0, dishes=None, customer=None, total=0):
        self.oid = oid
        self.dishes = dishes
        self.customer = customer
        self.total = total

    def show(self):
        print("~~~~~~~~~~~~~ORDER~~~~~~~~~~~~~~~~~~")
        print("{} | {}".format(self.oid, self.total))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("------------Order placed By--------------")
        self.customer.show()

        print("------------Order Dishes----------------")
        for dish in self.dishes:
            dish.show()
        print("----------------------------------------")

    def link_dishes(self, dishes):
        self.dishes = dishes

        for dish in self.dishes:
            self.total += dish.price

    def link_customer(self, customer):
        self.customer = customer