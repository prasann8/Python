# Dictionary
# The final and most important
friends = {"jj": "john", "je": "jennie", "ji": "jim"}
print(friends, type(friends), id(friends))
print(friends["jj"])

my_friends = {1: "Call", 2: "Message", 3: "Get a Callback"}

instagram = {
    "K_ISHANT": {"auribises", "john", "jennis", "jim", "fionna"},
    "auribises": {"jim", "majj", "jennis"}
}

print(instagram["K_ISHANT"])
print(instagram["auribises"])

print(instagram["K_ISHANT"] & instagram["auribises"])
