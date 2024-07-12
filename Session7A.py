def get_max(data, length):

    if len(data) == 1:
        return data[0]

    else:
        previous = get_max(data, length-1)
        current = data[length-1]

        if previous > current:
            return previous
        else:
            return current

numbers = [10, 20]

result = get_max(numbers, len(numbers))
print("Max is:", result)




# numbers = [1, 3, 5]
#
# max = numbers[0]
#
# for index in range(1,len(numbers)):
#     if numbers[index] > max:
#         max = numbers[index]