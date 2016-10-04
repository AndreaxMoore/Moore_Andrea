
def calcSurf(s):
    return(6*(s*s))
def display(s):
    print("The surface area of a cube whose sides are",s,"in length is","{:0.5f}".format(calcSurf(s)),".")
side = float(input("Please enter the length of the sides: "))
display(side)
