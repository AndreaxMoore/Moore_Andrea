word = input("Please enter a word: ")
def rightTri():
    for i in range(len(word),0,-1):
        print(word[i:len(word)])
rightTri()

