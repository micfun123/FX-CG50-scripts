nums = []

while True:
    inp = input("Enter a number: ")
    #if inp is a string break
    if inp == "" : break
    value = float(inp)
    nums.append(value)

average = sum(nums) / len(nums)
#2 decimal places
print("Average: {:.3f}".format(average))