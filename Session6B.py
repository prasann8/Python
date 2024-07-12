def square(num):
    print("1. num is:", num ,id(num))
    num = num * num # num *= num
    print("2. num is :",num, id(num))

# Function exists in memory
# print("square",square)  Gives hashcode and name of function

number = 10
print("A. number is:", number, id(number))
square(number)
print("B. number is :",number, id(number))
