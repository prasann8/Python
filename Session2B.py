john_friends = {"joe", "jim", "fionna", "harry", "kim", "joe"}
sia_friends = {"joe", "george", "fionna", "Leo", "jack", "ben"}

print(john_friends)
print(sia_friends)

mutual_friends = john_friends & sia_friends

print(mutual_friends)

# Will return error . It works on hashing,We cannot get data from set
print(john_friends[0])

