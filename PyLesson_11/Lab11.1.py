class Car:
    #Constructor
    def __init__ (self,p,i,e,t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
    #Modifier
    def setp(self,newp):
        self.paint = newp
    def seti(self,newi):
        self.interior = newi
    def sete(self,newe):
        self.engine = newe
    def sett(self,newt):
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
    interior = input("Please enter the interior: ")
    engine = input("Please enter the engine: ")
    tires = input("Please enter the tires: ")

    Car1 = Car(paint,interior,engine,tires)

    print("Your vehicle is ready......\nPaint: ",Car1.getPaint(),"\nInterior: ",Car1.getInterior(),"\nEngine: ",Car1.getEngine(),"\nTires: ",Car1.getTires())
    print("\"\"\"")
   
main()      
