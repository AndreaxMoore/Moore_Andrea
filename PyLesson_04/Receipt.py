def printf(food,price):
    print("*"+"{:>15} ........{:10.2f}".format(food,price))
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
printf(food1,price1)
printf(food2,price2)
printf(food3,price3)
print("\n")

price = price1+price2+price3
printf("Subtotal:",price)

tax = price*.07
printf("Tax:",tax)

total = price+tax
printf("Total:",total)

print("________________________________________")
print(" * Thank you for your support *")
