import random

player = random.randint(1,6)
computer = random.randint(1,6)

def rollDice():
    global player,computer
    if player > computer:
        return "player"
    if computer > player:
        return "computer"
winner = rollDice()
print("You rolled a",player)
print("Computer rolled a",computer)
print("The winner is",winner)

