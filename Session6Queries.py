floors = 10

floor = 0

floor_to_go = int(input("Enter Floor number to go:"))

while floor <= floors:
    print("At floor number:",floor)

    if floor_to_go == floor:
        print("You have reached at floor number:",floor)
        break

    floor += 1



for floor in range(0,10):
    print("At floor number:", floor)

    if floor_to_go == floor:
        print("You have reached at floor number:", floor)
        break

