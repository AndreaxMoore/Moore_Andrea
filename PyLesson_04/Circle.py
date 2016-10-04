
def calcArea(radius):
    return(3.14*(r**2))
def display(radius):
    print("The area of a circle with a radius of",r,"is","{:0.5f}".format(calcArea(radius)),".")
r = float(input("Please enter the radius of the circle: "))
display(r)
