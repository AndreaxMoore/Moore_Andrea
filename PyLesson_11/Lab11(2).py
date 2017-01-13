import math
class Distance:
    #Constructor
    def __init__(self,x1="",y1="",x2="",y2=""):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0
    #Modifier
    def setvalues(self,newx1,newy1,newx2,newy2):
        self.xOne = newx1
        self.yOne = newy1
        self.xTwo = newx2
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

    newDistance.setvalues(5,4,1,1)
 

    print("distance = ",newDistance.getDistance())

main()


  
