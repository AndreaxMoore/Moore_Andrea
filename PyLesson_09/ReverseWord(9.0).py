myList = ["Hello", "How", "Are", "You", "Today"]

print("In Order...")
output = ""
for i in myList:
    output +=  i + " "
print(output)
print("\n")

print("Reversed")

def reverse(words):
    output = ""
    for i in range(len(words)-1,-1,-1):
        output+=(words[i])+ " "
    print(output)

reverse(myList)      
      
