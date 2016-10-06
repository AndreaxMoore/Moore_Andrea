def calcSurf(s):
    global area
    area = float(6*(s*s))
def display(are):
    print("The surface area of a cube whose sides are",side,"in length is","{:0.5f}".format(are),".")
side = float(input("Please enter the length of the sides: "))

calcSurf(side)
display(area)

