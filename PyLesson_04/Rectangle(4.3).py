length = float(input("Please enter the length of your rectangle: "))
width = float(input("Please enter the width of your rectangle: "))
perim = 0

def calcPerim():
   global perim,length,width
   perim =((length*2)+(width*2))

def display():
    print("Your rectangle is","{:0.5f}".format(perim),"ft around.")

calcPerim()
display()
