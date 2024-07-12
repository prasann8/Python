# OPERATORS
# Arithmetic Operations
# +, -, *, **, /, //, %

product_price = 200
gst_tax = 0.18

price_to_pay = product_price + gst_tax*product_price

print(price_to_pay, type(price_to_pay), id(price_to_pay))

number = 10

result = number/3
print("Result is", result)

base = 2
result = base ** 3
print("Result is", result)

# Remainder Operation
bucketsize = 7
hashcode = 120 % 7
print("Hashcode of 120 is", hashcode)


# Assignment OPERATION
# =, +=, -=, *=, **=, /=, //=, %=

Age = 20
Age +=10  #Shorthand Operato add and assign

Age %=3
Age -=1
print(Age)

# Increment and Decrement
qty = 1
qty += 1
qty -= 1
qty += 5
qty -= 1
qty **= 2
print("Quantity is ", qty)








