
def calcSurf(s):
    return(6*(side*side))
def display(s):
    print("The surface area of a cube whose sides are",side,"in length is","{:0.5f}".format(calcSurf(s)),".")
side = float(input("Please enter the length of the sides: "))
display(side)
