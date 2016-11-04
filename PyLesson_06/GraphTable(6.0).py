size = int(input("Please enter the size of the table: "))
integer = int(input("please enter an integer: "))


for i in range(1, size+1):
    print("{:<4}{:<4}".format(i,i*integer))

