class Human:
    #Constructor
    def __init__(self,h="",e="",s=""):
        self.hair = h
        self.eyes = e
        self.skin = s
    #Modifier
    def setvalues(self,newh,newe,news):
        self.hair = newh
        self.eyes = newe
        self.skin = news
    #Accessors
    def getHair(self):
        return self.hair
    def getEyes(self):
        return self.eyes
    def getSkin(self):
        return self.skin
def main():
    hair = input("Please enter the hair color: ")
    eyes = input("Please enter the eyes color: ")
    skin = input("Please enter the skin color: ")

    Human1 = Human(hair,eyes,skin)

    print("My info...\nHair: ",Human1.getHair(),"\nEyes: ",Human1.getEyes(),"\nSkin: ",Human1.getSkin())

    Human1.setvalues("blone","blue","white")

    print("Friend's info...\nHair :",Human1.getHair(),"\nEyes: ",Human1.getEyes(),"\nSkin: ",Human1.getSkin())
main()
