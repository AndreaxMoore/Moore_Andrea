def calcArea(radius):
    global area
    area = float(3.14*(r**2))
def display(ra):
    print("The area of a circle with a radius of",r,"is","{:0.5f}".format(ra),".")
r = float(input("Please enter the radius of the circle: "))

calcArea(r)
display(area)
