word = input("Please enter a word: ")

def ReverseTri():
    for i in range(len(word),0,-1):
        print(word[0:i])
ReverseTri()


