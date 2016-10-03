def calcPerim(le,wi):
   global perim
   perim = float((le*2)+(wi*2))

def display(prm):
    print("Your rectangle is","{:0.5f}".format(prm),"sq ft around.")

length = float(input("Please enter the length of your rectangle: "))
width = float(input("Please enter the width of your rectangle: "))

calcPerim(length,width)
display(perim)
