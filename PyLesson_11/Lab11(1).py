class MilesPerHour:
    #Constructor
    def __init__(self, dis="", h="", m="",M = 0):
        self.distance = dis
        self.hours = h
        self.minutes = m
        self.mph = M
    #Modifier
    def setvalues(self, newdis,newh,newm,newM):
        self.distance = newdis
        self.hours = newh
        self.minutes = newm
        self.mph = newM
    #Accessors
    def getDistance(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMinutes(self):
        return self.minutes
    def getMph(self):
        self.mph= self.distance/(self.hours + self.minutes/60)
        return self.mph
def main():
    distance = int(input("Enter distance: "))
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))

    user1 = MilesPerHour(distance, hours, minutes)

    print(user1.getDistance(),"miles in", user1.getHours(),"hours and",user1.getMinutes(),"minutes =",user1.getMph(),"mph.")    

    user1.setvalues(35,5,0,0)
 

    print(user1.getDistance(),"miles in", user1.getHours(),"hours and",user1.getMinutes(),"minutes =",user1.getMph(),"mph.")

main()
