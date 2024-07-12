# LINEAR SEARCH


instagram_user_names = ["john.j", "fionna", "harry_h", "leo.32", "ben_a"]
names = ["John Jackson", "Fionna Flynn", "Harrison", "Leonardo", "Bennethan"]

user_name = input("Enter username")

index = 0

"""
if user_name == instagram_user_names[index]:
    print("NAME IS", names[index])
elif user_name == instagram_user_names[index + 1]:
    
      print("NAME IS", names[index])
else:
    print("Cannot find User")

"""

"""
while index < len(instagram_user_names):
    if user_name == instagram_user_names[index]:
        print("Name is ", names[index])
        break

    index += 1
"""
flag = False

for index in range(0, len(instagram_user_names)):
    if user_name == instagram_user_names[index]:
        print("Name is ", names[index])
        flag = True
        break

if flag == False:
    print(user_name,"Not found!")


