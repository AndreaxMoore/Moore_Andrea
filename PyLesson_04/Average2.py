num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))
mean = 0

def average():
    global mean,num1,num2,num3
    mean = (num1+num2+num3)/3

def display():
    print("The average of",num1,",",num2,",",num3,",is","{:0.5f}".format(mean),".")



average()
display()

