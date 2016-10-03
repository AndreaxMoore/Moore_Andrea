def average(n,nu,num):
    global mean
    mean = float((n+nu+num)/3)
def display(ave):
    print("The average of",num1,",",num2,",",num3,",is","{:0.5f}".format(ave),".")
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))

average(num1,num2,num3)
display(mean)
