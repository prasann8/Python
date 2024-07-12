def add(num1, num2, num3):
    result = num1 + num2 + num3
    print("result is: {}".format(result))


# Same thing
add(10, 20, 30)
add(num1=10, num2=20, num3=30)

# Default arguments/Inputs
def square(num=5):
    result = num * num
    print("result is: {}".format(result))

square()
square(3)
square(num=9)


# default values uses right to left convention
# def subtract(num1=10, num2): error
def subtract(num1, num2=10):
    result = num1 - num2
    print("result is: {}".format(result))

subtract(num1=10)