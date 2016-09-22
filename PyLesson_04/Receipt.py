def printf(food,space,price):
    print("*"+"{:>15}{:.<9}{:10.2f}".format(food,space,price))
food1 = input("Please enter item 1: ")
price1 = float(input("Please enter the price: "))
space = " "

food2 = input("Please enter item 2: ")
price2 = float(input("Please enter the price: "))
space = " "

food3 = input("Please enter item 3: ")
price3 = float(input("Please enter the price: "))
space = " "


print("\n")
print("<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>")
print("\n")
printf(food1,space,price1)
printf(food2,space,price2)
printf(food3,space,price3)
print("\n")

price = price1+price2+price3
printf("Subtotal:",space,price)

tax = price*.07
printf("Tax:",space,tax)

total = price+tax
printf("Total:",space,total)

print("________________________________________")
print(" * Thank you for your support *")
