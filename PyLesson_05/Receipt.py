food1 = input("Please enter item:")
price1 = float(input("Please enter price:"))
food2 = input("Please enter item:")
price2 = float(input("Please enter price:"))
food3 = input("Please enter item:")
price3 = float(input("Please enter price:"))
food4 = input("Please enter item:")
price4 = float(input("Please enter price:"))


Subtotal = (price1 + price2 + price3 + price4 )
if Subtotal > 2000:
    discount = Subtotal*0.15
if Subtotal < 2000:
    discount = 0
tax = Subtotal*0.17
Total = Subtotal - discount + tax

def Receipt(num1,num2):
    print("{:<18}.......${:0.2f}".format(num1,num2))

print("<<<<<<<<<<< Reciept >>>>>>>>>>>>>>")

Receipt(food1, price1)
Receipt(food2, price2)
Receipt(food3, price3)
Receipt(food4, price4)
print("\n")
Receipt("Subtotal:",Subtotal)
Receipt("Discount:",discount)
Receipt("Total:",Total)

print("___________________________________")
print("* Thank you *")



