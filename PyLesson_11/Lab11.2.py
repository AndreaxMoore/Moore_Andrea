import math
class Distance:
    def __int__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def setDistance(self,newx1,newy1,newx2,newy2):
        self.x1 = newx1
        self.y1 = newy1
        self.x2 = newx2
        self.y2 = newy2
    def getDistance(self):
        return self.Distance
        Distance = Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
def main(x1,y1,x2,y2):
    x1 = input("Enter first x coordinate: ")
    y1 = input("Enter first y coordinate: ")
    x2 = input("Enter second x coordinate: ")
    y2 = input("Enter second y coordinate: ")

    newDistance = Distance(x1,y1,x2,y2)

    print("distance = ",newDistance.getDistance())

    newDistance.setDistance("25.35")

    print("distance = ",newDistance.getDistance())

main(x1,y1,x2,y2)
