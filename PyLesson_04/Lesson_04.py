print("{:?>24}".format("test"))

def printf(number, word):
    print("{:_^8}\t{:>10}".format(number,word))

word = "hap"
number = 56

printf(number, word)

word = "jui"
number = 98

printf(number, word)


