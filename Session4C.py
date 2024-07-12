# Condition: You can apply promo code iff  min amount is 500

promo_code = "GET 200"
amount = float(input("Enter your amount:"))

min_amount = 500



if amount > min_amount:
    print("You can apply promo code", promo_code)
    amount = amount - 200
    print("Promo code applied successfully. Please pay", amount)
else:
    print("You cannot apply promocode", promo_code)
    print("Add items worth ", (min_amount-amount), "more")