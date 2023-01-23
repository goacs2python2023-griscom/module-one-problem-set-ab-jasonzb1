def raceResults(time, first, second, third):
    if time < first:
        return "gold"
    elif time < second:
        return "silver"
    elif time < third:
        return "bronze"
    else:
        return "no medal :("

print(raceResults(30, 27, 28, 29))