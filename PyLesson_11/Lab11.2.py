import math
class Distance:
    #Constructor
    def __init__(self,x1,y1,x2,y2,d=0):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = d
    #Modifier
    def setx1(self,newx1):
        self.xOne = newx1
    def sety1(self,newy1):
        self.yOne = newy1
    def setx2(self,newx2):
        self.xTwo = newx2
    def sety2(self,newy2):
        self.yTwo = newy2
    #Accessor
    def getxOne(self):
        return self.xOne
    def getyOne(self):
        return self.yOne
    def getxTwo(self):
        return self.xTwo
    def getyTwo(self):
        return self.yTwo
    def getDistance(self):
        self.Distance = math.sqrt((self.xTwo-self.xOne)*(self.xTwo-self.xOne)+(self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.Distance
def main():
    xOne = int(input("Enter first x coordinate: "))
    yOne = int(input("Enter first y coordinate: "))
    xTwo = int(input("Enter second x coordinate: "))
    yTwo = int(input("Enter second y coordinate: "))

    newDistance = Distance(xOne,yOne,xTwo,yTwo)

    print("distance = ",newDistance.getDistance())

    newDistance.setx1(5)
    newDistance.sety1(4)
    newDistance.setx2(1)
    newDistance.sety2(1)

    print("distance = ",newDistance.getDistance())

main()
