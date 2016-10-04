
def calcArea(r):
    return(3.14*(r**2))
def display(r):
    print("The area of a circle with a radius of",r,"is","{:0.5f}".format(calcArea(r)),".")
radius = float(input("Please enter the radius of the circle: "))
display(radius)
