number = int(input("Please enter a number: "))
num = number
rev = 0

def getReverse():
    global num,rev
    while num > 0:
        rev =(rev*10)+ (num%10)
        num = int(num/10)
getReverse()
print(number,"reversed is",rev)
             
