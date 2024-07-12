"""
   ZOMATO : 20% off
          : min value : 300

   BINGO : 50% off
         : min value : 500
         : max discount : 100
"""

# PEP (Python enhancement Proposal)

promo_code = input("Enter Promocode :")
amount = float(input("Enter Amount :"))


if promo_code == "ZOMATO":
    print("ZOMATO can be applied....")


    if amount > 300:
        discount = 0.2 * amount
        print("ZOMATO applied successfully. You got a discount of ",discount)
        print("You can pay", amount - discount)
    else:
        print("Amount is less . Please add items worth ", (300 - amount), "more!!!")


elif promo_code == "BINGO":
    print("BINGO can be applied...")

    if amount > 500:
        discount = 0.2 * amount

        if discount > 100:
            discount = 100


            print("BINGO Applied Successfully. You got a discount of", discount)
            amount -= discount
            amount = amount + 0.18 * amount
            amount += 16.5
            print("You can pay : \u090f", amount - discount)
        else:
            print("Amount is less . Please add items worth ", (300 - amount), "more!!!")

 # Indian Rupee :


else:
    print("Invalid Promocode")