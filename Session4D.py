# PromoCode : ZOMATO
# Condition1 : more than 149
# Condition2: 50% off upto 150

amount = float(input("Enter amount"))

promo_code = input("Enter PROMOCODE")
if promo_code == "ZOMATO":
    print("Promocode Exists")
    if amount > 249:
        print("Promocode applied")

        discount = 0.5 * amount

        if discount >= 150:
            discount = 150
        amount -= discount
        print("Please Pay", amount)
        print("Discount", discount)

    else:
        print("Amount is low...")

else:
    print(" Promocode Invalid ")
