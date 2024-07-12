# Bitwise Operators
# 7, |, ^

num1 = 10
num2 = 8

result1 = num1 and num2
result2 = num1 | num2
result3 = num1 ^ num2

print(result1)
print(result2)
print(result3)

# Shift Operators
# >>, <<

num1 = 8
num2 = 2

result1 = num1 >> num2 # 8// 2 power 2
print("Result1 right shift is :",result1)

number = result1 << num2
print("number is ",number)
result2 = num1 << num2 # 8*2 power 2
print("Result1 left shift is :",result2)



number = -13
result = number >> 2
print(number, ">> 2 is", result)
