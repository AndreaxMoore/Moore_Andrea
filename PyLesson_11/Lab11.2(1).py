import random
class User:
    #Constructor
    def __init__ (self, fName="", lName="", avat=""):
        self.firstname = fName
        self.lastname = lName
        self.avatar = avat
        self.userID = random.randint(0,1000000)
    #Modifier
    def setavat(self,newa):
        self.avatar = newa
    #Accessors
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def getAvatar(self):
        return self.avatar
    def getUserID(self):
        return self.userID

def __str__(self):
    return"Customer Info...\nFirst Name: " + self.firstname + \
                          "\nLast Name: " + self.lastname + \
                          "\nAvatar: " + self.avatar + \
                          "\nUser ID#: " + str(self.userID)   
def main():
    firstname = input("Please enter your firstname: ")
    lastname = input("Please enter your lastname: ")
    avat = input("Would you like to use a public avatar? y or n")
    if avat == "n":
        user1 = User(firstname,lastname)
    if avat == "y":
        avatar = input("Please enter your Avatar's name: ")
        user1 = User(firstname,lastname,avatar)
    print(user1.__str__())
main()


