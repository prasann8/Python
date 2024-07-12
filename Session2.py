numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers), id(numbers))
print(numbers[1], type(numbers[1]), id(numbers[1]))

# REFERENCE COPY Operation
my_numbers = numbers
print(my_numbers, type(my_numbers), id(my_numbers))

numbers[2] = 1122

print(numbers[2])
print(my_numbers[2])

del numbers
print(my_numbers)
