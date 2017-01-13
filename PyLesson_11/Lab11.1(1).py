class Car:
    #Constructor
    def __init__ (self,p="",i="",e="",t=""):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
    #Modifier
    def setvalues(self,newp,newi,newe,newt):
        self.paint = newp
        self.interior = newi
        self.engine = newe
        self.tires = newt
    #Accessors
    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires
    
def main():
    paint = input("Please enter the color of the paint: ")
    interior = input("Please enter the color of the interior: ")
    engine = input("Please enter the engine: ")
    tires = input("Please enter the tires: ")

    Car1 = Car(paint,interior,engine,tires)

    print("Your vehicle is ready......\nPaint: ",Car1.getPaint(),"\nInterior: ",Car1.getInterior(),"\nEngine: ",Car1.getEngine(),"\nTires: ",Car1.getTires())
    print("\"\"\"")

    Car1.setvalues("red","Corinthian leather","5 Litre v8 507hp","20\" Priellis")

    print("Your vehicle is ready......\nPaint: ",Car1.getPaint(),"\nInterior: ",Car1.getInterior(),"\nEngine: ",Car1.getEngine(),"\nTires: ",Car1.getTires())
    print("\"\"\"")
main()      
