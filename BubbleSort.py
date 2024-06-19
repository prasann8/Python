numbers = []

print("Enter numbers to add to the list. Type 'done' when you are finished.")

while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == 'done':
        break

    number = int(user_input)
    numbers.append(number)

print("The numbers in the list are:", numbers)

def sort(numbers):
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp


sort(numbers)
print("Numbers after sorting are:",numbers)