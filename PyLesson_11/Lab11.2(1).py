import random
class User:
    #Constructor
    def __int__ (self, fName, lName, avat=""):
        self.firstname = fName
        self.lastname = lName
        self.avatar = avat
        self.userID = random.randint(0,1000000)
    #Modifier
    def setvalues(self,newf,newl,newa):
        self.firstname = newf
        self.lastname = newl
        self.avatar = newa
    #Accessors
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def getAvatar(self):
        return self.avatar
    def getUserID(self):
        self.userID = random.randint(0,1000000)
        return self.UserID
    
def main():
    firstname = input("Please enter your firstname: ")
    lastname = input("Please enter your lastname: ")
    answer = input("Would you like to use a public avatar? y or n")
    if answer == "y":
        User1 = User(firstname,lastname)
    if answer == "n":
        firstname = input("Please enter your Avatar's Firstname: ")
        lastname = input("Please enter your Avatar's Lastname: ")
        User1 = User(firstname,lastname,avatar)
def __str__(self):
    return"Customer Info...\nFirst Name: " + self.firstname + "\nLast Name: " + self.lastname + "\nAvatar: " + self.avatar + "\nUser ID#: " + str(self.userID)
main()
