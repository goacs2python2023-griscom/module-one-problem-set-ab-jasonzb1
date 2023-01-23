import random

def sumGame():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total = roll1 + roll2
    if total == 6 or total == 7 or total == 8:
        return "win"
    else:
        return "lose"

print(sumGame())