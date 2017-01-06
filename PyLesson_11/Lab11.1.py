class MilesPerHour:
    #Constructor
    def __int__(self, dis="", h="", m=""):
        self.distance = dis
        self.hours = h
        self.minutes = m
        self.mph = M
    #Modifier
    def setdis(self, newdis):
        self.distance = newdis
    def seth(self,newh):
        self.hours = newh
    def setm(self,newm):
        self.minutes = newm
    def setM(self,newM):
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

    print(user1.getDistance(),"miles in", user1.getHours(),"hours and",user1.getMinutes(),"minutes =",user1.getM()>"mph.")    

    user1.setdis("5")
    user1.seth("1")
    user1.setm("0")

    print(user1.getDistance(),"miles in", user1.getHours(),"hours and",user1.getMinutes(),"minutes =",user1.getM()>"mph.")

main()
