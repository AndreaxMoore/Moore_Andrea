def calcPerim(le,wi):
    return(2*(le+wi))
def display(le,wi):
    print("Your rectangle is","{:0.5f}".format(calcPerim(le,wi)),"ft around.")
length = float(input("Please enter the length of your rectangle: "))
width = float(input("Please enter the width of your rectangle: "))

display(length,width)
