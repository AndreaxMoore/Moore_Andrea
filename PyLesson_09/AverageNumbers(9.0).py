numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,10):
    numbers[i]>1 and numbers[i]<100
print("Numbers...")

output = ""
for i in numbers:
    output += str(i) + " "
print(output)
print("\n")


def average(nums):
    average = 0
    for i in nums:
        average += i
    return str(average/i)
print("The average of the above number is...", average(numbers))
