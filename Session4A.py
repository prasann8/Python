# Conditional Operators
# ==, !=, >, <, >=, <=

cab_fare = 500
e_wallet = 500

result = e_wallet >= cab_fare

print("Can I book the cab?", result)
print(type(result))


email = input("Enter email")
password = input("Enter password")

print("Is login successful")
result = (email == "john@example.com") or (password == "john123")
print(result)

otp = 3027
user_otp = int(input("Enter OTP received"))
print("Is OTP correct??", otp == user_otp)


# Membership Testing
# is, is not

a = 10
b = 10

print(a == b)
print(a is b)
print(a is not b)