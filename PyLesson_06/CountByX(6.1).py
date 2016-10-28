num1 = int(input("Please enter a number1: "))
num2 = int(input("Please enter a number2: "))
output = ""
for i in range(num1,num2+1,2):
    output = output + str(i)+ " "
print(output)
