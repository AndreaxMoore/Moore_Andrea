class item:
    def __init__(self,manu,n,c,p):
        self.manufacturer = manu
        self.name = n
        self.category = c
        self.price = p
        self.UPC = random.randint(0,1000000000)

    def setvalues(self,newn,newmanu):
        self.name = newn
        self.manufacturer = newmanu

    def getManufacturer(self):
        return self.manufacturer
    def getName(self):
        return self.name
    def getCategory(self):
        return self.category
    def getPrice(self):
        return self.price
    def getUPC(self):
        return self.UPC
def main():

    name = input("Please enter the name: ")
    manufacturer = input("Please enter the manufacturer: ")
    c = input("Will you be entering category and price information? y or n")
    if c == "n":
        item1 = item(manufacturer,name)
    if c == "y":
        item1 = item(manufacturer,name,category,price)
def __str__(self):
    return"Item info...\nName: " + self.name + \
                       "\nManufacturer: " + self.manufacturer + \
                       "\nCategory: " + self.category + \
                       "\nPrice: " + self.price + \
                       "\nUPC#: " + str(self.UPC)

main()
