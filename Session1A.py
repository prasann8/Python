# CREATE STATEMENT
promo_Code1 = "ZOMATO40"
print(promo_Code1, type(promo_Code1), id(promo_Code1))

# REFERENCE COPY OPERATION
promo_Code2 = promo_Code1
print(promo_Code2, type(promo_Code2), id(promo_Code2))

# DELETE
del promo_Code1
print(promo_Code2, type(promo_Code2), id(promo_Code2))
print(promo_Code1, type(promo_Code1), id(promo_Code1))
