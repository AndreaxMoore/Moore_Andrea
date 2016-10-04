def average(n1,n2,n3):
    return((n1+n2+n3)/3)
def display(n1,n2,n3):
    print("The average of",n1,",",n2,",",n3,",is","{:0.5f}".format(average(n1,n2,n3)),".")
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))

display(num1,num2,num3)
