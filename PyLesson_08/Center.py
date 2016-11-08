word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
word3 = input("Please enter the third word: ")

def replace(word):
    if len(word) >= 20:
        return word
    else:
        return replace(" " + word + " ")

print(replace(word1))
print(replace(word2))
print(replace(word3))
