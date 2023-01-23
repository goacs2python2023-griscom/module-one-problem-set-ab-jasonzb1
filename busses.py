def bus(numStudents):
    capacity = 52
    numBuses = numStudents / capacity
    if numStudents % capacity > 0:
        numBuses += 1
    return int(numBuses)

print(bus(108))