number = int(input("Please enter your starting number: "))
size = int(input("Please enter your sequence size: "))

seq = []
output = ""
for i in range(0,size):
    if i == 0 or i == 1:
        seq.append(number)
    else:
        seq.append(seq[i-1]+seq[i-2]) 
    output += str(seq[i])+ " "
print(output)


