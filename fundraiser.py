def money_raised(numtickets):
    ticket = 5
    prize = 50
    total = numtickets * ticket - prize
    return total

print(money_raised(50))