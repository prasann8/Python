"""
     Another Brick in wall
     who placed the last brick
     Mr. John ->
"""



number = int(input("Enter number of bricks you want to build with:"))


index = 1
for index in range(1,number+1):
    jack = index
    joe = index*2

    bricks = jack + joe
    if bricks < number:
        break
        print("Number of bricks placed by john:", john)
        print("Number of bricks placed by joe:", joe)