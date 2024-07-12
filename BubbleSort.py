nums = []

print("Enter numbers to add to the list. Type 'done' when you are finished.")

while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == 'done':
        break

    number = int(user_input)
    nums.append(number)

print("The numbers in the list are:", nums)

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


sort(nums)
print("Numbers after sorting are:", nums)
