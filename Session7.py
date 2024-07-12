def print_number(number):
    print(number)

    if number < 10:
        print_number(number+1) # function calling itself again and again  # Results in recursion error


print_number(1)
