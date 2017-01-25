numbers = []
import random
for i in range(0,10):
    numbers.append(random.randint(1,100))
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
    return str(average/10)
print("The average of the above number is...", average(numbers))
