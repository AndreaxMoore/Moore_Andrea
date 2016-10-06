side = float(input("Please enter the length of the sides: "))
area = 0

def calcSurf():
    global area,side
    area = 6*(side*side)
def display():
    print("The surface area of a cube whose sides are",side,"in length is","{:0.5f}".format(area),".")

calcSurf()
display()

