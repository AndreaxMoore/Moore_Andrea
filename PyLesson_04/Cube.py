side = float(input("Please enter the length of the sides: "))
def calcSurf():
    return(6*(side*side))
def display():
    print("The surface area of a cube whose sides are",side,"in length is","{:0.5f}".format(calcSurf()),".")
display()
