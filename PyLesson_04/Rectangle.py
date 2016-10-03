length = float(input("Please enter the length of your rectangle: "))
width = float(input("Please enter the width of your rectangle: "))
height = float(input("Please enter the height of your rectangle: "))
def calcPerim():
    return(4*(length+width+height))
def display():
    print("Your rectangle is","{:0.5f}".format(calcPerim()),"sq ft around.")
display()
