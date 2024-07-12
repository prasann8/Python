# MULTI VALUE CONTAINER
friends = ["john", "jennis", "jim", "jack", "Joe"]
print(friends, type(friends), id(friends))

print(friends, type(friends), id(friends))

print(friends[0], type(friends[0]), id(friends[0]))
print(friends[1], type(friends[1]), id(friends[1]))
print(friends[2], type(friends[2]), id(friends[2]))
print(friends[3], type(friends[3]), id(friends[3]))
print(friends[4], type(friends[4]), id(friends[4]))

# Lets change
friends[0] = "johnnathon"
print(friends, type(friends), id(friends))