file = open("customer.csv", "r")
# data = file.read()

lines = file.readlines()
print("File Data:")

for i in range(len(lines)):
    print(lines[i])